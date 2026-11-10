"""Supplement S5 from table1_48.md, material_48.csv and wylaczenia_48.csv.
Usage: python3 -I build_S5.py <data/processed dir> <table1_48.md> <out.md>"""
import csv, sys, re, collections
P = sys.argv[1].rstrip("/") + "/"; T1 = sys.argv[2]; OUT = sys.argv[3]
rd = lambda n: list(csv.DictReader(open(P + n, encoding="utf-8-sig")))
mat = rd("material_48.csv"); wyl = rd("wylaczenia_48.csv")
KLASA = {"zbyt ogolna": "Too general", "brak wylonienia": "Does not emerge", "generyk": "Generic name of an established procedure",
         "nie technologia": "Not a technology", "obca dziedzina": "Another specialty", "wieloznaczny skrot": "Ambiguous abbreviation",
         "retronim": "Retronym", "metoda badawcza": "Research method", "powiklanie": "Complication"}
ORDER = ["zbyt ogolna", "generyk", "nie technologia", "powiklanie", "metoda badawcza", "retronim", "obca dziedzina", "wieloznaczny skrot", "brak wylonienia"]
def reason(r):
    p = r["powod"]
    m = re.search(r"\(([\d,\-]+%?)\)", p)
    if p.startswith("nazwa nie wskazuje"): return "name indicates neither a specific device nor a joint"
    if p.startswith("opisowa kategoria"): return "descriptive category of activity, not a named technology"
    if p.startswith("uwaga ortopedy"): return "surgeon's note 'too general'" + ("; variants merged by the surgeon" if "warianty" in p else "")
    if p.startswith("MRI w liczbie"): return "MRI in the plural: a general imaging method (as *CT imaging*); '?' on the sheet, reason confirmed by the surgeon 2026-10-30"
    if p.startswith("czynnik wzrostu"): return "a growth factor (molecule), not a technology (as *biomarker*); '?' on the sheet, reason confirmed 2026-10-30"
    if p.startswith("zabieg weterynaryjny"): return "veterinary procedure (66% of papers on dogs); records removed by the veterinary rule"
    if p.startswith("61,4% prac"): return "61.4% animal papers; below threshold after the veterinary rule"
    if p.startswith("brak dominujacego rozwiniecia; skrot wnosi"): return f"no dominant expansion; the abbreviation adds only 'abbreviation-only' papers ({m.group(1) if m else '—'}) that cannot be verified"
    if p.startswith("brak dominujacego rozwiniecia:"): return "no dominant expansion: cuff tear arthropathy 29.5%, CT angiography 16.7%"
    if p.startswith("nazwa powiklania"): return "name of a complication, not of a technology"
    if p.startswith("nazwa standardu"): return "name given to the standard when a rival appeared (" + re.search(r"\((.*)\)", p).group(1) + ")"
    if p.startswith("ogolne okreslenie"): return "adjective on a known procedure; retronym test negative"
    if p.startswith("82,5% prac stomatologicznych"): return "82.5% dental papers"
    if p.startswith("obszar chirurgii"): return "an area of surgery, not a procedure"
    if p.startswith("wskazanie"): return "an indication, not a technique"
    if p.startswith("system informatyczny"): return "an information system (organisation of care)"
    if p.startswith("przyrzad do badania"): return "instrument for testing implants, not used on patients (co-occurrence with material implants 9–25×)"
    if p.startswith("oprogramowanie do segmentacji"): return "segmentation software, an FEA tool (13.1×)"
    if p.startswith("po zliczeniu skrotu razem z pelna nazwa (3 541"): return "counted with its full form (3,541 papers) the group has no y₀: 2000–2002 baseline 1.35% of the field"
    if p.startswith("po zliczeniu skrotu"): return "counted with its full form, the group has no y₀ (S1.4)"
    if p.startswith("pelna nazwa nie jest"): return "full form is not a noun phrase and cannot be counted with the abbreviation (§4a)"
    if p.startswith("chirurgia naczyniowa"): return "vascular surgery; records removed by the vascular rule"
    if p.startswith("D5a usuwa"): return "the maxillofacial rule removes 44.0% of its papers (craniofacial planning); loses emergence"
    if p.startswith("w oknie 2000-2025"): return "higher baseline in the 2000–2025 window; below threshold"
    return p
DEC = {"ortopeda (PC)": "surgeon", "regula detektora": "detector rule", "ortopeda (PC) na rekomendacje VS Code": "surgeon, on the analyst's recommendation",
       "Cowork, decyzja D8; ortopeda (PC)": "scoping decision D8; surgeon", "kodeks v1.4 §4a": "coding manual §4a", "ortopeda (PC), potwierdzone z literatury": "surgeon, confirmed from the literature",
       "Cowork; ortopeda (PC)": "analyst; surgeon", "regula detektora (§4a)": "detector rule (§4a)", "regula pola D6": "field rule (veterinary)", "regula pola D6 (automatycznie)": "field rule (veterinary)",
       "kodeks v1.3 §2 (klauzula negatywna)": "coding manual v1.3 §2 (negative clause)", "VS Code (pomiar), przyjete przez Cowork": "measurement; analyst", "regula pola D4": "field rule (vascular)", "regula pola D5a": "field rule (maxillofacial)"}
SRC = {"stary": "candidate list", "nowy": "candidate list (2000 window)", "scalenie 4a": "merged under §4a", "propozycja VSC": "analyst's proposal, surgeon's decision",
       "synonim (np_synonimy)": "synonym list", "scalenie (90 z 91 prac robotycznych)": "merged (90 of 91 papers on robotic surgery)"}

out = ["# Supplement S5. The material in full: Table 1, the member phrases of each group, and every exclusion\n",
       "All numbers refer to the final material of 48 technology groups (86 phrases). Files: `osie_48.csv`, `kraj_pochodzenia_48.csv`, `material_48.csv`, `wylaczenia_48.csv`.\n",
       "## S5.1 Table 1\n", open(T1, encoding="utf-8").read().strip(), "\n",
       "## S5.2 Member phrases of each group\n",
       "A group is the union of the phrases listed: a record is counted once if it contains any of them. Phrases marked *merged under §4a* are the full forms of abbreviations added in the correction of 2026-10-28 (S1.4); the two marked *merged* in October 2026 are variants that had been agreed for the group but not counted (S1.3).\n",
       "| Group | Kind | Member phrases (how each entered) |\n|---|---|---|"]
groups = collections.OrderedDict()
for r in mat: groups.setdefault(r["grupa"], []).append(r)
for g, rs in sorted(groups.items(), key=lambda kv: (int(kv[1][0]["y0"]) if kv[1][0]["y0"] else 0, kv[0])):
    members = "; ".join(f"*{r['term']}* ({SRC.get(r['zrodlo'], r['zrodlo'])})" for r in rs)
    KIND = {"I": "Implant or material", "II": "Joint arthroplasty", "III": "Operative technique", "IV": "Assistive tool", "V": "Perioperative care", "VI": "Biological therapy"}
    kind = KIND[rs[0]["klasa"].split(".")[0]]
    out.append(f"| {g} | {kind} | {members} |")
out += ["\n## S5.3 Every phrase that was ever in a version of the material and is not in the final one\n",
        f"{len(wyl)} phrases in {len(set(r['grupa'] for r in wyl))} positions (a position is a phrase with its variants). Stage = the step of the project at which the position left; decision = who decided, under which rule. Five positions marked ¶ belong to the earlier window (2005–2025) and the field before the contamination rules, and were never candidates on the final field.\n"]
for k in ORDER:
    rows = [r for r in wyl if r["klasa"] == k]
    if not rows: continue
    pos = collections.OrderedDict()
    for r in rows: pos.setdefault(r["grupa"], []).append(r)
    out.append(f"\n**{KLASA[k]}** — {len(pos)} position{'s' if len(pos) > 1 else ''}, {len(rows)} phrase{'s' if len(rows) > 1 else ''}\n")
    out.append("| Position (phrases) | Stage | Reason | Decision |\n|---|---|---|---|")
    for g, rs in pos.items():
        phr = ", ".join(f"*{r['fraza']}*" for r in rs)
        early = "¶ " if rs[0]["etap"].startswith("wczesniejsze") else ""
        stage = rs[0]["etap"]
        stage = (stage.replace("lista kandydatow -> material roboczy", "candidate list → working material")
                 .replace("material 54 -> 48 (skroty scalone z pelna nazwa, §4a)", "material 54 → 48 (abbreviations merged, §4a)")
                 .replace("material 76 -> 66 (D8 w scoping_log)", "material 76 → 66 (scoping decision D8)")
                 .replace("wczesniejsze okno 2005-2025 / pole przed D4-D6", "earlier window / unfiltered field")
                 .replace("filtr weterynaryjny D6", "veterinary rule").replace("wieloznaczne skroty (§4a)", "ambiguous abbreviations (§4a)")
                 .replace("material 60 -> 56", "material 60 → 56").replace("material 66 -> 60", "material 66 → 60").replace("material 56 -> 54", "material 56 → 54")
                 .replace("dodane 2026-09-01 na oknie 2005-2025, zgubione przy przejsciu na okno 2000-2025", "agreed 2026-09-01, lost in the move to the 2000 window, recounted 2026-10-29")
                 .replace("przeglad kandydatow", "candidate review"))
        out.append(f"| {early}{phr} | {stage} ({rs[0]['data']}) | {reason(rs[0])} | {DEC.get(rs[0]['decyzja'], rs[0]['decyzja'])} |")
open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("S5 written:", len(groups), "groups,", len(wyl), "excluded phrases")
