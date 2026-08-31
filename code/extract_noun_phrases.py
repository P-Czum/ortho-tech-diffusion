"""extract_noun_phrases.py — bazowe frazy rzeczownikowe z pola def1 (brief §1).

Parsuje RAZ, osobno tytul i streszczenie, i zapisuje chunki surowe. Cztery warianty tekstowe
z planu §7 roznia sie tylko tym, ktore rekordy i ktore pole wchodza do zliczania, wiec parsowanie
jest dla nich wspolne i nie ma powodu robic go czterokrotnie. Kanonikalizacja jest osobnym
krokiem (count_noun_phrases.py) i uzywa zamrozonych list bez zmian.

WERSJE PRZYPIETE (brief §1 — parser jest zaleznoscia zewnetrzna i musi byc odtwarzalny):
    spacy           3.8.16
    en_core_web_sm  3.8.0
Wypisywane takze do naglowka wyniku i do <out>.meta.json.

scispaCy sprawdzone i odrzucone: przypina spacy<3.8, ktore nie ma kol dla Pythona 3.13
i nie buduje sie ze zrodel w tym srodowisku.

Obrobka chunku (brief §1):
  - chunki plaskie, bez zagniezdzonych fraz przyimkowych — noun_chunks spaCy sa wlasnie takie
  - obciecie wiodacych okreslnikow i zaimkow dzierzawczych oraz interpunkcji z obu koncow
  - dlugosc 1-5 tokenow po obcieciu

Uruchom:
    python code/extract_noun_phrases.py --text D:/medline_2026/parsed/field_text.parquet \
        --out D:/medline_2026/parsed/noun_chunks.parquet
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path

import pandas as pd

YEAR_MIN, YEAR_MAX = 2005, 2025
MODEL = "en_core_web_sm"
LEADING = {"the", "a", "an", "our", "their", "its", "his", "her"}
MIN_LEN, MAX_LEN = 1, 5
SEP = "\t"


def trim(chunk) -> str | None:
    toks = [t for t in chunk if not t.is_punct and not t.is_space]
    while toks and toks[0].lower_ in LEADING:
        toks = toks[1:]
    if not (MIN_LEN <= len(toks) <= MAX_LEN):
        return None
    return " ".join(t.text for t in toks)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, help="tylko N rekordow (do pomiaru czasu)")
    ap.add_argument("--procs", type=int, default=8)
    ap.add_argument("--batch", type=int, default=200)
    args = ap.parse_args()

    import spacy
    import importlib.metadata as md
    ver = {"spacy": spacy.__version__, MODEL: md.version(MODEL)}
    print(f"parser: spacy {ver['spacy']}, {MODEL} {ver[MODEL]}", file=sys.stderr)

    df = pd.read_parquet(args.text, columns=["pmid", "year", "title", "abstract", "language"])
    df = df[(df["year"] >= YEAR_MIN) & (df["year"] <= YEAR_MAX)].reset_index(drop=True)
    if args.limit:
        df = df.head(args.limit)
    print(f"rekordow: {len(df)}", file=sys.stderr)

    nlp = spacy.load(MODEL, exclude=["ner", "lemmatizer"])
    t0 = time.time()

    # strumien (tekst, (indeks, pole)) — tytul i streszczenie jako osobne dokumenty
    def stream():
        for i, (ti, ab) in enumerate(zip(df["title"].values, df["abstract"].values)):
            yield (ti or "", (i, "t"))
            yield (ab or "", (i, "a"))

    title_ch: list[list[str]] = [[] for _ in range(len(df))]
    abs_ch: list[list[str]] = [[] for _ in range(len(df))]
    done = 0
    for doc, (i, kind) in nlp.pipe(stream(), as_tuples=True,
                                   batch_size=args.batch, n_process=args.procs):
        out = [c for c in (trim(ch) for ch in doc.noun_chunks) if c]
        (title_ch if kind == "t" else abs_ch)[i] = out
        done += 1
        if done % 100000 == 0:
            print(f"  {done//2:,} rekordow, {(time.time()-t0)/60:.1f} min", file=sys.stderr)

    res = pd.DataFrame({
        "pmid": df["pmid"], "year": df["year"], "language": df["language"],
        "has_abstract": df["abstract"].str.len() > 0,
        "title_np": [SEP.join(x) for x in title_ch],
        "abstract_np": [SEP.join(x) for x in abs_ch],
    })
    res.to_parquet(args.out, index=False)
    meta = {"wersje": ver, "rekordow": len(df), "min_len": MIN_LEN, "max_len": MAX_LEN,
            "obciete_wiodace": sorted(LEADING), "minut": round((time.time() - t0) / 60, 1)}
    Path(args.out).with_suffix(".meta.json").write_text(
        json.dumps(meta, indent=1, ensure_ascii=False), encoding="utf-8")

    nt = sum(len(x) for x in title_ch)
    na = sum(len(x) for x in abs_ch)
    print(f"\nzapisano {args.out}", file=sys.stderr)
    print(f"  chunkow z tytulow: {nt:,} ({nt/len(df):.1f} na rekord)", file=sys.stderr)
    print(f"  chunkow ze streszczen: {na:,} ({na/len(df):.1f} na rekord)", file=sys.stderr)
    print(f"  czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
