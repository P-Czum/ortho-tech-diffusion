"""zaniki_przed_scaleniem.py — ile zanikow widac termin po terminie, a ile zostaje po scaleniu w grupy.

Zanik = udzial w 2025 / udzial w szczycie < 0,5 (ta sama regula co osie_{nr}.csv).
Termin liczony osobno (szereg z terms_d6_primary), grupa ze zliczaniem unijnym (osie_{nr}).
Kazdy termin w zaniku trafia do jednej z dwoch klas:
  druga_nazwa   — grupa tez zanika, a termin nie jest pierwszym w niej (duplikat wiersza);
  przesuniecie  — grupa jako calosc nie zanika (uwage przejmuje inny czlon).

Uruchom:
    python code/zaniki_przed_scaleniem.py --nr 48
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

import numpy as np
import pandas as pd

P = Path("D:/medline_2026/parsed")
D = Path("data/processed")
YC = [f"y{y}" for y in range(2000, 2026)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nr", required=True)
    nr = ap.parse_args().nr

    m = pd.read_csv(D / f"material_{nr}.csv", encoding="utf-8-sig")
    o = pd.read_csv(D / f"osie_{nr}.csv", encoding="utf-8-sig").set_index("grupa")
    t = pd.read_parquet(P / "terms_d6_primary.parquet", columns=["term"] + YC).set_index("term")
    den = json.loads((P / "terms_d6_primary.denom.json").read_text(encoding="utf-8"))["by_year"]
    s = t.reindex(m.term)[YC].to_numpy(float) / np.array([den[y[1:]] for y in YC], float)

    m["trw_terminu"] = np.round(s[:, -1] / s.max(axis=1), 4)
    m["trw_grupy"] = m.grupa.map(o.trwalosc_2025_do_szczytu)
    z = m[m.trw_terminu < 0.5].sort_values(["grupa", "trw_terminu"]).copy()
    pierwszy = ~z.duplicated("grupa")
    z["klasa_zaniku"] = np.where(z.trw_grupy >= 0.5, "przesuniecie",
                                 np.where(pierwszy, "zanik_grupy", "druga_nazwa"))
    z[["term", "trw_terminu", "grupa", "trw_grupy", "klasa_zaniku"]].to_csv(
        Path("results") / f"zaniki_przed_scaleniem_{nr}.csv", index=False, encoding="utf-8-sig",
        lineterminator="\n")

    n_gr = int((o.trwalosc_2025_do_szczytu < 0.5).sum())
    print(f"terminow w zaniku {len(z)}, grup w zaniku {n_gr}, usuwa scalenie {len(z) - n_gr}")
    print(z.klasa_zaniku.value_counts().to_string())
    print("grupy z przesunieciem:", sorted(z.grupa[z.klasa_zaniku == "przesuniecie"].unique()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
