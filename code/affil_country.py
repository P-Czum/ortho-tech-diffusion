"""affil_country.py — kraj pierwszego autora z afiliacji (os koncentracji geograficznej, §6).

Dlaczego z afiliacji, a nie z `country`. Pole `MedlineJournalInfo/Country` to kraj CZASOPISMA,
nie autora — praca z Seulu w czasopismie amerykanskim ma tam "United States". Do osi geograficznej
uzywamy wylacznie afiliacji pierwszego autora (`aff1`), zgodnie z §7 planu.

Format afiliacji jest przewidywalny: instytucja, miasto, kraj, czasem e-mail na koncu.
Dopasowujemy od KONCA napisu, bo nazwy krajow bywaja tez w nazwach instytucji
("China Medical University" w Tajwanie, "American Hospital of Paris" we Francji).

Lista wzorcow: data/canon/countries.csv — kolejnosc ma znaczenie, wzorce dluzsze i bardziej
swoiste ida pierwsze ("republic of korea" przed "korea", "hong kong" przed "china").

Rekordy bez rozpoznanego kraju wypadaja z MIANOWNIKA tej osi, a ich odsetek jest raportowany.
Nie zgadujemy.
"""
from __future__ import annotations
import csv, re, unicodedata
from pathlib import Path

EMAIL = re.compile(r"\S+@\S+")
# Kanadyjskie skroty prowincji wystepuja czesto BEZ nazwy kraju ("Montreal, QC").
CA_PROV = re.compile(r",\s*(?:QC|ON|AB|BC|MB|SK|NS|NB|NL|PE|YT|NT|NU|Ont|Que|Alta|Sask)\.?\s*$", re.I)


def strip_diacritics(s: str) -> str:
    """Afiliacje bywaja pisane z diakrytykami: Montreal, Turkiye, Espana, Wurzburg.
    Bez normalizacji wzorce ASCII ich nie lapia — to byla najwieksza pojedyncza luka."""
    return "".join(c for c in unicodedata.normalize("NFKD", s)
                   if not unicodedata.combining(c))
# ", XX 12345" albo ", XX 12345-6789" — stan + ZIP, jednoznacznie USA
US_ZIP = re.compile(r",\s*[A-Z]{2}\s+\d{5}(?:-\d{4})?\b")
US_STATES = {
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut",
    "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa",
    "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan",
    "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new hampshire",
    "new jersey", "new mexico", "new york", "north carolina", "north dakota", "ohio",
    "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina", "south dakota",
    "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west virginia",
    "wisconsin", "wyoming",
}


def load_patterns(path: Path) -> list[tuple[re.Pattern, str]]:
    out = []
    with open(path, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            p, c = (r.get("pattern") or "").strip(), (r.get("canonical") or "").strip()
            if not p or not c or p.startswith("#"):
                continue
            out.append((re.compile(rf"\b{p}\b", re.I), c))
    return out


def make_matcher(canon_dir: Path):
    pats = load_patterns(canon_dir / "countries.csv")

    def country(aff: str) -> str:
        if not aff:
            return ""
        s = strip_diacritics(EMAIL.sub(" ", aff))
        # dopasowanie od konca: bierzemy trafienie o najwiekszym offsecie,
        # bo kraj stoi na koncu, a nazwy krajow bywaja w nazwach instytucji
        best_pos, best = -1, ""
        for rx, name in pats:
            m = None
            for m in rx.finditer(s):
                pass
            if m is not None and m.start() > best_pos:
                best_pos, best = m.start(), name
        if best:
            return best
        if US_ZIP.search(s):
            return "USA"
        if CA_PROV.search(s.strip().rstrip(".") + " "):
            return "Canada"
        low = s.lower()
        for st in US_STATES:
            if re.search(rf"\b{re.escape(st)}\b", low):
                return "USA"
        return ""

    return country
