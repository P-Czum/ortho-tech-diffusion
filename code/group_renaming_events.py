"""group_renaming_events.py — ile odrebnych zdarzen kryje sie w parach powyzej progu.

Ta sama regula grupowania co przy pieedziesiatce (brief §1): dwie pary naleza do jednego
zdarzenia, gdy dziela token po stronie A ORAZ po stronie B; domkniecie przechodnie.

Implementacja jest inna niz przy 50 parach i to jest celowe. Tam porownywalem kazda z kazda,
co przy 10 562 parach daje 56 mln porownan. Tu klucz (token_A, token_B): wszystkie pary majace
ten sam token po stronie A i ten sam po stronie B sa wzajemnie polaczone, wiec wystarczy je
zlaczyc lancuchem. Kazde polaczenie z reguly ma jakis wspolny token po obu stronach, wiec
domkniecie przechodnie wychodzi identyczne — skrypt to sprawdza na pieedziesiatce.

Uruchom:
    python code/group_renaming_events.py --pairs results/renaming_pairs_above.csv \
        --out results/renaming_events.json
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

import numpy as np
import pandas as pd

PROGI = [0.2719, 0.35, 0.40, 0.45]
TOP_EVENTS = 30


class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def group_fast(A, B):
    """klucz (token_A, token_B) — liniowe wzgledem liczby par"""
    uf = UF()
    rep = {}
    for i, (a, b) in enumerate(zip(A, B)):
        uf.find(i)
        for t in set(a.split()):
            for u in set(b.split()):
                k = (t, u)
                if k in rep:
                    uf.union(i, rep[k])
                else:
                    rep[k] = i
    g = {}
    for i in range(len(A)):
        g.setdefault(uf.find(i), []).append(i)
    return list(g.values())


def group_pairwise(A, B):
    """regula wprost, kazda z kazda — tylko do sprawdzenia rownowaznosci na malym zbiorze"""
    uf = UF()
    tA = [set(a.split()) for a in A]
    tB = [set(b.split()) for b in B]
    for i in range(len(A)):
        uf.find(i)
        for j in range(i + 1, len(A)):
            if (tA[i] & tA[j]) and (tB[i] & tB[j]):
                uf.union(i, j)
    g = {}
    for i in range(len(A)):
        g.setdefault(uf.find(i), []).append(i)
    return list(g.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    d = pd.read_csv(args.pairs).sort_values("podobienstwo", ascending=False).reset_index(drop=True)
    print(f"par wczytanych: {len(d):,}  (min {d.podobienstwo.min():.4f}, "
          f"max {d.podobienstwo.max():.4f})")

    # kontrola rownowaznosci obu implementacji na pierwszych 50 parach
    s50 = d.head(50)
    f50 = {frozenset(x) for x in group_fast(s50.poprzednik_A.tolist(), s50.termin_B.tolist())}
    p50 = {frozenset(x) for x in group_pairwise(s50.poprzednik_A.tolist(), s50.termin_B.tolist())}
    print(f"kontrola na 50 parach: szybka {len(f50)} zdarzen, wprost {len(p50)}, "
          f"identyczne: {f50 == p50}")

    res = {"kontrola_rownowaznosci_na_50": {"szybka": len(f50), "wprost": len(p50),
                                            "identyczne": f50 == p50},
           "progi": {}}

    for prog in PROGI:
        sub = d[d.podobienstwo > prog].reset_index(drop=True)
        if not len(sub):
            continue
        groups = group_fast(sub.poprzednik_A.tolist(), sub.termin_B.tolist())
        sizes = np.array(sorted((len(g) for g in groups), reverse=True))
        res["progi"][str(prog)] = {
            "par": int(len(sub)), "zdarzen": int(len(groups)),
            "mediana_wielkosci": float(np.median(sizes)),
            "p90_wielkosci": float(np.percentile(sizes, 90)),
            "najwieksze": int(sizes[0]),
            "zdarzen_jednoparowych": int((sizes == 1).sum()),
            "udzial_najwiekszego_w_parach": round(float(sizes[0] / len(sub)), 4),
        }
        r = res["progi"][str(prog)]
        print(f"\nprog {prog}: par {r['par']:,} -> zdarzen {r['zdarzen']:,} | "
              f"mediana {r['mediana_wielkosci']:.0f}, p90 {r['p90_wielkosci']:.0f}, "
              f"najwieksze {r['najwieksze']:,}, jednoparowych {r['zdarzen_jednoparowych']:,}")

        if prog == PROGI[0]:
            groups.sort(key=len, reverse=True)
            top = []
            for g in groups[:TOP_EVENTS]:
                best = sub.loc[list(g)].sort_values("podobienstwo", ascending=False).iloc[0]
                top.append({"par": len(g), "poprzednik_A": best.poprzednik_A,
                            "termin_B": best.termin_B, "y0_B": int(best.y0_B),
                            "najlepsze": round(float(best.podobienstwo), 4)})
            res["najwieksze_zdarzenia"] = top
            print(f"\n{'par':>6}  {'poprzednik A':<30} {'termin B':<30} {'y0':>5} {'najl.':>7}")
            for t in top:
                print(f"{t['par']:>6}  {t['poprzednik_A']:<30} {t['termin_B']:<30} "
                      f"{t['y0_B']:>5} {t['najlepsze']:>7}")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisane: {args.out}")


if __name__ == "__main__":
    main()
