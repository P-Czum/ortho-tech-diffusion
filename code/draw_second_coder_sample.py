"""draw_second_coder_sample.py — podproba 60 terminow dla drugiego kodera (kodeks §5).

Kodeks v1.2 §5, zamrozony i w manifescie, mowi: "stratified random sample by y0 epoch
(2005-2012 / 2013-2019 / 2020+ -> proportional allocation 6 / 36 / 18) AND n-gram length".

Funkcja stratified() w llm_coder.py warstwuje WYLACZNIE po epoce, bez dlugosci n-gramu.
Ten skrypt realizuje regule zarejestrowana, czyli warstwowanie dwuwymiarowe. Rozbieznosc
zglaszam osobno; llm_coder.py zostawiam nietkniety i podaje mu gotowa podprobe przez
--sheet z --n 0, zeby nie bylo dwoch implementacji tej samej reguly.

Kwoty komorek wychodza ulamkowe (0,6 / 1,9 / 3,1 ...), wiec zaokraglam metoda najwiekszych
reszt: kazda komorka dostaje czesc calkowita, a pozostale miejsca ida do komorek o najwiekszej
reszcie. Metoda jest deterministyczna i sumuje sie dokladnie do 60.

Losowanie odbywa sie na ZAMROZONYM arkuszu kodera, ktory nie zawiera zadnych kategorii —
podproba jest wiec wyznaczona bez wgladu w kodowanie czlowieka.

Uruchom:
    python code/draw_second_coder_sample.py --sheet data/processed/coding_sheet_koder.csv \
        --out data/processed/second_coder_sample.csv
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20260827          # to samo ziarno co w llm_coder.py — czesc rejestracji
N_SUB = 60
EPOKI = [(2005, 2012, "2005-2012"), (2013, 2019, "2013-2019"), (2020, 2025, "2020+")]


def largest_remainder(counts: dict, total: int) -> dict:
    n = sum(counts.values())
    exact = {k: total * v / n for k, v in counts.items()}
    base = {k: int(v) for k, v in exact.items()}
    left = total - sum(base.values())
    for k in sorted(exact, key=lambda k: (-(exact[k] - base[k]), k))[:left]:
        base[k] += 1
    return base


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--n", type=int, default=N_SUB)
    ap.add_argument("--seed", type=int, default=SEED)
    args = ap.parse_args()

    df = pd.read_csv(args.sheet, encoding="utf-8-sig", dtype=str)
    if "kategoria" in df and df["kategoria"].fillna("").str.strip().any():
        raise SystemExit("arkusz zawiera kategorie — podproba musi byc losowana na widoku "
                         "zaslepionym, bez wgladu w kodowanie")
    df["y0"] = df["y0"].astype(int)
    df["n"] = df["n"].astype(int)

    def epoka(y):
        for a, b, lab in EPOKI:
            if a <= y <= b:
                return lab
        raise ValueError(y)

    df["epoka"] = df["y0"].map(epoka)
    cells = {(e, n): len(g) for (e, n), g in df.groupby(["epoka", "n"])}
    quota = largest_remainder(cells, args.n)

    rng = np.random.default_rng(args.seed)
    picked = []
    for key in sorted(cells):
        grp = df[(df["epoka"] == key[0]) & (df["n"] == key[1])]
        k = min(quota[key], len(grp))
        if k:
            picked.extend(rng.choice(grp.index.values, size=k, replace=False).tolist())
    sub = df.loc[sorted(picked)].drop(columns=["epoka"])

    print(f"{'epoka':<12} {'n':>2} {'w arkuszu':>10} {'kwota':>6} {'wylosowano':>11}")
    for key in sorted(cells):
        got = len(sub[(sub['y0'].map(epoka) == key[0]) & (sub['n'] == key[1])])
        print(f"{key[0]:<12} {key[1]:>2} {cells[key]:>10} {quota[key]:>6} {got:>11}")
    print(f"{'RAZEM':<12} {'':>2} {len(df):>10} {sum(quota.values()):>6} {len(sub):>11}")
    for a, b, lab in EPOKI:
        print(f"  epoka {lab}: {(sub['y0'].between(a, b)).sum()} "
              f"(kodeks §5 przewiduje {round(args.n * (df['y0'].between(a, b)).sum() / len(df))})")

    out = Path(args.out)
    sub.to_csv(out, index=False, encoding="utf-8-sig", lineterminator="\n")
    h = hashlib.sha256(out.read_bytes()).hexdigest()
    meta = {"ziarno": args.seed, "rozmiar": len(sub), "arkusz_zrodlowy": args.sheet,
            "sha256_arkusza": hashlib.sha256(Path(args.sheet).read_bytes()).hexdigest(),
            "sha256_podproby": h, "kwoty": {f"{k[0]}|n={k[1]}": v for k, v in quota.items()},
            "terminy": sub["term"].tolist()}
    out.with_suffix(".meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False),
                                             encoding="utf-8")
    print(f"\nzapisane: {out}\n  sha256 podproby: {h[:16]}…")


if __name__ == "__main__":
    main()
