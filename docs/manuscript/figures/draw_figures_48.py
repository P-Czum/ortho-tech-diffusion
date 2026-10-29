"""Figures 0–6 for the ortho-tech-diffusion manuscript, material 48.
Data: data/processed/{osie_48, kraj_pochodzenia_48, szeregi_48, szeregi_czlonow,
trwalosc_wzgledna_48, material_48}.csv — VS Code outputs of 2026-10-28.
Palette: one hue #3d6b8f for data, light tint for context, ink greys for text.
Kind encoded by marker shape; every figure readable in greyscale.
"""
import csv, math, sys, collections
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

SRC = sys.argv[1]; OUT = sys.argv[2]
HUE = "#3d6b8f"; TINT = "#c5d5e2"; INK = "#222222"; INK2 = "#555555"; INK3 = "#8a8a8a"; GRID = "#e4e4e4"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": INK3, "axes.linewidth": 0.6,
    "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2, "xtick.labelsize": 8, "ytick.labelsize": 8,
    "axes.titlesize": 9.5, "axes.titleweight": "bold", "axes.titlelocation": "left", "axes.titlecolor": INK,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False, "legend.fontsize": 8,
    "svg.fonttype": "none", "figure.dpi": 100,
})
YEARS = list(range(2000, 2026))
def rd(name): return list(csv.DictReader(open(f"{SRC}/{name}", encoding="utf-8-sig")))
osie = rd("osie_48.csv"); kraj = rd("kraj_pochodzenia_48.csv"); szer = rd("szeregi_48.csv")
czl = rd("szeregi_czlonow.csv"); trw = rd("trwalosc_wzgledna_48.csv"); mat = rd("material_48.csv")
klasa = {r["grupa"]: r["klasa"] for r in mat}
series = {r["grupa"]: np.array([float(r[f"y{y}"]) for y in YEARS]) for r in szer}

KIND_ORDER = ["I", "II", "III", "IV", "V", "VI"]
KIND_NAME = {"I": "Implant or material", "II": "Joint arthroplasty", "III": "Operative technique",
             "IV": "Assistive tool", "V": "Perioperative care", "VI": "Biological therapy"}
KIND_MARK = {"I": "s", "II": "D", "III": "o", "IV": "^", "V": "v", "VI": "P"}
def kind(g): return klasa[g].split(".")[0]
PRETTY = {"mom total hip arthroplasty": "metal-on-metal THA", "artificial intelligence / machine learning": "artificial intelligence",
          "percutaneous endoscopic lumbar discectomy": "endoscopic lumbar discectomy", "transforaminal lumbar interbody fusion": "TLIF",
          "medial patellofemoral ligament reconstruction": "MPFL reconstruction", "anterolateral ligament reconstruction": "ALL reconstruction",
          "minimally invasive plate osteosynthesis": "MIPO", "proximal femoral nail antirotation": "PFNA",
          "oblique lumbar interbody fusion": "OLIF", "lateral lumbar interbody fusion": "LLIF", "unicompartmental knee arthroplasty": "unicompartmental knee",
          "autologous chondrocyte implantation": "chondrocyte implantation", "open wedge high tibial osteotomy": "open-wedge HTO",
          "patient specific instrumentation": "patient-specific instrumentation", "mesenchymal stem cell": "mesenchymal stem cells",
          "double bundle reconstruction": "double-bundle ACL", "pedicle subtraction osteotomy": "pedicle subtraction osteotomy"}
def pretty(g): return PRETTY.get(g, g)
def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(f"{OUT}/{name}.svg", bbox_inches="tight", facecolor="white"); plt.close(fig); print("saved", name)
def fnum(x):
    try: return float(x)
    except: return float("nan")

# ------------------------------------------------------------------ Figure 0: anatomy
def fig0():
    g = "hip resurfacing"; s = series[g]; o = next(r for r in osie if r["grupa"] == g)
    y0 = int(o["y0"]); peak = int(o["rok_szczytu"]); thr = float(o["prog_pct"]); pk = s.max(); dt = float(o["czas_podwojenia_lat"])
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.plot(YEARS, s, color=HUE, lw=2, zorder=3); ax.scatter(YEARS, s, s=14, color=HUE, zorder=4)
    ax.axhline(thr, color=INK3, lw=0.8, ls=(0, (4, 3))); ax.text(2006.5, thr - 0.012, f"threshold = max(5 × baseline, 0.1 %) = {thr:.1f} %, and ≥ 5 papers", color=INK2, fontsize=7.5, va="top")
    ax.axvspan(2000, 2002.99, color=TINT, alpha=0.45, lw=0); ax.text(2001.5, pk * 0.98, "baseline\n2000–02", ha="center", va="top", color=INK2, fontsize=7.5)
    ax.annotate(f"emergence y₀ = {y0}\n(threshold held 3 years)", xy=(y0, s[y0 - 2000]), xytext=(y0 + 0.4, pk * 0.52), ha="left", color=INK, fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color=INK3, lw=0.7))
    ax.annotate(f"peak {peak}: {pk:.2f} %", xy=(peak, pk), xytext=(peak - 0.6, pk * 1.06), ha="right", va="bottom", color=INK, fontsize=7.5, arrowprops=dict(arrowstyle="-", color=INK3, lw=0.7))
    xs = np.arange(y0, peak + 1); ys = np.log(s[xs - 2000]); sl, ic = np.polyfit(xs, ys, 1)
    xf = np.linspace(y0 - 0.5, peak, 60); yf = np.exp(ic + sl * xf); keep = yf <= pk * 1.0
    ax.plot(xf[keep], yf[keep], color=INK3, lw=1, ls=":", zorder=2)
    ax.text(y0 + 3.3, np.exp(ic + sl * (y0 + 3.3)) * 0.78, f"doubling time {dt:.1f} y\n(log-linear fit, y₀ → peak)", color=INK2, fontsize=7.5, ha="left", va="top")
    for lo, hi, lab, lvl in [(1, 3, "+1–3 y", 1.10), (3, 5, "+3–5 y", 1.24), (5, 7, "+5–7 y", 1.10)]:
        a, b = peak + lo, min(peak + hi, 2025); win = s[(a - 2000):(b - 2000 + 1)].mean() / pk
        ax.plot([a, b], [pk * lvl] * 2, color=INK2, lw=0.8); ax.plot([a, a], [pk * (lvl - 0.02), pk * (lvl + 0.02)], color=INK2, lw=0.8); ax.plot([b, b], [pk * (lvl - 0.02), pk * (lvl + 0.02)], color=INK2, lw=0.8)
        ax.text((a + b) / 2, pk * (lvl + 0.025), f"{lab}\n{win:.2f} of peak", ha="center", va="bottom", color=INK2, fontsize=7)
    ax.text(2025.15, s[-1], f" 2025: {s[-1] / pk:.2f} of peak\n → decline (< 0.5)", va="center", color=INK, fontsize=7.5)
    ax.set_xlim(2000, 2025.5); ax.set_ylim(0, pk * 1.42); ax.set_xticks(range(2000, 2026, 5)); ax.set_ylabel("share of field records, %")
    ax.set_title("Figure 0. Anatomy of an attention curve — hip resurfacing"); ax.grid(axis="y", color=GRID, lw=0.5); ax.set_axisbelow(True)
    fig.text(0.01, -0.03, "Share = field records containing the phrase ÷ all field records that year. Persistence windows are anchored to the technology's own peak. Landmarks as defined in Box 1.", color=INK3, fontsize=7)
    save(fig, "fig_anatomy")

# ------------------------------------------------------------------ Figure 1: timeline
def fig1():
    rows = sorted(osie, key=lambda r: (KIND_ORDER.index(kind(r["grupa"])), int(r["y0"]), r["grupa"]))
    fig, ax = plt.subplots(figsize=(7.2, 10.2)); y = 0; ticks = []; labels = []; last = None
    for r in rows:
        k = kind(r["grupa"])
        if k != last:
            if last is not None: y += 1.0
            n = sum(1 for q in rows if kind(q["grupa"]) == k)
            ax.text(2004.0, y - 0.15, f"{KIND_NAME[k]} ({n})", ha="left", va="bottom", color=INK, fontsize=8, fontweight="bold")
            ax.axhline(y - 0.5, color=GRID, lw=0.6); y += 0.55
        last = k; y0 = int(r["y0"]); pk = int(r["rok_szczytu"]); growing = pk == 2025
        ax.plot([y0, pk], [y, y], color=HUE, lw=2.2, solid_capstyle="butt", alpha=0.5 if growing else 0.9, zorder=2, ls=(0, (2, 1.5)) if pk < y0 else "-")
        ax.scatter([y0], [y], marker=KIND_MARK[k], s=34, color=HUE, zorder=4, edgecolor="white", lw=0.5)
        if growing: ax.annotate("", xy=(2026.3, y), xytext=(2025, y), arrowprops=dict(arrowstyle="-|>", color=HUE, lw=1.4, alpha=0.5, mutation_scale=7))
        else: ax.scatter([pk], [y], marker="|", s=50, color=HUE, zorder=4)
        ticks.append(y); labels.append(pretty(r["grupa"])); y += 1
    ax.set_yticks(ticks); ax.set_yticklabels(labels, fontsize=7.4); ax.set_ylim(y - 0.3, -1.2); ax.set_xlim(2003.5, 2026.8); ax.set_xticks(range(2005, 2026, 5))
    ax.grid(axis="x", color=GRID, lw=0.5); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0); ax.spines["left"].set_visible(False)
    h = [Line2D([], [], marker=KIND_MARK[k], color=HUE, ls="", ms=5, label=KIND_NAME[k]) for k in KIND_ORDER]
    h += [Line2D([], [], color=HUE, lw=2.2, alpha=0.9, label="emergence → peak year"), Line2D([], [], color=HUE, lw=2.2, alpha=0.5, label="still growing (peak = 2025)")]
    h.append(Line2D([], [], color=HUE, lw=2.2, ls=(0, (2, 1.5)), label="peak before emergence (short spike)"))
    ax.legend(handles=h, loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=3, fontsize=7, handlelength=1.8, columnspacing=1.2)
    ax.set_title("Figure 1. What emerged, and when — 48 technologies, 2005–2023"); ax.set_xlabel("year")
    save(fig, "fig_timeline")

# ------------------------------------------------------------------ Figure 2: origin vs lead
def fig2():
    lead = collections.Counter(r["lider"] for r in kraj)
    started = collections.Counter(r["wczesne_top"] for r in kraj if r["wczesne_top"] == r["przed_y0_top"])
    same = [r for r in kraj if r["lider"] == r["wczesne_top"] == r["przed_y0_top"]]
    flow = [r for r in kraj if r["lider"] != r["wczesne_top"] and r["lider"] != r["przed_y0_top"]]
    unc = len(kraj) - len(same) - len(flow); strict = [r for r in flow if r["wczesne_top"] == r["przed_y0_top"]]
    toC = sum(1 for r in flow if r["lider"] == "China"); toC_s = sum(1 for r in strict if r["lider"] == "China")
    countries = ["USA", "China", "South Korea", "Germany", "France", "Japan"]
    fig, ax = plt.subplots(figsize=(6.4, 3.4)); x = np.arange(len(countries)); w = 0.36
    b1 = ax.bar(x - w / 2, [started[c] for c in countries], w, color=TINT, edgecolor=HUE, lw=0.8, label="started (country of earliest papers, both measures agree)")
    b2 = ax.bar(x + w / 2, [lead[c] for c in countries], w, color=HUE, label="leads (most papers from emergence onward)")
    for b in list(b1) + list(b2):
        if b.get_height() > 0: ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.4, f"{int(b.get_height())}", ha="center", va="bottom", color=INK, fontsize=7.5)
    ax.set_xticks(x); ax.set_xticklabels(["United States", "China", "South Korea", "Germany", "France", "Japan"]); ax.set_ylabel("technologies"); ax.set_ylim(0, 36)
    ax.grid(axis="y", color=GRID, lw=0.5); ax.set_axisbelow(True); ax.legend(loc="upper right", fontsize=7)
    ax.set_title("Figure 2. Who started a technology, and who leads its literature")
    ax.text(0.99, 0.52, f"{len(same)} technologies led by the country that started them ({sum(1 for r in same if r['lider']=='USA')} American)\n"
            f"{len(flow)} led by another country; {toC} of {len(flow)} of these flows end in China\n"
            f"({toC_s} of {len(strict)} when both measures must agree on the source); {unc} unclassified",
            transform=ax.transAxes, ha="right", va="center", color=INK2, fontsize=7)
    fig.text(0.01, -0.04, "Twelve technologies whose two origin measures disagree have no 'started' bar.", color=INK3, fontsize=7)
    save(fig, "fig_origin_lead")

# ------------------------------------------------------------------ Figure 3: concentration vs size
def fig3():
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    for r in osie:
        k = kind(r["grupa"]); n = int(r["prac_od_y0"]); e = float(r["kraj_eff_n"])
        ax.scatter(n, e, marker=KIND_MARK[k], s=36, color=HUE, alpha=0.85, edgecolor="white", lw=0.5, zorder=3)
    ax.axhline(2.5, color=INK3, lw=0.8, ls=(0, (4, 3))); ax.text(63, 2.6, "effective countries ≤ 2.5", color=INK2, fontsize=7, va="bottom", ha="left")
    single = sorted([r for r in osie if float(r["kraj_eff_n"]) <= 2.5], key=lambda r: int(r["prac_od_y0"]))
    offs = {"targeted muscle reinnervation": (-7, -7), "labral repair": (0, -11), "oblique lumbar interbody fusion": (-2, 9), "percutaneous endoscopic lumbar discectomy": (0, -11),
            "proximal femoral nail antirotation": (-9, 4), "femoral neck system": (9, 4), "hip arthroscopy": (0, -11)}
    key = []
    for i, r in enumerate(single, 1):
        n = int(r["prac_od_y0"]); e = float(r["kraj_eff_n"]); dx, dy = offs.get(r["grupa"], (8, 0))
        ax.annotate(str(i), xy=(n, e), xytext=(dx, dy), textcoords="offset points", fontsize=7, color=INK, ha="center", va="center", fontweight="bold")
        key.append(f"{i}  {pretty(r['grupa'])} — {r['kraj_top']} {float(r['kraj_top_pct']):.0f} %")
    ax.text(0.985, 0.985, "Single-country literatures (≤ 2.5)\n" + "\n".join(key), transform=ax.transAxes, ha="right", va="top", fontsize=6.8, color=INK2, linespacing=1.35)
    for g, dx, dy, ha in [("volar locking plate", 10, 0, "left"), ("mesenchymal stem cell", 10, 0, "left"), ("reverse shoulder arthroplasty", 9, 0, "left")]:
        r = next(q for q in osie if q["grupa"] == g); n = int(r["prac_od_y0"]); e = float(r["kraj_eff_n"])
        ax.annotate(f"{pretty(g)}\n({r['kraj_top']} {float(r['kraj_top_pct']):.0f} %, {e:.1f} countries)", xy=(n, e), xytext=(dx, dy), textcoords="offset points", fontsize=6.6, color=INK2, ha=ha, va="center")
    ax.set_xscale("log"); ax.set_xlabel("papers from emergence onward (log scale)"); ax.set_ylabel("effective number of countries (1 ÷ Σ p²)")
    ax.set_xlim(60, 30000); ax.set_ylim(0, 14.5); ax.set_xticks([100, 300, 1000, 3000, 10000]); ax.set_xticklabels(["100", "300", "1 000", "3 000", "10 000"]); ax.grid(color=GRID, lw=0.5); ax.set_axisbelow(True)
    h = [Line2D([], [], marker=KIND_MARK[k], color=HUE, ls="", ms=5, label=KIND_NAME[k]) for k in KIND_ORDER]
    ax.legend(handles=h, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=3, fontsize=7)
    ax.set_title("Figure 3. Concentration is not paper count"); save(fig, "fig_concentration")

# ------------------------------------------------------------------ Figure 4: six kinds
def fig4():
    from matplotlib.ticker import NullFormatter, FixedLocator
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.8), sharey=True)
    for ax, col, lab, lim in [(axes[0], "czas_podwojenia_lat", "doubling time, years (log scale)", (1.5, 90)), (axes[1], "kraj_eff_n", "effective number of countries", (0, 14))]:
        for i, k in enumerate(KIND_ORDER):
            yi = 5 - i
            vals = [fnum(r[col]) for r in osie if kind(r["grupa"]) == k]; vals = [v for v in vals if not math.isnan(v)]
            jit = np.linspace(-0.2, 0.2, len(vals)) if len(vals) > 1 else [0]
            ax.scatter(vals, [yi + j for j in jit], marker=KIND_MARK[k], s=30, color=HUE, alpha=0.7, edgecolor="white", lw=0.5, zorder=3)
            med = float(np.median(vals)); ax.plot([med, med], [yi - 0.36, yi + 0.36], color=INK, lw=1.8, zorder=4)
            ax.annotate(f"{med:.1f}", xy=(med, yi + 0.36), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", color=INK, fontsize=7, fontweight="bold")
        ax.set_yticks(range(6)); ax.set_yticklabels([f"{KIND_NAME[k]} ({sum(1 for r in osie if kind(r['grupa'])==k)})" for k in reversed(KIND_ORDER)])
        ax.set_ylim(-0.7, 5.9); ax.set_xlabel(lab); ax.set_xlim(*lim); ax.grid(axis="x", color=GRID, lw=0.5); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
        if "log" in lab:
            ax.set_xscale("log"); ax.xaxis.set_major_locator(FixedLocator([2, 5, 10, 20, 50])); ax.set_xticklabels(["2", "5", "10", "20", "50"]); ax.xaxis.set_minor_formatter(NullFormatter()); ax.tick_params(axis="x", which="minor", length=0)
    axes[0].text(0.0, 1.03, "Figure 4. Six kinds diffuse differently — dots are technologies, bars are medians", transform=axes[0].transAxes, fontsize=9.5, fontweight="bold", color=INK, va="bottom")
    fig.text(0.01, -0.04, "Doubling time undefined for 9 technologies (peak < 2 years after emergence, or fitted slope not positive); they appear only in the right panel.", color=INK3, fontsize=7)
    save(fig, "fig_kinds")

# ------------------------------------------------------------------ Figure 5: declines
def fig5():
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    dark = {"mom total hip arthroplasty", "hip resurfacing"}; ends = []
    for r in trw:
        g = r["grupa"]; pk = int(r["szczyt"]); s = series[g]; pkv = s.max()
        xs = [y - pk for y in YEARS if -3 <= y - pk <= 7]; ys = [s[y - 2000] / pkv for y in YEARS if -3 <= y - pk <= 7]
        isd = g in dark
        ax.plot(xs, ys, color=HUE if isd else TINT, lw=2.2 if isd else 1.4, zorder=4 if isd else 2, marker="o" if isd else None, ms=3.5)
        ends.append([xs[-1], ys[-1], f"{pretty(g)} ({pk})", isd])
    # repel labels vertically
    ends.sort(key=lambda e: e[1]); gap = 0.05
    for i in range(1, len(ends)):
        if ends[i][1] - ends[i - 1][1] < gap: ends[i][1] = ends[i - 1][1] + gap
    for x, y, t, isd in ends:
        ax.text(7.25, y, t, fontsize=6.8, color=INK if isd else INK2, va="center", fontweight="bold" if isd else "normal")
    ax.axhline(0.5, color=INK3, lw=0.8, ls=(0, (4, 3))); ax.text(7.1, 0.49, "half of peak", color=INK2, fontsize=7, va="top", ha="right")
    ax.axvline(0, color=INK3, lw=0.6); ax.set_xlim(-3, 10.2); ax.set_ylim(0, 1.05); ax.set_xticks(range(-3, 8))
    ax.set_xlabel("years after the technology's own peak"); ax.set_ylabel("share ÷ peak share"); ax.grid(axis="y", color=GRID, lw=0.5); ax.set_axisbelow(True)
    h = [Line2D([], [], color=HUE, lw=2.2, marker="o", ms=3.5, label="evidence turned against use"), Line2D([], [], color=TINT, lw=1.4, label="other declines")]
    ax.legend(handles=h, loc="lower left", fontsize=7)
    ax.set_title("Figure 5. Ten declines, relative to each technology's own peak")
    fig.text(0.01, -0.04, "Curves end at 2025; dual-mobility cup (peak 2020) has five post-peak years, so its +5–7 window is censored.", color=INK3, fontsize=7)
    save(fig, "fig_declines")

# ------------------------------------------------------------------ Figure 6: names
def fig6():
    fig, axes = plt.subplots(1, 3, figsize=(8.0, 3.4))
    def ser(panel, czlon): return np.array([float(r[f"y{y}"]) for r in czl if r["panel"] == panel and r["czlon"] == czlon for y in YEARS])
    ax = axes[0]; p = "retronim: single vs double bundle"
    ax.plot(YEARS, ser(p, "double bundle reconstruction"), color=HUE, lw=2, label="double-bundle reconstruction (the rival)")
    ax.plot(YEARS, ser(p, "single bundle"), color=INK2, lw=1.3, ls=(0, (4, 2)), label="'single bundle' (new name for the standard)")
    ax.set_title("(a) A rival creates a name")
    ax = axes[1]; p = "retronim: mechanical vs kinematic alignment"
    ax.plot(YEARS, ser(p, "kinematic alignment"), color=HUE, lw=2, label="kinematic alignment (the rival)")
    ax.plot(YEARS, ser(p, "mechanical alignment"), color=INK2, lw=1.3, ls=(0, (4, 2)), label="'mechanical alignment' (new name for the standard)")
    ax.set_title("(b) …and again")
    ax = axes[2]; p = "scalenie: kyphoplasty"; members = [r["czlon"] for r in czl if r["panel"] == p]
    styles = ["-", (0, (4, 2)), (0, (1, 1.5)), (0, (5, 1, 1, 1))]
    for i, m in enumerate(members):
        ax.plot(YEARS, ser(p, m), color=INK2, lw=1.1, ls=styles[i], alpha=0.8, label=m)
    ax.plot(YEARS, series["kyphoplasty"], color=HUE, lw=2.2, label="all four together (the group counted)"); ax.set_title("(c) Four names, one technology")
    for ax in axes:
        ax.set_xlim(2000, 2025); ax.set_xticks([2000, 2010, 2020]); ax.grid(axis="y", color=GRID, lw=0.5); ax.set_axisbelow(True)
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=6.4, handlelength=2.2)
    axes[0].set_ylabel("share of field records, %")
    fig.text(0.0, 1.0, "Figure 6. A name is not a technology", fontsize=9.5, fontweight="bold", color=INK, va="bottom")
    fig.tight_layout(w_pad=1.5); save(fig, "fig_names")

for f in (fig0, fig1, fig2, fig3, fig4, fig5, fig6): f()
