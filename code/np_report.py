"""np_report.py — liczby porownawcze frazy vs n-gramy (brief §4).

Nie liczy niczego nowego: czyta tabele _np wyprodukowane przez count_noun_phrases.py
i detect_emergence.py, sklada rdzen jako czesc wspolna czterech wariantow i wypisuje
dokladnie te wielkosci, o ktore prosi brief. Zadnej oceny list.

Uruchom:
    python code/np_report.py --dir D:/medline_2026/parsed --out results/np_report.json
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

import numpy as np
import pandas as pd

VARIANTS = ["primary", "s1_title", "s2_abstract", "s3_english"]
SZUKANE = ["3d printing", "3d printed", "robotic", "robotic assisted", "machine learning",
           "artificial intelligence", "patient specific", "augmented reality",
           "virtual reality", "deep learning", "navigation"]


def contains(a: list[str], b: list[str]) -> bool:
    return len(a) < len(b) and any(b[i:i + len(a)] == a for i in range(len(b) - len(a) + 1))


def families(terms: list[str]):
    par = {t: t for t in terms}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for i, a in enumerate(terms):
        for b in terms[i + 1:]:
            ta, tb = a.split(), b.split()
            if contains(ta, tb) or contains(tb, ta):
                ra, rb = find(a), find(b)
                if ra != rb:
                    par[ra] = rb
    g = {}
    for t in terms:
        g.setdefault(find(t), []).append(t)
    return [v for v in g.values() if len(v) > 1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    D = Path(args.dir)

    res = {}
    emsets = {}
    for v in VARIANTS:
        d = pd.read_parquet(D / f"emerging_np_{v}.parquet")
        emsets[v] = set(d.loc[d["emerging"], "term"])
        res[f"jednostek_{v}"] = int(len(d))
        res[f"wschodzacych_{v}"] = int(len(emsets[v]))
        print(f"{v:<12} jednostek {len(d):>8,}  wschodzacych {len(emsets[v]):>7,}")

    core = set.intersection(*emsets.values())
    prim = pd.read_parquet(D / "emerging_np_primary.parquet")
    rank = prim[prim["emerging"] & prim["term"].isin(core)].sort_values(
        "prevalence_2021_2025", ascending=False, kind="stable").reset_index(drop=True)
    res["rdzen"] = len(core)
    print(f"\nrdzen (czesc wspolna czterech wariantow): {len(core)}")

    terms = rank["term"].tolist()
    fam = families(terms)
    res["rodzin_zawierania"] = len(fam)
    res["terminow_w_rodzinach"] = sum(len(f) for f in fam)
    print(f"rodzin zawierania: {len(fam)}, terminow objetych: {sum(len(f) for f in fam)}")

    rob = [t for t in terms if any(w.startswith("robot") for w in t.split())]
    pr3d = [t for t in terms if any(w.startswith("print") or w == "3d" for w in t.split())]
    res["rodzina_robot"] = rob
    res["rodzina_3d_print"] = pr3d
    print(f"\nrodzina robot* w rdzeniu: {len(rob)} wierszy -> {rob}")
    print(f"rodzina 3d/print* w rdzeniu: {len(pr3d)} wierszy -> {pr3d}")

    dl = rank["n"].value_counts().sort_index()
    res["dlugosci_rdzenia"] = {int(k): int(v) for k, v in dl.items()}
    print("\ndlugosci fraz w rdzeniu:", ", ".join(f"{k}-tokenowe {v}" for k, v in dl.items()))

    pos = {t: (terms.index(t) + 1 if t in terms else None) for t in SZUKANE}
    res["pozycje_w_rdzeniu"] = pos
    print("\npozycje w rdzeniu:")
    for t, p in pos.items():
        print(f"  {t:<26} {p if p else '— poza rdzeniem'}")

    top50 = rank.head(50)[["term", "n", "y0", "prevalence_2021_2025", "docs_total"]].copy()
    top50["prevalence_pct"] = (100 * top50["prevalence_2021_2025"]).round(3)
    res["top50_rdzenia"] = top50[["term", "n", "y0", "prevalence_pct", "docs_total"]] \
        .to_dict("records")
    print("\n=== 50 pierwszych rdzenia po prevalence 2021-2025 ===")
    for i, r in enumerate(res["top50_rdzenia"], 1):
        print(f"{i:>3}  {r['term']:<38} n={r['n']}  y0={r['y0']}  {r['prevalence_pct']}%")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisane: {args.out}")


if __name__ == "__main__":
    main()
