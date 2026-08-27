"""stage1_field.py — Etap 1, krok 1: rozmiar pola i podstawowe szeregi tla.

Liczy na `analytic_index.parquet` (po dedupie):
  * przynaleznosc do pola wg definicji podstawowej: >=1 deskryptor MeSH z poddrzewa
    `Orthopedic Procedures` (56 UI z field_orthopedic_procedures.csv),
  * liczebnosc pola po latach 2005-2025 oraz liczebnosc calego zadeklarowanego podzbioru,
  * zgodnosc `indexed` vs `medline_indexed` WIERSZ PO WIERSZU (nie srednie),
  * odsetek rekordow z abstraktem po dekadach, w polu i poza,
  * rozklad `status` w polu,
  * szereg do testu nieciaglosci MTIX-2022.

Tabela ma ~41 mln wierszy i ~3,7 GB, wiec czytamy po grupach wierszy (jedna grupa =
jeden plik zrodlowy), nigdy w calosci: pelny wczyt to ~36 GB w pandas.

Uruchom:
    python code/stage1_field.py --parsed D:/medline_2026/parsed \
        --field data/processed/field_orthopedic_procedures.csv \
        --out data/processed/stage1_field.json
"""
from __future__ import annotations
import argparse, csv, json, sys, time
from collections import Counter, defaultdict
from pathlib import Path

try:
    import pandas as pd
    import pyarrow.parquet as pq
except ImportError:
    sys.exit("pip install pandas pyarrow")

COLS = ["pmid", "year", "mesh_ui", "status", "medline_indexed", "indexed",
        "has_abstract", "journal_nlm", "language", "pubtypes"]


def load_field_uis(path: Path) -> list[str]:
    with open(path, encoding="utf-8") as fh:
        uis = [r["ui"] for r in csv.DictReader(fh) if r["ui"].strip()]
    if not uis:
        sys.exit(f"Brak UI w {path}")
    import re as _re
    bad = [u for u in uis if not _re.fullmatch(r"D\d+", u)]
    if bad:
        sys.exit(f"UI o nietypowym formacie: {bad[:5]}")
    return uis


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parsed", required=True)
    ap.add_argument("--field", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit-groups", type=int, help="tylko N pierwszych grup (do testu)")
    args = ap.parse_args()

    uis = load_field_uis(Path(args.field))
    # UI MeSH NIE maja stalej dlugosci: obok D019637 wystepuja D000072228 (D + 9 cyfr).
    # Dopasowanie podciagiem byloby wiec niebezpieczne — krotszy UI moglby byc prefiksem
    # dluzszego obecnego w danych. Dopasowujemy z granicami separatora `|`.
    pattern = r"(?:^|\|)(?:" + "|".join(uis) + r")(?:\||$)"
    print(f"deskryptorow pola: {len(uis)}", file=sys.stderr)

    pf = pq.ParquetFile(Path(args.parsed) / "analytic_index.parquet")
    n_groups = pf.num_row_groups
    if args.limit_groups:
        n_groups = min(n_groups, args.limit_groups)
    print(f"grup wierszy: {n_groups}", file=sys.stderr)

    field_by_year: Counter = Counter()
    all_by_year: Counter = Counter()
    field_abs_by_year: Counter = Counter()      # w polu, z abstraktem
    all_abs_by_year: Counter = Counter()
    field_status: Counter = Counter()
    field_lang_en_by_year: Counter = Counter()
    status_by_year: defaultdict = defaultdict(Counter)
    n_rows = n_field = 0
    # zgodnosc indexed vs medline_indexed — tablica 2x2, wiersz po wierszu
    agree = Counter()

    t0 = time.time()
    for g in range(n_groups):
        df = pf.read_row_group(g, columns=COLS).to_pandas()
        n_rows += len(df)

        in_field = df["mesh_ui"].str.contains(pattern, regex=True, na=False)
        n_field += int(in_field.sum())

        yr = pd.to_numeric(df["year"], errors="coerce")
        has_abs = df["has_abstract"].astype(bool)
        en = df["language"].str.contains("eng", case=False, na=False)

        all_by_year.update(yr.dropna().astype(int).value_counts().to_dict())
        all_abs_by_year.update(yr[has_abs].dropna().astype(int).value_counts().to_dict())

        fy = yr[in_field]
        field_by_year.update(fy.dropna().astype(int).value_counts().to_dict())
        field_abs_by_year.update(yr[in_field & has_abs].dropna().astype(int).value_counts().to_dict())
        field_lang_en_by_year.update(yr[in_field & en].dropna().astype(int).value_counts().to_dict())
        field_status.update(df.loc[in_field, "status"].value_counts().to_dict())
        for y, s in zip(fy.dropna().astype(int), df.loc[in_field & yr.notna(), "status"]):
            status_by_year[y][s] += 1

        ix = df["indexed"].astype(bool)
        mix = df["medline_indexed"].astype(bool)
        agree["oba_true"] += int((ix & mix).sum())
        agree["oba_false"] += int((~ix & ~mix).sum())
        agree["indexed_bez_medline"] += int((ix & ~mix).sum())
        agree["medline_bez_indexed"] += int((~ix & mix).sum())

        if (g + 1) % 200 == 0:
            el = time.time() - t0
            print(f"  [{g+1}/{n_groups}] {n_rows:,} wierszy, {n_field:,} w polu, "
                  f"{el/60:.1f} min".replace(",", " "), file=sys.stderr)

    out = {
        "wierszy_ogolem": n_rows,
        "w_polu_ogolem": n_field,
        "deskryptorow_pola": len(uis),
        "indexed_vs_medline_indexed": dict(agree),
        "pole_status": dict(field_status),
        "pole_po_latach": {str(y): field_by_year[y] for y in sorted(field_by_year)},
        "wszystko_po_latach": {str(y): all_by_year[y] for y in sorted(all_by_year)},
        "pole_z_abstraktem_po_latach": {str(y): field_abs_by_year[y] for y in sorted(field_abs_by_year)},
        "wszystko_z_abstraktem_po_latach": {str(y): all_abs_by_year[y] for y in sorted(all_abs_by_year)},
        "pole_angielski_po_latach": {str(y): field_lang_en_by_year[y] for y in sorted(field_lang_en_by_year)},
        "pole_status_po_latach": {str(y): dict(c) for y, c in sorted(status_by_year.items())},
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nzapisano {args.out} | czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
