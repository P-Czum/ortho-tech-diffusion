"""powiklania_vs_szczyt.py — czy slownictwo powiklan wyprzedza szczyt technologii.

Obserwacja z metal-on-metal: frazy powiklan (pseudotumor y0 2013, metal debris 2012, adverse
local tissue reaction 2014) wylonily sie PRZED szczytem mom total hip arthroplasty (2018).
Pytanie: czy to cecha upadku technologii, czy cecha cyklu zycia kazdej technologii.

Przypadek probny, ktory moze wzorzec zlamac: cement leakage y0 2009 wobec szczytu kyphoplasty
2011 — ten sam uklad czasowy, ale kyphoplastyka jest w pasmie "dowody za, rutyna".

Procedura (brief Coworku, §Zadanie):
  1. dla kazdej z 76 grup materialu szukamy fraz rdzenia zaklasyfikowanych jako `rozpoznanie`,
     ktore wspolwystepuja z technologia ponad oczekiwanie: obs / (nA*nB/N) >= MIN_KROTNOSC
  2. dla kazdej pary: y0 powiklania minus rok szczytu technologii (ujemne = wyprzedza)
  3. zestawienie po pasmach zaniku i dla technologii bez zaniku

Bez interpretacji klinicznej — czy dane powiklanie podwaza technologie, rozstrzyga ortopeda.

Uruchom:
    python code/powiklania_vs_szczyt.py --out data/processed/powiklania_vs_szczyt.csv
"""
from __future__ import annotations
import argparse, io, json, sys, time
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402
from count_noun_phrases import SEP, split_years  # noqa: E402

P = Path("D:/medline_2026/parsed")
MIN_KROTNOSC = 5.0
MIN_WSPOLNYCH = 5          # ponizej tylu wspolnych prac krotnosc jest szumem


def oceny() -> dict:
    """kategoria ortopedy dla fraz rdzenia, z obu przebiegow oceny"""
    out = {}
    for f in ["ocena_mapy_2026-09-01.csv", "ocena_mapy_nowe_naprawiony.csv"]:
        raw = io.open(f, encoding="utf-8-sig").read().partition("# BRAKUJACE")[0]
        d = pd.read_csv(io.StringIO(raw))
        for t, k in zip(d["term"].astype(str).str.strip(),
                        d["kategoria_ocena"].fillna("").astype(str).str.strip()):
            if k:
                out[t] = k
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    t0 = time.time()

    osie = pd.read_csv("data/processed/osie_ostateczne.csv", encoding="utf-8-sig")
    grupy = json.loads(Path("data/processed/grupy_ostateczne.json").read_text(encoding="utf-8"))
    mech = pd.read_csv("data/processed/wycofania_mechanizmy.csv", encoding="utf-8-sig")
    pasmo = dict(zip(mech["grupa"], mech["przyczyna"]))

    kat = oceny()
    rdzen = set(json.loads(Path("data/processed/rdzen_d6.json").read_text(encoding="utf-8")))
    powiklania = sorted(t for t in rdzen if kat.get(t) == "rozpoznanie")
    print(f"grup materialu: {len(osie)} | fraz 'rozpoznanie' w rdzeniu: {len(powiklania)}",
          file=sys.stderr)

    em = pd.read_parquet(P / "emerging_d6_primary.parquet").set_index("term")
    canon = make_canonicalizer(*load_lists(Path("data/canon")))
    nc = pd.read_parquet(P / "noun_chunks_2000_2025.parquet")
    wyl = set(pd.read_csv("data/processed/pmid_pole_wylaczone_d6.csv", dtype=str)["pmid"])
    nc = nc[~nc["pmid"].isin(wyl)]
    N = len(nc)

    czlon = {g: set(grupy.get(g, [g])) for g in osie["grupa"]}
    cel = set().union(*czlon.values()) | set(powiklania)
    dok_g = {g: set() for g in czlon}
    dok_p = {t: set() for t in powiklania}
    tt, aa, pm = nc["title_np"].values, nc["abstract_np"].values, nc["pmid"].values
    for i in range(len(nc)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        ob = set()
        for c in raw:
            if c:
                ob.update(" ".join(p) for p in split_years(canon(c)))
        h = ob & cel
        if not h:
            continue
        for g, cz in czlon.items():
            if h & cz:
                dok_g[g].add(pm[i])
        for t in h & dok_p.keys():
            dok_p[t].add(pm[i])
        if (i + 1) % 50000 == 0:
            print(f"  {i+1:,}/{N:,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    rows = []
    for _, r in osie.iterrows():
        g, szczyt = r["grupa"], int(r["rok_szczytu"])
        A = dok_g[g]
        if not A:
            continue
        for t in powiklania:
            B = dok_p[t]
            if not B or t in czlon[g]:
                continue
            obs = len(A & B)
            if obs < MIN_WSPOLNYCH:
                continue
            ocz = len(A) * len(B) / N
            kr = obs / ocz if ocz else 0
            if kr < MIN_KROTNOSC:
                continue
            y0p = em.loc[t, "y0"] if t in em.index else None
            if not y0p or not em.loc[t, "emerging"]:
                continue
            rows.append({
                "grupa": g, "rok_szczytu": szczyt, "powiklanie": t, "y0_powiklania": int(y0p),
                "wyprzedzenie_lat": int(y0p) - szczyt,
                "wyprzedza": int(y0p) < szczyt,
                "prac_grupy": len(A), "prac_powiklania": len(B), "wspolnych": obs,
                "krotnosc": round(kr, 1),
                "pasmo": pasmo.get(g, "bez zaniku"),
            })

    d = pd.DataFrame(rows).sort_values(["grupa", "krotnosc"], ascending=[True, False])
    d.to_csv(args.out, index=False, encoding="utf-8-sig", lineterminator="\n")
    print(f"\npar powiklanie-technologia: {len(d)} przy {d['grupa'].nunique()} grupach",
          file=sys.stderr)

    print("\n=== czy powiklanie wyprzedza szczyt, wg pasma zaniku ===")
    g2 = d.groupby("pasmo").agg(par=("wyprzedza", "size"), wyprzedza=("wyprzedza", "sum"),
                                grup=("grupa", "nunique"),
                                mediana_lat=("wyprzedzenie_lat", "median"))
    g2["pct"] = (100 * g2["wyprzedza"] / g2["par"]).round(0)
    print(g2.sort_values("pct", ascending=False).to_string())
    print(f"\nzapisane: {args.out}  ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
