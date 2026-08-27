# OSF Preregistration — draft
## Emerging concepts in orthopaedic literature: distinguishing novelty from renaming

Author: Przemysław Czuma, MD (ORCID 0009-0009-8235-2053), Department of Orthopedics and
Traumatology, Piekary Śląskie, Poland · Polish Association for Artificial Intelligence in Medicine
Template: OSF Preregistration for Secondary Data Analysis · Date: 2026-08-27 · Status: DRAFT

---

## 1. Research questions

1. Which concepts in the procedural orthopaedic literature **emerged** between 2005 and 2025,
   and in which year (`year of emergence`)?
2. How strong was each emergence: breadth of scholarly diffusion (concentration measures),
   growth rate (doubling time), and peak prevalence (maximum annual share of the field)?
3. What proportion of emergences are genuinely new concepts, and what proportion are new names
   for, or evolutions of, concepts that already existed — across five categories: *novel
   concept*, *renaming*, *conceptual evolution*, *measurement artifact*, *non-technological term*?

This study measures **scholarly attention in the published literature, not clinical adoption**.
Publication counts proxy research interest and the circulation of ideas; they are not evidence
that a technology entered practice.

Design: discovery-oriented with a **preregistered apparatus**. We register the detector, its
thresholds, and the coding manual — not predicted findings.

## 2. Data (existing prior to registration)

PubMed Annual Baseline 2026 (`pubmed26n0001`–`n1334`, released 2026-01-30) plus daily update
files, mirrored locally. Deduplication: for repeated PMIDs the occurrence from the latest file
wins; PMIDs listed in any `DeleteCitation` are removed.

**Primary field definition:** MeSH descriptor `Orthopedic Procedures` plus all descendants
(56 descriptors, expanded programmatically from `desc2026.xml`) — **268,383 records**, 2005–2025.

**Secondary field definition** (sensitivity analysis): 137 journals carrying the NLM Broad
Subject Term "Orthopedics" — 281,261 records. The two definitions overlap only moderately
(Jaccard ≈ 0.31); they are not two measurements of one field, and the primary definition is
used for all main analyses.

## 3. Work already completed (explicit declaration)

Completed **before** registration: mirror construction and deduplication; both field
definitions; n-gram canonicalisation (frozen rule lists); emergence detection with text-
availability sensitivity variants S1–S3, yielding a **core of 287 terms** (the intersection of
all four variants); strength axes; predecessor-candidate generation (lift ≥ 3, used as a search
device); freezing of the coding sheet and manual (hashes in §7).

**Not completed: category coding.** No term has been assigned to any of the five categories by
any coder. The distribution of categories — the principal outcome of research question 3 — is
unknown at the time of registration.

## 4. Detector (frozen)

For each canonical term, `s(y)` denotes its share of field records in year `y`.

- Presence threshold `θ` = 0.1% of field records in that year, and at least 5 papers.
- **Year of emergence `y₀`** = the first year in which `s(y) ≥ max(θ, 5 × baseline)`, where
  baseline is the mean share over 2005–2007, sustained for at least three consecutive years.
- `y₀ ≤ 2023`, so that three confirmatory years fall inside the window.

Terms to be coded: those detected as emerging in **all four** text variants — title + abstract
(primary), title only (S1), abstract-bearing records only (S2), English-language records only
(S3). S1 is reported as a substantive filter, not a robustness check, because it requires
0.1% prevalence within titles (~12 words per record).

## 5. Coding

Manual: `coding_manual_v1.2.md` (hash in §7). It contains operational definitions of the five
categories, the **substitution test** (bidirectional substitution between a term and its
predecessor = *renaming*; unidirectional = *conceptual evolution*), a fixed decision tree, and
coder blinding.

**Blinding.** Coders see the term, its annual share series, `y₀` under the primary definition,
predecessor candidates with lift, and titles containing the term, the predecessor, and both
(window `y₀ ± 2`). Coders do **not** see doubling time, concentration axes, or results under the
secondary field definition — these three serve as **independent post-coding controls**, and a
control the coder can see measures compliance with a number rather than agreement between two
independent routes to the same distinction.

**Coder 1 (all 287 terms):** P. Czuma, working from the blinded view with a logged corpus
search tool.

**Coder 2 (60-term subsample):** the language model `openai/gpt-5.6-sol` accessed through
OpenRouter, seed 20260827, prompts frozen before coding (`prompt_system_v1.2_EN.txt`,
`prompt_user_v1.2_EN.txt`; hashes in §7). The `temperature` parameter is not supported by this
model, so determinism is established by the seed. The model receives the same blinded view and
applies the same procedure. Subsample drawn by stratified random sampling: `y₀` epoch
(2005–2012 / 2013–2019 / 2020+ → 6 / 36 / 18) × n-gram length.

**Agreement:** Cohen's κ, threshold ≥ 0.70, reported alongside raw agreement and weighted κ
(five categories of markedly unequal frequency make κ alone unstable). If the threshold is not
met: operational definitions are revised, the subsample is recoded, and **both rounds are
reported**.

**Explicit statement:** Coder 2 is a language model. The reported κ is therefore
**human–model agreement, not conventional inter-rater reliability between two human coders**.
It is named as such in the Methods and discussed in the Limitations. In exchange, coder 2 is
fully reproducible — model, provider, seed, prompt hash, and a log of raw responses are all
recorded. The model was not, and will not be, selected on the basis of its performance on the
subsample; any comparative pilot across models would use terms outside the subsample only.

## 6. Prespecified post-coding analyses

1. **Distribution of the five categories** across the 287-term core, reported with a mandatory
   scope caveat: the core was pre-filtered for robustness across four text variants, so the
   proportion of measurement artifacts is low **by construction**. The distribution describes
   robust emergences and does **not** generalise to the full set of 7,662 detected emergences.
2. **Consistency controls.** (a) Doubling time versus category — technologies are expected to
   double their share within 2–3 years and methodological terms within 8–15; agreement reported,
   discordant cases discussed individually. (b) Reproduction under the secondary field definition
   versus category. (c) Category distribution by `y₀` epoch, with a caution flag for `y₀ ≥ 2020`,
   the measured window of indexing lag.
3. **`y₀` reporting.** The primary-definition value with the secondary-definition value beside
   it, and a flag where the two differ by more than two years (25% of the core). The two values
   are not averaged: each is correct with respect to its own definition, and their divergence is
   reported as an estimate of uncertainty rather than a correction.
4. **Renaming pairs.** For terms coded as *renaming* or *conceptual evolution*: a figure showing
   the declining predecessor, the rising term, and their co-occurrence window.

## 7. Hashes of frozen files (sha256)

```
5bfc3d6a7add370d23c505dfcaa0020a6f1ec6d9f2fbb3b90d4e8328fdae46a1  coding_sheet_full.csv
bf065aadc07350bd02117b3e86b714906e2fb21caefbaff7c0946861853f3588  coding_sheet_koder.csv
<pending re-freeze>                                                coding_manual_v1.2.md
<pending re-freeze>                                                prompt_system_v1.2_EN.txt
<pending re-freeze>                                                prompt_user_v1.2_EN.txt
```

The full manifest (12 files, including canonicalisation rule lists, the field definition of
56 MeSH UIs, the list of 137 journals, and `emerging_core.json`) is
`docs/protocol/freeze_manifest.txt` in the project repository.

## 8. Deviations

Any deviation from this registration will be reported in the resulting publication, with its
rationale, and labelled as post hoc.
