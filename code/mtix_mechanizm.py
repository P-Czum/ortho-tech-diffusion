"""mtix_mechanizm.py — czy odchylenia po MTIX ida tam, gdzie przewiduje przesuniecie deskryptorow.

mtix_impact.py pokazal, ze terminy materialu odchylaja sie od wlasnego trendu po 2022,
z rozrzutem od z = -6,2 do +3,5. Sam ten fakt nie dowodzi niczego: wykladniczy trend
dopasowany na siedmiu latach i ekstrapolowany na trzy PRAWIE ZAWSZE przestrzeliwuje w gore,
bo wzrost sie nasyca. Mediana z = -0,87 jest wiec spodziewana i nie swiadczy o MTIX.

Rozstrzyga KIERUNEK, nie poziom. mtix_check.py zmierzyl, ktore deskryptory pola MTIX
przypisuje chetniej (Arthroplasty Replacement Knee +1,19 pp, Fracture Fixation Internal
+1,09, Arthroplasty Replacement Shoulder +0,84), a ktore rzadziej (Orthopedic Procedures
-2,94, Fracture Fixation -1,07, Arthroplasty -0,73).

Jesli hipoteza H3 dziala, to terminy, ktorych prace nosza deskryptory ZYSKUJACE, powinny
miec z wyzsze niz terminy z deskryptorami TRACACYMI. Jesli korelacja jest zerowa,
odchylenia to nasycenie trendu i sprawa jest zamknieta.

Uruchom:
    python code/mtix_mechanizm.py --parsed D:/medline_2026/parsed \
        --impact results/mtix_impact.json --check results/mtix_check.json \
        --terms data/processed/material_final.csv --out results/mtix_mechanizm.json
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from scipy import stats

OKNO_OD, OKNO_DO = 2023, 2025


def main() -> int:
    ap = argparse.ArgumentParser()
    for a in ("--parsed", "--impact", "--check", "--terms", "--out"):
        ap.add_argument(a, required=True)
    args = ap.parse_args()

    P = Path(args.parsed)
    imp = pd.DataFrame(json.loads(Path(args.impact).read_text(encoding="utf-8"))["t1"])
    chk = json.loads(Path(args.check).read_text(encoding="utf-8"))["h3_sklad"]
    waga = {r["ui"]: r["zmiana_pp"] for r in chk}
    print(f"deskryptorow z wyliczona zmiana: {len(waga)}", file=sys.stderr)

    # PMID-y terminow materialu w oknie po MTIX
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from canonicalize import load_lists, make_canonicalizer
    from count_noun_phrases import SEP, split_years
    canon = make_canonicalizer(*load_lists(Path("data/canon")))

    terms = set(pd.read_csv(args.terms, encoding="utf-8-sig")["term"]) & set(imp["term"])
    nc = pd.read_parquet(P / "noun_chunks_2000_2025.parquet")
    nc = nc[(nc.year >= OKNO_OD) & (nc.year <= OKNO_DO)]
    print(f"rekordow {OKNO_OD}-{OKNO_DO}: {len(nc):,}", file=sys.stderr)

    t0 = time.time()
    pmids = {t: set() for t in terms}
    tt, aa, pm = nc.title_np.values, nc.abstract_np.values, nc.pmid.values
    for i in range(len(nc)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        obec = set()
        for c in raw:
            if c:
                obec.update(" ".join(p) for p in split_years(canon(c)))
        for t in obec & terms:
            pmids[t].add(pm[i])
    print(f"  dopasowanie terminow: {(time.time()-t0)/60:.1f} min", file=sys.stderr)

    wszystkie = set().union(*pmids.values())
    mesh = {}
    pf = pq.ParquetFile(P / "analytic_index.parquet")
    for g in range(pf.metadata.num_row_groups):
        d = pf.read_row_group(g, columns=["pmid", "mesh_ui"]).to_pandas()
        d = d[d.pmid.isin(wszystkie)]
        for p, m in zip(d.pmid.values, d.mesh_ui.fillna("").values):
            mesh[p] = m
    print(f"  mesh dla {len(mesh):,} rekordow ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    wier = []
    for t in sorted(terms):
        ps = [p for p in pmids[t] if p in mesh]
        if len(ps) < 20:
            continue
        # ekspozycja terminu na przesuniecie: srednia zmiana pp deskryptorow jego prac
        exps = []
        for p in ps:
            uis = [u for u in mesh[p].split("|") if u in waga]
            if uis:
                exps.append(float(np.mean([waga[u] for u in uis])))
        if not exps:
            continue
        wier.append({"term": t, "prac": len(ps), "ekspozycja_pp": round(float(np.mean(exps)), 4)})

    d = pd.DataFrame(wier).merge(imp[["term", "z_po_mtix", "trend_rocznie_pct"]], on="term")
    d = d[d.z_po_mtix.notna()]
    rho = stats.spearmanr(d.ekspozycja_pp, d.z_po_mtix)
    pr = stats.pearsonr(d.ekspozycja_pp, d.z_po_mtix)
    print(f"\n=== zwiazek ekspozycji na przesuniecie deskryptorow z odchyleniem po MTIX ===")
    print(f"  terminow: {len(d)}")
    print(f"  Spearman rho = {rho.statistic:+.3f}  p = {rho.pvalue:.4f}")
    print(f"  Pearson  r   = {pr.statistic:+.3f}  p = {pr.pvalue:.4f}")
    print(f"\n{'termin':<44} {'prac':>5} {'ekspoz.':>9} {'z':>7}")
    for _, r in d.sort_values("ekspozycja_pp").iterrows():
        print(f"{r.term:<44} {int(r.prac):>5} {r.ekspozycja_pp:>+9.4f} {r.z_po_mtix:>+7.2f}")

    Path(args.out).write_text(json.dumps(
        {"spearman": round(float(rho.statistic), 4), "spearman_p": round(float(rho.pvalue), 5),
         "pearson": round(float(pr.statistic), 4), "pearson_p": round(float(pr.pvalue), 5),
         "n": len(d), "wiersze": d.to_dict("records")},
        indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisane: {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
