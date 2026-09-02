# Deviations from the OSF registration
## Register · compiled 2026-09-02 · covers 2026-08-27 → 2026-09-02

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
| D-3 | Observation window **2005–2025** | **2000–2025**; both windows reproducible from the same code | `hip resurfacing` could not emerge — its peak (2008) sat against an already-high 2005–2007 baseline. Indexing drift added (+23%, 2000→2005) is smaller than the drift already inside the accepted window (−27%, 2005→2025) | No | 2026-09-01 |
| D-4 | Coding manual v1.2 §2: technology = "device, material, computational or operative technique" | v1.3 §2: **positive definition extended** (active substance, periprocedural technique) **plus an explicit negative clause** | κ = 0.442 against a threshold of 0.70; 6 of 17 disagreements fell on a gap both coders read defensibly | **Yes** — v1.2 §5 prescribes "below threshold: revise definitions, recode, report both rounds" | 2026-08-31 |
| D-5 | Category **`measurement artifact`** | retired; decision tree loses step 1 | 0 observations in 287 by the human coder | Partly — §5 prescribes revision, not retirement of a category | 2026-08-31 |
| D-6 | **Weighted κ** reported alongside Cohen's κ | **Brennan–Prediger κ** in its place | v1.2 §5 requires the statistic but supplies no weight matrix, and five nominal categories admit no natural ordering | No — this is a defect in the registered document, not a change of plan | 2026-08-31 |
| D-7 | Field = MeSH `Orthopedic Procedures` subtree, **unfiltered** | four record-level exclusions: **D4** vascular, **D5a** dental/maxillofacial, **D5c** `Traction` homonym, **D6** veterinary | ≥ 6.5% of field records are not orthopaedics; separation measured at 94–100% foreign vs 0–2% orthopaedic | No | 2026-08-31 / 09-02 |
| D-8 | Object of study: technology diffusion across the field | **device and technique strata only**; drugs as a contrast layer; disease entities parked for a separate paper | 30 of 813 core phrases are technologies; the material as registered was 96% something else | No — this is the author's scoping decision, taken after seeing the composition | 2026-09-01 |
| D-9 | — (no rule) | v1.4 §4a: **two- and three-letter abbreviations require measured expansions** before entering the material, and may never stand as a separate row beside the full form | fourth occurrence of the same failure (`ml`, then `ha`, `cr`, `ka`, `ai`); no dominant expansion in four of five cases; abbreviation share drifts −5.3 to +3.0 pp/year | No | 2026-09-02 |
| D-10 | Second-coder round on a **60-term stratified subsample** | round two as a **census of the material** | five of seventeen disagreements were n-gram fragments that do not arise under chunking; at 75 groups a census is feasible | No | 2026-08-31 |

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

**Two of ten deviations had their response rule set in advance** (D-1, D-4). The rest were decided
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
   (MTIX: Spearman 0.14, p = 0.36, n = 43) rather than being replaced when it looked suspect.

## 4. Procedural incidents — recorded, not excused

**E1 unblinding, 2026-08-27.** The Cowork session computed the E1 estimate (13.2%, 95% CI
9.5–17.7%) **before coding was complete** and reported it to the coder, then warned him not to let
it influence the remainder. The warning does not undo the exposure. Coding of the affected sheet
was subsequently abandoned for unrelated reasons (D-1), so no reported quantity depends on it —
but had the n-gram branch survived, this would have compromised it. The blinding rule in v1.2 §1
was correct and was broken by the analyst, not by the design.

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
- **No systematic test for foreign-domain contamination exists.** Four leaks were found by four
  different accidents. This belongs in Limitations as stated, not as a solved problem.
