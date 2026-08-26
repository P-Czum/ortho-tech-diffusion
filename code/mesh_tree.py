"""mesh_tree.py — rozwijanie poddrzew MeSH i daty wprowadzenia deskryptorow.

Zrodlo: plik deskryptorow MeSH (descYYYY.xml) z
https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/xmlmesh/

Po co: definicja pola ("Orthopedic Procedures + wszystkie potomne") musi byc rozwijana
programowo, bo numery drzewa zmieniaja sie miedzy rocznikami i lista przepisana recznie
cicho sie rozjedzie. Ten sam plik daje daty wprowadzenia deskryptorow, potrzebne do
zaznaczenia na wykresach walidacyjnych.

Uzycie:
    python code/mesh_tree.py --desc D:/mesh/desc2026.xml --root "Orthopedic Procedures" \
        --out D:/medline_2026/parsed/field_orthopedic_procedures.csv
    python code/mesh_tree.py --desc D:/mesh/desc2026.xml --intro "Printing, Three-Dimensional"
"""
from __future__ import annotations
import argparse, csv, sys
from xml.etree import ElementTree as ET


def load(desc_path: str) -> tuple[dict, dict, dict]:
    """Zwraca (ui2name, ui2trees, ui2year)."""
    ui2name, ui2trees, ui2year = {}, {}, {}
    for _, el in ET.iterparse(desc_path, events=("end",)):
        if el.tag != "DescriptorRecord":
            continue
        ui = el.findtext("./DescriptorUI") or ""
        ui2name[ui] = el.findtext("./DescriptorName/String") or ""
        ui2trees[ui] = [t.text for t in el.findall("./TreeNumberList/TreeNumber") if t.text]
        y = el.findtext("./DateIntroduced/Year")   # DateEstablished nie istnieje w obecnym DTD MeSH
        if y:
            ui2year[ui] = int(y)
        el.clear()
    return ui2name, ui2trees, ui2year


def resolve(name: str, ui2name: dict) -> str:
    target = name.strip().lower()
    hits = [u for u, n in ui2name.items() if n.lower() == target]
    if not hits:
        near = [n for n in ui2name.values() if target in n.lower()][:8]
        sys.exit(f"Nie ma deskryptora '{name}'." + (f" Czy chodzilo o: {near}" if near else ""))
    return hits[0]


def descendants(root_ui: str, ui2trees: dict) -> set[str]:
    """UI wszystkich deskryptorow, ktorych numer drzewa zaczyna sie od numeru korzenia."""
    roots = ui2trees.get(root_ui, [])
    if not roots:
        sys.exit("Deskryptor nie ma numerow drzewa (kwalifikator?).")
    out = {root_ui}
    for ui, trees in ui2trees.items():
        if any(t.startswith(r + ".") or t == r for t in trees for r in roots):
            out.add(ui)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Poddrzewa MeSH i daty wprowadzenia.")
    ap.add_argument("--desc", required=True, help="sciezka do descYYYY.xml")
    ap.add_argument("--root", action="append", default=[],
                    help="nazwa deskryptora-korzenia; mozna podac wielokrotnie")
    ap.add_argument("--intro", action="append", default=[],
                    help="nazwa deskryptora — wypisz rok wprowadzenia")
    ap.add_argument("--out", help="zapisz rozwiniete poddrzewo do CSV")
    args = ap.parse_args()

    ui2name, ui2trees, ui2year = load(args.desc)
    print(f"wczytano {len(ui2name)} deskryptorow", file=sys.stderr)

    for name in args.intro:
        ui = resolve(name, ui2name)
        print(f"{ui2name[ui]}\t{ui}\trok wprowadzenia: {ui2year.get(ui, 'brak')}"
              f"\tdrzewo: {','.join(ui2trees.get(ui, []))}")

    if not args.root:
        return 0

    uis: set[str] = set()
    for name in args.root:
        root_ui = resolve(name, ui2name)
        sub = descendants(root_ui, ui2trees)
        print(f"{ui2name[root_ui]} ({root_ui}): {len(sub)} deskryptorow w poddrzewie", file=sys.stderr)
        uis |= sub

    rows = sorted(({"ui": u, "name": ui2name[u], "year": ui2year.get(u, ""),
                    "trees": ";".join(ui2trees.get(u, []))} for u in uis),
                  key=lambda r: r["name"])
    print(f"lacznie unikalnych: {len(rows)}", file=sys.stderr)
    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["ui", "name", "year", "trees"])
            w.writeheader(); w.writerows(rows)
        print(f"zapisano {args.out}", file=sys.stderr)
    else:
        for r in rows[:40]:
            print(f"{r['ui']}\t{r['name']}\t{r['trees']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
