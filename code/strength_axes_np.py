"""strength_axes_np.py — osie sily dla jednostki frazowej (plan v0.4 §6, brief osie_sily Z1).

Rozni sie od strength_axes.py DOKLADNIE jednostka. Koncentracja, klucz autora, dopasowanie
kraju i czas podwojenia sa importowane albo przeniesione bez zmian:

  * koncentracja = (udzial najwiekszego, efektywna liczba 1/HHI, n, nazwa najwiekszego)
  * klucz autora `nazwisko|kraj|instytucja`
  * KRAJ WYLACZNIE Z aff1, nigdy z MedlineJournalInfo/Country — pole czasopisma mowi,
    gdzie zarejestrowano tytul, nie skad sa autorzy
  * czas podwojenia z nachylenia log-udzialu od y0 do szczytu, przy >= 3 latach

Zmiana wobec oryginalu poza jednostka, celowa: metadane z analytic_index czytam
STRUMIENIOWO i filtruje do PMID pola od razu. Oryginal sklejal wszystkie 41 mln wierszy
w pamieci, co przy kolumnie aff1 nie miesci sie w rozsadnym RAM.

Uruchom:
    python code/strength_axes_np.py --terms data/processed/material_52.csv \
        --chunks D:/medline_2026/parsed/noun_chunks.parquet \
        --exclude data/processed/pmid_pole_wylaczone.csv --canon data/canon \
        --parsed D:/medline_2026/parsed \
        --auth D:/medline_2026/parsed/field_text_auth.parquet \
        --emerging D:/medline_2026/parsed/emerging_np_f_primary.parquet \
        --denom D:/medline_2026/parsed/terms_np_f_primary.denom.json \
        --out data/processed/np_osie_sily.csv --json results/np_osie_sily.json
"""
from __future__ import annotations
import argparse, json, sys, time
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import YEAR_MIN, YEAR_MAX, load_lists, make_canonicalizer  # noqa: E402
from count_noun_phrases import SEP, split_years  # noqa: E402
from strength_axes import concentration, institution  # noqa: E402
from affil_country import make_matcher  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    for a in ("--terms", "--chunks", "--canon", "--parsed", "--auth",
              "--emerging", "--denom", "--out", "--json"):
        ap.add_argument(a, required=True)
    ap.add_argument("--exclude")
    args = ap.parse_args()

    t0 = time.time()
    tab = pd.read_csv(args.terms, encoding="utf-8-sig")
    terms = list(tab["term"])
    y0 = dict(zip(tab["term"], tab["y0"]))
    tid = {t: i for i, t in enumerate(terms)}
    print(f"pozycji: {len(terms)}", file=sys.stderr)

    spell, irr, phr = load_lists(Path(args.canon))
    canon = make_canonicalizer(spell, irr, phr)
    cmatch = make_matcher(Path(args.canon))

    df = pd.read_parquet(args.chunks)
    if args.exclude:
        wyl = set(pd.read_csv(args.exclude, dtype=str)["pmid"])
        df = df[~df["pmid"].isin(wyl)].reset_index(drop=True)
    pole = set(df["pmid"])
    print(f"rekordow pola: {len(df):,}", file=sys.stderr)

    # metadane strumieniowo, od razu zawezone do pola
    meta = []
    pf = pq.ParquetFile(Path(args.parsed) / "analytic_index.parquet")
    for g in range(pf.metadata.num_row_groups):
        d = pf.read_row_group(g, columns=["pmid", "aff1", "journal_nlm"]).to_pandas()
        d = d[d["pmid"].isin(pole)]
        if len(d):
            meta.append(d)
    meta = pd.concat(meta, ignore_index=True)
    auth = pd.read_parquet(args.auth, columns=["pmid", "author1"])
    df = df.merge(meta, on="pmid", how="left").merge(auth, on="pmid", how="left")
    df["aff1"] = df["aff1"].fillna("")
    df["author1"] = df["author1"].fillna("")
    print(f"po scaleniu metadanych: {len(df):,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    kraj = [cmatch(a) if a else "" for a in df["aff1"]]
    autor = [f"{a}|{k}|{institution(f)}" if a else ""
             for a, k, f in zip(df["author1"], kraj, df["aff1"])]

    ca = [Counter() for _ in terms]
    ck = [Counter() for _ in terms]
    cj = [Counter() for _ in terms]
    brak_kraju = np.zeros(len(terms), dtype=np.int64)

    tt, aa = df["title_np"].values, df["abstract_np"].values
    jn = df["journal_nlm"].fillna("").values
    yr = df["year"].astype(int).values
    for i in range(len(df)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        present = set()
        for c in raw:
            if c:
                present.update(" ".join(p) for p in split_years(canon(c)))
        for t in present & tid.keys():
            j = tid[t]
            if yr[i] < y0[t]:
                continue
            if autor[i]:
                ca[j][autor[i]] += 1
            if kraj[i]:
                ck[j][kraj[i]] += 1
            else:
                brak_kraju[j] += 1
            if jn[i]:
                cj[j][jn[i]] += 1
        if (i + 1) % 50000 == 0:
            print(f"  {i+1:,}/{len(df):,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    den = json.loads(Path(args.denom).read_text(encoding="utf-8"))["by_year"]
    years = list(range(YEAR_MIN, YEAR_MAX + 1))
    em = pd.read_parquet(args.emerging).set_index("term")

    rows = []
    for t in terms:
        j = tid[t]
        a_top, a_eff, a_n, _ = concentration(ca[j])
        k_top, k_eff, k_n, k_name = concentration(ck[j])
        j_top, j_eff, j_n, j_name = concentration(cj[j])
        cnt = np.array([em.loc[t, f"y{y}"] for y in years], float)
        s = cnt / np.array([den[str(y)] for y in years], float)
        i0 = years.index(int(y0[t]))
        ipk = int(np.argmax(s))
        slope = dbl = float("nan")
        if ipk - i0 >= 2:
            xs, ys = np.arange(i0, ipk + 1), s[i0:ipk + 1]
            m = ys > 0
            if m.sum() >= 3:
                slope = float(np.polyfit(xs[m], np.log(ys[m]), 1)[0])
                if slope > 0:
                    dbl = float(np.log(2) / slope)
        rows.append({
            "term": t, "y0": int(y0[t]),
            "prac_od_y0": int(a_n),
            "autor_top_pct": round(100 * a_top, 1), "autor_eff_n": round(a_eff, 1),
            "kraj_top": k_name, "kraj_top_pct": round(100 * k_top, 1),
            "kraj_eff_n": round(k_eff, 1),
            "kraj_brak_pct": round(100 * brak_kraju[j] / max(k_n + brak_kraju[j], 1), 1),
            "czasopismo_top_nlm": j_name, "czasopismo_top_pct": round(100 * j_top, 1),
            "czasopismo_eff_n": round(j_eff, 1),
            "szczyt_pct": round(100 * s[ipk], 3), "rok_szczytu": years[ipk],
            "nachylenie_log": round(slope, 3) if slope == slope else "",
            "czas_podwojenia_lat": round(dbl, 1) if dbl == dbl else "",
            "trwalosc_2025_do_szczytu": round(s[-1] / s[ipk], 2) if s[ipk] > 0 else "",
        })

    out = pd.DataFrame(rows)
    if "kategoria" in tab.columns:
        out = out.merge(tab[["term", "kategoria"]], on="term", how="left")
    out.to_csv(args.out, index=False, encoding="utf-8-sig", lineterminator="\n")
    Path(args.json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.json).write_text(json.dumps({
        "pozycji": len(out), "mianownik": args.denom,
        "mediana_kraj_brak_pct": float(out["kraj_brak_pct"].median()),
        "wiersze": out.to_dict("records")}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisano {args.out}: {len(out)} wierszy", file=sys.stderr)
    print(f"  mediana kraj_brak_pct: {out['kraj_brak_pct'].median():.1f}%", file=sys.stderr)
    print(f"  czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
