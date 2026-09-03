"""retronimy.py — czy wyrzucone pozycje sa retronimami (brief §7).

Retronim: stary standard dostaje nazwe albo przymiotnik dopiero wtedy, gdy pojawia sie rywal.
Test: dla kazdej wyrzuconej pozycji szukamy w materiale technologii o najwyzszej krotnosci
wspolwystepowania (prog 5x, >= 5 wspolnych prac) i sprawdzamy, czy byla obecna w polu ZANIM
wyrzucona pozycja sie wylonila.

Kluczowe: "obecna" to rok pierwszej obecnosci (>= MIN_PRAC prac w roku), NIE y0. y0 rywala to
prog pieciokrotnosci i moze wypasc PO retronimie — kinematic alignment ma y0 2022, a mechanical
alignment wylonil sie w 2018. Tabela z y0 rywala bylaby nonsensem.

Bez rozstrzygania — ortopeda decyduje, ktore pary sa para "standard-rywal".

Uruchom:
    python code/retronimy.py --out data/processed/retronimy.csv
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402
from count_noun_phrases import SEP, split_years  # noqa: E402

P = Path("D:/medline_2026/parsed")
YEARS = list(range(2000, 2026))
MIN_KROTNOSC = 5.0
MIN_WSPOLNYCH = 5
MIN_PRAC = 5          # rok pierwszej obecnosci: >= tylu prac


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    t0 = time.time()

    WYRZUCONE = ["mechanical alignment", "single bundle", "anatomic total shoulder arthroplasty",
                 "primary anterior cruciate ligament reconstruction",
                 "unilateral anterior cruciate ligament reconstruction",
                 "primary unilateral total knee arthroplasty",
                 "elective total knee arthroplasty", "posterior lumbar fusion",
                 "pelvic fixation", "anterior cervical discectomy fusion"]
    grupy = json.loads(Path("data/processed/grupy_61.json").read_text(encoding="utf-8"))
    em = pd.read_parquet(P / "emerging_d6_primary.parquet").set_index("term")

    czl = {g: set(v) for g, v in grupy.items()}
    for t in WYRZUCONE:
        czl.setdefault(t, {t})
    cel = set().union(*czl.values())

    canon = make_canonicalizer(*load_lists(Path("data/canon")))
    nc = pd.read_parquet(P / "noun_chunks_2000_2025.parquet")
    wyl = set(pd.read_csv("data/processed/pmid_pole_wylaczone_d6.csv", dtype=str)["pmid"])
    nc = nc[~nc["pmid"].isin(wyl)]
    N = len(nc)

    dok = {g: set() for g in czl}
    rok = {g: {} for g in czl}
    tt, aa, pm, yr = (nc["title_np"].values, nc["abstract_np"].values,
                      nc["pmid"].values, nc["year"].astype(int).values)
    for i in range(len(nc)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        ob = set()
        for c in raw:
            if c:
                ob.update(" ".join(p) for p in split_years(canon(c)))
        if not (ob & cel):
            continue
        for g, cz in czl.items():
            if ob & cz:
                dok[g].add(pm[i])
                rok[g][yr[i]] = rok[g].get(yr[i], 0) + 1
        if (i + 1) % 50000 == 0:
            print(f"  {i+1:,}/{N:,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    def pierwsza_obecnosc(g):
        for y in YEARS:
            if rok[g].get(y, 0) >= MIN_PRAC:
                return y
        return None

    rows = []
    for w in WYRZUCONE:
        A = dok[w]
        y0w = int(em.loc[w, "y0"]) if w in em.index and em.loc[w, "emerging"] else None
        kand = []
        for g in grupy:
            if g == w:
                continue
            B = dok[g]
            obs = len(A & B)
            if obs < MIN_WSPOLNYCH:
                continue
            ocz = len(A) * len(B) / N
            kr = obs / ocz if ocz else 0
            if kr >= MIN_KROTNOSC:
                kand.append((kr, g, obs))
        kand.sort(reverse=True)
        if not kand:
            rows.append({"pozycja": w, "y0": y0w, "kandydat_rywal": "", "krotnosc": None,
                         "wspolnych": None, "rywal_obecny_od": None, "poprzedza": None})
            continue
        kr, g, obs = kand[0]
        po = pierwsza_obecnosc(g)
        rows.append({"pozycja": w, "y0": y0w, "kandydat_rywal": g, "krotnosc": round(kr, 1),
                     "wspolnych": obs, "rywal_obecny_od": po,
                     "poprzedza": (po is not None and y0w is not None and po < y0w),
                     "kolejni_kandydaci": " | ".join(f"{x[1]} ({x[0]:.0f}x)" for x in kand[1:4])})

    d = pd.DataFrame(rows)
    d.to_csv(args.out, index=False, encoding="utf-8-sig", lineterminator="\n")
    print(f"\n{'pozycja':<46} {'y0':>5} {'kandydat na rywala':<34} {'krot':>6} "
          f"{'od':>5} {'poprz':>6}")
    for _, r in d.iterrows():
        print(f"{r.pozycja:<46} {str(r.y0):>5} {str(r.kandydat_rywal)[:33]:<34} "
              f"{str(r.krotnosc):>6} {str(r.rywal_obecny_od):>5} {str(r.poprzedza):>6}")
    print(f"\nzapisane: {args.out}  ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
