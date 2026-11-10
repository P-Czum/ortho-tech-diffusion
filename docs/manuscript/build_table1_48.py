"""Table 1 (material 48) from osie_48.csv + kraj_pochodzenia_48.csv + material_48.csv.
Usage: python3 -I build_table1_48.py <data/processed dir> <out.md>"""
import csv, sys
P = sys.argv[1].rstrip("/") + "/"; OUT = sys.argv[2]
rd = lambda n: list(csv.DictReader(open(P + n, encoding="utf-8-sig")))
osie = rd("osie_48.csv"); kraj = {r["grupa"]: r for r in rd("kraj_pochodzenia_48.csv")}; mat = rd("material_48.csv")
klasa = {r["grupa"]: r["klasa"] for r in mat}
KN = {"I": "Implant/material", "II": "Arthroplasty", "III": "Technique", "IV": "Assistive tool", "V": "Perioperative", "VI": "Biological"}
REASON = {"nachylenie niedodatnie": "slope ≤ 0", "szczyt < 2 lata po y0": "peak < 2 y after y₀"}
def cls(k):
    if k["lider"] == k["wczesne_top"] == k["przed_y0_top"]: return "same"
    if k["lider"] != k["wczesne_top"] and k["lider"] != k["przed_y0_top"]: return "flow"
    return "unclassified"
rows = []
for r in sorted(osie, key=lambda r: (int(r["y0"]), r["grupa"])):
    g = r["grupa"]; k = kraj[g]; y0 = int(r["y0"]); pk = int(r["rok_szczytu"])
    d = r["czas_podwojenia_lat"]
    if d: d = f"{float(d):.1f}"
    elif pk < y0: d = "— (peak before y₀)"
    else: d = f"— ({REASON.get(r['powod_braku_podwojenia'], r['powod_braku_podwojenia'])})"
    pkcell = f"{pk}" + ("‡" if pk < y0 else ("§" if pk == y0 else ""))
    orig = k["wczesne_top"] if k["wczesne_top"] == k["przed_y0_top"] else "—†"
    rows.append(f"| {g} | {KN[klasa[g].split('.')[0]]} | {y0} | {pkcell} | {d} | {float(r['kraj_eff_n']):.1f} | {r['kraj_top']} ({float(r['kraj_top_pct']):.0f} %) | {orig} | {cls(k)} |")
hdr = ("**Table 1.** The 48 technologies, in order of emergence. Doubling time in years (or why undefined); effective countries = 1 ÷ Σ p²; "
       "leading country = most papers from emergence onward, first-author affiliation; country of earliest papers = most frequent country among the ten earliest papers "
       "*and* among all papers before emergence, given only where the two agree (36 of 48); origin class = same (leading country is most frequent under both origin measures), "
       "flow (under neither), unclassified (one of the two).\n\n| Technology | Kind | y₀ | Peak | Doubling | Eff. countries | Leading country | Earliest papers | Origin |\n|---|---|---:|---:|---:|---:|---|---|---|\n")
foot = ("\n† the two origin measures name different countries. ‡ peaked in a short spike before the first three consecutive years above threshold "
        "(mesenchymal stem cells 2013, highly cross-linked polyethylene 2008). § peaked in its year of emergence.\n")
open(OUT, "w", encoding="utf-8").write(hdr + "\n".join(rows) + "\n" + foot)
print(len(rows), "rows;", sum("—†" in x for x in rows), "without origin;", sum("| same |" in x for x in rows), sum("| flow |" in x for x in rows))
