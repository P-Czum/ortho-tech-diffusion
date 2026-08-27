"""llm_coder.py — przebieg drugiego kodera (model jezykowy) wg promptu v1.0.

Prompt zrodlowy: docs/protocol/prompt_kodera_v1.md — materiał prerejestracyjny, zamrozony
przed kodowaniem. Ten skrypt go WYKONUJE, nie definiuje; tresc promptu jest tutaj wpisana
doslownie i jej hash trafia do wyniku, zeby dalo sie sprawdzic zgodnosc z zarejestrowana wersja.

Co jest zaslepione. Model dostaje wylacznie pola z szablonu: termin, serie, rok wylonienia,
kandydatow, cztery zestawy tytulow. NIE dostaje czasu podwojenia, osi koncentracji ani wynikow
definicji 2 — bo te sluza jako niezalezne kontrole PO kodowaniu (kodeks §5). Zaslepienie jest
tu latwiejsze niz u czlowieka: model nie zobaczy tego, czego nie wyslemy.

Odtwarzalnosc jest jedyna realna przewaga tej konstrukcji nad koderem-czlowiekiem i trzeba ja
wykorzystac: temperatura 0, model podawany jawnie, kazda surowa odpowiedz zapisywana do JSONL,
hash promptu w wyniku. Recenzent moze przebieg powtorzyc.

Uruchom:
    set OPENAI_API_KEY=...
    python code/llm_coder.py --sheet data/processed/coding_sheet_full.csv \
        --model <nazwa-modelu> --n 60 --out data/processed/llm_coding.csv
"""
from __future__ import annotations
import argparse, hashlib, json, os, sys, time
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
except ImportError:
    sys.exit("pip install pandas")

YEARS = list(range(2005, 2026))
SEED = 20260827          # ziarno losowania podproby — czesc rejestracji

SYSTEM = """Jesteś koderem w badaniu bibliometrycznym. Twoim zadaniem jest przypisanie terminowi jednej
z pięciu kategorii według podanego niżej kodeksu.

Zasada nadrzędna: rozstrzygasz WYŁĄCZNIE na podstawie materiału podanego w zapytaniu.
Jeśli posiadasz wiedzę o danej technologii spoza tego materiału, NIE używaj jej jako podstawy
rozstrzygnięcia. W uzasadnieniu wskaż konkretny element materiału, na którym się opierasz —
tytuł, rok, kandydata na poprzednika. Jeśli materiał nie wystarcza do rozstrzygnięcia, wybierz
kategorię, którą materiał najlepiej wspiera, i napisz w uzasadnieniu, czego zabrakło.

Kodujesz DESYGNAT terminu (zdolność, urządzenie, praktykę), nie sam napis.

PIĘĆ KATEGORII:

novel concept — desygnat nie istniał w polu przed oknem wyłonienia pod żadną nazwą.
  Warunki: tytuły z okolic roku wyłonienia opisują zdolność bez wcześniejszego odpowiednika;
  brak kandydata na poprzednika, którego desygnat odpowiada desygnatowi terminu.
  Pusta lista kandydatów to hipoteza domyślna, nie rozstrzygnięcie — poprzednik mógł istnieć
  poniżej progu zliczania.

renaming — desygnat identyczny z desygnatem poprzednika. Test podstawienia: zamiana terminu
  na poprzednika w tytułach z okresu nakładania zachowuje sens W OBU KIERUNKACH.
  Wspiera: występowanie obu terminów w tych samych tytułach, zapis typu "X (Y)".

conceptual evolution — desygnat nowego terminu zawiera desygnat poprzednika PLUS element
  konstytutywny, którego poprzednik nie miał. Test podstawienia przechodzi w jedną stronę,
  a w drugą nie: każdy robot używa nawigacji, ale nie każda nawigacja jest robotem.

measurement artifact — wyłonienie napędzane pomiarem, nie zjawiskiem: konwencją zapisu
  (formuły dat, zwroty szablonu abstraktu, nazwy baz danych, elementy struktury streszczenia)
  albo zmianą praktyk indeksowania. Wskazówka pomocnicza: rok wyłonienia 2020 lub późniejszy
  przypada na okres opóźnienia indeksowania w tym korpusie.

non-technological term — desygnat prawdziwy i wschodzący, ale niebędący technologią:
  metodologia badań, statystyka, konwencja raportowania, organizacja opieki, temat kliniczny.
  To NIE jest kategoria odpadowa — jej udział jest wynikiem badania.

PROCEDURA — w tej kolejności, pierwszy pasujący krok kończy:
  1. Czy wyłonienie jest artefaktem pomiaru? -> measurement artifact.
  2. Czy desygnat jest technologią (urządzenie, materiał, technika obliczeniowa lub
     operacyjna)? Jeśli NIE -> non-technological term.
  3. Czy wśród kandydatów jest poprzednik o odpowiadającym desygnacie? Jeśli NIE ->
     novel concept.
  4. Test podstawienia z tym poprzednikiem: obustronny -> renaming; jednostronny ->
     conceptual evolution. Jeśli test nie przechodzi w żadną stronę, przejdź do kolejnego
     kandydata z listy; po wyczerpaniu listy -> novel concept.

Odpowiadasz wyłącznie obiektem JSON o polach:
  "kategoria"    — dokładnie jedna z pięciu nazw powyżej, po angielsku
  "poprzednik"   — termin poprzednika przy renaming i conceptual evolution, w innych ""
  "uzasadnienie" — jedno zdanie po polsku, wskazujące konkretny element materiału
  "krok"         — numer kroku procedury, który zakończył rozstrzygnięcie (1-4)
  "material_wystarczajacy" — true albo false"""

USER = """TERMIN: {term}
Rok wyłonienia: {y0}
Udział w polu, rok po roku (2005-2025, w procentach):
{seria}

KANDYDACI NA POPRZEDNIKA (lift = ile razy częściej współwystępuje z terminem, niż wynikałoby
z jego własnej częstości; lift jest podpowiedzią wyszukiwania, NIE dowodem):
{kandydaci}

TYTUŁY ZAWIERAJĄCE TERMIN, z okolic roku wyłonienia:
{tytuly_y0}

TYTUŁY ZAWIERAJĄCE TERMIN, z lat 2023-2025:
{tytuly_pozne}

TYTUŁY ZAWIERAJĄCE GŁÓWNEGO KANDYDATA NA POPRZEDNIKA ({poprzednik}), z okresu nakładania:
{tytuly_poprzednika}

TYTUŁY ZAWIERAJĄCE OBA TERMINY NARAZ:
{tytuly_wspolne}"""

CATEGORIES = {"novel concept", "renaming", "conceptual evolution",
              "measurement artifact", "non-technological term"}


def stratified(df: pd.DataFrame, n: int, seed: int) -> pd.DataFrame:
    """Losowanie warstwowe po epoce roku wylonienia. Warstwy: 2005-2012 / 2013-2019 / 2020+.

    NIE warstwujemy po obecnosci kandydata na poprzednika, jak proponowal brief: kandydata ma
    274 z 287 terminow (95%), wiec mniejsza warstwa dostalaby okolo trzech pozycji z 60."""
    ep = pd.cut(df["y0"], [2004, 2012, 2019, 2025], labels=["a", "b", "c"])
    out = []
    rng = np.random.default_rng(seed)
    for lab, grp in df.groupby(ep, observed=True):
        k = max(1, round(n * len(grp) / len(df)))
        idx = rng.choice(grp.index.values, size=min(k, len(grp)), replace=False)
        out.append(df.loc[idx])
    res = pd.concat(out)
    return res.iloc[:n] if len(res) > n else res


def fmt_series(row) -> str:
    vals = []
    for y in YEARS:
        v = row.get(f"udzial_{y}")
        vals.append(f"{y}:{v}" if v != "" and pd.notna(v) else f"{y}:-")
    return " ".join(vals)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", required=True)
    ap.add_argument("--model", required=True,
                    help="nazwa modelu — podawana jawnie, trafia do wyniku i do rejestracji")
    ap.add_argument("--out", required=True)
    ap.add_argument("--n", type=int, default=60, help="rozmiar podproby (0 = wszystkie)")
    ap.add_argument("--runs", type=int, default=1, help=">1 pozwala zmierzyc zgodnosc wewnetrzna")
    ap.add_argument("--seed", type=int, default=SEED)
    ap.add_argument("--dry-run", action="store_true", help="pokaz pierwszy prompt i wyjdz")
    args = ap.parse_args()

    if not args.dry_run and not os.environ.get("OPENAI_API_KEY"):
        sys.exit("Brak OPENAI_API_KEY w srodowisku.")

    sheet = pd.read_csv(args.sheet, encoding="utf-8-sig").fillna("")
    need = {"term", "y0", "kandydaci_na_poprzednika", "tytuly_okolo_y0",
            "tytuly_2023_2025", "poprzednik_glowny", "tytuly_poprzednika", "tytuly_WSPOLNE"}
    need |= {f"udzial_{y}" for y in YEARS}
    miss = need - set(sheet.columns)
    if miss:
        sys.exit(f"Arkusz nie ma kolumn: {sorted(miss)}")

    sub = sheet if args.n == 0 else stratified(sheet, args.n, args.seed)
    print(f"do zakodowania: {len(sub)} z {len(sheet)} terminow", file=sys.stderr)

    prompt_hash = hashlib.sha256((SYSTEM + USER).encode("utf-8")).hexdigest()[:16]
    print(f"hash promptu: {prompt_hash}", file=sys.stderr)

    def build(r) -> str:
        return USER.format(
            term=r["term"], y0=r["y0"], seria=fmt_series(r),
            kandydaci=r["kandydaci_na_poprzednika"] or "(brak kandydatow powyzej progu)",
            tytuly_y0=r["tytuly_okolo_y0"] or "(brak)",
            tytuly_pozne=r["tytuly_2023_2025"] or "(brak)",
            poprzednik=r["poprzednik_glowny"] or "brak",
            tytuly_poprzednika=r["tytuly_poprzednika"] or "(brak)",
            tytuly_wspolne=r["tytuly_WSPOLNE"] or "(brak)")

    if args.dry_run:
        print("=== SYSTEM ===\n" + SYSTEM + "\n\n=== USER (pierwszy termin) ===")
        print(build(sub.iloc[0]))
        return 0

    from openai import OpenAI
    client = OpenAI()
    raw_path = Path(args.out).with_suffix(".raw.jsonl")
    rows, t0 = [], time.time()
    with open(raw_path, "a", encoding="utf-8") as raw:
        for run in range(1, args.runs + 1):
            for i, (_, r) in enumerate(sub.iterrows(), 1):
                msg = build(r)
                try:
                    resp = client.chat.completions.create(
                        model=args.model, temperature=0,
                        response_format={"type": "json_object"},
                        messages=[{"role": "system", "content": SYSTEM},
                                  {"role": "user", "content": msg}])
                    txt = resp.choices[0].message.content
                    obj = json.loads(txt)
                    err = ""
                except Exception as exc:
                    txt, obj, err = "", {}, f"{type(exc).__name__}: {exc}"
                cat = str(obj.get("kategoria", "")).strip()
                if cat and cat not in CATEGORIES:
                    err = err or f"kategoria spoza listy: {cat!r}"
                raw.write(json.dumps({"run": run, "term": r["term"], "model": args.model,
                                      "prompt_hash": prompt_hash, "raw": txt, "blad": err},
                                     ensure_ascii=False) + "\n")
                rows.append({"run": run, "term": r["term"], "y0": r["y0"],
                             "kategoria": cat, "poprzednik": obj.get("poprzednik", ""),
                             "uzasadnienie": obj.get("uzasadnienie", ""),
                             "krok": obj.get("krok", ""),
                             "material_wystarczajacy": obj.get("material_wystarczajacy", ""),
                             "blad": err})
                if i % 10 == 0:
                    print(f"  run {run}: {i}/{len(sub)} ({(time.time()-t0)/60:.1f} min)",
                          file=sys.stderr)

    out = pd.DataFrame(rows)
    out.insert(0, "model", args.model)
    out.insert(1, "prompt_hash", prompt_hash)
    out.to_csv(args.out, index=False, encoding="utf-8-sig")
    n_err = int((out["blad"] != "").sum())
    print(f"\nzapisano {args.out}: {len(out)} wierszy, surowe -> {raw_path}", file=sys.stderr)
    print(f"  bledow: {n_err}", file=sys.stderr)
    if n_err == 0:
        print("  rozklad kategorii:", file=sys.stderr)
        for k, v in out["kategoria"].value_counts().items():
            print(f"    {k:24s} {v}", file=sys.stderr)
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
