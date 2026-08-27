"""canonicalize.py — kanonikalizacja tekstu pola i zliczanie n-gramow 1-3 (plan §3, §3.1).

Realizuje szesc regul z §3.1 w podanej kolejnosci:
  1. male litery, interpunkcja i dywiz -> spacja, tokenizacja
  2. warianty brytyjsko-amerykanskie z zamknietej listy (data/canon/spelling_uk_us.csv)
  3. liczba mnoga -> pojedyncza, regulowo (regula spisana nizej, jest czescia preregistracji)
  4. warianty cyfrowo-slowne i rozwiniecie skrotow z zamknietej listy (data/canon/phrase_map.csv),
     stosowane na sekwencji tokenow, bo "three dimensional" -> "3d" zmienia dlugosc
  5. n-gramy 1-3, prog wejscia: >=MIN_OCC wystapien w calym okresie
  6. zwijanie zagniezdzonych n-gramow — OSOBNY krok, w collapse_nested.py, bo wymaga
     zbiorow rekordow, ktore powstaja dopiero tutaj

Regula liczby mnogiej (dokladnie ta, nic wiecej):
  konczy sie na "ies" i dlugosc > 4  -> "y"      (arthroplasties -> arthroplasty)
  konczy sie na "sses"               -> "ss"     (stresses -> stress)
  konczy sie na "s", nie na "ss"/"us"/"is"/"as", dlugosc > 3 -> bez "s"
Wyjatki inne niz powyzsze nie sa obslugiwane celowo — kazdy dodatkowy wyjatek
byloby trzeba prerejestrowac, a zysk jest znikomy.

Skala. 268 tys. rekordow to ~62 mln tokenow; zliczanie wszystkich n-gramow 1-3 naraz to
kilkanascie GB. Uzywamy zasady Apriori: n-gram nie moze wystapic >=MIN_OCC razy, jesli
ktorykolwiek jego skladnik wystepuje rzadziej. Liczymy wiec etapami — unigramy, potem
bigramy zlozone z czestych unigramow, potem trigramy, ktorych OBA bigramy skladowe sa czeste.
Wynik jest dokladnie taki sam jak przy zliczaniu wprost, tylko miesci sie w pamieci.

Uruchom:
    python code/canonicalize.py --text D:/medline_2026/parsed/field_text.parquet \
        --canon data/canon --out D:/medline_2026/parsed/terms.parquet
"""
from __future__ import annotations
import argparse, csv, re, sys, time
from collections import Counter, defaultdict
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
except ImportError:
    sys.exit("pip install pandas pyarrow")

YEAR_MIN, YEAR_MAX = 2005, 2025
TOKEN_SPLIT = re.compile(r"[^a-z0-9]+")
# Token czterocyfrowy z zakresu 1900-2100 to cytowany rocznik ("studies published between
# 2010 and 2020"), nie termin. Kazdy rocznik "wschodzi", gdy staje sie cytowalny, i opada,
# gdy sie starzeje — 28,2% terminow wschodzacych w przebiegu z 2026-08-27 zawieralo
# samodzielna liczbe. Takie tokeny NIE wchodza do slownika i dzialaja jak separator,
# a nie sa wycinane ze sklejeniem sasiadow — inaczej "published in 2015 and followed"
# wyprodukowaloby nieistniejacy bigram "published followed".
YEAR_TOKEN = re.compile(r"^(?:19\d{2}|20\d{2}|2100)$")
NESTED_JACCARD = 0.90


def plural_to_singular(t: str) -> str:
    if len(t) > 4 and t.endswith("ies"):
        return t[:-3] + "y"
    if t.endswith("sses"):
        return t[:-2]
    if (len(t) > 3 and t.endswith("s")
            and not t.endswith(("ss", "us", "is", "as"))):
        return t[:-1]
    return t


def load_lists(canon_dir: Path):
    spell = {}
    with open(canon_dir / "spelling_uk_us.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            v, c = r["variant"].strip().lower(), r["canonical"].strip().lower()
            if v and c:
                spell[v] = c
    irregular = {}
    with open(canon_dir / "irregular_plurals.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            f, c = r["form"].strip().lower(), r["canonical"].strip().lower()
            if f and c:
                irregular[f] = c
    phrases = {}
    with open(canon_dir / "phrase_map.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            src, tgt = r.get("source"), r.get("target")
            # wiersze zaczynajace sie od "#" to zapis wpisow USUNIETYCH wraz z uzasadnieniem.
            # Trzymamy go w tym samym pliku, bo to slad decyzji preregistracyjnej — ale CSV
            # nie ma skladni komentarza, wiec pomijamy je tutaj.
            if not src or src.lstrip().startswith("#") or not tgt:
                continue
            s = tuple(src.strip().lower().split())
            t = tuple(tgt.strip().lower().split())
            if s and t:
                phrases[s] = t
    return spell, irregular, phrases


def make_canonicalizer(spell: dict, irregular: dict, phrases: dict):
    max_len = max(len(k) for k in phrases) if phrases else 1

    def canon(text: str) -> list[str]:
        toks = [t for t in TOKEN_SPLIT.split(text.lower()) if t]
        toks = [spell.get(t, t) for t in toks]                          # regula 2
        # regula 3: lista nieregularnych ma pierwszenstwo przed regula ogolna,
        # bo ta dalaby "series" -> "sery" i "prostheses" -> "prosthese"
        toks = [irregular[t] if t in irregular else plural_to_singular(t) for t in toks]
        out, i, n = [], 0, len(toks)                                    # regula 4
        while i < n:
            hit = None
            for L in range(min(max_len, n - i), 0, -1):
                cand = tuple(toks[i:i + L])
                if cand in phrases:
                    hit = (L, phrases[cand]); break
            if hit:
                L, rep = hit
                # Abstrakty pisza rutynowo "pelna nazwa (SKROT)". Po rozwinieciu skrotu
                # fraza pojawilaby sie dwa razy pod rzad, zawyzajac liczniki i tworzac
                # sztuczne trigramy na styku. Pomijamy powtorzenie.
                if len(out) >= len(rep) and tuple(out[-len(rep):]) == rep:
                    i += L
                    continue
                out.extend(rep); i += L
            else:
                out.append(toks[i]); i += 1
        return out

    return canon


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--canon", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--min-occ", type=int, default=50, help="prog wejscia (plan §3)")
    ap.add_argument("--limit", type=int, help="tylko N rekordow (do testu)")
    args = ap.parse_args()

    t0 = time.time()
    spell, irregular, phrases = load_lists(Path(args.canon))
    canon = make_canonicalizer(spell, irregular, phrases)
    print(f"listy zamkniete: {len(spell)} pisowni, {len(irregular)} nieregularnych, {len(phrases)} fraz", file=sys.stderr)

    df = pd.read_parquet(args.text, columns=["pmid", "year", "title", "abstract"])
    df = df[(df["year"] >= YEAR_MIN) & (df["year"] <= YEAR_MAX)]
    if args.limit:
        df = df.head(args.limit)
    years = df["year"].astype(int).values
    n_rec = len(df)
    print(f"rekordow: {n_rec}", file=sys.stderr)

    # --- etap 1: unigramy
    uni = Counter()
    docs: list[list[str]] = []
    for title, abstract in zip(df["title"].values, df["abstract"].values):
        toks = canon(f"{title} {abstract}")
        docs.append(toks)
        uni.update(toks)
    print(f"etap 1: {len(uni)} roznych unigramow, {sum(uni.values())} tokenow "
          f"({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    n_year_tok = sum(c for t, c in uni.items() if YEAR_TOKEN.match(t))
    kept = sorted(t for t, c in uni.items() if c >= args.min_occ and not YEAR_TOKEN.match(t))
    vocab = {t: i for i, t in enumerate(kept)}
    print(f"       pominieto {n_year_tok} wystapien tokenow-rocznikow (separator)", file=sys.stderr)
    inv = {i: t for t, i in vocab.items()}
    print(f"etap 2: {len(vocab)} unigramow >= {args.min_occ}", file=sys.stderr)

    # kodowanie: rzadkie tokeny staja sie separatorem (-1), zeby n-gramy przez nie nie przeskakiwaly
    enc = [np.fromiter((vocab.get(t, -1) for t in toks), dtype=np.int32, count=len(toks))
           for toks in docs]
    del docs

    # --- etap 3: bigramy z czestych unigramow
    bi = Counter()
    for a in enc:
        m = a[:-1] >= 0
        m &= a[1:] >= 0
        for x, y in zip(a[:-1][m], a[1:][m]):
            bi[(int(x), int(y))] += 1
    bi = {k: v for k, v in bi.items() if v >= args.min_occ}
    print(f"etap 3: {len(bi)} bigramow >= {args.min_occ} "
          f"({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    # --- etap 4: trigramy, ktorych OBA bigramy skladowe sa czeste
    tri = Counter()
    for a in enc:
        for i in range(len(a) - 2):
            x, y, z = int(a[i]), int(a[i + 1]), int(a[i + 2])
            if x < 0 or y < 0 or z < 0:
                continue
            if (x, y) in bi and (y, z) in bi:
                tri[(x, y, z)] += 1
    tri = {k: v for k, v in tri.items() if v >= args.min_occ}
    print(f"etap 4: {len(tri)} trigramow >= {args.min_occ} "
          f"({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    # --- etap 5: liczby dokumentow po latach dla wszystkich terminow, ktore przeszly
    keys1 = {i for t, i in vocab.items() if uni[t] >= args.min_occ}
    per_year: dict[tuple, Counter] = defaultdict(Counter)
    doc_total: Counter = Counter()
    for a, y in zip(enc, years):
        seen = set()
        for v in a:
            if v >= 0:
                seen.add((int(v),))
        for i in range(len(a) - 1):
            k = (int(a[i]), int(a[i + 1]))
            if k in bi:
                seen.add(k)
        for i in range(len(a) - 2):
            k = (int(a[i]), int(a[i + 1]), int(a[i + 2]))
            if k in tri:
                seen.add(k)
        for k in seen:
            per_year[k][y] += 1
            doc_total[k] += 1

    # --- regula 6 (§3.1): zwijanie zagniezdzonych n-gramow
    # Jesli krotszy n-gram zawiera sie w dluzszym, to KAZDY dokument z dluzszym zawiera tez
    # krotszy, wiec docs(dluzszy) jest podzbiorem docs(krotszy). Przeciecie = |dluzszy|,
    # suma = |krotszy|, a Jaccard redukuje sie do ILORAZU liczby dokumentow — dokladnie,
    # bez trzymania w pamieci par termin-dokument.
    drop: set[tuple] = set()
    for k in list(tri):
        n_long = doc_total[k]
        subs = [(k[0], k[1]), (k[1], k[2]), (k[0],), (k[1],), (k[2],)]
        for sub in subs:
            d = doc_total.get(sub)
            if d and n_long / d >= NESTED_JACCARD:
                drop.add(sub)
    for k in list(bi):
        n_long = doc_total[k]
        for sub in ((k[0],), (k[1],)):
            d = doc_total.get(sub)
            if d and n_long / d >= NESTED_JACCARD:
                drop.add(sub)
    print(f"regula 6: zwinieto {len(drop)} krotszych n-gramow "
          f"(Jaccard >= {NESTED_JACCARD})", file=sys.stderr)

    rows = []
    occ = {}
    occ.update({(i,): uni[t] for t, i in vocab.items()})
    occ.update(bi); occ.update(tri)
    for k, dt in doc_total.items():
        if k in drop:
            continue
        rows.append({
            "term": " ".join(inv[i] for i in k),
            "n": len(k),
            "occurrences": occ.get(k, 0),
            "docs_total": dt,
            **{f"y{y}": per_year[k].get(y, 0) for y in range(YEAR_MIN, YEAR_MAX + 1)},
        })
    out = pd.DataFrame(rows).sort_values("docs_total", ascending=False)
    out.to_parquet(args.out, index=False)

    print(f"\nzapisano {args.out}: {len(out)} terminow", file=sys.stderr)
    print(f"  unigramow {int((out.n==1).sum())}, bigramow {int((out.n==2).sum())}, "
          f"trigramow {int((out.n==3).sum())}", file=sys.stderr)
    print(f"  rekordow w podstawie: {n_rec}", file=sys.stderr)
    print(f"  czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
