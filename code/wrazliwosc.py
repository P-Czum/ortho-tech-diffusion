"""wrazliwosc.py — analizy wrazliwosci po recenzji zewnetrznej (brief walidacja_po_recenzji, Z1/Z3/Z4).

Nic tu nie zmienia materialu 54 ani osi. Regula detektora jest przepisana jako jedna funkcja
z parametrami jawnie w argumentach; ZANIM policzymy jakikolwiek wariant, sprawdzamy, ze przy
parametrach domyslnych odtwarza ona dokladnie:
  - zbiory i y0 z emerging_d6_{primary,s2_abstract,s3_english}.parquet (poziom terminu),
  - y0 i rok szczytu z osie_54.csv (poziom grupy, szeregi z szeregi_grup.py).
Jesli ktores sie nie zgadza, skrypt konczy sie bledem — wariant liczony inna regula niz
wynik glowny bylby bezwartosciowy.

Z1  jeden parametr na raz (k = RATIO, m = PERSIST, theta), reszta domyslna.
    Y0_MAX = 2025 - (m - 1), tak jak w Box 1 ("hence y0 <= window end - 2" przy m = 3).
Z3  wylonienia primary, ktore odpadly na przecieciu z S2/S3 — gdzie i co to jest.
Z4  y0 grup na polu bez filtra D6 (D4+D5a+D5c) obok obecnego.

Uruchom (po szeregi_grup.py):
    python code/wrazliwosc.py
"""
from __future__ import annotations
import json, sys
from pathlib import Path

import numpy as np
import pandas as pd

P = Path("D:/medline_2026/parsed")
D = Path("data/processed")
R = Path("results")
YEARS = list(range(2000, 2026))
YC = [f"y{y}" for y in YEARS]
BAZA = (2000, 2002)
DOM = {"ratio": 5.0, "persist": 3, "theta": 0.001}
WARIANTY = ([("k", "ratio", v) for v in (3.0, 4.0, 7.0)]
            + [("m", "persist", v) for v in (2, 4)]
            + [("theta", "theta", v) for v in (0.0005, 0.002)])
TECH = {"technologia", "technika"}


def wykryj(cnt: np.ndarray, den: np.ndarray, ratio: float, persist: int, theta: float,
           min_prac: int = 5) -> np.ndarray:
    """y0 dla kazdego wiersza (0 = brak); ta sama regula co detect_emergence.py"""
    s = cnt / den
    b = s[:, YEARS.index(BAZA[0]):YEARS.index(BAZA[1]) + 1].mean(axis=1)
    above = (s >= np.maximum(theta, ratio * b)[:, None]) & (cnt >= min_prac)
    run = np.zeros(above.shape, dtype=np.int32)
    run[:, -1] = above[:, -1]
    for j in range(len(YEARS) - 2, -1, -1):
        run[:, j] = np.where(above[:, j], run[:, j + 1] + 1, 0)
    ok = run >= persist
    y0 = np.where(ok.any(axis=1), np.array(YEARS)[ok.argmax(axis=1)], 0)
    return np.where(y0 <= YEARS[-1] - (persist - 1), y0, 0)


def mianownik(nazwa: str) -> np.ndarray:
    m = json.loads((P / f"{nazwa}.denom.json").read_text(encoding="utf-8"))["by_year"]
    return np.array([m[str(y)] for y in YEARS], float)


def main() -> int:
    # --- poziom terminu: trzy warianty tekstu -------------------------------------------
    term = {}
    for v in ("primary", "s2_abstract", "s3_english"):
        t = pd.read_parquet(P / f"terms_d6_{v}.parquet", columns=["term"] + YC)
        y0 = wykryj(t[YC].to_numpy(float), mianownik(f"terms_d6_{v}"), **DOM)
        ref = pd.read_parquet(P / f"emerging_d6_{v}.parquet", columns=["term", "y0", "emerging"])
        ref = dict(zip(ref.term[ref.emerging], ref.y0[ref.emerging]))
        moje = {a: int(b) for a, b in zip(t.term, y0) if b}
        if moje != ref:
            sys.exit(f"KONTROLA: detektor nie odtwarza emerging_d6_{v} ({len(moje)} vs {len(ref)})")
        term[v] = t
    rdzen = set(json.loads((D / "rdzen_d6.json").read_text(encoding="utf-8")))
    print(f"kontrola terminow: 3 warianty odtworzone, rdzen {len(rdzen)}", file=sys.stderr)

    def rdzen_przy(**par) -> set[str]:
        zb = []
        for v, t in term.items():
            y0 = wykryj(t[YC].to_numpy(float), mianownik(f"terms_d6_{v}"), **par)
            zb.append(set(t.term[y0 > 0]))
        return zb[0] & zb[1] & zb[2]

    if rdzen_przy(**DOM) != rdzen:
        sys.exit("KONTROLA: przeciecie nie odtwarza rdzen_d6.json")

    # --- poziom grupy --------------------------------------------------------------------
    osie = pd.read_csv(D / "osie_54.csv", encoding="utf-8-sig").set_index("grupa")
    gp = pd.read_csv(D / "szeregi_54_prace.csv", encoding="utf-8-sig").set_index("grupa")
    dv = mianownik("terms_d6_primary")
    gc = gp[YC].to_numpy(float)
    y0_dom = pd.Series(wykryj(gc, dv, **DOM), index=gp.index)
    ref_y0 = osie["y0"].reindex(gp.index).fillna(0).astype(int)
    ref_pk = osie["rok_szczytu"].reindex(gp.index)
    pk = pd.Series(np.array(YEARS)[(gc / dv).argmax(axis=1)], index=gp.index)
    if not ((y0_dom == ref_y0).all() and (pk == ref_pk).all()):
        zle = gp.index[(y0_dom != ref_y0) | (pk != ref_pk)].tolist()
        sys.exit(f"KONTROLA: szeregi grup nie odtwarzaja osie_54: {zle}")
    print("kontrola grup: y0 i rok szczytu 54/54 zgodne z osie_54", file=sys.stderr)

    kat = pd.read_csv(D / "np_kategorie_propozycja.tsv", sep="\t")
    kat = dict(zip(kat.term, kat.kategoria))
    material = set(pd.read_csv(D / "material_54.csv", encoding="utf-8-sig").term)

    # --- Z1 ------------------------------------------------------------------------------
    wiersze, nowe = [], []
    for nazwa, klucz, wart in WARIANTY:
        par = {**DOM, klucz: wart}
        y0 = pd.Series(wykryj(gc, dv, **par), index=gp.index)
        wsp = (y0 > 0) & (y0_dom > 0)
        d = (y0 - y0_dom)[wsp]
        imax = d.abs().idxmax()
        rv = rdzen_przy(**par)
        przyb = sorted(rv - rdzen)
        k_tech = [t for t in przyb if kat.get(t) in TECH]
        k_zn = [t for t in przyb if t in kat]
        for t in przyb:
            nowe.append({"parametr": nazwa, "wartosc": wart, "term": t,
                         "kategoria_istniejaca": kat.get(t, "")})
        wiersze.append({
            "parametr": nazwa, "wartosc": wart,
            "grup_nadal_wylania": int((y0 > 0).sum()), "grup_z_54": len(gp),
            "grupy_wypadajace": " | ".join(gp.index[(y0 == 0) & (y0_dom > 0)]),
            "mediana_abs_dy0": float(d.abs().median()),
            "max_abs_dy0": int(abs(d[imax])), "max_dy0_grupa": imax if d[imax] else "",
            "rdzen": len(rv), "ubylo_z_rdzenia": len(rdzen - rv),
            "terminow_materialu_poza_rdzeniem": len(material - rv),
            "nowe_frazy_w_rdzeniu": len(przyb),
            "nowe_z_istniejaca_kategoria": len(k_zn),
            "nowe_technologia_lub_technika": len(k_tech),
            "nowe_technologie_nazwy": " | ".join(k_tech),
        })
    z1 = pd.DataFrame(wiersze)
    z1.to_csv(R / "wrazliwosc_parametrow.csv", index=False, encoding="utf-8-sig",
              lineterminator="\n")
    pd.DataFrame(nowe).to_csv(R / "wrazliwosc_nowe_frazy.csv", index=False,
                              encoding="utf-8-sig", lineterminator="\n")
    print(z1.drop(columns=["nowe_technologie_nazwy", "grupy_wypadajace"]).to_string(index=False))

    # --- Z3 ------------------------------------------------------------------------------
    em = {}
    for v, t in term.items():
        y0 = wykryj(t[YC].to_numpy(float), mianownik(f"terms_d6_{v}"), **DOM)
        em[v] = dict(zip(t.term[y0 > 0], y0[y0 > 0]))
    slow = {v: set(t.term) for v, t in term.items()}
    odp = []
    for t in sorted(set(em["primary"]) - rdzen):
        w2, w3 = t in em["s2_abstract"], t in em["s3_english"]
        odp.append({
            "term": t, "y0_primary": int(em["primary"][t]),
            "wypada_w": "oba" if not (w2 or w3) else ("S2" if not w2 else "S3"),
            "s2": "wylania" if w2 else ("nie wylania" if t in slow["s2_abstract"] else "brak w slowniku"),
            "s3": "wylania" if w3 else ("nie wylania" if t in slow["s3_english"] else "brak w slowniku"),
            "kategoria_istniejaca": kat.get(t, ""),
        })
    z3 = pd.DataFrame(odp)
    z3.to_csv(R / "warianty_odrzucone.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    print(f"\nZ3: primary {len(em['primary'])}, rdzen {len(rdzen)}, odpada {len(z3)}")
    print(z3.wypada_w.value_counts().to_string())
    print(z3.kategoria_istniejaca.replace("", "(brak)").value_counts().to_string())
    print(z3[z3.kategoria_istniejaca.isin(TECH)].to_string(index=False))

    # --- Z4 ------------------------------------------------------------------------------
    bp = pd.read_csv(R / "szeregi_54_bez_d6_prace.csv", encoding="utf-8-sig").set_index("grupa")
    bp = bp.reindex(gp.index)
    y0_bez = pd.Series(wykryj(bp[YC].to_numpy(float), mianownik("terms_w2000_primary"), **DOM),
                       index=gp.index)
    przed = [(bp.loc[g, YC] - gp.loc[g, YC]).to_numpy()[:YEARS.index(y0_dom[g])].sum()
             if y0_dom[g] else 0 for g in gp.index]
    z4 = pd.DataFrame({"grupa": gp.index, "y0": y0_dom.values, "y0_bez_d6": y0_bez.values,
                       "dy0": (y0_dom - y0_bez).where((y0_dom > 0) & (y0_bez > 0)).values,
                       "prac_d6_lacznie": (bp[YC].sum(axis=1) - gp[YC].sum(axis=1)).values,
                       "prac_d6_przed_y0": przed})
    z4.to_csv(R / "d6_vs_y0.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    print("\nZ4: dy0 = y0 (z D6) - y0 (bez D6)")
    print(z4.dy0.value_counts().sort_index().to_string())
    print(z4[z4.dy0.abs() >= 1].to_string(index=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
