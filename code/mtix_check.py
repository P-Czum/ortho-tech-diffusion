"""mtix_check.py — czy spadek udzialu pola po 2022 to nieciaglosc indeksowania (test z planu §10).

Zmierzone: udzial pola w PubMedzie rosnie do 1,257% w 2011 i spada do 0,825% w 2025, o 34%.
NLM przeszla w 2022 na automatyczne indeksowanie MTIX. Pytanie nie brzmi "czy spadek jest",
tylko CZYM JEST — bo od tego zalezy, czy prevalence_2021_2025 nadaje sie na os rankingu.

Trzy rozlaczne hipotezy, kazda z wlasnym sygnalem:

  H1 mniej rekordow indeksowanych w ogole   -> spada udzial rekordow z jakimkolwiek MeSH
  H2 plytsze indeksowanie tych, ktore sa    -> spada srednia liczba deskryptorow na rekord
  H3 przesuniecie skladu deskryptorow       -> zmienia sie rozklad deskryptorow pola

H1 i H2 sa nieszkodliwe dla osi, jesli dzialaja rownomiernie: licznik i mianownik kurcza sie
razem, bo pole jest definiowane przez MeSH. H3 jest grozne — jesli MTIX chetniej przypisuje
jedne deskryptory pola niz inne, to zmienia sie SKLAD pola, a nie tylko jego rozmiar,
i ranking premiuje terminy z prac opisywanych deskryptorami, ktore MTIX lubi.

Uruchom:
    python code/mtix_check.py --parsed D:/medline_2026/parsed \
        --field data/processed/field_orthopedic_procedures.csv --out results/mtix_check.json
"""
from __future__ import annotations
import argparse, csv, json, sys, time
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd
import pyarrow.parquet as pq

YEARS = list(range(2000, 2026))
COLS = ["year", "mesh_ui", "status", "medline_indexed", "indexed"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parsed", required=True)
    ap.add_argument("--field", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    FIELD = {r["ui"] for r in csv.DictReader(open(args.field, encoding="utf-8"))
             if r["ui"].strip()}
    nazwa = {r["ui"]: r["name"] for r in csv.DictReader(open(args.field, encoding="utf-8"))}

    t0 = time.time()
    f = pq.ParquetFile(Path(args.parsed) / "analytic_index.parquet")
    rec = Counter()          # (rok, miara) -> liczba
    desk = defaultdict(Counter)   # rok -> Counter(ui)
    for g in range(f.metadata.num_row_groups):
        d = f.read_row_group(g, columns=COLS).to_pandas()
        d["year"] = pd.to_numeric(d["year"], errors="coerce")
        d = d[(d.year >= 2000) & (d.year <= 2025)]
        if d.empty:
            continue
        mu = d["mesh_ui"].fillna("")
        ma_mesh = mu.str.len() > 0
        n_desk = mu.str.count(r"\|") + ma_mesh.astype(int)
        for y, sub in d.groupby(d.year.astype(int)):
            i = sub.index
            rec[(y, "wszystkie")] += len(sub)
            rec[(y, "z_mesh")] += int(ma_mesh[i].sum())
            rec[(y, "deskryptorow")] += int(n_desk[i].sum())
        w_polu = mu.apply(lambda s: bool(set(s.split("|")) & FIELD) if s else False)
        for y, sub in d[w_polu].groupby(d.year[w_polu].astype(int)):
            y = int(y)
            rec[(y, "w_polu")] += len(sub)
            rec[(y, "deskryptorow_pola")] += int(n_desk[sub.index].sum())
            for s in mu[sub.index]:
                desk[y].update(set(s.split("|")) & FIELD)
        if (g + 1) % 400 == 0:
            print(f"  grupa {g+1}/{f.metadata.num_row_groups} "
                  f"({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    print(f"\n{'rok':>5} {'PubMed':>10} {'z MeSH':>8} {'% z MeSH':>9} "
          f"{'desk/rek':>9} {'pole':>8} {'% pola':>8} {'desk/rek pola':>14}")
    out = {}
    for y in YEARS:
        n = rec[(y, "wszystkie")]
        if not n:
            continue
        zm, wp = rec[(y, "z_mesh")], rec[(y, "w_polu")]
        row = {"pubmed": n, "z_mesh": zm, "pct_z_mesh": round(100 * zm / n, 2),
               "desk_na_rekord": round(rec[(y, "deskryptorow")] / max(zm, 1), 2),
               "pole": wp, "pct_pola": round(100 * wp / n, 3),
               "desk_na_rekord_pola": round(rec[(y, "deskryptorow_pola")] / max(wp, 1), 2)}
        out[y] = row
        print(f"{y:>5} {n:>10,} {zm:>8,} {row['pct_z_mesh']:>8.2f}% "
              f"{row['desk_na_rekord']:>9.2f} {wp:>8,} {row['pct_pola']:>7.3f}% "
              f"{row['desk_na_rekord_pola']:>14.2f}")

    # H3: sklad deskryptorow pola przed i po MTIX
    przed = Counter()
    po = Counter()
    for y in range(2015, 2022):
        przed.update(desk[y])
    for y in range(2023, 2026):
        po.update(desk[y])
    sp, so = sum(przed.values()), sum(po.values())
    zmiany = []
    for ui in FIELD:
        a, b = przed.get(ui, 0) / sp, po.get(ui, 0) / so
        if przed.get(ui, 0) + po.get(ui, 0) >= 200:
            zmiany.append((b - a, a, b, ui, nazwa.get(ui, "")))
    zmiany.sort()
    print(f"\n=== H3: sklad deskryptorow pola, 2015-2021 wobec 2023-2025 ===")
    print(f"{'deskryptor':<44} {'przed':>8} {'po':>8} {'zmiana':>9}")
    for d_, a, b, ui, nm in zmiany[:8] + zmiany[-8:]:
        print(f"{nm[:43]:<44} {100*a:>7.2f}% {100*b:>7.2f}% {100*d_:>+8.2f}pp")

    res = {"lata": out,
           "h3_sklad": [{"ui": ui, "nazwa": nm, "pct_2015_2021": round(100*a, 3),
                         "pct_2023_2025": round(100*b, 3), "zmiana_pp": round(100*d_, 3)}
                        for d_, a, b, ui, nm in zmiany]}
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nzapisane: {args.out}  ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
