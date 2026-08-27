"""coder_search.py — narzędzie wyszukiwania tytułów dla kodera (kodeks v1.1 §1).

Po co. Kodeks pozwala koderowi przeszukać korpus poza materiałem z arkusza, ale wymaga, żeby
robił to **wyłącznie tym narzędziem** i żeby każde zapytanie było odnotowane. Bez tego
przeszukanie jest nieodtwarzalne, a rejestracja nie może objąć czegoś, czego nie widać.

Czego narzędzie NIE robi, celowo: nie rankuje, nie podpowiada, nie pokazuje udziałów ani
kandydatów. Samo wyszukiwanie — wynik to tytuły z rokiem i PMID w kolejności chronologicznej.
Wszystko, co ponad to, byłoby kolejnym kanałem, którym liczba wpływa na osąd.

Dopasowanie idzie po tekście SKANONIKALIZOWANYM tą samą funkcją co detektor, więc zapytanie
"3d printing" znajdzie też "three-dimensional printing" i "3-D printing" — koder szuka
terminu kanonicznego, nie napisu.

Log: logs/coder_queries.log — znacznik czasu, zapytanie, zakres lat, liczba trafień.

Uruchom:
    python code/coder_search.py --term "rapid prototyping"
    python code/coder_search.py --term "computer navigation" --from 2010 --to 2018 --limit 40
"""
from __future__ import annotations
import argparse, sys, time
from datetime import datetime, timezone
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("pip install pandas pyarrow")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path("D:/medline_2026/parsed/field_canon.parquet")
LOG = ROOT / "logs" / "coder_queries.log"


def build_cache(text_path: Path, canon_dir: Path) -> pd.DataFrame:
    """Jednorazowo kanonikalizuje caly korpus pola i zapisuje. Bez tego kazde zapytanie
    kosztowaloby ~2 min i koder przestalby z narzedzia korzystac."""
    print("buduje cache kanonikalizacji (jednorazowo, ~3 min)...", file=sys.stderr)
    spell, irr, phr = load_lists(canon_dir)
    canon = make_canonicalizer(spell, irr, phr)
    df = pd.read_parquet(text_path, columns=["pmid", "year", "title", "abstract"])
    t0 = time.time()
    df["canon"] = [" " + " ".join(canon(f"{t} {a}")) + " "
                   for t, a in zip(df["title"].values, df["abstract"].values)]
    df[["pmid", "year", "title", "canon"]].to_parquet(CACHE, index=False)
    print(f"  zapisano {CACHE} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)
    return df


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--term", required=True, help="termin kanoniczny, np. \"rapid prototyping\"")
    ap.add_argument("--from", dest="y_from", type=int, default=2005)
    ap.add_argument("--to", dest="y_to", type=int, default=2025)
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--text", default="D:/medline_2026/parsed/field_text.parquet")
    ap.add_argument("--canon", default=str(ROOT / "data" / "canon"))
    ap.add_argument("--rebuild-cache", action="store_true")
    args = ap.parse_args()

    if args.rebuild_cache or not CACHE.exists():
        df = build_cache(Path(args.text), Path(args.canon))
        df = df[["pmid", "year", "title", "canon"]]
    else:
        df = pd.read_parquet(CACHE)

    spell, irr, phr = load_lists(Path(args.canon))
    canon = make_canonicalizer(spell, irr, phr)
    needle = " " + " ".join(canon(args.term)) + " "
    if needle.strip() == "":
        sys.exit("Puste zapytanie po kanonikalizacji.")

    sel = df[(df["year"] >= args.y_from) & (df["year"] <= args.y_to)
             & df["canon"].str.contains(needle, regex=False, na=False)]
    sel = sel.sort_values("year")

    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')}\t"
                 f"{args.term}\t{needle.strip()}\t{args.y_from}-{args.y_to}\t{len(sel)}\n")

    print(f"zapytanie: {args.term!r} -> kanonicznie {needle.strip()!r}")
    print(f"lata {args.y_from}-{args.y_to}: {len(sel)} trafien"
          f"{f', pokazuje {args.limit}' if len(sel) > args.limit else ''}")
    print(f"(zapisano do {LOG.relative_to(ROOT)})")
    print()
    if len(sel) > args.limit:
        # rowny rozklad po latach zamiast pierwszych N — inaczej koder widzi same
        # najstarsze prace i wyrabia sobie zdanie o poczatku okresu, nie o calosci
        step = len(sel) / args.limit
        sel = sel.iloc[[int(i * step) for i in range(args.limit)]]
    for _, r in sel.iterrows():
        print(f"  [{int(r['year'])}] PMID {r['pmid']}  {r['title']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
