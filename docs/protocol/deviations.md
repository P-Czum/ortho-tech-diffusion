# Deviations from the OSF registration
## Register · compiled 2026-09-02, extended 2026-10-29 · covers 2026-08-27 → 2026-10-29

The registration (OSF, secondary-data preregistration, 2026-08-27) cites twelve frozen files by
SHA-256. **All twelve are unchanged; the manifest verifies 12/12.** Every change below is therefore
a declared deviation recorded against those files, not an edit to them.

This register exists because the Methods section cannot be written from a diary. Each row states
what was registered, what is being done instead, the measurement that forced the change, and —
the column a reviewer will look for first — **whether the rule for responding to that measurement
was set before the measurement was taken**.

---

## 1. The register

| # | Registered | Now | Forced by | Response rule set in advance? | Date |
|---|---|---|---|---|---|
| D-1 | Unit of analysis: **n-grams** | **noun phrases** (spaCy 3.8.16, `en_core_web_sm` 3.8.0) | 79.8% of the human coding fell in one category; ~80% of the top-50 was abstract template; the robotics family fragmented into 8 rows | **Yes** — the two-part acceptance criterion (template gone, family ≤ 2–3 rows) was written and sent before the run | 2026-08-28 |
| D-2 | Core = intersection of **four** text variants | **three** (primary ∩ S2 ∩ S3); S1 reported as sensitivity | S1's dictionary holds 1,882 phrases against 25,419 in primary and yields 85 emergences against 936; it removed 94.2% of the core mechanically, not by judgement | No | 2026-08-31 |
| D-3 | Observation window **2005–2025** | **2000–2025**; both windows reproducible from the same code | `hip resurfacing` could not emerge — its peak (2008) sat against an already-high 2005–2007 baseline. Indexing drift added (field share of PubMed +23%, 2000→2005) is no larger than the drift already inside the accepted window (−23%, 2005→2025; `results/mtix_check.json`). First measured 2026-09-01 as +23% / −27% on an earlier state of the mirror; re-read 2026-10-29 | No | 2026-09-01 |
| D-4 | Coding manual v1.2 §2: technology = "device, material, computational or operative technique" | v1.3 §2: **positive definition extended** (active substance, periprocedural technique) **plus an explicit negative clause** | κ = 0.442 against a threshold of 0.70; 6 of 17 disagreements fell on a gap both coders read defensibly | **Yes** — v1.2 §5 prescribes "below threshold: revise definitions, recode, report both rounds" | 2026-08-31 |
| D-5 | Category **`measurement artifact`** | retired; decision tree loses step 1 | 0 observations in 287 by the human coder | Partly — §5 prescribes revision, not retirement of a category | 2026-08-31 |
| D-6 | **Weighted κ** reported alongside Cohen's κ | **Brennan–Prediger κ** in its place | v1.2 §5 requires the statistic but supplies no weight matrix, and five nominal categories admit no natural ordering | No — this is a defect in the registered document, not a change of plan | 2026-08-31 |
| D-7 | Field = MeSH `Orthopedic Procedures` subtree, **unfiltered** | four record-level exclusions: **D4** vascular, **D5a** dental/maxillofacial, **D5c** `Traction` homonym, **D6** veterinary | ≥ 6.5% of field records are not orthopaedics. Separation, as the share of each control term's documents that the rule removes: D4 92–99% of foreign vs 0–2% of orthopaedic terms; D5c 72–100% vs 0–4.3%; D6 94–97% vs 0–10.8% (the upper end is genuine animal work on orthopaedic implants); D5a not measured on control terms. Corrected 2026-10-29 from a summary ("94–100% vs 0–2%") that no single rule met | No | 2026-08-31 / 09-02 |
| D-8 | Object of study: technology diffusion across the field | **device and technique strata only**; drugs as a contrast layer; disease entities parked for a separate paper | 30 of 813 core phrases are technologies; the material as registered was 96% something else | No — this is the author's scoping decision, taken after seeing the composition | 2026-09-01 |
| D-9 | — (no rule) | v1.4 §4a: **two- and three-letter abbreviations require measured expansions** before entering the material, and may never stand as a separate row beside the full form | fourth occurrence of the same failure (`ml`, then `ha`, `cr`, `ka`, `ai`); no dominant expansion in four of five cases; abbreviation share drifts −5.3 to +3.0 pp/year | No | 2026-09-02 |
| D-10 | Second-coder round on a **60-term stratified subsample** | round two as a **census of the material** | five of seventeen disagreements were n-gram fragments that do not arise under chunking; at 75 groups a census is feasible | No | 2026-08-31 |
| D-11 | RQ3: distribution of the **five categories** over the 287-term core; §6.2 consistency controls; after κ < 0.70, **recoding and reporting of both rounds** | coder 1's distribution over the 287-term core reported as a **closed result** in S1 (non-technological 229, renaming 20, novel concept 20, conceptual evolution 18, measurement artifact 0); **round two not run**; the five-category scheme is not applied to the noun-phrase material; §6.2(a) and (c) not performed | D-1 retired the n-gram core as material. The human coder saw concentration axes, doubling times and persistence while the material was being defined, so a second round could be blinded only on the model side and would not measure what the registration specified | No | 2026-10-27 |
| D-12 | §6.3: `y₀` under the primary definition **with the secondary-definition value beside it**, flag where they differ by > 2 years; §6.2(b) reproduction under the secondary definition | `y₀` reported under the **primary definition only** | Not forced by a measurement — the author's decision to keep the paper to one field definition. The secondary definition exists only as n-gram counts for 2005–2025 (before D-1 and D-3); the two definitions overlap at Jaccard ≈ 0.31 and the secondary includes rheumatology and basic science, so its `y₀` differences would mix measurement uncertainty with field composition rather than estimate the former. Text for 2000–2025 (316,091 records) is extracted and retained; the analysis was not run | No — scoping decision | 2026-10-27 |

## 2. What was deliberately left alone

Listed because a reviewer will otherwise assume everything moved:

- the agreement threshold, **κ ≥ 0.70**;
- the emergence rule — θ = 0.1% of field records and ≥ 5 papers, `y₀` sustained ≥ 3 years;
- the blinding rule (doubling time, concentration axes and secondary-definition results stay
  closed to the coder until coding is complete);
- the lift threshold (≥ 3) and its status as a search device, not a decision rule;
- the substitution test;
- the alternative field definition (137 journals), left **unfiltered** even though three of its
  journals are questionable, because pruning it against the primary definition would destroy its
  value as an independent control.

Revising any of these in the same pass as a failed agreement result would be indistinguishable
from tuning the instrument until the number passes.

## 3. The honest reading of column four

**Two of twelve deviations had their response rule set in advance** (D-1, D-4). The rest were decided
after seeing a measurement. That is the weakest point of this project and it should be stated in
the Methods rather than discovered by a reader.

Three things bound how much it can be exploited:

1. **Every change is documented with the number that forced it**, and those numbers were computed
   before the change, not after. The register above is auditable against `scoping_log.md` and the
   dated briefs in `docs/briefs/`.
2. **The changes move in the costly direction.** D-2 grew the core from 47 to 813 — more work,
   more rubbish to classify. D-7 removed 6.5% of the field. D-8 discarded the largest and most
   striking stratum of the results. None of them made a result easier to obtain.
3. **The primary quantities were not re-specified.** The ranking axis survived a direct test
   (MTIX: Spearman 0.14, p = 0.36, n = 43; re-run on the final material 2026-09-03: Spearman
   0.14, p = 0.18, n = 88; on material 48 after the variant correction of 2026-10-29: Spearman 0.15, p = 0.20, n = 76 phrases) rather than being replaced when it looked suspect.

## 4. Procedural incidents — recorded, not excused

**E1 unblinding, 2026-08-27.** The Cowork session computed the E1 estimate (13.2%, 95% CI
9.5–17.7%) **before coding was complete** and reported it to the coder, then warned him not to let
it influence the remainder. The warning does not undo the exposure. Coding of the affected sheet
was subsequently abandoned for unrelated reasons (D-1), so no reported quantity depends on it —
but had the n-gram branch survived, this would have compromised it. The blinding rule in v1.2 §1
was correct and was broken by the analyst, not by the design.

**Abbreviations counted without their full forms, found 2026-10-28.** Coding manual v1.4 §4a
(D-9) requires an abbreviation to be counted together with its full form. The analyst applied it
incompletely: nine groups were labelled with the full name but counted the abbreviation alone
(`taa`/`tar`, `pao`, `tea`, `fnb`, `pvp`, `mep`, `pfna`, `mua`; and `anterolateral ligament`
without the phrase the group is named after). This is a counting error, not a change of plan, and
it is not a finding. Full forms are now merged. Five groups do not emerge once counted correctly
and leave the material (total ankle arthroplasty, total elbow arthroplasty, periacetabular
osteotomy, femoral nerve block, vertebroplasty); `manipulation under anesthesia` is excluded
because its full form is not a noun phrase and cannot be counted. Material 54 → **48**; the 45
groups not touched are unchanged cell for cell. Found by the sensitivity analysis of the
text-variant intersection, which placed `vertebroplasty` (1,518 papers) outside the group named
after it; a sweep of every abbreviation in the material found the rest.

**Variants agreed for a group but not counted in it, found 2026-10-29.** The same error by another
route. `locking plate fixation` is on the synonym list as a variant of *locking plate*, and the
surgeon marked it so; it dropped out of the group because, after D6, it no longer emerged on its
own, and group membership had been carried over only for phrases that emerged individually.
`ra total knee arthroplasty` (90 of 91 papers about robotic surgery) and `imn` were agreed for the
material on 2026-09-01 on the 2005–2025 window and lost in the move to 2000–2025, because they
had no category proposal and the default for such phrases was *research method*. Corrected:
*locking plate* 1,574 → 1,692 papers, doubling time 6.2 → 5.6 years, y₀ and peak unchanged, not a
decline (0.51 → 0.52 of peak); *robotic assistance* 679 → 714 papers, y₀ 2019 → **2018**; `imn`,
counted with *intramedullary nail(ing)*, does not emerge (baseline 1.35% of the field) and is
recorded among the exclusions. The other 46 groups are unchanged cell for cell. Material: 48
groups, 86 phrases. Every exclusion is now listed with its stage, reason and source in
`data/processed/wylaczenia_48.csv`; a check confirms that it covers every phrase that was ever in
a version of the material and is not in the final one.

**Precision of the material is measured by the domain expert, not by the analyst.** The category
proposals in `np_kategorie_propozycja.tsv` are the language model's; the adjudication is the
orthopaedic surgeon's, and his file is the record. Where his ratings are quoted (43 apt, 7
doubtful, 1 wrong of 51 rated), they are his.

## 5. Open items that would change this register

- ~~D-9 carries an unmeasured risk.~~ **Closed 2026-09-02.** The by-year share was measured for
  every excluded abbreviation and falls or is flat (`ai` −5.27 pp/year, `ka` −0.90, `cr` −0.04),
  so exclusion removes early foreign documents rather than late genuine ones. The same measurement
  found the risk operating on the abbreviations that are *kept*: eight of them rise (`cda` 0.0% →
  33.3%, `tdr` 28.8% → 50.2%), which is why v1.4 §4a now forbids leaving an abbreviation as a
  separate material row. The synonym dictionary turns out to be a safeguard on `y₀` and doubling
  time, not a cosmetic merge.
- **D5b is proposed but not implemented** — the dental leak entering through `Osteogenesis,
  Distraction` and `Bone Transplantation`. Its size (≥ 1.44% of the field) is a lower bound from
  title probes, not a measurement.
- ~~No systematic test for foreign-domain contamination exists.~~ **Closed 2026-09-03.**
  `audyt_skazenia.py` measured, for every material group, the share of documents carrying a
  descriptor from a foreign domain: 0 of 60 groups above 20%, median 0.6%, veterinary share 0.0%
  in every group. The one group above the threshold before the audit (cone-beam CT, 82.5% dental)
  had already been removed. The four earlier leaks were still found by accident; the audit is
  the planned test that now stands behind them. **Re-run on material 48, 2026-10-29**, after the
  corrected domain list (dental, digestive, urogenital, eye) was moved from a post-processed CSV
  column into `audyt_skazenia.py`: 0 of 48 groups above 20%, 0 above 10%, median 0.5%, maximum
  8.6% (ACDF, digestive); veterinary share 0.0% in every group (`audyt_skazenia_48.csv`).
