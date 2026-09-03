"""kontrast_leki.py — warstwa kontrastowa: leki policzone na tym samym detektorze co material.

Leki sa technologia definicyjnie (kodeks v1.3 §2, decyzja ortopedy 2026-08-31), ale wychodza
z materialu glownego, bo dyfunduja bez ograniczen szkoleniowych i kapitalowych, ktore ksztaltuja
technike operacyjna. Raportowane osobno jako warstwa kontrastowa.

Pierwsza wersja pliku powstala doraznie 2026-09-01, PRZED filtrami pola D4/D5a/D5c/D6, i dwa
z siedmiu lekow mialy przez to y0 starsze o trzy lata (multimodal analgesia 2021 zamiast 2018,
local infiltration analgesia 2017 zamiast 2014). Ten skrypt odtwarza plik z biezacego detektora.

Kolumna `w_rdzeniu_4` z pierwszej wersji odnosila sie do rdzenia czterech wariantow tekstu
z ery n-gramow. Po D-2 rdzen ma trzy warianty, wiec kolumna nazywa sie `w_rdzeniu`.
Kolumna `pozycja` (ranga w tamtej liscie kandydatow) nie ma odpowiednika i wypada.

Uruchom:
    python code/kontrast_leki.py --out data/processed/kontrast_leki.csv
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

import pandas as pd

P = Path("D:/medline_2026/parsed")

# siedem fraz zakwalifikowanych przez ortopede jako lek albo schemat lekowy
LEKI = ["tranexamic acid", "dexamethasone", "multimodal analgesia", "vte prophylaxis",
        "local infiltration analgesia", "liposomal bupivacaine", "rivaroxaban"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    em = pd.read_parquet(P / "emerging_d6_primary.parquet").set_index("term")
    rdzen = set(json.loads(Path("data/processed/rdzen_d6.json").read_text(encoding="utf-8")))

    rows = []
    for t in LEKI:
        if t not in em.index:
            print(f"UWAGA: {t} nie ma w detektorze", file=sys.stderr)
            continue
        e = em.loc[t]
        rows.append({
            "term": t,
            "kategoria": "lek",
            "n": int(e.n),
            "y0": int(e.y0) if e.emerging else None,
            "peak_year": int(e.peak_year),
            "docs_total": int(e.docs_total),
            "prevalence_pct": round(100 * float(e.prevalence_2021_2025), 3),
            "peak_share_pct": round(100 * float(e.peak_share), 3),
            "w_rdzeniu": t in rdzen,
        })

    d = pd.DataFrame(rows).sort_values("docs_total", ascending=False)
    d.to_csv(args.out, index=False, encoding="utf-8-sig", lineterminator="\n")
    print(d.to_string(index=False))
    print(f"\nzapisane: {args.out}  ({len(d)} lekow, {int(d.w_rdzeniu.sum())} w rdzeniu)",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
