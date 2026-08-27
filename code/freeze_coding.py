"""freeze_coding.py — widok kodera i manifest zamrożenia (kodeks v1.1 §1, brief Cowork pkt 3).

Widok kodera to arkusz BEZ kolumn zaślepionych. Zaślepione są dokładnie te wielkości, które
kodeks §5 przewiduje jako niezależne kontrole po kodowaniu: czas podwojenia, trzy osie
koncentracji i wszystko, co z nich pochodzi. Kontrola, którą koder widzi podczas pracy, mierzy
jego posłuszeństwo wobec liczby, nie zgodność dwóch niezależnych dróg.

Manifest liczy sha256 wszystkich plików wchodzących do rejestracji. Od momentu zapisania
manifestu żaden z nich nie może się zmienić bez unieważnienia rejestracji — dlatego skrypt
odmawia nadpisania istniejącego manifestu bez --force.

Uruchom:
    python code/freeze_coding.py --sheet data/processed/coding_sheet_full.csv \
        --out-view data/processed/coding_sheet_koder.csv \
        --manifest docs/protocol/freeze_manifest.txt
"""
from __future__ import annotations
import argparse, hashlib, sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("pip install pandas")

ROOT = Path(__file__).resolve().parent.parent

# Kolumny zaślepione — pochodne osi siły z §6, służące jako kontrole PO kodowaniu (§5).
BLINDED = [
    "autor_top_pct", "autor_eff_n",
    "kraj_top", "kraj_top_pct", "kraj_eff_n", "kraj_brak_pct",
    "czasopismo_top_nlm", "czasopismo_top_pct", "czasopismo_eff_n",
    "nachylenie_log", "czas_podwojenia_lat", "trwalosc_2025_do_szczytu",
    "prac_w_oknie",
]

IN_MANIFEST = [
    "data/processed/coding_sheet_full.csv",
    "data/processed/coding_sheet_koder.csv",
    # Od 2026-08-27 material koderski jest po angielsku. Manifest haszuje to, czego
    # FAKTYCZNIE uzyto — wersje polskie zostaja w repo jako historia, ale poza manifestem.
    "docs/protocol/coding_manual_v1.2.md",
    "docs/protocol/prompt_system_v1.2_EN.txt",
    "docs/protocol/prompt_user_v1.2_EN.txt",
    "data/canon/spelling_uk_us.csv",
    "data/canon/irregular_plurals.csv",
    "data/canon/phrase_map.csv",
    "data/canon/countries.csv",
    "data/processed/field_orthopedic_procedures.csv",
    "data/processed/journals_orthopedics.csv",
    "data/processed/emerging_core.json",
]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        while blk := fh.read(1 << 20):
            h.update(blk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", required=True)
    ap.add_argument("--out-view", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    man = Path(args.manifest)
    if man.exists() and not args.force:
        sys.exit(f"{man} juz istnieje. Zamrozenie jest jednorazowe — uzyj --force tylko, "
                 f"jesli rejestracja NIE zostala jeszcze zlozona.")

    df = pd.read_csv(args.sheet, encoding="utf-8-sig")
    present = [c for c in BLINDED if c in df.columns]
    missing = [c for c in BLINDED if c not in df.columns]
    if missing:
        print(f"UWAGA: brak kolumn do zaslepienia: {missing}", file=sys.stderr)
    view = df.drop(columns=present)
    Path(args.out_view).parent.mkdir(parents=True, exist_ok=True)
    view.to_csv(args.out_view, index=False, encoding="utf-8-sig")
    print(f"widok kodera: {args.out_view} — {len(view)} wierszy, {len(view.columns)} kolumn "
          f"(zaslepiono {len(present)})", file=sys.stderr)

    lines = [
        "# Manifest zamrożenia — materiał prerejestracyjny",
        f"# Zamrożono: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "#",
        "# Od tej chwili żaden z poniższych plików nie może się zmienić bez unieważnienia",
        "# rejestracji. Kodowanie rusza po złożeniu rejestracji.",
        "#",
    ]
    bad = []
    for rel in IN_MANIFEST:
        p = ROOT / rel
        if not p.exists():
            bad.append(rel)
            lines.append(f"BRAK  {rel}")
            continue
        lines.append(f"{sha256(p)}  {rel}")
    man.parent.mkdir(parents=True, exist_ok=True)
    man.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"manifest: {man} — {len(IN_MANIFEST) - len(bad)}/{len(IN_MANIFEST)} plikow",
          file=sys.stderr)
    if bad:
        print(f"  BRAKUJACE: {bad}", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
