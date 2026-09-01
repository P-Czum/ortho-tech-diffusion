"""apply_d4_filter.py — decyzja D4: wylaczenie pismiennictwa naczyniowego z pola.

Poddrzewo `Orthopedic Procedures` ma wsrod 56 potomkow `Amputation, Surgical` (D000671),
`Limb Salvage` (D023821), `Disarticulation` (D004188) i `Hemipelvectomy` (D006428). Wchodzi
tedy pismiennictwo o niedokrwieniu konczyn, ktore ortopedia nie jest.

Regula D4 (scoping_log, wpis 2026-08-31) — rekord wylaczony, gdy:

    (mesh_ui przeciete FIELD) zawiera sie w {D023821, D000671, D004188, D006428}
        ORAZ
    (mesh_ui przeciete VASC) niepuste

Pierwszy warunek: rekord wchodzi do pola WYLACZNIE przez amputacje albo ratowanie konczyny.
Drugi: ma jednoczesnie deskryptor naczyniowy albo cukrzycowy. Sama amputacja nie wystarcza —
`transfemoral amputation` zostaje w polu swiadomie, bo to protetyka i rehabilitacja.

Regula jest filtrem NA REKORDACH. Poddrzewa 56 deskryptorow nie rusza.

Uruchom:
    python code/apply_d4_filter.py --parsed D:/medline_2026/parsed \
        --field data/processed/field_orthopedic_procedures.csv \
        --out data/processed/pmid_d4_wylaczone.csv
"""
from __future__ import annotations
import argparse, csv, sys, time
from pathlib import Path

import pandas as pd
import pyarrow.parquet as pq

BRAMA = {"D023821", "D000671", "D004188", "D006428"}
VASC = {"D058729", "D016491", "D007511", "D017719", "D014652",
        "D001157", "D003920", "D048909"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parsed", required=True)
    ap.add_argument("--field", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--porownaj", help="lista PMID od Coworku do kontroli")
    args = ap.parse_args()

    P = Path(args.parsed)
    uis = {r["ui"] for r in csv.DictReader(open(args.field, encoding="utf-8")) if r["ui"].strip()}
    print(f"poddrzewo: {len(uis)} deskryptorow", file=sys.stderr)
    assert BRAMA <= uis, f"deskryptory bramy spoza poddrzewa: {BRAMA - uis}"

    pole = set(pd.read_parquet(P / "field_canon.parquet", columns=["pmid"])["pmid"])
    print(f"pole przed D4: {len(pole):,}", file=sys.stderr)

    t0 = time.time()
    f = pq.ParquetFile(P / "analytic_index.parquet")
    wyl, widziane = [], 0
    for g in range(f.metadata.num_row_groups):
        d = f.read_row_group(g, columns=["pmid", "mesh_ui"]).to_pandas()
        d = d[d["pmid"].isin(pole)]
        if d.empty:
            continue
        widziane += len(d)
        for pmid, mu in zip(d["pmid"].values, d["mesh_ui"].fillna("").values):
            s = set(mu.split("|")) if mu else set()
            if (s & uis) <= BRAMA and (s & VASC):
                wyl.append(pmid)
        if (g + 1) % 200 == 0:
            print(f"  grupa {g+1}/{f.metadata.num_row_groups}, dopasowanych {widziane:,}, "
                  f"wylaczonych {len(wyl):,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    wyl = sorted(set(wyl))
    print(f"\nrekordow pola znalezionych w indeksie: {widziane:,} z {len(pole):,}", file=sys.stderr)
    print(f"wylaczonych przez D4: {len(wyl):,} ({100*len(wyl)/len(pole):.2f}% pola)",
          file=sys.stderr)
    print(f"pole po D4: {len(pole)-len(wyl):,}", file=sys.stderr)

    pd.DataFrame({"pmid": wyl}).to_csv(args.out, index=False, encoding="utf-8",
                                       lineterminator="\n")
    if args.porownaj:
        ref = set(pd.read_csv(args.porownaj, dtype=str)["pmid"])
        mine = set(wyl)
        print(f"\nkontrola wobec {args.porownaj}: Cowork {len(ref):,}, moje {len(mine):,}",
              file=sys.stderr)
        print(f"  wspolnych {len(ref & mine):,} | tylko u Coworku {len(ref - mine):,} | "
              f"tylko u mnie {len(mine - ref):,}", file=sys.stderr)
    print(f"czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
