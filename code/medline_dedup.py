"""medline_dedup.py — budowa tabeli analitycznej z lustra PubMed: dedup PMID + DeleteCitation.

Problem (luka BIBLIO poz. 10): rekord zmieniony po wydaniu baseline'u wystepuje DWA razy —
raz w baseline, raz w updatefiles. Bez reguly rozstrzygajacej mianownik jest zawyzony.
Osobno: pliki aktualizacyjne zawieraja <DeleteCitation> — PMID-y usuniete z PubMedu,
ktore muszą zniknac z korpusu.

Regula, ktora tu implementuje (zgodna z instrukcja NLM "baseline first, then updates in order"):

  1. pliki przetwarzane w kolejnosci rosnacej: baseline n0001..n1334, potem updatefiles n1335..
  2. dla powtorzonego PMID wygrywa WYSTAPIENIE Z NAJPOZNIEJSZEGO PLIKU
  3. PMID wymieniony w jakimkolwiek <DeleteCitation> jest usuwany z korpusu — niezaleznie
     od tego, w ktorym pliku wystapil (usuniecie zawsze jest pozniejsze niz rekord)

DeleteCitation wystepuje wylacznie w updatefiles, wiec skanujemy tylko je (~9 GB), a nie
caly baseline. Nie wymaga zmian w medline_extract.py.

Uzycie:
    python code/medline_dedup.py --src D:/medline_2026 --parsed D:/medline_2026/parsed
    python code/medline_dedup.py --src D:/medline_2026 --parsed D:/medline_2026/parsed --msk
"""
from __future__ import annotations
import argparse, gzip, json, re, sys, time
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    import numpy as np
    import pandas as pd
except ImportError:
    sys.exit("pip install pandas pyarrow")

FILE_ORDER = re.compile(r"pubmed(\d{2})n(\d{4})")


def sort_key(p: Path) -> tuple[int, int]:
    m = FILE_ORDER.search(p.name)
    return (int(m.group(1)), int(m.group(2))) if m else (99, 9999)


def deleted_pmids(update_dir: Path) -> tuple[set[str], int]:
    """PMID-y z <DeleteCitation> we wszystkich plikach aktualizacyjnych."""
    out: set[str] = set()
    files = sorted(update_dir.glob("*.xml.gz"), key=sort_key)
    for i, path in enumerate(files, 1):
        try:
            with gzip.open(path, "rb") as fh:
                for _, el in ET.iterparse(fh, events=("end",)):
                    if el.tag == "DeleteCitation":
                        out.update((p.text or "").strip() for p in el.findall("./PMID"))
                        el.clear()
                    elif el.tag in ("PubmedArticle", "PubmedBookArticle"):
                        el.clear()          # nie trzymamy artykulow w pamieci
        except Exception as exc:
            print(f"  ! {path.name}: {type(exc).__name__}: {exc}", file=sys.stderr)
        if i % 50 == 0:
            print(f"  DeleteCitation: {i}/{len(files)} plikow, {len(out)} PMID", file=sys.stderr)
    out.discard("")
    return out, len(files)


def _ord_of(p: Path) -> int:
    y, n = sort_key(p)
    return y * 10000 + n


def build(parsed: Path, sub: str, deleted: set[str], out_path: Path) -> dict:
    """Dwa przebiegi + strumieniowy zapis.

    Naiwne `pd.concat` wszystkich parquetow nie przechodzi na pelnej skali: zmierzone
    872 B/wiersz x ~48 mln wierszy = ~42 GB RAM. Dlatego przebieg 1 wczytuje wylacznie
    kolumne pmid (jako int64, 8 B/wiersz), rozstrzyga zwyciezcow, a przebieg 2 czyta
    pliki po kolei i dopisuje przefiltrowane wiersze przez ParquetWriter, nigdy nie
    trzymajac calosci w pamieci.
    """
    import pyarrow as pa
    import pyarrow.parquet as pq

    files = sorted((parsed / sub).glob("*.parquet"), key=sort_key)
    if not files:
        sys.exit(f"Brak plikow w {parsed / sub}")

    # --- przebieg 1: tylko pmid + numer pliku
    keys, n_bad = [], 0
    for p in files:
        s = pd.read_parquet(p, columns=["pmid"])["pmid"]
        v = pd.to_numeric(s, errors="coerce")
        n_bad += int(v.isna().sum())
        v = v.dropna().astype("int64")
        keys.append(pd.DataFrame({"pmid": v.values,
                                  "_ord": np.full(len(v), _ord_of(p), dtype="int64")}))
    k = pd.concat(keys, ignore_index=True)
    del keys
    n_raw = len(k)

    # 2. ostatni plik wygrywa
    k = k.sort_values("_ord", kind="stable").drop_duplicates("pmid", keep="last")
    n_dup = n_raw - len(k)

    # 3. skasowane
    before = len(k)
    if deleted:
        del_int = np.fromiter((int(d) for d in deleted if d.isdigit()), dtype="int64")
        k = k[~k["pmid"].isin(del_int)]
    n_del = before - len(k)

    # zwyciezcy w rozbiciu na plik zrodlowy — tablice numpy, nie zbiory Pythona
    winners = {o: g["pmid"].values for o, g in k.groupby("_ord", sort=False)}
    n_final_expected = len(k)
    del k

    # --- przebieg 2: strumieniowy zapis
    writer, schema, n_final = None, None, 0
    try:
        for p in files:
            w = winners.get(_ord_of(p))
            if w is None or not len(w):
                continue
            df = pd.read_parquet(p)
            df = df[pd.to_numeric(df["pmid"], errors="coerce").isin(w)]
            if df.empty:
                continue
            # Ten sam PMID potrafi wystapic dwa razy w JEDNYM pliku (rekord poprawiony
            # dwukrotnie w tej samej paczce aktualizacyjnej — zmierzone: 100 PMID-ow,
            # 115 nadmiarowych wierszy na 45 mln). Przebieg 1 zwija je przez
            # drop_duplicates(keep="last"), wiec przebieg 2 musi zrobic to samo:
            # isin() dopuszcza oba wiersze, bo pyta tylko o przynaleznosc PMID.
            df = df.drop_duplicates(subset="pmid", keep="last")
            df["_src"] = p.stem
            tbl = pa.Table.from_pandas(df, preserve_index=False)
            if writer is None:
                schema = tbl.schema
                writer = pq.ParquetWriter(out_path, schema)
            elif not tbl.schema.equals(schema):
                try:
                    tbl = tbl.cast(schema)
                except Exception as exc:
                    sys.exit(f"Niezgodny schemat w {p.name}: {exc}")
            writer.write_table(tbl)
            n_final += len(df)
    finally:
        if writer is not None:
            writer.close()

    stats = {"subset": sub, "wierszy_surowych": n_raw, "duplikatow_pmid": n_dup,
             "usunietych_DeleteCitation": n_del, "rekordow_finalnie": n_final,
             "plikow": len(files)}
    if n_bad:
        stats["pmid_nieliczbowych_pominietych"] = n_bad
    if n_final != n_final_expected:
        stats["OSTRZEZENIE"] = (f"zapisano {n_final}, oczekiwano {n_final_expected} "
                                "— rozjazd miedzy przebiegami")
    return stats


def main() -> int:
    ap = argparse.ArgumentParser(description="Dedup PMID + DeleteCitation -> tabela analityczna.")
    ap.add_argument("--src", required=True, help="katalog z baseline/ i updatefiles/")
    ap.add_argument("--parsed", required=True, help="katalog z index/ i msk/")
    ap.add_argument("--msk", action="store_true", help="zdeduplikuj takze tabele msk/")
    ap.add_argument("--deleted-cache", help="plik JSON z lista skasowanych PMID (zapis/odczyt)")
    args = ap.parse_args()

    src, parsed = Path(args.src).resolve(), Path(args.parsed).resolve()
    cache = Path(args.deleted_cache) if args.deleted_cache else parsed / "deleted_pmids.json"

    t0 = time.time()
    if cache.exists():
        deleted = set(json.loads(cache.read_text()))
        print(f"DeleteCitation z cache: {len(deleted)} PMID ({cache.name})")
    else:
        print("Skanuje updatefiles w poszukiwaniu <DeleteCitation>...")
        deleted, n_files = deleted_pmids(src / "updatefiles")
        cache.write_text(json.dumps(sorted(deleted)), encoding="utf-8")
        print(f"DeleteCitation: {len(deleted)} PMID z {n_files} plikow "
              f"({time.time()-t0:.0f}s) -> {cache.name}")

    report = []
    for sub in (["index", "msk"] if args.msk else ["index"]):
        out = parsed / f"analytic_{sub}.parquet"
        stats = build(parsed, sub, deleted, out)
        stats["plik_wyjsciowy"] = str(out)
        report.append(stats)
        print(json.dumps(stats, ensure_ascii=False, indent=2))

    (parsed / "dedup_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nRaport: {parsed / 'dedup_report.json'} | czas {time.time()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
