"""agreement.py — zgodnosc kodera-czlowieka z koderem-modelem (kodeks §5).

Kodeks v1.2 §5: "Cohen's kappa, threshold >= 0.70, reported alongside raw agreement and
weighted kappa (five categories of markedly unequal frequency make kappa alone unstable)".

Kappa wazona wymaga macierzy wag, a kodeks jej nie podaje. Dla pieciu kategorii NOMINALNYCH
nie ma naturalnego porzadku, wiec nie wymyslam wag. Zamiast tego licze kappe Brennana-Predigera,
ktora jest standardowa odpowiedzia dokladnie na problem opisany w kodeksie: przy skrajnie
nierownych czestosciach brzegowych kappa Cohena zanizat sie przez wysoki poziom zgodnosci
przypadkowej. BP zastepuje czestosci brzegowe rozkladem jednostajnym po kategoriach.
Rozbieznosc zglaszam, nie rozstrzygam sam.

Uruchom:
    python code/agreement.py --human coding_sheet_koder_CODED_2026-08-28.csv \
        --model results/model_coding.csv --out results/agreement.json
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

import numpy as np
import pandas as pd

CATS = ["novel concept", "renaming", "conceptual evolution",
        "measurement artifact", "non-technological term"]


def kappas(a: list[str], b: list[str], cats: list[str]) -> dict:
    k = len(cats)
    idx = {c: i for i, c in enumerate(cats)}
    m = np.zeros((k, k))
    for x, y in zip(a, b):
        m[idx[x], idx[y]] += 1
    n = m.sum()
    po = np.trace(m) / n
    pe_cohen = float((m.sum(0) / n) @ (m.sum(1) / n))
    return {
        "n": int(n),
        "zgodnosc_surowa": round(po, 4),
        "kappa_cohena": round((po - pe_cohen) / (1 - pe_cohen), 4) if pe_cohen < 1 else None,
        "pe_cohena": round(pe_cohen, 4),
        "kappa_brennana_predigera": round((po - 1 / k) / (1 - 1 / k), 4),
        "macierz": m.astype(int).tolist(),
        "kategorie": cats,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--human", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    h = pd.read_csv(args.human, encoding="utf-8-sig", dtype=str)
    m = pd.read_csv(args.model, encoding="utf-8-sig", dtype=str)
    if "run" in m and m["run"].nunique() > 1:
        m = m[m["run"] == m["run"].min()]
    j = h[["term", "kategoria", "step"]].merge(
        m[["term", "category", "step"]].rename(columns={"step": "step_model"}),
        on="term", how="inner")
    j = j[j["kategoria"].notna() & j["category"].notna()]
    print(f"terminow wspolnych: {len(j)} (podproba modelu: {len(m)}, arkusz: {len(h)})")

    unknown = set(j["kategoria"]) | set(j["category"]) - set(CATS)
    unknown -= set(CATS)
    if unknown:
        raise SystemExit(f"kategorie spoza listy: {sorted(unknown)}")

    res = {"kategoria": kappas(j["kategoria"].tolist(), j["category"].tolist(), CATS)}
    r = res["kategoria"]
    print(f"\nzgodnosc surowa: {r['zgodnosc_surowa']:.1%}")
    print(f"kappa Cohena:            {r['kappa_cohena']}   (prog kodeksu >= 0.70)")
    print(f"kappa Brennana-Predigera {r['kappa_brennana_predigera']}")
    print(f"zgodnosc przypadkowa Cohena: {r['pe_cohena']:.4f}")

    print(f"\n{'':<24}" + "".join(f"{c[:11]:>13}" for c in CATS) + "   (wiersze: czlowiek)")
    for i, c in enumerate(CATS):
        print(f"{c:<24}" + "".join(f"{v:>13}" for v in r["macierz"][i]))

    print("\nrozklady brzegowe:")
    for who, col in [("czlowiek", "kategoria"), ("model", "category")]:
        vc = j[col].value_counts()
        print(f"  {who:<9} " + ", ".join(f"{k}={v}" for k, v in vc.items()))

    st = j[j["step"].notna() & j["step_model"].notna()]
    if len(st):
        agree = (st["step"].astype(str).str.strip() == st["step_model"].astype(str).str.strip())
        res["step"] = {"n": int(len(st)), "zgodnosc_surowa": round(float(agree.mean()), 4)}
        both = st[agree & (st["kategoria"] != st["category"])]
        res["step_zgodny_kategoria_nie"] = int(len(both))
        print(f"\nzgodnosc na kroku drzewa: {agree.mean():.1%} z {len(st)}")
        print(f"  ten sam krok przy roznej kategorii: {len(both)} "
              f"(najostrzejsze miejsce niezgodnosci wg briefu Coworku)")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisane: {args.out}")


if __name__ == "__main__":
    main()
