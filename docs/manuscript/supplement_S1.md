# Supplement S1. Preregistration, deviation register, and correction record

The study was registered on OSF on 2026-08-27 as a secondary-data preregistration citing twelve frozen files by SHA-256 (protocol, coding manual v1.2, field definition, detector code, and data manifests). All twelve files are unchanged; the manifest verifies 12/12 at the time of writing. Every change described below is a declared deviation recorded against those files, not an edit to them. The register is kept in the project repository as `docs/protocol/deviations.md`; this supplement reproduces it.

## S1.1 Deviation register

Each row states what was registered, what was done instead, the measurement that forced the change, and whether the rule for responding to that measurement had been set before the measurement was taken.

| # | Registered | Done instead | Forced by | Response rule set in advance? |
|---|---|---|---|---|
| D-1 | Unit of analysis: n-grams | Noun phrases (spaCy 3.8.16, `en_core_web_sm` 3.8.0) | 79.8% of the human coding of the n-gram core fell in one category; about 80% of the top-50 n-grams were abstract template; the robotics family fragmented into eight rows | **Yes** — a two-part acceptance criterion (template absent from the top 50; the robotics family reduced to at most three rows) was written and sent before the noun-phrase run |
| D-2 | Core = intersection of four text variants | Intersection of three (primary ∩ abstract subset ∩ English subset); the title-only variant reported as sensitivity | The title variant's dictionary holds 1,882 phrases against 25,419 in the primary and yields 85 emergences against 936; its intersection destroyed the core rather than confirming it | No |
| D-3 | Observation window 2005–2025 | 2000–2025, both windows reproducible from the same code | Hip resurfacing could not emerge: its peak (2008) sat against an already-high 2005–2007 baseline | No |
| D-4 | Coding manual v1.2 §2: technology = "device, material, computational or operative technique" | v1.3 §2: positive definition extended (active substance, periprocedural technique) plus an explicit negative clause | κ = 0.442 against a threshold of 0.70; 6 of 17 disagreements fell on a gap in the definition that both coders read defensibly | **Yes** — v1.2 §5 prescribes "below threshold: revise definitions, recode, report both rounds" |
| D-5 | Category `measurement artifact` | Retired; the decision tree loses its first step | 0 observations in 287 coded phrases | Partly — §5 prescribes revision, not retirement, of a category |
| D-6 | Weighted κ reported alongside Cohen's κ | Brennan–Prediger κ in its place | v1.2 §5 requires the statistic but supplies no weight matrix, and five nominal categories admit no natural ordering | No — a defect in the registered document, not a change of plan |
| D-7 | Field = MeSH *Orthopedic Procedures* subtree, unfiltered | Four record-level exclusions: vascular limb salvage, dental and maxillofacial, the *Traction* homonym, veterinary | ≥ 6.5% of field records belonged to other specialties; separation of each rule measured on terms known to belong to each side (S3) | No |
| D-8 | Object of study: technology diffusion across the field, all categories | Device and technique strata only; drugs as a contrast layer; disease entities parked for a separate study | Only 30 of 813 core phrases named a technology; 96% of the material as registered was something else | No — the author's scoping decision, taken after seeing the composition |
| D-9 | — (no rule) | v1.4 §4a: two- and three-letter abbreviations require measured expansions before entering the material, and may never stand as a separate row beside the full form | Fourth occurrence of the same abbreviation problem in coding; the by-year share of kept abbreviations rises (e.g. `tdr` 28.8% → 50.2% of its technology's papers), so a separate abbreviation row would bias emergence year and doubling time | No |
| D-10 | Second-coder round on a 60-term stratified subsample | Round two as a census of the material | Five of seventeen disagreements were n-gram fragments that do not arise under chunking; at 75 groups a census was feasible | No |
| D-11 | RQ3: distribution of the five categories over the 287-term core; consistency controls; after κ < 0.70, recoding and reporting of both rounds | Coder 1's distribution over the 287-term core reported as a closed result (non-technological 229, renaming 20, novel concept 20, conceptual evolution 18, measurement artifact 0); round two not run; the five-category scheme not applied to the noun-phrase material | D-1 retired the n-gram core. The human coder had seen concentration axes, doubling times and persistence while the material was being defined, so a second round could have been blinded only on the model side and would not have measured what the registration specified | No |
| D-12 | y₀ under the primary definition with the secondary-definition value beside it, flagged where they differ by > 2 years | y₀ reported under the primary field definition only; the secondary definition (137 orthopaedic journals) not analysed | Not forced by a measurement. The secondary definition exists only as n-gram counts for 2005–2025 (before D-1 and D-3); the two definitions overlap at Jaccard ≈ 0.31 and the secondary includes rheumatology and basic science, so its y₀ differences would mix measurement uncertainty with field composition | No — the author's scoping decision |

**What was deliberately left alone**, because revising it in the same pass as a failed agreement result would be indistinguishable from tuning the instrument until a number passes: the agreement threshold κ ≥ 0.70; the emergence rule (θ = 0.1% of field records and ≥ 5 papers, sustained ≥ 3 years); the blinding rule (doubling time, concentration axes and secondary-definition results closed to the coder until coding was complete); the lift threshold (≥ 3) and its status as a search device rather than a decision rule; the substitution test; and the alternative field definition (137 journals), left unfiltered.

## S1.2 The honest reading of the last column

Two of twelve deviations had their response rule set in advance (D-1, D-4). The rest were decided after seeing a measurement. Three things bound how much this can be exploited. First, every change is documented with the number that forced it, and those numbers were computed before the change, not after; the register is auditable against the dated project log. Second, the changes move in the costly direction: D-2 grew the core from 47 to 813 phrases, D-7 removed 6.5% of the field, D-8 discarded the largest and most striking stratum of the results. None made a result easier to obtain. Third, the primary quantities were not re-specified: the ranking axis survived a direct test (MTIX, S8.4) rather than being replaced when it looked suspect.

## S1.3 Procedural incidents

Recorded, not excused.

**Unblinding, 2026-08-27.** The analyst computed an estimate from the first coding sheet before coding was complete and reported it to the coder, then warned him not to let it influence the remainder. The warning does not undo the exposure. Coding of that sheet was subsequently abandoned for unrelated reasons (D-1), so no reported quantity depends on it; had the n-gram branch survived, this would have compromised it. The blinding rule was correct and was broken by the analyst, not by the design.

**Abbreviations counted without their full forms, found 2026-10-28.** Coding manual v1.4 §4a (D-9) requires an abbreviation to be counted together with its full form. The analyst applied it incompletely: nine groups were labelled with a full name but counted the abbreviation alone. This is a counting error, not a change of plan, and it is not a finding; the correction record is S1.4. It was found by the sensitivity analysis of the text-variant intersection (S8.2), which placed *vertebroplasty* (1,518 papers) outside the group named after it; a sweep of every abbreviation in the material found the rest.

**Who measures precision.** Category proposals were generated by a language model; the adjudication is the orthopaedic surgeon's, and his file is the record (S4). Where his ratings are quoted, they are his.

## S1.4 Correction record: abbreviations merged with full forms (material 54 → 48)

Each group now contains the expansion of its abbreviation and the phrase it is named after. The 45 groups not affected are unchanged cell for cell (axes, series, persistence, origin). Five groups do not emerge once counted correctly and leave the material; one is excluded because its full name is not a noun phrase and cannot be counted.

| Group as labelled | Counted before | Counted after merging | Outcome |
|---|---|---|---|
| total ankle arthroplasty | `taa`, `tar` — 853 papers, y₀ 2007 | + *total ankle arthroplasty*, *total ankle replacement* — 1,498 | no y₀ → leaves the material |
| periacetabular osteotomy | `pao` — 404, y₀ 2012 | + full name — 700 | leaves |
| total elbow arthroplasty | `tea` — 321, y₀ 2013 | + full name — 605, peak 2005 | leaves |
| femoral nerve block | `fnb` — 188, y₀ 2014 | + full name — 411 | leaves |
| vertebroplasty | `pvp`, *vertebral augmentation* — 886, y₀ 2005 | + *vertebroplasty*, *percutaneous vertebroplasty* — 2,601, peak 2009 | leaves |
| manipulation under anaesthesia | `mua` — 242 | full name is not a noun phrase¹ | excluded under §4a |
| motor evoked potential | `mep` — 592 | 642 | stays; y₀ 2013 unchanged |
| proximal femoral nail antirotation | `pfna` — 308 | 345 | stays; y₀ 2011 unchanged |
| anterolateral ligament reconstruction | *anterolateral ligament* — 158 | 231 | stays; y₀ 2016; peak year 2017 → 2025 |

¹ A noun phrase ends before a preposition, so *manipulation under anaesthesia* is never chunked as one phrase.

The curves counted before correction rose with the habit of writing abbreviations in abstracts, not with the technologies. Nothing in the Results depends on the groups that left; Methods state the rule in one sentence.
