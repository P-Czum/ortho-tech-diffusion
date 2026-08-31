"""renaming_precision_test.py — ile par wskazanych przez miare to prawdziwe przemianowania.

Test kontekstowy pokazal czulosc na dwoch parach znanych z gory. Ten test pyta odwrotnie:
gdy miara sama generuje kandydatow, ile z najwyzej punktowanych sie broni.

REGULA GENEROWANIA PAR — zapisana przed uruchomieniem (brief §2, §5):

  B                 termin wylonony w wariancie `primary` (emerging == True)
  okno pozne B      [y0, y0+3], cztery lata od y0 wlacznie
  okno wczesne      [y0-4, y0-1], cztery lata przed y0
  zakres y0         2009..2022, zeby OBA okna miescily sie w calosci w 2005-2025
  kandydat A        udzial w oknie wczesnym >= 2x udzial w oknie poznym B (spadek o polowe)
  liczebnosc        A >= MIN_DOCS rekordow w oknie wczesnym, B >= MIN_DOCS w oknie poznym
  wykluczenie       pary, w ktorych jeden termin jest ciaglym podciagiem tokenow drugiego
                    (warianty zapisu, nie przemianowania)

MIARA — bez zmiany wobec context_shift_test.py: kosinus wektorow PPMI kontekstu,
czestosc dokumentowa, tlo per-okno, usuwane tokeny OBU terminow, MIN_DF = 50.

Uruchom:
    python code/renaming_precision_test.py --out data/processed/renaming_candidates_top50.csv \
        --stats results/renaming_precision_stats.json
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from context_shift_test import Corpus, sim as pairsim, MIN_DF, TOL, N_RANDOM, SEED  # noqa: E402

EMERGING = "D:/medline_2026/parsed/emerging_primary.parquet"
YEARS = list(range(2005, 2026))
Y0_MIN, Y0_MAX = 2009, 2022
MIN_DOCS = 30
DROP_RATIO = 2.0        # udzial wczesny >= 2x pozny
TOP_N = 50
N_TITLES = 5
LOSOWE_MAX = 0.2719     # maksimum rozkladu losowego pary 1 z testu kontekstowego


def contiguous(a: list[str], b: list[str]) -> bool:
    """czy a jest ciaglym podciagiem b"""
    return len(a) <= len(b) and any(b[i:i + len(a)] == a for i in range(len(b) - len(a) + 1))


def matrix(C: Corpus, terms, a, b):
    """wektory PPMI dla listy terminow w oknie [a,b]"""
    V = C.V
    X = np.zeros((len(terms), V), dtype=np.float32)
    for k, t in enumerate(terms):
        v, _ = C.vector(t, a, b, [])
        if v is not None:
            X[k] = v
    return X


def corrected_cosine(A, B, tokA, tokB, hasB):
    """kosinus po usunieciu z OBU wektorow wymiarow odpowiadajacych tokenom OBU terminow.

    Liczymy pelne iloczyny i odejmujemy wklad wymiarow do usuniecia, zamiast budowac
    osobne wektory na kazda z milionow par. Wynik jest identyczny z usunieciem wprost.

    Dla wielkosci q(i,j,d) potrzebne sa trzy skladniki:
        S1 = suma po d z tokenow A_i, S2 = suma po d z tokenow B_j,
        OV = suma po czesci wspolnej, odejmowanej dwa razy przez S1 i S2.
    """
    nA, nB = A.shape[0], B.shape[0]

    def subtract(target, row_val, col_val):
        s = np.zeros((nA, nB), dtype=np.float32)
        for i, ts in enumerate(tokA):
            for dd in ts:
                v = row_val(i, dd)                 # wektor po j
                s[i] += v
                s[i] -= v * hasB[:, dd]            # czesc wspolna odjeta z gory
        for j, ts in enumerate(tokB):
            for dd in ts:
                s[:, j] += col_val(j, dd)          # wektor po i
        return target - s

    dot = subtract(A @ B.T,
                   lambda i, dd: A[i, dd] * B[:, dd],
                   lambda j, dd: A[:, dd] * B[j, dd])
    sqA = subtract(np.repeat((A * A).sum(1)[:, None], nB, axis=1),
                   lambda i, dd: np.full(nB, A[i, dd] ** 2, dtype=np.float32),
                   lambda j, dd: A[:, dd] ** 2)
    sqB = subtract(np.repeat((B * B).sum(1)[None, :], nA, axis=0),
                   lambda i, dd: B[:, dd] ** 2,
                   lambda j, dd: np.full(nA, B[j, dd] ** 2, dtype=np.float32))

    with np.errstate(divide="ignore", invalid="ignore"):
        out = dot / np.sqrt(np.maximum(sqA, 0) * np.maximum(sqB, 0))
    return np.where(np.isfinite(out), out, 0.0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--stats", required=True)
    ap.add_argument("--dump-above", help="zrzuc wszystkie pary powyzej progu i zakoncz")
    args = ap.parse_args()

    print("wczytuje korpus...", flush=True)
    C = Corpus()
    print(f"  {len(C.text)} rekordow, slownik {C.V} unigramow (df >= {MIN_DF})", flush=True)

    d = pd.read_parquet(EMERGING)
    terms = d["term"].to_numpy()
    M = d[[f"y{y}" for y in YEARS]].to_numpy()
    em, y0 = d["emerging"].to_numpy(), d["y0"].to_numpy()
    cf = pd.read_parquet("D:/medline_2026/parsed/field_canon.parquet", columns=["year", "title"])
    den = cf["year"].value_counts().reindex(YEARS).to_numpy().astype(float)
    titles = cf["title"].to_numpy()
    ix = {y: k for k, y in enumerate(YEARS)}
    toks = {t: t.split() for t in terms}

    okB = em & (y0 >= Y0_MIN) & (y0 <= Y0_MAX)
    print(f"  B po warunku okien: {okB.sum()} z {em.sum()} wylonionych", flush=True)

    all_sims, top, above = [], [], []
    for yy in sorted(set(y0[okB].tolist())):
        cl = M[:, ix[yy]:ix[yy + 3] + 1].sum(1)
        ce = M[:, ix[yy - 4]:ix[yy - 1] + 1].sum(1)
        dl = den[ix[yy]:ix[yy + 3] + 1].sum()
        de = den[ix[yy - 4]:ix[yy - 1] + 1].sum()
        Bi = np.flatnonzero(okB & (y0 == yy) & (cl >= MIN_DOCS))
        Ai = np.flatnonzero((ce >= MIN_DOCS) & (ce / de >= DROP_RATIO * cl / dl))
        if not len(Bi) or not len(Ai):
            continue
        At, Bt = terms[Ai].tolist(), terms[Bi].tolist()
        print(f"y0={yy}: A={len(At)} B={len(Bt)} par={len(At)*len(Bt):,} — buduje wektory...",
              flush=True)
        A = matrix(C, At, yy - 4, yy - 1)
        B = matrix(C, Bt, yy, yy + 3)

        tokA = [[C.vocab[w] for w in toks[t] if w in C.vocab] for t in At]
        tokB = [[C.vocab[w] for w in toks[t] if w in C.vocab] for t in Bt]
        hasB = np.zeros((len(Bt), C.V), dtype=np.float32)
        for j, ts in enumerate(tokB):
            hasB[j, ts] = 1.0
        S = corrected_cosine(A, B, tokA, tokB, hasB)

        # wykluczenie zawierania — tylko pary dzielace jakikolwiek token moga sie zawierac
        hasA = np.zeros((len(At), C.V), dtype=np.float32)
        for i, ts in enumerate(tokA):
            hasA[i, ts] = 1.0
        shared = (hasA @ hasB.T) > 0
        for i, j in zip(*np.nonzero(shared)):
            a_, b_ = toks[At[i]], toks[Bt[j]]
            if a_ == b_ or contiguous(a_, b_) or contiguous(b_, a_):
                S[i, j] = np.nan
        drop = int(np.isnan(S).sum())

        v = S[~np.isnan(S)]
        all_sims.append(v.astype(np.float32))
        if args.dump_above:
            for i, j in zip(*np.nonzero(np.nan_to_num(S, nan=-1) > LOSOWE_MAX)):
                above.append((At[i], Bt[j], yy, float(S[i, j])))
        k = min(TOP_N, v.size)
        flat = np.where(np.isnan(S), -np.inf, S).ravel()
        for p in np.argpartition(-flat, k - 1)[:k]:
            i, j = divmod(int(p), len(Bt))
            top.append((float(S[i, j]), At[i], Bt[j], yy))
        print(f"   par po wykluczeniu zawierania: {v.size:,} (odrzucono {drop:,}), "
              f"max {v.max():.4f}", flush=True)

    sims = np.concatenate(all_sims)
    stats = {
        "par_ogolem": int(sims.size),
        "mediana": float(np.median(sims)),
        "p90": float(np.percentile(sims, 90)),
        "p99": float(np.percentile(sims, 99)),
        "max": float(sims.max()),
        "powyzej_maksimum_losowego": int((sims > LOSOWE_MAX).sum()),
        "prog_maksimum_losowego": LOSOWE_MAX,
        "regula": {"Y0_MIN": Y0_MIN, "Y0_MAX": Y0_MAX, "MIN_DOCS": MIN_DOCS,
                   "DROP_RATIO": DROP_RATIO, "MIN_DF": MIN_DF, "SEED": SEED},
    }
    print("\n=== ROZKLAD WSZYSTKICH PAR ===", flush=True)
    for k_, v_ in stats.items():
        if not isinstance(v_, dict):
            print(f"  {k_}: {v_:,}" if isinstance(v_, int) else f"  {k_}: {v_}", flush=True)

    if args.dump_above:
        pd.DataFrame(above, columns=["poprzednik_A", "termin_B", "y0_B", "podobienstwo"]).sort_values(
            "podobienstwo", ascending=False).to_csv(
            args.dump_above, index=False, encoding="utf-8", lineterminator="\n")
        print(f"zrzucone {len(above):,} par powyzej {LOSOWE_MAX} do {args.dump_above}")
        Path(args.stats).parent.mkdir(parents=True, exist_ok=True)
        Path(args.stats).write_text(json.dumps(stats, indent=2, ensure_ascii=False),
                                    encoding="utf-8")
        return

    top.sort(reverse=True)
    top = top[:TOP_N]
    print(f"\nliczę rozklady losowe dla {len(top)} par...", flush=True)

    rng = np.random.default_rng(SEED)
    pool = d[d["docs_total"] >= 20]["term"].tolist()
    rows = []
    for rank, (s, a_, b_, yy) in enumerate(top, 1):
        e1, e2, l1, l2 = yy - 4, yy - 1, yy, yy + 3
        nA, nB = len(C.hits(a_, e1, e2)), len(C.hits(b_, l1, l2))

        def draw(lo, hi, w1, w2, need):
            out = []
            for jj in rng.permutation(len(pool)):
                t = pool[jj]
                if C.maxhits(t) < lo:
                    continue
                if lo <= len(C.hits(t, w1, w2)) <= hi:
                    out.append(t)
                    if len(out) >= need:
                        break
            return out

        RA = draw(nA * (1 - TOL), nA * (1 + TOL), e1, e2, N_RANDOM)
        RB = draw(nB * (1 - TOL), nB * (1 + TOL), l1, l2, N_RANDOM)
        null = [pairsim(C, (x, e1, e2), (y, l1, l2))[0] for x, y in zip(RA, RB) if x != y]
        null = np.array([z for z in null if not np.isnan(z)])
        pct = float((null < s).mean() * 100) if null.size else float("nan")

        ia = np.flatnonzero(terms == a_)[0]
        ib = np.flatnonzero(terms == b_)[0]
        hA, hB = C.hits(a_, e1, e2), C.hits(b_, l1, l2)
        common = np.intersect1d(C.hits(a_, l1, l2), hB)
        row = {
            "rank": rank, "poprzednik_A": a_, "termin_B": b_, "y0_B": yy,
            "podobienstwo": round(s, 4), "percentyl_losowy": round(pct, 1),
            "n_A_okno_wczesne": nA, "n_B_okno_pozne": nB,
            "okno_wczesne": f"{e1}-{e2}", "okno_pozne": f"{l1}-{l2}",
            "n_wspolnych_prac": int(common.size),
        }
        for y in YEARS:
            row[f"A_{y}"] = int(M[ia, ix[y]])
            row[f"B_{y}"] = int(M[ib, ix[y]])
        row["tytuly_A_wczesne"] = "\n".join(titles[i] for i in hA[:N_TITLES])
        row["tytuly_B_pozne"] = "\n".join(titles[i] for i in hB[:N_TITLES])
        row["tytuly_WSPOLNE"] = "\n".join(titles[i] for i in common[:N_TITLES])
        row["werdykt"] = ""
        rows.append(row)
        print(f"  {rank:>3} {a_:<28} -> {b_:<28} {s:.4f}  pct {pct:.1f}  "
              f"wspolnych {common.size}", flush=True)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out, index=False, encoding="utf-8-sig", lineterminator="\n")
    Path(args.stats).parent.mkdir(parents=True, exist_ok=True)
    Path(args.stats).write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisane: {out} i {args.stats}")


if __name__ == "__main__":
    main()
