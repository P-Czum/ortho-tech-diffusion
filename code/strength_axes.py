"""strength_axes.py — osie sily dla terminow z rdzenia (plan §6).

Trzy osie koncentracji, tempo i pulap. Liczone w oknie od `y0` do 2025 — koncentracja
przed wylonieniem to szum z pojedynczych prac.

Koncentracja mierzona DWOMA liczbami na os, nieprowadzonymi do jednej:
  * udzial najwiekszego (autora / kraju / czasopisma)
  * efektywna liczba = 1/HHI (odwrotnosc indeksu Herfindahla)

Roznica miedzy "najwiekszy osrodek odpowiada za 4% prac" a "za 48%" to roznica miedzy
dyfuzja a dorobkiem jednej grupy — i tego jedna liczba nie odda.

TOZSAMOSC AUTORA: nazwisko+inicjaly NIE WYSTARCZA. Zmierzone na tym korpusie: mediana
licznosci nazwiska pierwszego autora wynosi 15 dla Chin i 14 dla Korei, wobec 1 dla Brazylii
i 2 dla Turcji. Sklejanie roznych osob w jedno nazwisko PODNOSI udzial najczestszego autora
i OBNIZA efektywna ich liczbe — czyli ZAWYZA koncentracje, a nie zaniza. Blad jest przy tym
roznicowy: termin badany glownie w Chinach wyszedlby na sztucznie skoncentrowany, co tworzy
pozorna korelacje z osia krajowa.

Uzywamy wiec klucza `nazwisko|kraj|instytucja`, ktory zrownuje rozpietosc miedzykrajowa
z 3,0x do 1,0x. Ma wlasne obciazenie — ta sama osoba zmieniajaca instytucje rozpada sie na
dwie tozsamosci — ale ono ZANIZA koncentracje, czyli idzie w strone bezpieczna: wysoka
zmierzona koncentracja jest dolnym oszacowaniem.

KRAJ: wylacznie z afiliacji pierwszego autora (`aff1`). Pole MedlineJournalInfo/Country to
kraj CZASOPISMA i do tej osi sie nie nadaje.

Uruchom:
    python code/strength_axes.py --sheet data/processed/coding_sheet.csv \
        --text D:/medline_2026/parsed/field_text.parquet \
        --auth D:/medline_2026/parsed/field_text_auth.parquet \
        --parsed D:/medline_2026/parsed --canon data/canon \
        --denom D:/medline_2026/parsed/terms_primary.denom.json \
        --out data/processed/coding_sheet_full.csv
"""
from __future__ import annotations
import argparse, csv, json, re, sys, time
from collections import Counter, defaultdict
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
    import pyarrow.parquet as pq
except ImportError:
    sys.exit("pip install pandas pyarrow")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402
from affil_country import make_matcher, strip_diacritics  # noqa: E402

YEAR_MIN, YEAR_MAX = 2005, 2025
INST = re.compile(
    r"[^,]*\b(?:university|universit|hospital|institute|institut|center|centre|clinic|"
    r"college|school|klinik|krankenhaus|hopital|ospedale|hospit)\b[^,]*", re.I)


def institution(aff: str) -> str:
    m = INST.search(strip_diacritics(aff or ""))
    if not m:
        return ""
    return " ".join(re.sub(r"[^a-z ]", " ", m.group(0).lower()).split()[:4])


def concentration(c: Counter) -> tuple[float, float, int, str]:
    """Zwraca (udzial najwiekszego, efektywna liczba = 1/HHI, liczba obserwacji, nazwa najwiekszego).

    Nazwa jest istotna, nie ozdobna: "48,9% Chiny" i "48,9% USA" to zupelnie inne
    historie o tym, gdzie technologia jest badana."""
    n = sum(c.values())
    if not n:
        return (float("nan"), float("nan"), 0, "")
    top, top_n = c.most_common(1)[0]
    p = np.array(list(c.values()), dtype=float) / n
    return (float(p.max()), float(1.0 / (p ** 2).sum()), n, top)


def ngrams(toks: list[str]) -> set[str]:
    out = set()
    for i, t in enumerate(toks):
        out.add(t)
        if i + 1 < len(toks):
            out.add(t + " " + toks[i + 1])
        if i + 2 < len(toks):
            out.add(t + " " + toks[i + 1] + " " + toks[i + 2])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    for a in ("--sheet", "--text", "--auth", "--parsed", "--canon", "--denom", "--out"):
        ap.add_argument(a, required=True)
    args = ap.parse_args()

    t0 = time.time()
    sheet = pd.read_csv(args.sheet, encoding="utf-8-sig")
    terms = list(sheet["term"])
    y0 = dict(zip(sheet["term"], sheet["y0"]))
    tid = {t: i for i, t in enumerate(terms)}
    print(f"terminow: {len(terms)}", file=sys.stderr)

    spell, irr, phr = load_lists(Path(args.canon))
    canon = make_canonicalizer(spell, irr, phr)
    cmatch = make_matcher(Path(args.canon))

    # metadane rekordow: kraj i czasopismo z analytic_index, autor z osobnego przebiegu
    meta = []
    pf = pq.ParquetFile(Path(args.parsed) / "analytic_index.parquet")
    for g in range(pf.num_row_groups):
        d = pf.read_row_group(g, columns=["pmid", "aff1", "journal_nlm"]).to_pandas()
        meta.append(d)
    meta = pd.concat(meta, ignore_index=True)
    auth = pd.read_parquet(args.auth, columns=["pmid", "author1"])
    txt = pd.read_parquet(args.text, columns=["pmid", "year", "title", "abstract"])
    df = txt.merge(meta, on="pmid", how="left").merge(auth, on="pmid", how="left")
    df["aff1"] = df["aff1"].fillna("")
    df["author1"] = df["author1"].fillna("")
    print(f"rekordow: {len(df)}, laczenie {(time.time()-t0)/60:.1f} min", file=sys.stderr)

    df["kraj"] = [cmatch(a) if a else "" for a in df["aff1"]]
    df["autor"] = [f"{a}|{k}|{institution(f)}" if a else ""
                   for a, k, f in zip(df["author1"], df["kraj"], df["aff1"])]

    ca = [Counter() for _ in terms]
    ck = [Counter() for _ in terms]
    cj = [Counter() for _ in terms]
    n_no_country = np.zeros(len(terms), dtype=np.int64)

    for i, (yr, title, abstract, autor, kraj, jn) in enumerate(zip(
            df["year"].values, df["title"].values, df["abstract"].values,
            df["autor"].values, df["kraj"].values, df["journal_nlm"].fillna("").values)):
        present = ngrams(canon(f"{title} {abstract}"))
        for t in present:
            j = tid.get(t)
            if j is None or int(yr) < y0[t]:
                continue
            if autor:
                ca[j][autor] += 1
            if kraj:
                ck[j][kraj] += 1
            else:
                n_no_country[j] += 1
            if jn:
                cj[j][jn] += 1
        if (i + 1) % 50000 == 0:
            print(f"  {i+1}/{len(df)} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    den = json.loads(Path(args.denom).read_text(encoding="utf-8"))["by_year"]
    years = list(range(YEAR_MIN, YEAR_MAX + 1))
    em = pd.read_parquet(Path(args.parsed) / "emerging_primary.parquet")
    em = em.set_index("term")

    add = []
    for t in terms:
        j = tid[t]
        a_top, a_eff, a_n, _ = concentration(ca[j])
        k_top, k_eff, k_n, k_name = concentration(ck[j])
        j_top, j_eff, j_n, j_name = concentration(cj[j])
        cnt = np.array([em.loc[t, f"y{y}"] for y in years], float)
        s = cnt / np.array([den[str(y)] for y in years], float)
        i0 = years.index(int(y0[t]))
        ipk = int(np.argmax(s))
        # tempo: nachylenie log-udzialu od y0 do szczytu, tylko przy >=3 latach
        slope = dbl = float("nan")
        if ipk - i0 >= 2:
            xs = np.arange(i0, ipk + 1)
            ys = s[i0:ipk + 1]
            m = ys > 0
            if m.sum() >= 3:
                slope = float(np.polyfit(xs[m], np.log(ys[m]), 1)[0])
                if slope > 0:
                    dbl = float(np.log(2) / slope)
        add.append({
            "autor_top_pct": round(100 * a_top, 1), "autor_eff_n": round(a_eff, 1),
            "kraj_top": k_name, "kraj_top_pct": round(100 * k_top, 1), "kraj_eff_n": round(k_eff, 1),
            "kraj_brak_pct": round(100 * n_no_country[j] / max(k_n + n_no_country[j], 1), 1),
            "czasopismo_top_nlm": j_name, "czasopismo_top_pct": round(100 * j_top, 1), "czasopismo_eff_n": round(j_eff, 1),
            "nachylenie_log": round(slope, 3) if slope == slope else "",
            "czas_podwojenia_lat": round(dbl, 1) if dbl == dbl else "",
            "trwalosc_2025_do_szczytu": round(s[-1] / s[ipk], 2) if s[ipk] > 0 else "",
            "prac_w_oknie": a_n,
        })

    out = pd.concat([sheet.reset_index(drop=True), pd.DataFrame(add)], axis=1)
    # kolumny do kodowania na koniec
    tail = [c for c in ("kategoria", "poprzednik", "uwagi") if c in out.columns]
    out = out[[c for c in out.columns if c not in tail] + tail]
    out.to_csv(args.out, index=False, encoding="utf-8-sig")
    print(f"\nzapisano {args.out}: {len(out)} wierszy, {len(out.columns)} kolumn", file=sys.stderr)
    print(f"  mediana kraj_brak_pct: {out['kraj_brak_pct'].median():.1f}%", file=sys.stderr)
    print(f"  czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
