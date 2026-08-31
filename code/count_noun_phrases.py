"""count_noun_phrases.py — kanonikalizacja fraz i zliczanie, odpowiednik canonicalize.py.

Rozni sie od canonicalize.py DOKLADNIE jednostka. Wszystko inne jest przeniesione bez zmian:
zamrozone listy z data/canon w tej samej kolejnosci (make_canonicalizer), prog wejscia >=50
wystapien, tokeny-roczniki jako separator, regula 6 (zwijanie zagniezdzonych, Jaccard 0,90),
warianty tekstowe primary/S1/S2/S3 z zawezeniem LICZNIKA I MIANOWNIKA naraz, mianownik
zapisywany jawnie do .denom.json.

Zadnej nowej reguly kanonikalizacji (brief §2). Jesli czegos brakuje — do zgloszenia, nie tutaj.

Dwie rzeczy wymagaly przeniesienia reguly na nowa jednostke, obie zapisane jawnie:

  token-rocznik. W n-gramach dzialal jak separator, zeby "published in 2015 and followed"
  nie dalo bigramu "published followed". We frazie robi to samo: rozcina fraze na czesci,
  a nie jest z niej wycinany ze sklejeniem sasiadow.

  regula 6. W n-gramach zwijala podciagi dlugosci 1-2 wewnatrz 2-3. Tu ta sama regula na
  frazach dlugosci 1-5: dla kazdej frazy sprawdzamy WSZYSTKIE jej ciagle podfrazy obecne
  w slowniku. Zawieranie nadal implikuje zawieranie zbiorow dokumentow, wiec Jaccard nadal
  redukuje sie do ilorazu liczby dokumentow.

Uruchom:
    python code/count_noun_phrases.py --chunks D:/medline_2026/parsed/noun_chunks.parquet \
        --canon data/canon --base primary --out D:/medline_2026/parsed/terms_np_primary.parquet
"""
from __future__ import annotations
import argparse, json, sys, time
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import (  # noqa: E402
    YEAR_MIN, YEAR_MAX, YEAR_TOKEN, NESTED_JACCARD, load_lists, make_canonicalizer,
)

SEP = "\t"
MAX_LEN = 5


def split_years(toks: list[str]) -> list[tuple[str, ...]]:
    """token-rocznik rozcina fraze, tak jak byl separatorem miedzy n-gramami"""
    out, cur = [], []
    for t in toks:
        if YEAR_TOKEN.match(t):
            if cur:
                out.append(tuple(cur))
            cur = []
        else:
            cur.append(t)
    if cur:
        out.append(tuple(cur))
    return [p for p in out if 1 <= len(p) <= MAX_LEN]


def subphrases(k: tuple[str, ...]):
    """wszystkie ciagle podfrazy krotsze od k"""
    n = len(k)
    return {k[i:j] for i in range(n) for j in range(i + 1, n + 1) if j - i < n}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunks", required=True)
    ap.add_argument("--canon", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--min-occ", type=int, default=50)
    ap.add_argument("--base", default="primary",
                    choices=["primary", "s1_title", "s2_abstract", "s3_english"])
    args = ap.parse_args()

    t0 = time.time()
    spell, irregular, phrases = load_lists(Path(args.canon))
    canon = make_canonicalizer(spell, irregular, phrases)
    print(f"listy zamkniete: {len(spell)} pisowni, {len(irregular)} nieregularnych, "
          f"{len(phrases)} fraz", file=sys.stderr)

    df = pd.read_parquet(args.chunks)
    n_field = len(df)
    if args.base == "s2_abstract":
        df = df[df["has_abstract"]]
    elif args.base == "s3_english":
        df = df[df["language"].str.contains("eng", case=False, na=False)]
    title_only = args.base == "s1_title"
    years = df["year"].astype(int).values
    n_rec = len(df)
    print(f"wariant {args.base}: {n_rec} rekordow z {n_field} ({100*n_rec/n_field:.1f}%)",
          file=sys.stderr)

    # --- kanonikalizacja fraz i zliczanie wystapien
    occ: Counter = Counter()
    docs: list[list[tuple[str, ...]]] = []
    tt = df["title_np"].values
    aa = df["abstract_np"].values
    for i in range(n_rec):
        raw = tt[i].split(SEP) if tt[i] else []
        if not title_only and aa[i]:
            raw += aa[i].split(SEP)
        ph = []
        for c in raw:
            if not c:
                continue
            for p in split_years(canon(c)):
                ph.append(p)
        docs.append(ph)
        occ.update(ph)
    print(f"etap 1: {len(occ):,} roznych fraz, {sum(occ.values()):,} wystapien "
          f"({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    keep = {k for k, c in occ.items() if c >= args.min_occ}
    print(f"etap 2: {len(keep):,} fraz >= {args.min_occ} wystapien", file=sys.stderr)

    per_year: dict[tuple, Counter] = defaultdict(Counter)
    doc_total: Counter = Counter()
    for ph, y in zip(docs, years):
        for k in {p for p in ph if p in keep}:
            per_year[k][y] += 1
            doc_total[k] += 1
    del docs

    # --- regula 6 (§3.1): zwijanie zagniezdzonych
    drop: set[tuple] = set()
    for k in keep:
        if len(k) < 2:
            continue
        n_long = doc_total[k]
        for sub in subphrases(k):
            d = doc_total.get(sub)
            if d and n_long / d >= NESTED_JACCARD:
                drop.add(sub)
    print(f"regula 6: zwinieto {len(drop):,} krotszych fraz (Jaccard >= {NESTED_JACCARD})",
          file=sys.stderr)

    rows = [{
        "term": " ".join(k), "n": len(k), "occurrences": occ[k], "docs_total": dt,
        **{f"y{y}": per_year[k].get(y, 0) for y in range(YEAR_MIN, YEAR_MAX + 1)},
    } for k, dt in doc_total.items() if k not in drop]
    out = pd.DataFrame(rows).sort_values("docs_total", ascending=False)
    out.to_parquet(args.out, index=False)

    denom = {str(y): int((years == y).sum()) for y in range(YEAR_MIN, YEAR_MAX + 1)}
    Path(args.out).with_suffix(".denom.json").write_text(
        json.dumps({"base": args.base, "records": n_rec, "field_records": n_field,
                    "by_year": denom}, indent=1), encoding="utf-8")

    print(f"\nzapisano {args.out}: {len(out):,} fraz", file=sys.stderr)
    for L in range(1, MAX_LEN + 1):
        c = int((out.n == L).sum())
        if c:
            print(f"  dlugosc {L}: {c:,}", file=sys.stderr)
    print(f"  czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
