# Box 1 — Definitions of the curve landmarks, and the figure plan
### 2026-10-28 · written so that the scheme transfers to any clinical field; nothing below names orthopaedics

---

## Box 1. Landmarks of an attention curve (field-agnostic)

Let a **field** be a set of records defined before analysis (here: a MeSH subtree, filtered for contaminating literatures by measured rules). Let a **unit** be a noun phrase or a merged group of phrases naming one technology. For each unit and year *t*, the **share** *s(t)* is the number of field records containing the unit divided by the number of field records that year. All landmarks are defined on *s(t)*, not on raw counts, so that growth of the field and of the database cancel.

| Landmark | Definition | Parameters (this study) |
|---|---|---|
| **Baseline** | Mean share over the first *b* years of the window | *b* = 3 (2000–2002) |
| **Threshold** | max(*k* × baseline, *θ*), with *θ* an absolute floor; in addition at least 5 papers in the year | *k* = 5; *θ* = 0.1 %; ≥ 5 papers per year |
| **Emergence, y₀** | First year in which both threshold conditions hold and continue to hold for *m* consecutive years | *m* = 3; hence y₀ ≤ window end − (*m* − 1) = 2023 |
| **Peak** | max *s(t)* over the window, and the year it occurs | — |
| **Doubling time** | ln 2 ÷ slope of log *s(t)* fitted from y₀ to the peak year; undefined if the peak is < 2 years after y₀ or the fitted slope is not positive | — |
| **Persistence** | *s* in a window after the unit's own peak ÷ peak share; windows anchored to each unit's peak, not to calendar years | windows +1–3, +3–5, +5–7 years |
| **Decline** | Share in the last year of the window ÷ peak share < *d* (not the post-peak windows, which are descriptive) | *d* = 0.5; last year 2025 |
| **Still growing** | Peak year = last year of window | — |
| **Leading country** | Country with most papers from y₀ onward, first-author affiliation | — |
| **Effective number of countries** | 1 ÷ Σ *pᵢ*², *pᵢ* = share of country *i* | — |
| **Over-representation** | Country's share of the unit's papers ÷ its share of all field papers, same years (y₀ to window end) | — |
| **Country of origin** | Most frequent country among the *n* earliest papers with a known first-author country (measure 1) and among all such papers before y₀ (measure 2) | *n* = 10 |
| **Same-country / flow** | *Same-country* if the leading country is most frequent under both origin measures; *flow* if under neither; else unclassified. Source of a flow named only where both measures agree | — |
| **Retronym** | A unit that emerges for an existing standard after a rival unit becomes present (≥ 5 papers) | identified by specialist review |

**What transfers and what must be re-done.** The landmarks, parameters, and detector transfer unchanged. Three things do not and must be repeated for each field: (1) the field's contaminating literatures — found by audit of each MeSH descriptor's sole-entry records, not by a fixed list; (2) the specialist screen that separates technologies from methods, scales, diagnoses, and retronyms; (3) the synonym and abbreviation dictionary. The first two are the method's cost; without them the detector reports names, not technologies.

**Parameters to report with any reuse.** *b*, *k*, *θ*, *m*, *d*, window, *n*, the contamination rules with their measured separation, and the count of units removed at specialist screen by reason.

---

## Figure plan — six figures, each showing landmarks from Box 1

| # | Title | Form | Shows | Data | Status |
|---|---|---|---|---|---|
| **0** | Anatomy of an attention curve | one real series, annotated | every landmark in Box 1 on **hip resurfacing** (y₀ 2005, doubling 2.4 y, peak 2011, all three windows complete, decline). Metal-on-metal THA was the first choice but has no defined doubling time (fitted slope not positive), so it could not show that landmark | `szeregi_48.csv` | **done** (`fig_anatomy`) |
| **1** | What emerged, and when | timeline: one row per technology, dot at y₀, bar to peak year, open end if still growing; rows grouped by kind | y₀, peak year, growing, kind; dashed bar where peak < y₀ (MSC, HXLPE), footnote with microfracture | `osie_48.csv` + `material_48.csv` (kind) | **done** (`fig_timeline`, 2026-10-29 audit) |
| **2** | Who started and who leads | paired bars per country: started vs leads | origin, lead, flows | `kraj_pochodzenia_48.csv` | **done** (`fig_origin_lead`) |
| **3** | Concentration is not paper count | scatter: effective countries (y) vs papers since y₀ (x, log); labelled extremes; kind by marker | effective countries, papers, kind | `osie_48.csv` | **done** (`fig_concentration`) |
| **4** | Six kinds diffuse differently | small multiples: doubling time and effective countries by kind, dots + median bar | doubling, effective countries, kind | `osie_48.csv` | **done** (`fig_kinds`) |
| **5** | Ten declines, relative to own peak | 10 lines, x = years after own peak (−3…+7), y = share ÷ peak; rejected pair in dark, others light; 0.5 line | persistence | `szeregi_48.csv`, `trwalosc_wzgledna_48.csv` (window status) | **done** (`fig_declines`) |
| **6** | A name is not a technology | two panels: (a) retronym pair — rival and standard's name, both series; (b) one merged group — members' series and the group's union | retronyms, merging | `szeregi_czlonow.csv` | **done** (`fig_names`) |

Figures 1, 3, 4 can be drawn now from `osie_48.csv`. Figures 5 and 6 need one file from VS Code: `szeregi_48.csv` — share by year for each of the 48 groups (union of members, the same series `trwalosc_wzgledna_48` was computed from), plus the member-level series for the retronym pairs and for one merged group (kyphoplasty: four members).

Palette: one hue for data (`#3d6b8f`), one light tint for context, text in ink colours; kind encoded by marker shape, never by colour alone; every figure readable in greyscale.

**Drawn 2026-10-29** from `docs/manuscript/figures/draw_figures_48.py` (reads the six `_48` files; one hue `#3d6b8f`, kind by marker, greyscale-readable). `fig_countries.*` (material 54, leads only) is superseded by `fig_origin_lead` and moved to `figures/_superseded/`.
