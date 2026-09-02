"""merge_and_axes.py — scalenie wariantow wskazanych przez ortopede i osie sily na scalonym materiale.

Scalenia pochodza WYLACZNIE z uwag ortopedy w ocena_mapy_*.csv. Zadnej grupy nie dokladam
z wlasnej inicjatywy.

Kluczowe: szereg roczny grupy to liczba DOKUMENTOW ZAWIERAJACYCH DOWOLNY jej czlon, a nie
suma szeregow czlonow. Praca uzywajaca "reverse shoulder arthroplasty" i "reverse total
shoulder arthroplasty" naraz liczy sie raz. Suma szeregow zawyzalaby grupe tym bardziej,
im bardziej jej czlony wspolwystepuja — czyli najmocniej tam, gdzie scalenie jest najbardziej
uzasadnione.

y0, szczyt i prevalence licze na scalonym szeregu regula detektora bez zmian:
prog = max(THETA, RATIO x srednia 2005-2007), utrzymany PERSIST lat, przy >= MIN_PAPERS pracach,
y0 <= Y0_MAX.

Uruchom:
    python code/merge_and_axes.py --terms data/processed/material_52.csv \
        --grupy data/processed/scalenia.json --chunks D:/medline_2026/parsed/noun_chunks.parquet \
        --exclude data/processed/pmid_pole_wylaczone.csv --canon data/canon \
        --parsed D:/medline_2026/parsed \
        --auth D:/medline_2026/parsed/field_text_auth.parquet \
        --denom D:/medline_2026/parsed/terms_np_f_primary.denom.json \
        --out data/processed/np_osie_sily_scalone.csv
"""
from __future__ import annotations
import argparse, json, sys, time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402
from count_noun_phrases import SEP, split_years  # noqa: E402
from detect_emergence import (  # noqa: E402
    YEAR_MIN, YEAR_MAX, THETA, MIN_PAPERS, PERSIST, RATIO,
    BASE_FROM, BASE_TO, Y0_MAX, SEL_FROM, SEL_TO,
)
from strength_axes import concentration, institution  # noqa: E402
from affil_country import make_matcher  # noqa: E402

# zakres i baza sa parametrami, bo skrypt biega na dwoch oknach (2005-2025 i 2000-2025);
# import stalych dawalby ciche policzenie y0 na niewlasciwej bazie
YEARS: list[int] = []
BAZA: tuple[int, int] = (BASE_FROM, BASE_TO)


def wylonienie(cnt: np.ndarray, den: np.ndarray) -> dict:
    """regula detektora na pojedynczym szeregu, bez zmian wobec detect_emergence.py"""
    s = cnt / den
    baseline = float(s[YEARS.index(BAZA[0]):YEARS.index(BAZA[1]) + 1].mean())
    thr = max(THETA, RATIO * baseline)
    above = (s >= thr) & (cnt >= MIN_PAPERS)
    y0 = None
    for i in range(len(YEARS) - PERSIST + 1):
        if above[i:i + PERSIST].all():
            y0 = YEARS[i]
            break
    ipk = int(np.argmax(s))
    sel = slice(YEARS.index(SEL_FROM), YEARS.index(SEL_TO) + 1)
    return {"y0": y0 if (y0 and y0 <= Y0_MAX) else None,
            "baseline_pct": round(100 * baseline, 4), "prog_pct": round(100 * thr, 4),
            "szczyt_pct": round(100 * float(s[ipk]), 3), "rok_szczytu": YEARS[ipk],
            "prevalence_2021_2025_pct": round(100 * cnt[sel].sum() / den[sel].sum(), 3),
            "docs_total": int(cnt.sum()),
            "trwalosc_2025_do_szczytu": round(float(s[-1] / s[ipk]), 2) if s[ipk] else None,
            "_s": s}


def main() -> int:
    ap = argparse.ArgumentParser()
    for a in ("--terms", "--grupy", "--chunks", "--canon", "--parsed",
              "--auth", "--denom", "--out"):
        ap.add_argument(a, required=True)
    ap.add_argument("--exclude")
    ap.add_argument("--year-min", type=int, default=YEAR_MIN)
    ap.add_argument("--year-max", type=int, default=YEAR_MAX)
    ap.add_argument("--base-from", type=int, default=BASE_FROM)
    ap.add_argument("--base-to", type=int, default=BASE_TO)
    args = ap.parse_args()
    global YEARS, BAZA
    YEARS = list(range(args.year_min, args.year_max + 1))
    BAZA = (args.base_from, args.base_to)
    print(f"okno {args.year_min}-{args.year_max}, baza {BAZA[0]}-{BAZA[1]}", file=sys.stderr)

    t0 = time.time()
    tab = pd.read_csv(args.terms, encoding="utf-8-sig")
    grupy = json.loads(Path(args.grupy).read_text(encoding="utf-8"))
    do_grupy = {t: g for g, cz in grupy.items() for t in cz}
    etykieta = {t: do_grupy.get(t, t) for t in tab["term"]}
    czlonkowie = defaultdict(list)
    for t in tab["term"]:
        czlonkowie[etykieta[t]].append(t)
    print(f"pozycji {len(tab)} -> grup {len(czlonkowie)}", file=sys.stderr)
    for g, cz in czlonkowie.items():
        if len(cz) > 1:
            print(f"  [{len(cz)}] {g}: " + " | ".join(cz), file=sys.stderr)

    spell, irr, phr = load_lists(Path(args.canon))
    canon = make_canonicalizer(spell, irr, phr)
    cmatch = make_matcher(Path(args.canon))

    df = pd.read_parquet(args.chunks)
    if args.exclude:
        wyl = set(pd.read_csv(args.exclude, dtype=str)["pmid"])
        df = df[~df["pmid"].isin(wyl)].reset_index(drop=True)
    pole = set(df["pmid"])

    meta = []
    pf = pq.ParquetFile(Path(args.parsed) / "analytic_index.parquet")
    for g in range(pf.metadata.num_row_groups):
        d = pf.read_row_group(g, columns=["pmid", "aff1", "journal_nlm"]).to_pandas()
        d = d[d["pmid"].isin(pole)]
        if len(d):
            meta.append(d)
    df = df.merge(pd.concat(meta, ignore_index=True), on="pmid", how="left").merge(
        pd.read_parquet(args.auth, columns=["pmid", "author1"]), on="pmid", how="left")
    df["aff1"] = df["aff1"].fillna("")
    df["author1"] = df["author1"].fillna("")
    print(f"rekordow: {len(df):,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    kraj = [cmatch(a) if a else "" for a in df["aff1"]]
    autor = [f"{a}|{k}|{institution(f)}" if a else ""
             for a, k, f in zip(df["author1"], kraj, df["aff1"])]

    klucze = list(czlonkowie)
    gid = {g: i for i, g in enumerate(klucze)}
    szukane = set(etykieta)
    cnt = np.zeros((len(klucze), len(YEARS)), dtype=np.int64)
    ca = [Counter() for _ in klucze]
    ck = [Counter() for _ in klucze]
    cj = [Counter() for _ in klucze]
    brak = np.zeros(len(klucze), dtype=np.int64)

    tt, aa = df["title_np"].values, df["abstract_np"].values
    jn = df["journal_nlm"].fillna("").values
    yr = df["year"].astype(int).values
    yi = {y: i for i, y in enumerate(YEARS)}
    for i in range(len(df)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        obecne = set()
        for c in raw:
            if c:
                obecne.update(" ".join(p) for p in split_years(canon(c)))
        trafione = obecne & szukane
        if not trafione:
            continue
        for g in {etykieta[t] for t in trafione}:       # dokument liczy sie RAZ na grupe
            j = gid[g]
            cnt[j, yi[yr[i]]] += 1
        if (i + 1) % 50000 == 0:
            print(f"  {i+1:,}/{len(df):,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    den = json.loads(Path(args.denom).read_text(encoding="utf-8"))["by_year"]
    dv = np.array([den[str(y)] for y in YEARS], float)
    wyn = {g: wylonienie(cnt[gid[g]].astype(float), dv) for g in klucze}

    # koncentracja liczona od y0 grupy, na dokumentach grupy
    for i in range(len(df)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        obecne = set()
        for c in raw:
            if c:
                obecne.update(" ".join(p) for p in split_years(canon(c)))
        for g in {etykieta[t] for t in (obecne & szukane)}:
            j, y0 = gid[g], wyn[g]["y0"]
            if y0 is None or yr[i] < y0:
                continue
            if autor[i]:
                ca[j][autor[i]] += 1
            if kraj[i]:
                ck[j][kraj[i]] += 1
            else:
                brak[j] += 1
            if jn[i]:
                cj[j][jn[i]] += 1

    rows = []
    for g in klucze:
        j, w = gid[g], wyn[g]
        a_top, a_eff, a_n, _ = concentration(ca[j])
        k_top, k_eff, k_n, k_name = concentration(ck[j])
        j_top, j_eff, _, j_name = concentration(cj[j])
        s = w.pop("_s")
        slope = dbl = float("nan")
        if w["y0"]:
            i0, ipk = YEARS.index(w["y0"]), YEARS.index(w["rok_szczytu"])
            if ipk - i0 >= 2:
                xs, ys = np.arange(i0, ipk + 1), s[i0:ipk + 1]
                m = ys > 0
                if m.sum() >= 3:
                    slope = float(np.polyfit(xs[m], np.log(ys[m]), 1)[0])
                    if slope > 0:
                        dbl = float(np.log(2) / slope)
        rows.append({"grupa": g, "czlonow": len(czlonkowie[g]),
                     "czlony": " | ".join(czlonkowie[g]) if len(czlonkowie[g]) > 1 else "",
                     **w, "prac_od_y0": int(a_n),
                     "autor_top_pct": round(100 * a_top, 1), "autor_eff_n": round(a_eff, 1),
                     "kraj_top": k_name, "kraj_top_pct": round(100 * k_top, 1),
                     "kraj_eff_n": round(k_eff, 1),
                     "kraj_brak_pct": round(100 * brak[j] / max(k_n + brak[j], 1), 1),
                     "czasopismo_top_nlm": j_name, "czasopismo_top_pct": round(100 * j_top, 1),
                     "czasopismo_eff_n": round(j_eff, 1),
                     "czas_podwojenia_lat": round(dbl, 1) if dbl == dbl else ""})

    out = pd.DataFrame(rows).sort_values("prevalence_2021_2025_pct", ascending=False)
    out.to_csv(args.out, index=False, encoding="utf-8-sig", lineterminator="\n")
    print(f"\nzapisano {args.out}: {len(out)} grup", file=sys.stderr)
    print(f"  bez y0 po scaleniu: {int(out['y0'].isna().sum())}", file=sys.stderr)
    print(f"  czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
