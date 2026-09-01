"""mtix_impact.py — czy nieciaglosc MTIX-2022 przesuwa ranking, czy tylko mianownik.

mtix_check.py pokazal, ze po 2022 sklad deskryptorow pola przesuwa sie z terminow ogolnych
na szczegolowe (Orthopedic Procedures -2,94 pp, Arthroplasty Replacement Knee +1,19 pp).
Przynaleznosc do pola to przezywa, bo rodzic i dziecko sa w tym samym poddrzewie — ale
ZAWARTOSC pola sie zmienia, a tego mianownik nie koryguje.

Dwa testy, oba na materiale:

  T1 SKOK NA PRZEJSCIU. Dla kazdego terminu dopasowujemy trend log-udzialu na latach
     2015-2021 (przed MTIX) i porownujemy przewidywanie na 2023-2025 z obserwacja.
     Termin, ktory skacze w gore ponad przedzial trendu, jest podejrzany o premie MTIX;
     w dol — o kare. Rozklad reszt mowi, czy to zjawisko systematyczne, czy szum.

  T2 STABILNOSC RANKINGU. Korelacja rangowa miedzy osia obecnosci (prevalence 2021-2025,
     wrazliwa na mianownik) a osia przekroczenia progu (iloraz, znacznie mniej wrazliwa).
     Liczona osobno na oknie przed MTIX i po. Jesli os obecnosci sie rozjezdza, a os
     przekroczenia nie — mamy gotowa zamienna, ktora plan juz przewiduje.

Uruchom:
    python code/mtix_impact.py --emerging D:/medline_2026/parsed/emerging_w2000_primary.parquet \
        --denom D:/medline_2026/parsed/terms_w2000_primary.denom.json \
        --terms data/processed/material_final.csv --out results/mtix_impact.json
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

TREND_OD, TREND_DO = 2015, 2021
PO_OD, PO_DO = 2023, 2025


def main() -> int:
    ap = argparse.ArgumentParser()
    for a in ("--emerging", "--denom", "--terms", "--out"):
        ap.add_argument(a, required=True)
    args = ap.parse_args()

    em = pd.read_parquet(args.emerging).set_index("term")
    den = json.loads(Path(args.denom).read_text(encoding="utf-8"))["by_year"]
    lata = sorted(int(y) for y in den)
    dv = np.array([den[str(y)] for y in lata], float)
    terms = [t for t in pd.read_csv(args.terms, encoding="utf-8-sig")["term"]
             if t in em.index]
    print(f"terminow materialu obecnych w tabeli: {len(terms)}", file=sys.stderr)

    i1, i2 = lata.index(TREND_OD), lata.index(TREND_DO)
    j1, j2 = lata.index(PO_OD), lata.index(PO_DO)
    wier = []
    for t in terms:
        r = em.loc[t]
        s = np.array([r[f"y{y}"] for y in lata], float) / dv
        tr = s[i1:i2 + 1]
        m = tr > 0
        if m.sum() < 5:
            continue
        xs = np.arange(i1, i2 + 1)[m]
        b, a = np.polyfit(xs, np.log(tr[m]), 1)
        resid = np.log(tr[m]) - (a + b * xs)
        sd = float(resid.std(ddof=2)) or 1e-9
        xo = np.arange(j1, j2 + 1)
        obs = s[j1:j2 + 1]
        with np.errstate(divide="ignore"):
            z = float(np.mean((np.log(np.where(obs > 0, obs, np.nan)) - (a + b * xo)) / sd))
        wier.append({"term": t, "trend_rocznie_pct": round(100 * (np.exp(b) - 1), 1),
                     "z_po_mtix": round(z, 2)})

    d = pd.DataFrame(wier).sort_values("z_po_mtix")
    zs = d["z_po_mtix"].dropna()
    print(f"\n=== T1: skok na przejsciu 2022 (z = odchylenie od trendu 2015-2021) ===")
    print(f"  terminow: {len(zs)} | mediana z = {zs.median():+.2f} | "
          f"srednia {zs.mean():+.2f} | sd {zs.std():.2f}")
    print(f"  |z| > 2: {int((zs.abs() > 2).sum())} | z > 2: {int((zs > 2).sum())} | "
          f"z < -2: {int((zs < -2).sum())}")
    print(f"\n  najmocniej PONIZEJ trendu:")
    for _, r in d.head(6).iterrows():
        print(f"    {r.term:<44} z={r.z_po_mtix:>6.2f}  trend {r.trend_rocznie_pct:+.1f}%/rok")
    print(f"  najmocniej POWYZEJ trendu:")
    for _, r in d.tail(6).iloc[::-1].iterrows():
        print(f"    {r.term:<44} z={r.z_po_mtix:>6.2f}  trend {r.trend_rocznie_pct:+.1f}%/rok")

    # T2: stabilnosc rankingu — obecnosc kontra przekroczenie progu
    sub = em.loc[[t for t in terms if t in em.index]].copy()
    okna = {"przed MTIX 2017-2021": (2017, 2021), "po MTIX 2023-2025": (2023, 2025)}
    res_rank = {}
    for nazwa, (a_, b_) in okna.items():
        k1, k2 = lata.index(a_), lata.index(b_)
        cnt = sub[[f"y{y}" for y in range(a_, b_ + 1)]].to_numpy(float).sum(1)
        obec = cnt / dv[k1:k2 + 1].sum()
        prog = np.maximum(0.001, 5.0 * sub["baseline_share"].to_numpy(float))
        szczyt = np.array([max((sub.loc[t, f"y{y}"] / den[str(y)]) for y in range(a_, b_ + 1))
                           for t in sub.index])
        przekr = szczyt / prog
        rho = stats.spearmanr(obec, przekr).statistic
        res_rank[nazwa] = {"spearman_obecnosc_przekroczenie": round(float(rho), 3)}
        print(f"\n=== T2: {nazwa} — Spearman obecnosc vs przekroczenie: {rho:.3f}")

    # czy ranking po obecnosci sam sie przestawia miedzy oknami
    k = {}
    for nazwa, (a_, b_) in okna.items():
        cnt = sub[[f"y{y}" for y in range(a_, b_ + 1)]].to_numpy(float).sum(1)
        kk = lata.index(a_), lata.index(b_)
        k[nazwa] = cnt / dv[kk[0]:kk[1] + 1].sum()
    rho_ob = stats.spearmanr(*k.values()).statistic
    print(f"\n  ranking po OBECNOSCI, przed wobec po: Spearman {rho_ob:.3f}")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(
        {"t1": d.to_dict("records"), "t2": res_rank,
         "spearman_obecnosc_przed_po": round(float(rho_ob), 3),
         "mediana_z": round(float(zs.median()), 3)},
        indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisane: {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
