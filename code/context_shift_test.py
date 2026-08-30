"""context_shift_test.py — czy przemianowanie widac w kontekstach uzycia.

Hipoteza: jesli dwa terminy nazywaja to samo pojecie, to rekordy ich uzywajace maja
podobne otoczenie leksykalne, nawet gdy okna lat sa rozlaczne.

DECYZJE PODJETE PRZED POLICZENIEM (brief §3: zadnego strojenia progow pod wynik):

  korpus            field_canon.parquet, 268 383 rekordow pola def1, 2005-2025,
                    tekst po kanonizacji z §3.1. Jeden zbior przez caly test.
  wystapienie       dopasowanie ciaglego ciagu tokenow w polu `canon`
  slownik kontekstu unigramy o czestosci dokumentowej >= MIN_DF w calym korpusie
  wektor            dla terminu t w oknie W: czestosc DOKUMENTOWA kazdego unigramu
                    w rekordach zawierajacych t, wazona PPMI wzgledem tla TEGO SAMEGO
                    okna. Tlo per-okno, bo inaczej mierzylibysmy dryf czestosci w czasie.
  wykluczenia       z obu wektorow usuwane sa tokeny OBU porownywanych terminow,
                    tak samo dla par docelowych i losowych
  podobienstwo      kosinus
  rozklad odniesien N_RANDOM par losowych na pare docelowa, dobranych tak, by liczebnosci
                    w obu oknach miescily sie w +/- TOL wzgledem pary docelowej
  ziarno            SEED, ustalone z gory

Uruchom:
    python code/context_shift_test.py --out results/context_shift.json
"""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

CANON = "D:/medline_2026/parsed/field_canon.parquet"
EMERGING = "D:/medline_2026/parsed/emerging_primary.parquet"
MIN_DF = 50          # unigram musi wystapic w >= 50 rekordach korpusu
TOL = 0.30           # tolerancja doboru liczebnosci w parach losowych
N_RANDOM = 200
MIN_DOCS_POOL = 20   # termin wchodzi do puli losowania, gdy ma >= tylu prac ogolem
SEED = 20260828

PAIRS = [
    ("para 1 druk 3D", ("rapid prototyping", 2008, 2013), ("3d printing", 2016, 2021)),
    ("para 2 nawigacja robot", ("computer navigation", 2008, 2013), ("robotic", 2018, 2023)),
]
# Kontrola pozytywna zamowiona w briefie opiera sie na 6 rekordach w oknie wczesnym,
# wiec mierzy rzadkosc, nie gorny kres miary. Druga kontrola pozytywna ma przyzwoita
# liczebnosc po obu stronach i dopiero ona jest uzytecznym gornym kresem.
CONTROLS = [
    ("kontrola + zamowiona", ("3d printing", 2008, 2013), ("3d printing", 2016, 2021)),
    ("kontrola + liczebna", ("venous thromboembolism", 2008, 2013),
                            ("venous thromboembolism", 2016, 2021)),
    ("kontrola -", ("3d printing", 2016, 2021), ("venous thromboembolism", 2016, 2021)),
]


class Corpus:
    def __init__(self):
        d = pd.read_parquet(CANON, columns=["year", "canon"])
        self.year = d["year"].to_numpy()
        self.text = d["canon"].to_numpy()
        df = Counter()
        sets = []
        for s in self.text:
            t = set(s.split())
            sets.append(t)
            df.update(t)
        self.df = df
        self.vocab = {w: i for i, w in enumerate(sorted(w for w, c in df.items() if c >= MIN_DF))}
        self.V = len(self.vocab)
        self.ids = [np.fromiter((self.vocab[w] for w in t if w in self.vocab), dtype=np.int32)
                    for t in sets]
        # indeks odwrotny token -> rekordy. Bez niego kazde sprawdzenie terminu skanuje
        # cale okno (~80 tys. lancuchow), a rozklad odniesienia potrzebuje tysiecy sprawdzen.
        rows = np.repeat(np.arange(len(self.ids), dtype=np.int32),
                         np.fromiter((len(x) for x in self.ids), dtype=np.int64))
        cols = np.concatenate(self.ids)
        order = np.argsort(cols, kind="stable")
        cuts = np.searchsorted(cols[order], np.arange(self.V + 1))
        rows_sorted = rows[order]
        self.post = [rows_sorted[cuts[i]:cuts[i + 1]] for i in range(self.V)]
        self._bg = {}
        self._hits = {}
        self._inwin = {}

    def window(self, a, b):
        return np.flatnonzero((self.year >= a) & (self.year <= b))

    def bg(self, a, b):
        """tlo okna: czestosc dokumentowa kazdego unigramu / liczba rekordow okna"""
        if (a, b) not in self._bg:
            idx = self.window(a, b)
            c = np.bincount(np.concatenate([self.ids[i] for i in idx]), minlength=self.V)
            self._bg[(a, b)] = c / len(idx)
        return self._bg[(a, b)]

    def inwin(self, a, b):
        if (a, b) not in self._inwin:
            self._inwin[(a, b)] = (self.year >= a) & (self.year <= b)
        return self._inwin[(a, b)]

    def hits(self, term, a, b):
        """rekordy okna zawierajace termin jako ciagly ciag tokenow"""
        k = (term, a, b)
        if k in self._hits:
            return self._hits[k]
        toks = term.split()
        if all(w in self.vocab for w in toks):
            # kandydaci z najrzadszego tokenu, potem dopasowanie ciaglosci
            cand = min((self.post[self.vocab[w]] for w in toks), key=len)
        else:
            cand = self.window(a, b)          # termin ma token ponizej MIN_DF
        m = self.inwin(a, b)
        pat = " " + term + " "
        self._hits[k] = np.array([i for i in cand if m[i] and pat in self.text[i]],
                                 dtype=np.int64)
        return self._hits[k]

    def maxhits(self, term):
        """gorne ograniczenie liczby wystapien: min czestosci dokumentowej tokenow"""
        return min(self.df.get(w, 0) for w in term.split())

    def vector(self, term, a, b, drop):
        idx = self.hits(term, a, b)
        if len(idx) == 0:
            return None, 0
        p = np.bincount(np.concatenate([self.ids[i] for i in idx]), minlength=self.V) / len(idx)
        bg = self.bg(a, b)
        ok = (p > 0) & (bg > 0)
        v = np.zeros(self.V)
        v[ok] = np.maximum(0.0, np.log2(p[ok] / bg[ok]))
        v[drop] = 0.0
        return v, len(idx)


def sim(C, t1, t2):
    drop = [C.vocab[w] for w in set(t1[0].split()) | set(t2[0].split()) if w in C.vocab]
    u, n1 = C.vector(*t1, drop)
    v, n2 = C.vector(*t2, drop)
    if u is None or v is None:
        return float("nan"), n1, n2
    nu, nv = np.linalg.norm(u), np.linalg.norm(v)
    return (float(u @ v / (nu * nv)) if nu and nv else float("nan")), n1, n2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    print("wczytuje korpus...", flush=True)
    C = Corpus()
    print(f"  {len(C.text)} rekordow, slownik {C.V} unigramow (df >= {MIN_DF})", flush=True)

    pool = pd.read_parquet(EMERGING, columns=["term", "docs_total"])
    pool = pool[pool["docs_total"] >= MIN_DOCS_POOL]["term"].tolist()
    rng = np.random.default_rng(SEED)
    print(f"  pula terminow do par losowych: {len(pool)}", flush=True)

    res = {"parametry": {"MIN_DF": MIN_DF, "TOL": TOL, "N_RANDOM": N_RANDOM, "SEED": SEED,
                         "MIN_DOCS_POOL": MIN_DOCS_POOL, "korpus": CANON,
                         "miara": "kosinus wektorow PPMI, tlo per-okno"},
           "kontrole": {}, "pary": {}}

    for name, t1, t2 in CONTROLS:
        s, n1, n2 = sim(C, t1, t2)
        res["kontrole"][name] = {"sim": s, "n1": n1, "n2": n2,
                                 "opis": f"{t1[0]} [{t1[1]}-{t1[2]}] vs {t2[0]} [{t2[1]}-{t2[2]}]"}
        print(f"{name:<24} {s:.4f}   n={n1}/{n2}", flush=True)

    def draw(lo, hi, a, b, need):
        """termin nie moze miec wiecej wystapien niz najrzadszy jego token — ten
        warunek odsiewa wiekszosc puli bez dotykania tekstu"""
        out = []
        for j in rng.permutation(len(pool)):
            t = pool[j]
            if C.maxhits(t) < lo:
                continue
            if lo <= len(C.hits(t, a, b)) <= hi:
                out.append(t)
                if len(out) >= need:
                    break
        return out

    for name, t1, t2 in PAIRS:
        s, n1, n2 = sim(C, t1, t2)
        print(f"\n{name}: sim={s:.4f}  n={n1}/{n2}", flush=True)
        A = draw(n1 * (1 - TOL), n1 * (1 + TOL), t1[1], t1[2], N_RANDOM)
        B = draw(n2 * (1 - TOL), n2 * (1 + TOL), t2[1], t2[2], N_RANDOM)
        print(f"  dobrano {len(A)} terminow do okna 1, {len(B)} do okna 2", flush=True)
        null, who = [], []
        for a_, b_ in zip(A, B):
            if a_ == b_:
                continue
            s_, _, _ = sim(C, (a_, t1[1], t1[2]), (b_, t2[1], t2[2]))
            if not np.isnan(s_):
                null.append(s_)
                who.append((a_, b_))
        null = np.array(null)
        top = sorted(zip(null, who), reverse=True)[:5]
        print("  najwyzsze pary losowe: " +
              "; ".join(f"{v:.4f} {x} / {y}" for v, (x, y) in top), flush=True)
        pct = float((null < s).mean() * 100)
        res["pary"][name] = {
            "sim": s, "n1": n1, "n2": n2,
            "opis": f"{t1[0]} [{t1[1]}-{t1[2]}] vs {t2[0]} [{t2[1]}-{t2[2]}]",
            "n_par_losowych": len(null),
            "null_srednia": float(null.mean()), "null_sd": float(null.std()),
            "null_p50": float(np.percentile(null, 50)),
            "null_p95": float(np.percentile(null, 95)),
            "null_max": float(null.max()), "percentyl_pary": pct,
            "najwyzsze_pary_losowe": [[float(v), x, y] for v, (x, y) in top],
        }
        print(f"  rozklad losowy: srednia {null.mean():.4f}, p50 {np.percentile(null, 50):.4f}, "
              f"p95 {np.percentile(null, 95):.4f}, max {null.max():.4f}  (n={len(null)})",
              flush=True)
        print(f"  PERCENTYL PARY DOCELOWEJ: {pct:.1f}", flush=True)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisane: {args.out}")


if __name__ == "__main__":
    main()
