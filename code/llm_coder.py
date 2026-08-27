"""llm_coder.py — przebieg drugiego kodera (model jezykowy) wg promptu v1.1.

Prompt zrodlowy: docs/protocol/prompt_system_v1.1.txt + prompt_user_v1.1.txt — material
prerejestracyjny, zamrozony przed kodowaniem i zahaszowany w freeze_manifest.txt. Ten skrypt
prompt WCZYTUJE, nie definiuje: dwie kopie moglyby sie rozejsc niezauwazenie.

Co jest zaslepione. Model dostaje wylacznie pola z szablonu: termin, serie, rok wylonienia,
kandydatow, cztery zestawy tytulow. NIE dostaje czasu podwojenia, osi koncentracji ani wynikow
definicji 2 — bo te sluza jako niezalezne kontrole PO kodowaniu (kodeks §5). Zaslepienie jest
tu latwiejsze niz u czlowieka: model nie zobaczy tego, czego nie wyslemy.

Odtwarzalnosc jest jedyna realna przewaga tej konstrukcji nad koderem-czlowiekiem i trzeba ja
wykorzystac: seed podawany jawnie, model i dostawca w wyniku, kazda surowa odpowiedz
zapisywana do JSONL, hash promptu w wyniku. Recenzent moze przebieg powtorzyc.

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

PROMPT_DIR = Path(__file__).resolve().parent.parent / "docs" / "protocol"
# Prompt zyje w plikach, nie w kodzie: to on jest materialem prerejestracyjnym i to jego
# hash trafia do manifestu zamrozenia. Wbudowanie go w skrypt dawaloby dwa zrodla prawdy,
# ktore moglyby sie rozejsc niezauwazenie.
SYSTEM = (PROMPT_DIR / "prompt_system_v1.1.txt").read_text(encoding="utf-8")
USER = (PROMPT_DIR / "prompt_user_v1.1.txt").read_text(encoding="utf-8")

CATEGORIES = {"novel concept", "renaming", "conceptual evolution",
              "measurement artifact", "non-technological term"}

# Dwaj dostawcy, bo identyfikatory modeli sie roznia: "gpt-5.6-sol" u OpenAI wobec
# "openai/gpt-5.6-sol" w OpenRouter. Do rejestracji trafia dostawca I identyfikator,
# bo sam identyfikator nie wystarcza do odtworzenia przebiegu.
BASE_URL = {"openai": None, "openrouter": "https://openrouter.ai/api/v1"}
KEY_VAR = {"openai": "OPENAI_API_KEY", "openrouter": "OPENROUTER_API_KEY"}


def key_var(provider: str) -> str:
    return KEY_VAR[provider]


def make_client(provider: str):
    from openai import OpenAI
    kw = {"api_key": os.environ.get(KEY_VAR[provider])}
    if BASE_URL[provider]:
        kw["base_url"] = BASE_URL[provider]
    return OpenAI(**kw)


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
    ap.add_argument("--model", help="nazwa modelu — trafia do wyniku i do rejestracji DOSLOWNIE")
    ap.add_argument("--list-models", action="store_true",
                    help="wypisz modele dostepne na tym koncie i wyjdz")
    ap.add_argument("--provider", choices=["openai", "openrouter"], default="openai",
                    help="dostawca API; identyfikatory modeli sie ROZNIA "
                         "(gpt-5.6-sol vs openai/gpt-5.6-sol) i oba ida do rejestracji doslownie")
    ap.add_argument("--out", required=True)
    ap.add_argument("--n", type=int, default=60, help="rozmiar podproby (0 = wszystkie)")
    ap.add_argument("--runs", type=int, default=1, help=">1 pozwala zmierzyc zgodnosc wewnetrzna")
    ap.add_argument("--seed", type=int, default=SEED)
    ap.add_argument("--dry-run", action="store_true", help="pokaz pierwszy prompt i wyjdz")
    args = ap.parse_args()

    if args.list_models:
        if not os.environ.get(key_var(args.provider)):
            sys.exit(f"Brak {key_var(args.provider)} w srodowisku.")
        ms = sorted(m.id for m in make_client(args.provider).models.list().data)
        print(f"modeli dostepnych: {len(ms)}")
        print()
        for m in ms:
            print(" ", m)
        print()
        print("Identyfikator wybranego modelu trafia do rejestracji doslownie.")
        return 0
    if not args.model:
        sys.exit("Podaj --model (albo --list-models, zeby zobaczyc dostepne).")
    if not args.dry_run and not os.environ.get(key_var(args.provider)):
        sys.exit(f"Brak {key_var(args.provider)} w srodowisku.")

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

    client = make_client(args.provider)
    raw_path = Path(args.out).with_suffix(".raw.jsonl")
    rows, t0 = [], time.time()
    with open(raw_path, "a", encoding="utf-8") as raw:
        for run in range(1, args.runs + 1):
            for i, (_, r) in enumerate(sub.iterrows(), 1):
                msg = build(r)
                try:
                    # BEZ temperature: modele serii GPT-5.6 jej NIE wspieraja (sprawdzone
                    # w metadanych OpenRouter). Determinizm zapewnia seed, ktory wspieraja —
                    # i ktory jest do naszych celow lepszy, bo jest jawna liczba do rejestracji,
                    # a nie zalozeniem o interpretacji temperatury zerowej.
                    resp = client.chat.completions.create(
                        model=args.model, seed=args.seed,
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
                                      "provider": args.provider, "seed": args.seed,
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
    out.insert(0, "provider", args.provider)
    out.insert(1, "model", args.model)
    out.insert(2, "prompt_hash", prompt_hash)
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
