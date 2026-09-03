"""audyt_skazenia.py — systematyczny test na obca dziedzine dla calego materialu.

Cowork nazwal to ograniczeniem wprost: "nie mamy systematycznego testu na obca dziedzine,
tylko serie wykryc ad hoc". Cztery wycieki (naczyniowy, stomatologiczny, homonim, weterynaryjny)
znaleziono czterema niezaplanowanymi drogami. CBCT z 82,5% stomatologii wyszlo dopiero wtedy,
gdy ktos zgadl, ze warto sprawdzic akurat te pozycje.

Ten skrypt liczy dla KAZDEJ pozycji materialu udzial dokumentow niosacych deskryptory obcych
dziedzin — tych samych, ktore definiuja reguly D4, D5a, D5c i D6. Reguly dzialaja na poziomie
rekordu i wylaczaja tylko przypadki skrajne (np. D5a: rekord, ktorego WSZYSTKIE deskryptory pola
sa stomatologiczne). Technologia moze wiec byc czysta wobec regul, a mimo to w wiekszosci
opisywac inna dziedzine — dokladnie jak CBCT.

Nie wylacza niczego. Podaje liczby; prog dzialania ustala Cowork (dotad: 20%).

Uruchom:
    python code/audyt_skazenia.py --grupy data/processed/grupy_61.json \
        --out data/processed/audyt_skazenia.csv
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path

import pandas as pd
import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402
from count_noun_phrases import SEP, split_years  # noqa: E402

P = Path("D:/medline_2026/parsed")
# dziedziny obce, po prefiksach drzew MeSH — te same, ktore stoja za D5a, D5c i D4
DZIEDZINY = {
    "stomatologia": ("A14", "C07", "E06", "E04.545"),
    "trawienny": ("C06",),
    "moczowoplciowy": ("C12",),
    "oko": ("C11",),
    "sercowonaczyniowy": ("C14",),
    "nerwowy": ("C10",),
    "nowotwory": ("C04",),
}
UI_ZWIERZ = "D000818"
UI_LUDZIE = "D006801"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--grupy", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    t0 = time.time()

    ui2t = json.loads((P / "mesh_ui2trees.json").read_text(encoding="utf-8"))
    zbior = {n: {u for u, ts in ui2t.items() if any(t.startswith(pref) for t in ts)}
             for n, pref in DZIEDZINY.items()}
    for n, s in zbior.items():
        print(f"  {n:<20} {len(s)} deskryptorow", file=sys.stderr)

    grupy = json.loads(Path(args.grupy).read_text(encoding="utf-8"))
    czl = {g: set(v) for g, v in grupy.items()}
    cel = set().union(*czl.values())

    canon = make_canonicalizer(*load_lists(Path("data/canon")))
    nc = pd.read_parquet(P / "noun_chunks_2000_2025.parquet")
    wyl = set(pd.read_csv("data/processed/pmid_pole_wylaczone_d6.csv", dtype=str)["pmid"])
    nc = nc[~nc["pmid"].isin(wyl)]

    dok = {g: set() for g in czl}
    tt, aa, pm = nc["title_np"].values, nc["abstract_np"].values, nc["pmid"].values
    for i in range(len(nc)):
        raw = (tt[i].split(SEP) if tt[i] else []) + (aa[i].split(SEP) if aa[i] else [])
        ob = set()
        for c in raw:
            if c:
                ob.update(" ".join(p) for p in split_years(canon(c)))
        if not (ob & cel):
            continue
        for g, cz in czl.items():
            if ob & cz:
                dok[g].add(pm[i])
        if (i + 1) % 50000 == 0:
            print(f"  {i+1:,} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    wsz = set().union(*dok.values())
    mesh = {}
    f = pq.ParquetFile(P / "analytic_index.parquet")
    for g_ in range(f.metadata.num_row_groups):
        d_ = f.read_row_group(g_, columns=["pmid", "mesh_ui"]).to_pandas()
        d_ = d_[d_["pmid"].isin(wsz)]
        for p, m in zip(d_["pmid"].values, d_["mesh_ui"].fillna("").values):
            mesh[p] = set(m.split("|")) if m else set()
    print(f"mesh dla {len(mesh):,} rekordow ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    rows = []
    for g, ps in dok.items():
        ps = [p for p in ps if p in mesh]
        if not ps:
            continue
        r = {"grupa": g, "prac": len(ps)}
        for n, s in zbior.items():
            r[n] = round(100 * sum(1 for p in ps if mesh[p] & s) / len(ps), 1)
        r["zwierzeta_bez_ludzi"] = round(
            100 * sum(1 for p in ps if UI_ZWIERZ in mesh[p] and UI_LUDZIE not in mesh[p])
            / len(ps), 1)
        r["max_obca"] = max(r[n] for n in zbior)
        r["dziedzina_max"] = max(zbior, key=lambda n: r[n])
        rows.append(r)

    d = pd.DataFrame(rows).sort_values("max_obca", ascending=False)
    d.to_csv(args.out, index=False, encoding="utf-8-sig", lineterminator="\n")

    print(f"\n{'grupa':<42} {'prac':>5} {'max obca':>9} {'dziedzina':<18} {'zwierz':>7}")
    for _, r in d.head(20).iterrows():
        print(f"{r.grupa[:41]:<42} {int(r.prac):>5} {r.max_obca:>8.1f}% "
              f"{r.dziedzina_max:<18} {r.zwierzeta_bez_ludzi:>6.1f}%")
    print(f"\npowyzej 20% w jakiejkolwiek dziedzinie: "
          f"{int((d.max_obca > 20).sum())} z {len(d)}")
    print(f"mediana max_obca: {d.max_obca.median():.1f}%")
    print(f"\nzapisane: {args.out}  ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
