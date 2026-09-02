"""skrot_po_latach.py — czy odrzucenie skrotu przesuwa y0 (kontrola z §2 briefu Coworku).

Odrzucenie wieloznacznego skrotu jest zachowawcze dla OBECNOSCI terminu, ale nie musi byc
neutralne dla y0 i czasu podwojenia. Jesli udzial dokumentow uzywajacych SAMEGO skrotu rosl
w czasie — a to prawdopodobne, bo skrot upowszechnia sie razem z tematem — to odrzucenie
usuwa nieproporcjonalnie duzo dokumentow poznych, splaszcza krzywa, przesuwa y0 pozno
i zawyza czas podwojenia.

Dla kazdej pary skrot/pelna postac liczymy po latach trzy rozlaczne klasy dokumentow:
  tylko pelna | oba | tylko skrot
i sprawdzamy, czy udzial "tylko skrot" ma trend. Nachylenie regresji liniowej udzialu
po latach, wazone liczba dokumentow w roku.

Uruchom:
    python code/skrot_po_latach.py --pary data/processed/skroty_pary.json \
        --chunks D:/medline_2026/parsed/noun_chunks_2000_2025.parquet \
        --exclude data/processed/pmid_pole_wylaczone_d6.csv --canon data/canon \
        --out results/skrot_po_latach.json
"""
from __future__ import annotations
import argparse, json, sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402
from count_noun_phrases import SEP, split_years  # noqa: E402

MIN_ROK = 10          # rok wchodzi do regresji, gdy ma >= tylu dokumentow


def main() -> int:
    ap = argparse.ArgumentParser()
    for a in ("--pary", "--chunks", "--canon", "--out"):
        ap.add_argument(a, required=True)
    ap.add_argument("--exclude")
    args = ap.parse_args()

    pary = json.loads(Path(args.pary).read_text(encoding="utf-8"))
    canon = make_canonicalizer(*load_lists(Path(args.canon)))
    cel = set(pary) | {x for v in pary.values() for x in v}

    df = pd.read_parquet(args.chunks)
    if args.exclude:
        wyl = set(pd.read_csv(args.exclude, dtype=str)["pmid"])
        df = df[~df["pmid"].isin(wyl)]
    print(f"rekordow: {len(df):,}", file=sys.stderr)

    tt, aa, yr = df.title_np.values, df.abstract_np.values, df.year.astype(int).values
    obec = defaultdict(lambda: defaultdict(lambda: [0, 0, 0]))   # skrot -> rok -> [pelna, oba, skrot]
    for i in range(len(df)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        ob = set()
        for c in raw:
            if c:
                ob.update(" ".join(p) for p in split_years(canon(c)))
        if not (ob & cel):
            continue
        for skr, pelne in pary.items():
            s, p = skr in ob, bool(ob & set(pelne))
            if s and p:
                obec[skr][yr[i]][1] += 1
            elif s:
                obec[skr][yr[i]][2] += 1
            elif p:
                obec[skr][yr[i]][0] += 1

    res = {}
    for skr, lata in obec.items():
        ys = sorted(y for y in lata if sum(lata[y]) >= MIN_ROK)
        if len(ys) < 8:
            continue
        n = np.array([sum(lata[y]) for y in ys], float)
        udz = np.array([lata[y][2] / sum(lata[y]) for y in ys], float)
        b, a = np.polyfit(np.array(ys, float), udz, 1, w=np.sqrt(n))
        res[skr] = {"lat": len(ys), "udzial_pierwsze_3": round(float(udz[:3].mean()), 3),
                    "udzial_ostatnie_3": round(float(udz[-3:].mean()), 3),
                    "nachylenie_pp_na_rok": round(float(100 * b), 2),
                    "dokumentow": int(n.sum())}
        r = res[skr]
        print(f"\n=== {skr} ({r['dokumentow']} dok., {r['lat']} lat) ===")
        print(f"  udzial 'tylko skrot': pierwsze 3 lata {100*r['udzial_pierwsze_3']:.1f}% "
              f"-> ostatnie 3 lata {100*r['udzial_ostatnie_3']:.1f}%")
        print(f"  nachylenie: {r['nachylenie_pp_na_rok']:+.2f} pp/rok")
        print("  " + " ".join(f"{y%100:>4}" for y in ys))
        print("  " + " ".join(f"{100*u:>4.0f}" for u in udz))

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisane: {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
