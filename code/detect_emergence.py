"""detect_emergence.py — detektor momentu wylonienia (plan §4) i wybor 50 do analizy (§5).

Regula, dokladnie jak w planie, przeliczalna recznie:

  s(y)  = udzial rekordow pola z danego roku, w ktorych termin wystepuje
  prog  = s(y) >= THETA (0,1% pola) ORAZ liczba prac >= MIN_PAPERS (5)
  y0    = pierwszy rok, w ktorym prog jest spelniony i UTRZYMUJE SIE przez >=PERSIST (3) lat
  dodatkowo: s(y0) >= RATIO (5) x poziom bazowy, ALBO poziom bazowy < THETA/5
  poziom bazowy = srednia s(y) z lat BASE_FROM..BASE_TO (2005-2007)
  y0 <= Y0_MAX (2023), zeby zmiescily sie trzy lata potwierdzenia

Detektor daje odpowiedz dwustanowa PLUS rok wylonienia. Nie jest miara sily — sila to trzy
osobne osie z §6, liczone osobno. Swiadomie nie uzywamy algorytmu Kleinberga (§4).

Wybor do analizy poglebionej (§5): 50 terminow wschodzacych o najwyzszej obecnosci
2021-2025, nazywane wprost "50 emerging terms with the highest 2021-2025 prevalence".
Nie "50 najsilniejszych" — skoro sila nie jest jedna liczba, ranking sily nie istnieje.

Uruchom:
    python code/detect_emergence.py --terms D:/medline_2026/parsed/terms.parquet \
        --text D:/medline_2026/parsed/field_text.parquet \
        --out D:/medline_2026/parsed/emerging.parquet
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
except ImportError:
    sys.exit("pip install pandas pyarrow")

YEAR_MIN, YEAR_MAX = 2005, 2025
THETA = 0.001          # 0,1% rekordow pola
MIN_PAPERS = 5
PERSIST = 3
RATIO = 5.0
BASE_FROM, BASE_TO = 2005, 2007
Y0_MAX = 2023
SEL_FROM, SEL_TO = 2021, 2025


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--terms", required=True)
    ap.add_argument("--text", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=50)
    args = ap.parse_args()

    years = list(range(YEAR_MIN, YEAR_MAX + 1))
    ycols = [f"y{y}" for y in years]

    # mianownik: liczba rekordow pola w danym roku, z tej samej podstawy co liczniki
    txt = pd.read_parquet(args.text, columns=["year"])
    denom = txt["year"].astype(int).value_counts().reindex(years).fillna(0).astype(int)
    if (denom == 0).any():
        sys.exit(f"Rok bez rekordow pola: {denom[denom == 0].index.tolist()}")
    print("mianownik (rekordy pola):", ", ".join(f"{y}:{denom[y]}" for y in years[:3]) + " ...",
          file=sys.stderr)

    df = pd.read_parquet(args.terms)
    cnt = df[ycols].to_numpy(dtype=np.float64)
    d = denom.to_numpy(dtype=np.float64)
    s = cnt / d                                     # udzial w polu, rok po roku

    # Prog wykrycia jest indywidualny dla terminu: max(THETA, RATIO x poziom bazowy).
    #
    # Dlaczego nie sam THETA (v0.7 §4). Przy stalym progu y0 przykleja sie do pierwszego roku
    # przekroczenia progu OBECNOSCI, a warunek "s(y0) >= 5 x baseline" jest wtedy sprawdzany
    # na poczatku szeregu, gdzie z definicji nie moze przejsc. Zmierzone: `robotic` rosnie
    # z 0,17% (2005) do 2,90% (2025), siedemnastokrotnie, a przy starej regule NIE jest
    # wykrywany, bo byl powyzej 0,1% juz w 2005.
    #
    # To nie jest nowy warunek, tylko ten sam wypowiedziany spojnie: dotychczasowy wyjatek
    # "albo baseline < THETA/5" jest przypadkiem szczegolnym, bo wtedy RATIO*baseline < THETA
    # i max() wynosi dokladnie THETA. Stary warunek ilorazowy jest przez to subsumowany
    # i nie wystepuje juz osobno.
    bi = [years.index(BASE_FROM), years.index(BASE_TO)]
    baseline = s[:, bi[0]:bi[1] + 1].mean(axis=1)
    thr = np.maximum(THETA, RATIO * baseline)

    above = (s >= thr[:, None]) & (cnt >= MIN_PAPERS)

    # y0: pierwszy rok z PERSIST kolejnymi latami powyzej progu
    n_y = len(years)
    run = np.zeros_like(above, dtype=np.int32)
    run[:, -1] = above[:, -1]
    for j in range(n_y - 2, -1, -1):
        run[:, j] = np.where(above[:, j], run[:, j + 1] + 1, 0)
    ok_start = run >= PERSIST
    has = ok_start.any(axis=1)
    first = np.where(has, ok_start.argmax(axis=1), -1)

    s_at_y0 = np.where(first >= 0, s[np.arange(len(s)), np.clip(first, 0, n_y - 1)], 0.0)
    y0 = np.where(first >= 0, np.array(years)[np.clip(first, 0, n_y - 1)], 0)
    cond_window = (y0 > 0) & (y0 <= Y0_MAX)

    emerging = has & cond_window
    df = df.assign(
        y0=np.where(emerging, y0, 0),
        baseline_share=baseline,
        share_at_y0=np.where(emerging, s_at_y0, np.nan),
        peak_share=s.max(axis=1),
        peak_year=np.array(years)[s.argmax(axis=1)],
        docs_2021_2025=df[[f"y{y}" for y in range(SEL_FROM, SEL_TO + 1)]].sum(axis=1),
        emerging=emerging,
    )
    sel_denom = int(denom.loc[SEL_FROM:SEL_TO].sum())
    df["prevalence_2021_2025"] = df["docs_2021_2025"] / sel_denom

    # Druga os wyboru (§5, wariant C z 2026-08-27). Sam ranking po obecnosci wybiera
    # to, co najczestsze, a najczestsze w abstraktach jest szablon metodologiczny:
    # technologie zyja przy 0,2-2% obecnosci, "cohort" i "were included" przy 4-18%.
    # Zmierzone: pierwsza technologia lądowala na pozycji 143.
    #
    # Miara nie wprowadza zadnej nowej stalej — dzieli osiagniety pulap przez PROG
    # WYLONIENIA TEGO TERMINU, czyli max(THETA, RATIO x baseline) z detektora. Czyta sie
    # wprost: "ile razy termin przekroczyl wlasna poprzeczke". Termin o wysokiej bazie
    # ma poprzeczke wysoko i musi urosnac proporcjonalnie, zeby wyprzedzic technologie.
    df["threshold"] = thr
    df["exceedance"] = np.where(emerging, s.max(axis=1) / thr, np.nan)

    df.to_parquet(args.out, index=False)
    em = df[df["emerging"]].copy()
    print(f"\nterminow ogolem        : {len(df)}", file=sys.stderr)
    print(f"wschodzacych           : {len(em)}  ({100*len(em)/len(df):.2f}%)", file=sys.stderr)
    print(f"  unigramy {int((em.n==1).sum())}, bigramy {int((em.n==2).sum())}, "
          f"trigramy {int((em.n==3).sum())}", file=sys.stderr)
    print(f"rozklad roku wylonienia:", file=sys.stderr)
    for y, c in em["y0"].value_counts().sort_index().items():
        print(f"    {y}: {c}", file=sys.stderr)

    cols = ["term", "n", "y0", "peak_year", "peak_share", "baseline_share", "threshold",
            "exceedance", "prevalence_2021_2025", "docs_total", "occurrences"]
    outdir = Path(args.out).parent
    # DWIE tabele, bez wazenia i bez laczenia w jedna liczbe — tak samo jak §6 raportuje
    # trzy osie sily obok siebie, zamiast sprowadzac je do rankingu.
    for label, key in (("prevalence", "prevalence_2021_2025"), ("exceedance", "exceedance")):
        t = em.sort_values(key, ascending=False).head(args.top)
        p = outdir / f"emerging_top_{label}.csv"
        t[cols].to_csv(p, index=False, encoding="utf-8")
        print(f"zapisano {p}", file=sys.stderr)
    print(f"zapisano {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
