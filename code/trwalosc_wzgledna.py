"""trwalosc_wzgledna.py — trwalosc mierzona wzgledem WLASNEGO szczytu kazdej technologii.

Okno kalendarzowe bylo bledem, ktory wychwycil ortopeda: technologia ze szczytem w 2007
mierzona w latach 2021-22 jest czternascie lat po szczycie, a ta ze szczytem w 2020 — dwa.
Nazywanie tego jedna miara unieważnia porownanie. Tu okna sa przesuniete wobec szczytu
kazdej grupy z osobna: +1..3, +3..5 i +5..7 lat po jej wlasnym roku szczytowym.

Zliczanie UNIJNE — dokument z dwoma czlonami grupy liczy sie raz. Suma szeregow czlonow
zawyzalaby grupy wieloczlonowe.

Klasa stanu dowodow pochodzi z oceny ortopedy i jest wczytywana z pliku, nie zgadywana.

Uruchom:
    python code/trwalosc_wzgledna.py --grupy data/processed/grupy_56.json \
        --osie data/processed/osie_56.csv --klasy data/processed/mechanizmy_zanikow.csv \
        --out data/processed/trwalosc_wzgledna_56.csv
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
OKNA = [("po_1_3", 1, 3), ("po_3_5", 3, 5), ("po_5_7", 5, 7)]
PROG = 0.5


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--grupy", required=True)
    ap.add_argument("--osie", required=True)
    ap.add_argument("--klasy")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    t0 = time.time()

    grupy = json.loads(Path(args.grupy).read_text(encoding="utf-8"))
    osie = pd.read_csv(args.osie, encoding="utf-8-sig")
    zanik = osie[osie["trwalosc_2025_do_szczytu"] < PROG]
    czl = {g: set(grupy[g]) for g in zanik.grupa}
    cel = set().union(*czl.values())
    szczyt = dict(zip(zanik.grupa, zanik.rok_szczytu))
    print(f"grup w zaniku: {len(czl)}", file=sys.stderr)

    denom = json.loads((P / "terms_d6_primary.denom.json").read_text(encoding="utf-8"))["by_year"]
    dv = np.array([denom[str(y)] for y in YEARS], float)

    canon = make_canonicalizer(*load_lists(Path("data/canon")))
    nc = pd.read_parquet(P / "noun_chunks_2000_2025.parquet")
    wyl = set(pd.read_csv("data/processed/pmid_pole_wylaczone_d6.csv", dtype=str)["pmid"])
    nc = nc[~nc["pmid"].isin(wyl)]

    licz = {g: np.zeros(len(YEARS)) for g in czl}
    tt, aa, yr = nc["title_np"].values, nc["abstract_np"].values, nc["year"].astype(int).values
    for i in range(len(nc)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        ob = set()
        for c in raw:
            if c:
                ob.update(" ".join(p) for p in split_years(canon(c)))
        if not (ob & cel):
            continue
        j = YEARS.index(yr[i])
        for g, cz in czl.items():
            if ob & cz:
                licz[g][j] += 1
        if (i + 1) % 100000 == 0:
            print(f"  {i+1:,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    klasy = {}
    if args.klasy and Path(args.klasy).exists():
        k = pd.read_csv(args.klasy, encoding="utf-8-sig")
        klasy = dict(zip(k.iloc[:, 0], k.iloc[:, 1]))

    rows = []
    for g, c in licz.items():
        s = c / dv
        pk = int(szczyt[g])
        sz = s[YEARS.index(pk)]
        r = {"grupa": g, "przyczyna": klasy.get(g, ""), "szczyt": pk}
        for nazwa, a, b in OKNA:
            lata = [y for y in range(pk + a, pk + b + 1) if y in YEARS]
            r[nazwa] = round(float(np.mean([s[YEARS.index(y)] for y in lata]) / sz), 4) \
                if lata and sz else None
        rows.append(r)

    d = pd.DataFrame(rows).sort_values("po_3_5")
    d.to_csv(args.out, index=False, encoding="utf-8-sig", lineterminator="\n")
    print(d.to_string(index=False))
    print(f"\nzapisane: {args.out}  ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
