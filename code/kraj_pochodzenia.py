"""kraj_pochodzenia.py — czy kraj czolowy literatury jest krajem, z ktorego pochodza najwczesniejsze prace.

Teza do sprawdzenia: piec grup prowadzonych przez kraj spoza pary USA/Chiny (Francja, Niemcy,
Japonia, Korea Pld. x2) to za kazdym razem kraj pochodzenia technologii. Dane nie znaja
historii techniki, ale znaja kraj najwczesniejszych prac — to jest jedyny test, ktory da sie
przeprowadzic na korpusie.

Liczone dla WSZYSTKICH grup, nie tylko pieciu: bez czestosci bazowej nie wiadomo, czy
"najwczesniejsze prace z kraju czolowego" to cos szczegolnego, czy regula dla kazdej grupy.

Ograniczenie wpisane w konstrukcje: okno zaczyna sie w 2000. Dla technik starszych (np. dual
mobility, 1974) najwczesniejsze prace w korpusie NIE sa pracami zalozycielskimi.

Kraj z afiliacji pierwszego autora, ta sama regula co w merge_and_axes.py.

Uruchom:
    python code/kraj_pochodzenia.py --grupy data/processed/grupy_54.json \
        --osie data/processed/osie_54.csv --out data/processed/kraj_pochodzenia_54.csv
"""
from __future__ import annotations
import argparse, json, sys
from collections import Counter
from pathlib import Path

import pandas as pd
import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402
from count_noun_phrases import SEP, split_years  # noqa: E402
from affil_country import make_matcher  # noqa: E402

P = Path("D:/medline_2026/parsed")
WCZESNE = 10          # ile najwczesniejszych prac ze znanym krajem


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--grupy", required=True)
    ap.add_argument("--osie", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    grupy = json.loads(Path(args.grupy).read_text(encoding="utf-8"))
    czl = {g: set(v) for g, v in grupy.items()}
    cel = set().union(*czl.values())
    osie = pd.read_csv(args.osie, encoding="utf-8-sig").set_index("grupa")

    canon = make_canonicalizer(*load_lists(Path("data/canon")))
    nc = pd.read_parquet(P / "noun_chunks_2000_2025.parquet")
    wyl = set(pd.read_csv("data/processed/pmid_pole_wylaczone_d6.csv", dtype=str)["pmid"])
    nc = nc[~nc["pmid"].isin(wyl)]

    dok = {g: [] for g in czl}          # (rok, pmid)
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
                dok[g].append((yr[i], pm[i]))

    potrzebne = {p for v in dok.values() for _, p in v}
    aff = {}
    pf = pq.ParquetFile(P / "analytic_index.parquet")
    for k in range(pf.metadata.num_row_groups):
        d = pf.read_row_group(k, columns=["pmid", "aff1"]).to_pandas()
        d = d[d["pmid"].isin(potrzebne)]
        aff.update(zip(d["pmid"], d["aff1"].fillna("")))
    cmatch = make_matcher(Path("data/canon"))

    rows = []
    for g, v in dok.items():
        y0 = int(osie.loc[g, "y0"])
        lider = osie.loc[g, "kraj_top"]
        z_krajem = [(y, p, cmatch(aff.get(p, ""))) for y, p in sorted(v)]
        z_krajem = [x for x in z_krajem if x[2]]
        wcz = z_krajem[:WCZESNE]
        przed = [k for y, _, k in z_krajem if y < y0]
        kw = Counter(k for _, _, k in wcz)
        kp = Counter(przed)
        top_w, n_w = kw.most_common(1)[0] if kw else ("", 0)
        top_p, n_p = kp.most_common(1)[0] if kp else ("", 0)
        rows.append({
            "grupa": g, "y0": y0, "lider": lider,
            "pierwszy_rok_z_krajem": wcz[0][0] if wcz else None,
            "pierwszy_kraj": wcz[0][2] if wcz else "",
            "wczesne_top": top_w, "wczesne_top_n": n_w, "wczesne_n": len(wcz),
            "wczesne_lider_n": kw.get(lider, 0),
            "przed_y0_n": len(przed), "przed_y0_top": top_p, "przed_y0_top_n": n_p,
            "przed_y0_lider_n": kp.get(lider, 0),
            "lider_wsrod_wczesnych_najczestszy": top_w == lider,
        })
    d = pd.DataFrame(rows).sort_values("grupa")
    d.to_csv(args.out, index=False, encoding="utf-8-sig", lineterminator="\n")
    print(f"zapisane: {args.out}  ({len(d)} grup)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
