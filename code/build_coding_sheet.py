"""build_coding_sheet.py — arkusz do recznego kodowania kategorii (plan §8).

Co robi maszyna, a czego NIE robi. Maszyna dostarcza materialu do osadu: szereg czasowy,
przykladowe tytuly z okolic roku wylonienia i z konca okresu oraz KANDYDATOW NA POPRZEDNIKA.
Kategorie z §8 przypisuje czlowiek — skrypt nie proponuje zadnej.

Kandydat na poprzednika. §8: "terminu, ktorego udzial opada w tym samym okresie i ktory
WSPOLWYSTEPUJE z kandydatem w pracach z lat przejsciowych". Sam spadek nie wystarcza —
najsilniej opadaja slowa ogolne ("degree", "because", "problem"), ktore wspolwystepuja
ze wszystkim. Dlatego rankujemy po LIFT:

    lift = P(poprzednik | termin, okno przejsciowe) / P(poprzednik | okno przejsciowe)

Slowo ogolne ma lift ~1 niezaleznie od czestosci. Prawdziwy poprzednik wspolwystepuje
nieproporcjonalnie czesto, wiec lift jest wysoki. Okno przejsciowe: y0-2 .. y0+2.

Uruchom:
    python code/build_coding_sheet.py --text D:/medline_2026/parsed/field_text.parquet \
        --canon data/canon --emerging D:/medline_2026/parsed/emerging_primary.parquet \
        --core data/processed/emerging_core.json --out data/processed/coding_sheet.csv
"""
from __future__ import annotations
import argparse, json, sys, time
from collections import defaultdict
from pathlib import Path

try:
    import numpy as np
    import pandas as pd
except ImportError:
    sys.exit("pip install pandas pyarrow")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize import load_lists, make_canonicalizer  # noqa: E402

YEAR_MIN, YEAR_MAX = 2005, 2025
WINDOW = 2            # okno przejsciowe: y0-2 .. y0+2
N_TITLES = 3
TOP_PRED = 5
# Progi kandydata na poprzednika. UWAGA na MIN_CO: prawdziwa para przemianowania jest
# z natury RZADKA w liczbach bezwzglednych — stary termin umiera, nowy sie rodzi, wiec okno
# nakladania jest cienkie. Zmierzone: "rapid prototyping" przy "3d printing" ma lift 52,1
# (najwyzszy sygnal w zbiorze) przy zaledwie 5 wspolwystapieniach. Prog MIN_CO=10 wycinal
# wiec najlepszy przyklad demonstracyjny z planu. Tlumienie szumu nalezy do MIN_LIFT,
# nie do licznosci.
MIN_LIFT = 3.0
MIN_CO = 4


def ngrams(toks: list[str]):
    seen = set()
    for i, t in enumerate(toks):
        seen.add(t)
        if i + 1 < len(toks):
            seen.add(t + " " + toks[i + 1])
        if i + 2 < len(toks):
            seen.add(t + " " + toks[i + 1] + " " + toks[i + 2])
    return seen


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--canon", required=True)
    ap.add_argument("--emerging", required=True)
    ap.add_argument("--core", required=True)
    ap.add_argument("--denom", required=True, help="plik .denom.json zapisany przez canonicalize.py")
    ap.add_argument("--out", required=True)
    ap.add_argument("--min-lift", type=float, default=MIN_LIFT)
    ap.add_argument("--min-co", type=int, default=MIN_CO)
    args = ap.parse_args()

    t0 = time.time()
    spell, irr, phr = load_lists(Path(args.canon))
    canon = make_canonicalizer(spell, irr, phr)

    em = pd.read_parquet(args.emerging)
    core = set(json.loads(Path(args.core).read_text(encoding="utf-8")))
    tgt = em[em["term"].isin(core)].copy().reset_index(drop=True)
    if len(tgt) != len(core):
        print(f"UWAGA: {len(core)} w core, {len(tgt)} znalezionych w tabeli", file=sys.stderr)

    years = list(range(YEAR_MIN, YEAR_MAX + 1))
    ycols = [f"y{y}" for y in years]
    cnt = em[ycols].to_numpy(float)
    den = json.loads(Path(args.denom).read_text(encoding="utf-8"))
    den_by_year = {y: den["by_year"][str(y)] for y in years}
    dv = np.array([den["by_year"][str(y)] for y in years], float)
    sh = cnt / dv
    em = em.assign(early=sh[:, :5].mean(axis=1), late=sh[:, -5:].mean(axis=1))
    dec = em[(em.docs_total >= 200) & (em.early > 0.0005) & (em.early >= 2 * em.late)]
    dec_terms = list(dec["term"])
    print(f"celow: {len(tgt)}, kandydatow na poprzednika: {len(dec_terms)}", file=sys.stderr)

    terms = list(tgt["term"])
    tgt_id = {t: i for i, t in enumerate(terms)}
    dec_id = {t: i for i, t in enumerate(dec_terms)}
    y0 = tgt["y0"].to_numpy(int)

    df = pd.read_parquet(args.text, columns=["year", "title", "abstract"])
    df = df[(df["year"] >= YEAR_MIN) & (df["year"] <= YEAR_MAX)]

    co = np.zeros((len(tgt), len(dec_terms)), dtype=np.int32)
    dec_by_year = np.zeros((len(dec_terms), len(years)), dtype=np.int32)
    rec_by_year = np.zeros(len(years), dtype=np.int64)
    titles_early: dict[int, list] = defaultdict(list)
    titles_late: dict[int, list] = defaultdict(list)

    for n, (yr, title, abstract) in enumerate(
            zip(df["year"].values, df["title"].values, df["abstract"].values)):
        yi = int(yr) - YEAR_MIN
        rec_by_year[yi] += 1
        present = ngrams(canon(f"{title} {abstract}"))
        ds = np.fromiter((dec_id[t] for t in present if t in dec_id), dtype=np.int32)
        if len(ds):
            dec_by_year[ds, yi] += 1
        for t in present:
            i = tgt_id.get(t)
            if i is None:
                continue
            if abs(int(yr) - y0[i]) <= WINDOW and len(ds):
                co[i, ds] += 1
            if len(titles_early[i]) < N_TITLES and abs(int(yr) - y0[i]) <= 1 and title:
                titles_early[i].append(f"[{int(yr)}] {title}")
            elif len(titles_late[i]) < N_TITLES and int(yr) >= 2023 and title:
                titles_late[i].append(f"[{int(yr)}] {title}")
        if (n + 1) % 50000 == 0:
            print(f"  {n+1}/{len(df)} ({(time.time()-t0)/60:.1f} min)", file=sys.stderr)

    # --- przebieg 2: tytuly POPRZEDNIKA i tytuly WSPOLNE.
    # Test podstawienia z kodeksu §2 wymaga materialu z okresu nakladania po OBU stronach:
    # bez tytulow zawierajacych poprzednika koder moze test tylko wyobrazic sobie, nie wykonac.
    best_pred: dict[int, str] = {}
    for i in range(len(tgt)):
        lo = max(YEAR_MIN, y0[i] - WINDOW) - YEAR_MIN
        hi = min(YEAR_MAX, y0[i] + WINDOW) - YEAR_MIN
        n_win = int(rec_by_year[lo:hi + 1].sum())
        base = dec_by_year[:, lo:hi + 1].sum(axis=1) / max(n_win, 1)
        n_t = max(int(co[i].max()), 1)
        with np.errstate(divide="ignore", invalid="ignore"):
            lift = np.where(base > 0, (co[i] / n_t) / base, 0.0)
        ok = (co[i] >= args.min_co) & (lift >= args.min_lift)
        if ok.any():
            best_pred[i] = dec_terms[int(np.argmax(lift * ok))]

    titles_pred: dict[int, list] = defaultdict(list)
    titles_both: dict[int, list] = defaultdict(list)
    want = {}
    for i, pterm in best_pred.items():
        want.setdefault(pterm, []).append(i)
    print(f"przebieg 2: tytuly poprzednika dla {len(best_pred)} terminow", file=sys.stderr)
    for yr, title, abstract in zip(df["year"].values, df["title"].values, df["abstract"].values):
        if not title:
            continue
        present = ngrams(canon(f"{title} {abstract}"))
        for pterm, idxs in want.items():
            if pterm not in present:
                continue
            for i in idxs:
                if abs(int(yr) - y0[i]) > WINDOW:
                    continue
                if terms[i] in present and len(titles_both[i]) < N_TITLES:
                    titles_both[i].append(f"[{int(yr)}] {title}")
                elif len(titles_pred[i]) < N_TITLES:
                    titles_pred[i].append(f"[{int(yr)}] {title}")

    rows = []
    for i, r in tgt.iterrows():
        lo, hi = max(YEAR_MIN, y0[i] - WINDOW) - YEAR_MIN, min(YEAR_MAX, y0[i] + WINDOW) - YEAR_MIN
        n_win = int(rec_by_year[lo:hi + 1].sum())
        n_tgt = int(cnt[em.index[em.term == r["term"]][0], lo:hi + 1].sum())
        base = dec_by_year[:, lo:hi + 1].sum(axis=1) / max(n_win, 1)
        obs = co[i] / max(n_tgt, 1)
        with np.errstate(divide="ignore", invalid="ignore"):
            lift = np.where(base > 0, obs / base, 0.0)
        ok = (co[i] >= args.min_co) & (lift >= args.min_lift)
        idx = np.argsort(-lift * ok)[:TOP_PRED]
        preds = "; ".join(f"{dec_terms[j]} (lift {lift[j]:.1f}, wsp. {co[i, j]})"
                          for j in idx if ok[j])
        rows.append({
            "term": r["term"], "n": r["n"], "y0": int(r["y0"]),
            # Roczny udzial w polu — arkusz musi byc SAMOWYSTARCZALNY, bo to jego zamrazamy
            # i haszujemy do rejestracji. Bez ksztaltu krzywej koder nie rozpozna ani artefaktu
            # pomiaru, ani okna nakladania z poprzednikiem.
            **{f"udzial_{y}": round(100 * r[f"y{y}"] / den_by_year[y], 3)
               for y in range(YEAR_MIN, YEAR_MAX + 1)},
            "peak_year": int(r["peak_year"]), "peak_share_pct": round(100 * r["peak_share"], 3),
            "prevalence_2021_2025_pct": round(100 * r["prevalence_2021_2025"], 3),
            "docs_total": int(r["docs_total"]),
            "kandydaci_na_poprzednika": preds,
            "tytuly_okolo_y0": " | ".join(titles_early.get(i, []))[:600],
            "tytuly_2023_2025": " | ".join(titles_late.get(i, []))[:600],
            "poprzednik_glowny": best_pred.get(i, ""),
            "tytuly_poprzednika": " | ".join(titles_pred.get(i, []))[:600],
            "tytuly_WSPOLNE": " | ".join(titles_both.get(i, []))[:600],
            "kategoria": "", "poprzednik": "", "uwagi": "",
        })

    out = pd.DataFrame(rows).sort_values("prevalence_2021_2025_pct", ascending=False)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False, encoding="utf-8-sig")
    n_pred = int((out["kandydaci_na_poprzednika"] != "").sum())
    print(f"\nzapisano {args.out}: {len(out)} terminow", file=sys.stderr)
    print(f"  z kandydatem na poprzednika: {n_pred} ({100*n_pred/len(out):.0f}%)", file=sys.stderr)
    print(f"  czas {(time.time()-t0)/60:.1f} min", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
