"""medline_extract.py — parsowanie lustra MEDLINE do tabel analitycznych.

Z kazdego pubmed26nXXXX.xml.gz robi dwa wyjscia:

  index/<plik>.parquet  — WSZYSTKIE rekordy, bez tekstu: pmid, rok, miesiac, doi, czasopismo,
                          typy publikacji, MeSH (UI), jezyk, afiliacja pierwszego autora,
                          oraz TRZY ROZNE flagi statusu (patrz nizej).
                          To jest mianownik do normalizacji trendow.

UWAGA — PubMed to nie MEDLINE. Baseline zawiera caly PubMed; MEDLINE jest jego podzbiorem.
Dlatego zapisujemy osobno:
  status           — MedlineCitation/@Status: MEDLINE | In-Process | In-Data-Review |
                     Publisher | PubMed-not-MEDLINE | OLDMEDLINE
  medline_indexed  — status == "MEDLINE" (rekord w pelni zaindeksowany w MEDLINE)
  indexed          — rekord ma jakikolwiek deskryptor MeSH
  citation_subset  — podzbiory NLM (np. IM)
Mianownik trendu musi byc liczony na jednoznacznie zdefiniowanym podzbiorze, a nie "na PubMedzie".
  msk/<plik>.parquet    — rekordy przechodzace szerokie sito miesniowo-szkieletowe:
                          to samo + tytul, abstrakt i MeSH slownie.

Sito jest celowo szerokie (czulosc przed swoistoscia) — zawezanie robimy pozniej na tabeli,
nie na etapie parsowania, zeby nie trzeba bylo czytac 38 mln rekordow drugi raz.

Uruchom z Windows: python code/medline_extract.py --src D:/medline_2026 --out D:/medline_2026/parsed
"""
from __future__ import annotations
import argparse, gzip, logging, os, re, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    import pandas as pd
except ImportError:
    sys.exit("pip install pandas pyarrow")

# --- szerokie sito MSK -------------------------------------------------------
MESH_MSK = {
    "orthopedics", "orthopedic procedures", "arthroplasty", "arthroplasty, replacement",
    "arthroplasty, replacement, hip", "arthroplasty, replacement, knee", "joint prosthesis",
    "hip prosthesis", "knee prosthesis", "prosthesis implantation", "bone plates",
    "bone screws", "bone nails", "fracture fixation", "fracture fixation, internal",
    "fractures, bone", "musculoskeletal diseases", "bone diseases", "joint diseases",
    "spinal diseases", "spinal fusion", "osteoarthritis", "osteoarthritis, hip",
    "osteoarthritis, knee", "osteoporosis", "scoliosis", "rotator cuff",
    "anterior cruciate ligament", "cartilage, articular", "bone and bones",
    "bone regeneration", "bone transplantation", "amputation", "arthroscopy",
    "sports medicine", "athletic injuries", "tendon injuries",
}
TEXT_MSK = re.compile(
    r"orthopa?edic|arthroplast|arthroscop|osteotom|osteosynthes|spinal fusion|spondylo"
    r"|scolios|rotator cuff|meniscus|meniscal|cruciate ligament|\bacl\b|labral"
    r"|femoral neck|hip fracture|distal radius|tibial|femoral shaft|intramedullary"
    r"|bone graft|nonunion|non-union|prosthe(?:sis|tic) joint|periprosthetic"
    r"|total (?:hip|knee|shoulder|ankle)|\bthа\b|\btha\b|\btka\b|\btsa\b"
    r"|musculoskeletal|osteoarthrit|osteoporo|fragility fracture|limb salvage",
    re.I)

TEXT_FIELDS = ("title", "abstract", "mesh_terms", "keywords")


def setup_logging(out: Path) -> str:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (out / "logs").mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler(out / "logs" / f"extract_{run_id}.log", encoding="utf-8"),
                  logging.StreamHandler(sys.stdout)])
    return run_id


MONTHS = {m: f"{i:02d}" for i, m in enumerate(
    ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"], 1)}


def norm_month(v: str) -> str:
    """MEDLINE miesza '12', 'Jul' i puste. Normalizujemy do '01'-'12' albo ''."""
    v = (v or "").strip()
    if v.isdigit():
        return f"{int(v):02d}" if 1 <= int(v) <= 12 else ""
    return MONTHS.get(v[:3].lower(), "")


def text_of(el) -> str:
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip() if el is not None else ""


def parse_year_month(article) -> tuple[str, str]:
    """ArticleDate ma pierwszenstwo (data elektroniczna), potem PubDate, potem MedlineDate."""
    ad = article.find("./ArticleDate")
    if ad is not None:
        return (text_of(ad.find("Year")), norm_month(text_of(ad.find("Month"))))
    pd_ = article.find("./Journal/JournalIssue/PubDate")
    if pd_ is None:
        return ("", "")
    y = text_of(pd_.find("Year"))
    if y:
        return (y, norm_month(text_of(pd_.find("Month"))))
    md = text_of(pd_.find("MedlineDate"))          # np. "2019 Jan-Feb"
    m = re.match(r"(\d{4})", md)
    return (m.group(1) if m else "", "")


def parse_record(cit) -> dict:
    art = cit.find("./Article")
    pmid = text_of(cit.find("./PMID"))
    year, month = parse_year_month(art) if art is not None else ("", "")

    mesh_ui, mesh_terms, mesh_major = [], [], []
    for mh in cit.findall("./MeshHeadingList/MeshHeading/DescriptorName"):
        mesh_ui.append(mh.get("UI", ""))
        mesh_terms.append(mh.text or "")
        if mh.get("MajorTopicYN") == "Y":
            mesh_major.append(mh.text or "")

    abstract = " ".join(
        (("%s: " % a.get("Label")) if a.get("Label") else "") + text_of(a)
        for a in art.findall("./Abstract/AbstractText")) if art is not None else ""

    a1 = art.find("./AuthorList/Author") if art is not None else None
    status = cit.get("Status", "")
    return {
        "pmid": pmid,
        "year": year,
        "month": month,
        "status": status,
        "medline_indexed": status == "MEDLINE",
        "citation_subset": "|".join(text_of(c) for c in cit.findall("./CitationSubset")),
        "aff1": text_of(a1.find("./AffiliationInfo/Affiliation")) if a1 is not None else "",
        "journal": text_of(art.find("./Journal/Title")) if art is not None else "",
        "journal_nlm": text_of(cit.find("./MedlineJournalInfo/NlmUniqueID")),
        "country": text_of(cit.find("./MedlineJournalInfo/Country")),
        "language": "|".join(text_of(l) for l in art.findall("./Language")) if art is not None else "",
        "pubtypes": "|".join(text_of(p) for p in art.findall("./PublicationTypeList/PublicationType"))
                    if art is not None else "",
        "n_authors": len(art.findall("./AuthorList/Author")) if art is not None else 0,
        "mesh_ui": "|".join(mesh_ui),
        "mesh_terms": "|".join(mesh_terms),
        "mesh_major": "|".join(mesh_major),
        "indexed": bool(mesh_ui),
        "has_abstract": bool(abstract),
        "title": text_of(art.find("./ArticleTitle")) if art is not None else "",
        "abstract": abstract,
        "keywords": "|".join(text_of(k) for k in cit.findall("./KeywordList/Keyword")),
    }


def is_msk(rec: dict) -> bool:
    if {t.strip().lower() for t in rec["mesh_terms"].split("|")} & MESH_MSK:
        return True
    return bool(TEXT_MSK.search(" ".join(rec[f] for f in TEXT_FIELDS)))


INDEX_COLS = ["pmid", "year", "month", "journal_nlm", "country", "language", "pubtypes",
              "n_authors", "mesh_ui", "status", "medline_indexed", "citation_subset",
              "indexed", "has_abstract", "doi", "aff1"]


def parse_file(path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    index_rows, msk_rows = [], []
    with gzip.open(path, "rb") as fh:
        for _, elem in ET.iterparse(fh, events=("end",)):
            if not elem.tag.endswith("PubmedArticle"):
                continue
            cit = elem.find("./MedlineCitation")
            if cit is not None:
                rec = parse_record(cit)
                doi = ""
                for aid in elem.findall("./PubmedData/ArticleIdList/ArticleId"):
                    if aid.get("IdType") == "doi":
                        doi = (aid.text or "").strip()
                rec["doi"] = doi
                index_rows.append({k: rec[k] for k in INDEX_COLS})
                if is_msk(rec):
                    msk_rows.append(rec)
            elem.clear()
    return pd.DataFrame(index_rows), pd.DataFrame(msk_rows)


def process_one(job: tuple[str, str]) -> tuple[str, int, int, str]:
    """Worker: parsuje jeden plik i od razu zapisuje parquet, zeby nie odsylac
    ramek przez IPC. Zwraca (stem, n_index, n_msk, blad)."""
    src, out = Path(job[0]), Path(job[1])
    stem = src.name.split(".")[0]
    try:
        idx, msk = parse_file(src)
    except Exception as exc:
        return (stem, 0, 0, f"{type(exc).__name__}: {exc}")
    idx.to_parquet(out / "index" / f"{stem}.parquet", index=False)
    if len(msk):
        msk.to_parquet(out / "msk" / f"{stem}.parquet", index=False)
    return (stem, len(idx), len(msk), "")


def main() -> int:
    ap = argparse.ArgumentParser(description="Parsowanie lustra MEDLINE do parquet.")
    ap.add_argument("--src", required=True, help="katalog z baseline/ i updatefiles/")
    ap.add_argument("--out", required=True, help="katalog wyjsciowy")
    ap.add_argument("--limit", type=int, help="przetworz najwyzej N plikow (do testu)")
    ap.add_argument("--workers", type=int, default=min(8, os.cpu_count() or 4),
                    help="rownolegle procesy parsujace (kazdy plik jest niezalezny)")
    args = ap.parse_args()

    src, out = Path(args.src).resolve(), Path(args.out).resolve()
    (out / "index").mkdir(parents=True, exist_ok=True)
    (out / "msk").mkdir(parents=True, exist_ok=True)
    run_id = setup_logging(out)

    files = sorted(p for sub in ("baseline", "updatefiles") for p in (src / sub).glob("*.xml.gz"))
    todo = [p for p in files if not (out / "index" / f"{p.name.split('.')[0]}.parquet").exists()]
    logging.info(f"START run_id={run_id} plikow={len(files)} do zrobienia={len(todo)}")
    if args.limit:
        todo = todo[: args.limit]

    t0, n_idx, n_msk, n_err = time.time(), 0, 0, 0
    logging.info(f"workers={args.workers}")
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(process_one, (str(p), str(out))) for p in todo]
        for i, fut in enumerate(as_completed(futures), 1):
            stem, ni, nm, err = fut.result()
            if err:
                n_err += 1
                logging.error(f"  ! {stem}: {err}")
                continue
            n_idx += ni; n_msk += nm
            el = time.time() - t0
            logging.info(f"  [{i}/{len(todo)}] {stem}: {ni} rekordow, {nm} MSK "
                         f"| lacznie {n_idx}/{n_msk} | eta {(len(todo)-i)/(i/el)/60:.1f} min")

    logging.info(f"END rekordow={n_idx} MSK={n_msk} ({100*n_msk/max(n_idx,1):.2f}%) "
                 f"bledow={n_err} elapsed={(time.time()-t0)/60:.1f} min")
    return 0


if __name__ == "__main__":
    sys.exit(main())
