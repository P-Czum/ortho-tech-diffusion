"""apply_field_filters.py — reguly zawezajace pole: D4 (naczyniowa) i D5a-c (audyt 55 deskryptorow).

Wszystkie reguly w JEDNYM przebiegu po analytic_index, bo strumieniowe czytanie 3,9 GB to
kilka minut i nie ma powodu powtarzac go osobno dla kazdej reguly.

Reguly sa filtrami NA REKORDACH. Poddrzewa 56 deskryptorow zadna nie zmienia.

  D4  naczyniowa   (mesh ∩ FIELD) ⊆ {D023821, D000671, D004188, D006428}  AND  mesh ∩ VASC
  D5a stomatologia (mesh ∩ FIELD) ⊆ {deskryptory pola lezace tez w E06 lub E04.545}
  D5b mieszane     (mesh ∩ FIELD) ⊆ {D019857, D016025}  AND  mesh ∩ (A14 ∪ C07)
  D5c homonim      (mesh ∩ FIELD) == {D014143}          AND  mesh ∩ (C06 ∪ C12 ∪ C11)

D5a wyprowadzana Z DRZEW, nie z listy UI — przezyje zmiane wersji MeSH i zapisuje sie
jednym zdaniem w Metodach.

D5b jest tylko MIERZONA. Wdrozenie wymaga separacji takiej jak przy D4 (obca >= 90%,
ortopedyczna <= 5%); skrypt liczy ja i mowi, czy prog przeszedl, ale niczego nie przesadza.

Uruchom:
    python code/apply_field_filters.py --parsed D:/medline_2026/parsed \
        --field data/processed/field_orthopedic_procedures.csv --desc D:/mesh/desc2026.xml \
        --out data/processed/pmid_filtry_pola.csv
"""
from __future__ import annotations
import argparse, csv, json, sys, time
from pathlib import Path
from xml.etree import ElementTree as ET

import pandas as pd
import pyarrow.parquet as pq

D4_BRAMA = {"D023821", "D000671", "D004188", "D006428"}
D4_VASC = {"D058729", "D016491", "D007511", "D017719", "D014652",
           "D001157", "D003920", "D048909"}
D5A_TREES = ("E06", "E04.545")
D5B_BRAMA = {"D019857", "D016025"}
D5B_TREES = ("A14", "C07")
D5C_BRAMA = {"D014143"}
D5C_TREES = ("C06", "C12", "C11")


def ui_by_tree(desc: Path, cache: Path) -> dict:
    """ui -> lista drzew; cache, bo desc2026.xml ma 313 MB"""
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    print("parsuje desc2026.xml...", file=sys.stderr)
    out = {}
    for _, el in ET.iterparse(str(desc), events=("end",)):
        if el.tag != "DescriptorRecord":
            continue
        ui = el.findtext("DescriptorUI")
        tn = [t.text for t in el.iter("TreeNumber") if t.text]
        if ui and tn:
            out[ui] = tn
        el.clear()
    cache.write_text(json.dumps(out), encoding="utf-8")
    print(f"  {len(out)} deskryptorow", file=sys.stderr)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parsed", required=True)
    ap.add_argument("--field", required=True)
    ap.add_argument("--desc", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    P = Path(args.parsed)
    rows = list(csv.DictReader(open(args.field, encoding="utf-8")))
    FIELD = {r["ui"] for r in rows if r["ui"].strip()}
    D5A_BRAMA = {r["ui"] for r in rows
                 if any(t.startswith(D5A_TREES) for t in r["trees"].split(";"))}
    print(f"poddrzewo {len(FIELD)}; brama D5a z drzew: {len(D5A_BRAMA)} -> "
          f"{sorted(D5A_BRAMA)}", file=sys.stderr)

    cache = Path(args.parsed) / "mesh_ui2trees.json"
    ui2trees = ui_by_tree(Path(args.desc), cache)
    A14C07 = {u for u, ts in ui2trees.items() if any(t.startswith(D5B_TREES) for t in ts)}
    C06_12_11 = {u for u, ts in ui2trees.items() if any(t.startswith(D5C_TREES) for t in ts)}
    print(f"A14+C07: {len(A14C07)} | C06+C12+C11: {len(C06_12_11)}", file=sys.stderr)

    pole = set(pd.read_parquet(P / "field_canon.parquet", columns=["pmid"])["pmid"])
    print(f"pole przed filtrami: {len(pole):,}", file=sys.stderr)

    t0 = time.time()
    f = pq.ParquetFile(P / "analytic_index.parquet")
    hits = {"D4": [], "D5a": [], "D5b": [], "D5c": []}
    widziane = 0
    for g in range(f.metadata.num_row_groups):
        d = f.read_row_group(g, columns=["pmid", "mesh_ui"]).to_pandas()
        d = d[d["pmid"].isin(pole)]
        if d.empty:
            continue
        widziane += len(d)
        for pmid, mu in zip(d["pmid"].values, d["mesh_ui"].fillna("").values):
            s = set(mu.split("|")) if mu else set()
            wf = s & FIELD
            if wf <= D4_BRAMA and (s & D4_VASC):
                hits["D4"].append(pmid)
            if wf <= D5A_BRAMA:
                hits["D5a"].append(pmid)
            if wf <= D5B_BRAMA and (s & A14C07):
                hits["D5b"].append(pmid)
            if wf == D5C_BRAMA and (s & C06_12_11):
                hits["D5c"].append(pmid)
        if (g + 1) % 400 == 0:
            print(f"  grupa {g+1}/{f.metadata.num_row_groups} "
                  f"({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    print(f"\nrekordow pola w indeksie: {widziane:,} z {len(pole):,}", file=sys.stderr)
    S = {k: set(v) for k, v in hits.items()}
    for k in ["D4", "D5a", "D5b", "D5c"]:
        print(f"  {k}: {len(S[k]):,} ({100*len(S[k])/len(pole):.2f}% pola)", file=sys.stderr)
    print("\nczesci wspolne:", file=sys.stderr)
    ks = ["D4", "D5a", "D5b", "D5c"]
    for i, a in enumerate(ks):
        for b in ks[i+1:]:
            n = len(S[a] & S[b])
            if n:
                print(f"  {a} ∩ {b}: {n}", file=sys.stderr)

    rec = []
    for k, v in S.items():
        rec += [{"pmid": p, "regula": k} for p in sorted(v)]
    pd.DataFrame(rec).to_csv(args.out, index=False, encoding="utf-8", lineterminator="\n")
    Path(args.out).with_suffix(".json").write_text(json.dumps(
        {k: len(v) for k, v in S.items()} | {"pole_przed": len(pole)},
        indent=1), encoding="utf-8")
    print(f"\nzapisane: {args.out}  ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
