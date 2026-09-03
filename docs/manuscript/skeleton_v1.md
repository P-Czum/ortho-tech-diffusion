# Manuscript skeleton v1 — for CORR
### 2026-09-03 · for approval before drafting · every number below is to be re-verified against `osie_ostateczne.csv` and `scoping_log.md` at drafting time; those marked ⟨…⟩ are not yet computed

---

## Title — three candidates

1. **What the Literature Pays Attention To: Emergence, Spread, and Decline of Surgical Technologies in Orthopaedics, 2000–2025**
2. **Scholarly Attention Is Not Clinical Adoption: A Preregistered Bibliometric Study of Orthopaedic Technologies Whose Registered Analysis Failed**
3. **Which Orthopaedic Technologies Emerged in the 21st Century, How Far Did They Spread, and Why Did Attention to Some of Them Fade?**

Recommendation: **3** as title, with the "attention is not adoption" idea as the first sentence of the abstract. CORR titles are questions or plain statements; 2 is honest but reads as a confession, and the confession belongs in Methods, not on the cover.

---

## Structured abstract (CORR format)

**Background.** Bibliometric studies routinely treat publication counts as a measure of how a technology spreads. Whether a count of papers can distinguish a technology entering practice from one being argued about, renamed, or abandoned has not been tested in orthopaedics — and the field definitions such studies rely on have not been checked for what they let in.

**Questions/purposes.** (1) Which surgical technologies and techniques emerged in the procedural orthopaedic literature between 2000 and 2025, and when? (2) How concentrated was scholarly attention to each — by country, author, and journal — and how fast did it grow? (3) Among technologies whose attention later declined, is the depth of the decline ordered by the state of clinical evidence? (4) How much of a MeSH-defined orthopaedic literature is not orthopaedics, and what happens to a preregistered n-gram analysis of it?

**Methods.** PubMed 2026 baseline; field = MeSH *Orthopedic Procedures* and descendants, 2000–2025, ⟨N⟩ records after removal of four measured contaminants (vascular limb salvage, maxillofacial surgery, the *Traction* homonym, veterinary literature — together ≈ 9% of records). Units: noun phrases (spaCy), replacing the preregistered n-gram unit after the registered analysis failed (79.8% of the registered 287-term core named no technology; human–model agreement κ = 0.44 against a preregistered 0.70). Emergence: first year a phrase's share of the field reaches max(0.1%, 5× its 2000–2002 baseline), sustained three years. Material: 76 technology groups after category screening by an orthopaedic surgeon and merging of abbreviations and variants. Strength: effective number of countries, authors and journals (1/HHI, country from first affiliation), doubling time, peak share, persistence (2025 share / peak share). Evidence state for 13 declining technologies classified from guidelines, systematic reviews and registries. Eleven deviations from the OSF registration are tabulated with the measurement that forced each.

**Results.** (1) 76 groups, from hip resurfacing (y₀ 2005) to femoral neck system (2021); the earliest decade is visible only because the window opens before 2005. (2) Concentration separates technologies that paper counts cannot: percutaneous kyphoplasty (545 papers, China 90.5%, 1.2 effective countries) versus cone-beam CT (553 papers, 15.9%, 14.7 countries). Fastest doubling: hip arthroscopy 1.7 years, robotic assistance 2.0, AI/ML 2.1. (3) Persistence of the 13 declines orders by evidence state without overlap: evidence against use 0.10–0.17 (metal-on-metal, resurfacing); unresolved 0.20–0.39; evidence for use and routine adoption 0.43–0.61 (Ponseti, kyphoplasty). Eleven of 24 apparent declines were terminological transitions, not abandonments. (4) ≈ 9% of the MeSH-defined field was vascular surgery, dentistry, veterinary medicine or a homonym, with 94–100% separation on term-level tests; the registered n-gram analysis could not be completed.

**Conclusions.** Attention in the literature can be measured for named technologies once the unit is a phrase and the field is cleaned, and its concentration and persistence carry information that counts alone do not. Attention is not adoption: its decline tracks the closing of a clinical question — against, unresolved, or settled — not the fate of the technology. The evidence-gradient finding is exploratory (n = 13) and is stated so that it can be refuted; ⟨a blinded re-rating and a test on the alternative field definition were preregistered before execution — insert DOI⟩.

**Clinical relevance.** Surgeons reading bibliometric claims about "trending" or "declining" technologies should ask whether the count reflects adoption, controversy, or renaming; this study shows the three are distinguishable, and how.

---

## Section plan — one sentence per heading on what it must say

### Introduction (≈ 600 words)
- **P1.** Publication counts are used as a proxy for technology diffusion in surgery, but a count cannot tell a technology in use from one being disputed or renamed.
- **P2.** Existing normalisation in bibliometrics corrects citation impact for field, not publication share for field growth; diffusion of technology is measured with patents, which miss operative technique (this is the gap from `scoping_log.md` §"Luka").
- **P3.** We preregistered a detector and a coding manual, not findings; the registered analysis failed in a measured way, and what follows is exploratory. State this here, in the fourth paragraph, not in a footnote.
- **P4.** Four questions.

### Methods (≈ 1,400 words)
- **Data and field.** PubMed baseline, deduplication rule, MeSH subtree, two windows (2005 registered, 2000 used; both reproducible), why 2000 (hip resurfacing invisible with 2005 baseline; indexing drift added +23% smaller than drift already accepted −27%).
- **Field contamination.** Four leaks, how each was found (none by a planned test), rule for each, size, term-level separation test with the 90/5 criterion; D6 authoritative (NLM check tags), others heuristic; alternative definition left unfiltered on purpose.
- **Unit of analysis.** n-gram registered → failure (template, fragmentation, 79.8%) → noun phrases with the pre-set two-part acceptance criterion; 9.6× fewer units, 8.2× fewer emergences; S1 dropped because its dictionary is 1,882 vs 25,419 (mechanical, not evaluative).
- **Emergence detector.** Unchanged from registration: θ, 5× baseline, three-year sustain; core = intersection of three text variants.
- **Material.** Category proposal by a language model, adjudication by the orthopaedic surgeon (his file is the record); technology = device, material, computational method, operative or periprocedural technique; not technology = methodology, scales, outcomes, disease entities; abbreviations merged or excluded, never separate (measured drift −5.3 to +3.0 pp/yr); 76 groups.
- **Strength axes.** Concentration (1/HHI; author key surname|country|institution; country from first affiliation only, median missingness 9.0%), doubling time from log-share slope y₀→peak, peak share, persistence; drugs reported as a contrast layer, not in the main table (different diffusion mechanism, n = 7).
- **Evidence state.** Three states, sources, who classified; ⟨blinded re-rating by an independent surgeon — done / preregistered⟩.
- **Indexing discontinuity.** MTIX 2022 tested as three hypotheses; H1–H3 all confirmed; H3 does not transfer to the ranking (Spearman 0.14, p = 0.36, n = 43); axis retained; small-power caveat.
- **Deviations.** One paragraph pointing to Supplementary Table S1 (11 rows, column "response rule set in advance": 2 of 11), with the three bounds on exploitation (numbers computed before changes; changes in the costly direction; primary axis tested rather than replaced).
- **Preregistration statement and the E1 incident.** OSF DOI; 12/12 frozen files unchanged; one blinding breach by the analyst, recorded.

### Results (≈ 1,200 words + 3 tables + 3 figures)
- **R1 — What emerged and when.** Table 1: 76 groups, y₀, peak year, peak share, category. Figure 1: timeline. One paragraph on the first decade (navigation, PEEK, HXLPE, UKA, Ponseti, ACI) being invisible from a 2005 window.
- **R2 — How far and how fast.** Table 2: concentration and doubling time. Figure 2: effective countries vs papers, kyphoplasty and CBCT labelled. The China/USA pattern reported as pattern, with the publishing-habit caveat stated, not resolved.
- **R3 — Declines and evidence.** Table 3: 13 declines, persistence, evidence state, level of external support. Figure 3: persistence by evidence state, non-overlapping ranges. The 24→13 correction reported as a result: eleven "withdrawals" were renamings.
- **R4 — The field and the registered analysis.** Contamination table; the κ result; 79.8%. Short. This is a result, not an apology.

### Discussion (≈ 1,200 words)
- **Principal finding.** Attention can be measured for named technologies, and its shape carries information counts lack — but attention is not adoption, and the paper's own history shows how easily one is mistaken for the other (four corrections in one session, all from the surgeon).
- **The evidence gradient.** Why the interpretation is coherent (evidence "no" kills the literature; "yes" moves it to registries and series); why it is a hypothesis (n = 13); what would refute it.
- **What the failed registration teaches.** n-grams are not a unit of meaning; a preregistered apparatus can fail in a way that is itself a finding; the deviation table and its uncomfortable column.
- **Limitations — as measured properties, not disclaimers.** Detector sees starts, not gradual growth (PRP); moving the window moves the blind spot (BMP, resurfacing, VR); attention confounds clinical value with access (ACI vs microfracture); leaving the field is indistinguishable from fading (MSC); no systematic contamination test exists — four leaks, four accidents; MTIX discontinuity real, effect on ranking not detected at n = 43; alternative field definition itself contaminated (Head & Face Medicine) and deliberately left so.
- **Where this goes.** Preregistered confirmatory test of the evidence gradient on another surgical specialty, registered before the pipeline touches it.

### Supplement
- S1 deviations table (from `deviations.md`); S2 coding manual v1.4; S3 field-filter rules with PMID lists; S4 category proposals and adjudication file; S5 full 76-group table with all axes; S6 MTIX analysis; S7 the 13 decline series.

---

## Three decisions needed before drafting

1. **Registered question 3 (novel / renaming / evolution).** It cannot be answered as registered — κ failed and round two on the census was not run. Options: (a) drop it, report only the failure and the 11-of-24 renaming finding as what survives; (b) run round two now on 76 groups with v1.4 and report it. (a) is honest and cheap; (b) adds a week and a result. Skeleton assumes **(a)**.
2. **The blinded re-rating and def2 test.** Skeleton assumes they are **preregistered and done before submission**; if not, the Conclusions sentence and the last Discussion paragraph change.
3. **Author list.** Independent rater for evidence state, if used, is a co-author.
