"""szeregi_grup.py — roczne szeregi grup materialu (zliczanie unijne) do rycin i analiz wrazliwosci.

Eksport tego, co juz policzone w merge_and_axes.py i trwalosc_wzgledna.py, ale zapisany rok po
roku: szereg grupy to liczba dokumentow zawierajacych DOWOLNY jej czlon, dzielona przez rekordy
pola w roku. Plus szeregi pojedynczych czlonow dla ryciny o scaleniu i retronimach.

Jeden przebieg liczy dwa pola naraz: obecne (D4+D5a+D5c+D6) i bez filtra weterynaryjnego D6
(D4+D5a+D5c) — to drugie tylko do analizy wrazliwosci y0 na D6, nie jako nowa definicja pola.

Uruchom:
    python code/szeregi_grup.py --grupy data/processed/grupy_54.json --out-dir data/processed \
        --bez-d6 results/szeregi_54_bez_d6_prace.csv
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402
from count_noun_phrases import SEP, split_years  # noqa: E402

P = Path("D:/medline_2026/parsed")
YEARS = list(range(2000, 2026))
# panel ryciny -> pojedyncze czlony (kazdy liczony osobno, nie jako grupa)
CZLONY = {
    "scalenie: kyphoplasty": ["kyphoplasty", "balloon kyphoplasty", "percutaneous kyphoplasty", "pkp"],
    "retronim: single vs double bundle": ["single bundle", "double bundle reconstruction"],
    "retronim: mechanical vs kinematic alignment": ["mechanical alignment", "kinematic alignment"],
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--grupy", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--bez-d6", required=True)
    args = ap.parse_args()
    t0 = time.time()

    grupy = json.loads(Path(args.grupy).read_text(encoding="utf-8"))
    jednostki = {g: set(cz) for g, cz in grupy.items()}
    for panel, cz in CZLONY.items():
        for t in cz:
            jednostki[f"{panel}|{t}"] = {t}
    klucze = list(jednostki)
    cel = set().union(*jednostki.values())

    wyl_d6 = set(pd.read_csv("data/processed/pmid_pole_wylaczone_d6.csv", dtype=str)["pmid"])
    wyl_bez = set(pd.read_csv("data/processed/pmid_pole_wylaczone_2000.csv", dtype=str)["pmid"])
    canon = make_canonicalizer(*load_lists(Path("data/canon")))
    nc = pd.read_parquet(P / "noun_chunks_2000_2025.parquet")
    nc = nc[~nc["pmid"].isin(wyl_bez)]                 # wyl_bez jest podzbiorem wyl_d6

    cnt_d6 = np.zeros((len(klucze), len(YEARS)), dtype=np.int64)
    cnt_bez = np.zeros_like(cnt_d6)
    tt, aa, pm = nc["title_np"].values, nc["abstract_np"].values, nc["pmid"].values
    yr = nc["year"].astype(int).values
    for i in range(len(nc)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        ob = set()
        for c in raw:
            if c:
                ob.update(" ".join(p) for p in split_years(canon(c)))
        if not (ob & cel):
            continue
        j = YEARS.index(yr[i])
        w_d6 = pm[i] not in wyl_d6
        for k, g in enumerate(klucze):
            if ob & jednostki[g]:                      # dokument liczy sie RAZ na jednostke
                cnt_bez[k, j] += 1
                if w_d6:
                    cnt_d6[k, j] += 1
        if (i + 1) % 100000 == 0:
            print(f"  {i+1:,}/{len(nc):,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    den = json.loads((P / "terms_d6_primary.denom.json").read_text(encoding="utf-8"))["by_year"]
    dv = np.array([den[str(y)] for y in YEARS], float)
    ycols = [f"y{y}" for y in YEARS]
    out = Path(args.out_dir)
    ng = len(grupy)

    pd.DataFrame(np.round(100 * cnt_d6[:ng] / dv, 4), columns=ycols).assign(
        grupa=klucze[:ng])[["grupa"] + ycols].to_csv(
        out / "szeregi_54.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    pd.DataFrame(cnt_d6[:ng], columns=ycols).assign(grupa=klucze[:ng])[["grupa"] + ycols].to_csv(
        out / "szeregi_54_prace.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    pd.DataFrame(cnt_bez[:ng], columns=ycols).assign(grupa=klucze[:ng])[["grupa"] + ycols].to_csv(
        args.bez_d6, index=False, encoding="utf-8-sig", lineterminator="\n")

    cz = pd.DataFrame(np.round(100 * cnt_d6[ng:] / dv, 4), columns=ycols)
    cz.insert(0, "czlon", [k.split("|")[1] for k in klucze[ng:]])
    cz.insert(0, "panel", [k.split("|")[0] for k in klucze[ng:]])
    cz.to_csv(out / "szeregi_czlonow.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    print(f"zapisane ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
