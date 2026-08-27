"""extract_field_text.py — tytul i abstrakt dla rekordow pola, z pelnego lustra.

Po co osobny przebieg. `analytic_index` nie ma tekstu (celowo — to mianownik), a tabela `msk`
pokrywa tylko 90,74% pola. Brakujace 9,26% NIE sa losowe: sito MSK zbudowano ze slownika
dzisiejszego jezyka, wiec rekordy, ktore przez nie nie przeszly, to nieproporcjonalnie te
o nietypowej lub nowej terminologii — czyli populacja, w ktorej zyja terminy wschodzace.
Detektor oparty na `msk` bylby obciazony w strone slownictwa ugruntowanego, czyli mialby
dokladnie te wade, ktorej praca dotyczy.

Ktora wersje rekordu bierzemy. `analytic_index` niesie kolumne `_src` — plik, z ktorego
pochodzi zwycieski wiersz po dedupie. Kazdy worker czyta wiec tylko te PMID-y, dla ktorych
JEGO plik jest zwycieski. Dzieki temu nie ma etapu scalania i regula wyboru wersji jest
identyczna z medline_dedup.py, bez powtarzania jej logiki.

Uruchom:
    python code/extract_field_text.py --src D:/medline_2026 --parsed D:/medline_2026/parsed \
        --field data/processed/field_orthopedic_procedures.csv \
        --out D:/medline_2026/parsed/field_text.parquet
"""
from __future__ import annotations
import argparse, csv, gzip, re, sys, time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    import pandas as pd
    import pyarrow as pa
    import pyarrow.parquet as pq
except ImportError:
    sys.exit("pip install pandas pyarrow")

YEAR_MIN, YEAR_MAX = 2005, 2025


def text_of(el) -> str:
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip() if el is not None else ""


def worker(job: tuple[str, list[str]]) -> tuple[str, list[dict], str]:
    """Wyciaga tytul+abstrakt dla zadanych PMID-ow z jednego pliku lustra."""
    path, pmids = Path(job[0]), set(job[1])
    out = []
    try:
        with gzip.open(path, "rb") as fh:
            for _, elem in ET.iterparse(fh, events=("end",)):
                if not elem.tag.endswith("PubmedArticle"):
                    continue
                cit = elem.find("./MedlineCitation")
                if cit is not None:
                    pmid = (cit.findtext("./PMID") or "").strip()
                    if pmid in pmids:
                        art = cit.find("./Article")
                        title = text_of(art.find("./ArticleTitle")) if art is not None else ""
                        abstract = " ".join(
                            (("%s: " % a.get("Label")) if a.get("Label") else "") + text_of(a)
                            for a in art.findall("./Abstract/AbstractText")) if art is not None else ""
                        # pierwszy autor: nazwisko + inicjaly. Potrzebne do osi koncentracji
                        # autorskiej (§6). Bez dezambiguacji — "Kim J" sklei rozne osoby, co
                        # ZANIZA koncentracje, wiec wysoka koncentracja mimo sklejania jest
                        # tym mocniejszym sygnalem. Do ograniczen.
                        a1 = art.find("./AuthorList/Author") if art is not None else None
                        if a1 is not None:
                            last = (a1.findtext("./LastName") or "").strip()
                            init = (a1.findtext("./Initials") or "").strip()
                            coll = (a1.findtext("./CollectiveName") or "").strip()
                            author1 = f"{last} {init}".strip() or coll
                        else:
                            author1 = ""
                        out.append({"pmid": pmid, "title": title, "abstract": abstract,
                                    "author1": author1})
                elem.clear()
    except Exception as exc:
        return (path.name, out, f"{type(exc).__name__}: {exc}")
    return (path.name, out, "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--parsed", required=True)
    ap.add_argument("--field", help="CSV z UI deskryptorow MeSH (definicja 1)")
    ap.add_argument("--journals", help="CSV z NlmUniqueID czasopism (definicja 2)")
    ap.add_argument("--reuse", help="parquet z juz wyciagnietym tekstem — te PMID-y pomijamy")
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    if bool(args.field) == bool(args.journals):
        sys.exit("Podaj dokladnie jedno: --field (definicja 1) albo --journals (definicja 2).")
    pattern, jids = None, None
    if args.field:
        with open(args.field, encoding="utf-8") as fh:
            uis = [r["ui"] for r in csv.DictReader(fh) if r["ui"].strip()]
        bad = [u for u in uis if not re.fullmatch(r"D\d+", u)]
        if bad:
            sys.exit(f"UI o nietypowym formacie: {bad[:5]}")
        # granice separatora, bo UI nie maja stalej dlugosci (D019637 obok D000072228)
        pattern = r"(?:^|\|)(?:" + "|".join(uis) + r")(?:\||$)"
    else:
        with open(args.journals, encoding="utf-8") as fh:
            jids = {r["nlm_unique_id"].strip() for r in csv.DictReader(fh) if r["nlm_unique_id"].strip()}

    t0 = time.time()
    reuse = set()
    if args.reuse and Path(args.reuse).exists():
        reuse = set(pd.read_parquet(args.reuse, columns=["pmid"])["pmid"])
        print(f"ponowne uzycie: {len(reuse)} PMID-ow juz wyciagnietych", file=sys.stderr)
    pf = pq.ParquetFile(Path(args.parsed) / "analytic_index.parquet")
    by_src: dict[str, list[str]] = defaultdict(list)
    years: dict[str, int] = {}
    for g in range(pf.num_row_groups):
        df = pf.read_row_group(g, columns=["pmid", "year", "mesh_ui", "_src", "journal_nlm"]).to_pandas()
        yr = pd.to_numeric(df["year"], errors="coerce")
        inb = (df["mesh_ui"].str.contains(pattern, regex=True, na=False) if pattern is not None
               else df["journal_nlm"].isin(jids))
        sel = (yr >= YEAR_MIN) & (yr <= YEAR_MAX) & inb
        if reuse:
            sel &= ~df["pmid"].isin(reuse)
        if not sel.any():
            continue
        sub = df.loc[sel, ["pmid", "_src"]]
        for p, s in zip(sub["pmid"], sub["_src"]):
            by_src[s].append(p)
        for p, y in zip(sub["pmid"], yr[sel].astype(int)):
            years[p] = int(y)
    n_target = sum(len(v) for v in by_src.values())
    print(f"pole {YEAR_MIN}-{YEAR_MAX}: {n_target} rekordow w {len(by_src)} plikach", file=sys.stderr)

    src = Path(args.src)
    jobs = []
    for stem, pmids in by_src.items():
        for sub in ("baseline", "updatefiles"):
            p = src / sub / f"{stem}.xml.gz"
            if p.exists():
                jobs.append((str(p), pmids))
                break
        else:
            sys.exit(f"Nie znaleziono pliku zrodlowego dla {stem}")

    rows, errors, done = [], [], 0
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(worker, j) for j in jobs]
        for fut in as_completed(futures):
            name, got, err = fut.result()
            done += 1
            if err:
                errors.append(f"{name}: {err}")
            rows.extend(got)
            if done % 100 == 0:
                print(f"  [{done}/{len(jobs)}] {len(rows)} rekordow, "
                      f"{(time.time()-t0)/60:.1f} min", file=sys.stderr)

    df = pd.DataFrame(rows)
    if df.empty:
        sys.exit("Nic nie wyciagnieto.")
    df["year"] = df["pmid"].map(years)
    got = set(df["pmid"])
    missing = [p for v in by_src.values() for p in v if p not in got]

    # Ten sam PMID potrafi wystapic dwukrotnie w JEDNYM pliku lustra, a `pmid in pmids`
    # dopasowuje oba wystapienia — tak samo jak isin() w medline_dedup.py. Zwijamy
    # ta sama regula: zostaje pozniejsze wystapienie w kolejnosci dokumentu.
    dup = len(df) - df["pmid"].nunique()
    if dup:
        df = df.drop_duplicates(subset="pmid", keep="last")

    df.to_parquet(args.out, index=False)
    print(f"\nzapisano {args.out}: {len(df)} wierszy", file=sys.stderr)
    print(f"  brakujacych wobec celu : {len(missing)}", file=sys.stderr)
    print(f"  duplikatow PMID        : {dup}", file=sys.stderr)
    print(f"  pustych tytulow        : {int((df['title'].str.len() == 0).sum())}", file=sys.stderr)
    print(f"  pustych abstraktow     : {int((df['abstract'].str.len() == 0).sum())}", file=sys.stderr)
    if errors:
        print(f"  BLEDY ({len(errors)}): {errors[:3]}", file=sys.stderr)
    print(f"  czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 1 if (errors or missing or dup) else 0


if __name__ == "__main__":
    sys.exit(main())
