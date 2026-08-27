"""nlm_broad_subject.py — lista czasopism NLM wg Broad Subject Term.

Po co: druga, niezalezna od indeksowania MeSH definicja pola (plan §2). Definicja
podstawowa wymaga deskryptora MeSH, wiec strukturalnie nie widzi rekordow spoza MEDLINE
ani swiezych, jeszcze niezaindeksowanych — a wlasnie tam szukamy terminow wschodzacych.

Zrodlo: NLM Catalog przez E-utilities, pole `[st]` (Broad Subject Term). Zapytanie jest
odtwarzalne i idzie do metod.

Uwaga na zakres: `currentlyindexed` zawezalby do czasopism indeksowanych DZIS, a okno badania
siega 2005 r. i obejmuje tytuly, ktore juz nie sa indeksowane. Domyslnie bierzemy wszystkie.

Uruchom:
    python code/nlm_broad_subject.py --term orthopedics --out data/processed/journals_orthopedics.csv
"""
from __future__ import annotations
import argparse, csv, json, sys, time, urllib.parse, urllib.request
from pathlib import Path

UA = {"User-Agent": "ortho-tech-diffusion/1.0 (research; przemek.czuma@gmail.com)"}
BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def get(url: str, retries: int = 4):
    for a in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return json.load(r)
        except Exception as exc:
            if a == retries - 1:
                sys.exit(f"E-utilities nie odpowiada: {type(exc).__name__}: {exc}")
            time.sleep(2 ** a)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--term", default="orthopedics", help="Broad Subject Term")
    ap.add_argument("--out", required=True)
    ap.add_argument("--currently-indexed", action="store_true",
                    help="zawez do czasopism indeksowanych obecnie (NIE zalecane dla okna historycznego)")
    args = ap.parse_args()

    term = f"{args.term}[st]"
    if args.currently_indexed:
        term += " AND currentlyindexed[All]"

    j = get(f"{BASE}/esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "nlmcatalog", "term": term, "retmode": "json", "retmax": 1000}))
    ids = j["esearchresult"]["idlist"]
    total = int(j["esearchresult"]["count"])
    print(f"zapytanie: {term!r} -> {total} rekordow, pobrano {len(ids)}", file=sys.stderr)
    if len(ids) < total:
        sys.exit(f"Niepelne pobranie ({len(ids)}/{total}) — podnies retmax.")

    rows, missing, wrong_heading = [], 0, []
    for i in range(0, len(ids), 200):
        chunk = ids[i:i + 200]
        s = get(f"{BASE}/esummary.fcgi?" + urllib.parse.urlencode(
            {"db": "nlmcatalog", "id": ",".join(chunk), "retmode": "json"}))
        for cid in chunk:
            r = s["result"].get(cid, {})
            nlm = (r.get("nlmuniqueid") or "").strip()
            if not nlm:
                missing += 1
                continue
            headings = [h for h in (r.get("broadheading") or [])]
            # kontrola: kazdy pobrany tytul musi faktycznie miec zadany Broad Subject Term
            if not any(args.term.lower() == h.lower() for h in headings):
                wrong_heading.append((nlm, headings))
            titles = r.get("titlemainlist") or [{}]
            issns = [x.get("issn", "") for x in (r.get("issnlist") or []) if x.get("issn")]
            rows.append({
                "nlm_unique_id": nlm,
                "title": (titles[0].get("title") or "").strip().rstrip("."),
                "medlineabbr": (r.get("medlineta") or "").strip(),
                "issn": ";".join(issns),
                "country": (r.get("country") or "").strip(),
                "startyear": (r.get("startyear") or "").strip(),
                "endyear": (r.get("endyear") or "").strip(),
                "currently_indexed": "1" if (r.get("currentindexingstatus") or "").upper() == "Y" else "0",
                "broad_headings": ";".join(headings),
                "catalog_uid": cid,
            })
        time.sleep(0.4)

    if wrong_heading:
        print(f"UWAGA: {len(wrong_heading)} rekordow bez zadanego Broad Subject Term "
              f"(np. {wrong_heading[:2]})", file=sys.stderr)

    rows.sort(key=lambda r: r["title"].lower())
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    dup = len(rows) - len({r["nlm_unique_id"] for r in rows})
    print(f"zapisano {args.out}: {len(rows)} czasopism"
          f"{f', {missing} bez NlmUniqueID' if missing else ''}"
          f"{f', {dup} zduplikowanych ID' if dup else ''}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
