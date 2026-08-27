# Coding manual — emerging terms
## v1.2 (English) · 2026-08-27

**This is a translation of v1.1 (Polish), not a revision.** No operational rule was changed.
The switch to English removes a second statement of the same rules in another language, which
is how prompt and documentation diverged once before. From v1.2 onward, the English text is
the single source of truth; v1.1 is retained for history only.

---

## 1. Material and blinding

The unit of coding is a **term** from the frozen sheet (287 rows, hash in the freeze manifest).

The coder sees: the term; its annual share series; `y₀` under the primary field definition;
predecessor candidates with lift (a **search device**, see §3); titles containing the term from
around `y₀` and from 2023–2025; **titles containing the predecessor**; and **titles containing
both**, drawn from the window `y₀ ± 2` (columns `poprzednik_glowny`, `tytuly_poprzednika`,
`tytuly_WSPOLNE`; coverage 284/287).

The coder may search the corpus **only through the supplied tool** (canonical-term search with
a query log); every search is noted in `uwagi`.

The coder does **not** see, during coding: doubling time, concentration axes, or results under
the secondary field definition. These three are **independent post-coding controls** (§6).
A control the coder can see measures the coder's compliance with a number, not agreement
between two independent routes to the same distinction. The coder's view is the sheet without
those columns; the full sheet stays closed until coding is complete.

## 2. The five categories — operational definitions

We code the **referent** of a term (a capability, device, or practice), not the string itself.

**`novel concept`** — the referent did not exist in the field before the emergence window,
under any name. Conditions: (a) titles from around `y₀` describe a capability with no earlier
counterpart; (b) no candidate on the list has a referent matching the term's referent.
An empty candidate list is a **default hypothesis, not a verdict** — a predecessor may have
lived below the 50-occurrence threshold or outside the field; the coder confirms by reading
titles.

**`renaming`** — the referent is identical to the predecessor's. Operational test — the
**substitution test**, applied to the material in the `tytuly_*` columns: substituting the
predecessor for the term in titles from the overlap period preserves meaning **in both
directions**. Supporting evidence: shared titles (e.g. "3D rapid prototyping"), a co-occurrence
window. Exemplar: `rapid prototyping → 3d printing`.

**`conceptual evolution`** — the new term's referent contains the predecessor's **plus a
constitutive element** (or substantially changes its scope). The substitution test passes in
one direction only: every robot uses navigation, not every navigation is a robot. Exemplar:
`navigation → robotic` (cf. the shared title "robotic navigation system").

**`measurement artifact`** — the emergence is driven by measurement rather than by a phenomenon.
Indications: `y₀ ≥ 2020`, inside the measured indexing-lag window, **in conjunction with**
term content indicating a writing or indexing convention (date formulas, abstract-template
phrases, reporting-registry terms). The date alone is not sufficient — 86 core terms have
`y₀ ≥ 2020` and most of them are real phenomena.

**`non-technological term`** — the referent is real and emerging but is not a technology:
research methodology, statistics, reporting convention, care organisation, or a clinical topic.
Exemplars: `systematic review` yes; `length of stay` yes (care organisation); `machine learning`
no (a technology). This category is not a bin: the distribution of categories is a primary
finding.

## 3. Predecessor candidates — the status of lift

Lift is a **device for finding candidates, not a decision rule**. Measurement shows that lift
does not separate signal from noise (`we tested the` has lift 36.0 against `machine learning`);
the coder separates them semantically. Candidate-list threshold: **lift ≥ 3, identical in the
sheet and in this manual**. The threshold is deliberately permissive: missing a true predecessor
costs more than one extra candidate to reject (cf. the `MIN_CO` lesson, where an over-strict
frequency threshold removed the pair with the highest lift in the dataset).

## 4. Procedure — decision tree

1. Is the emergence a measurement artifact (per §2)? → YES: `measurement artifact`, stop.
2. Is the referent a technology (device, material, computational or operative technique)?
   → NO: `non-technological term`, stop.
3. Is there a predecessor with a matching referent, on the list or found manually with the
   tool from §1? → NO: `novel concept`, stop.
4. Substitution test against that candidate: bidirectional → `renaming`; unidirectional →
   `conceptual evolution`; fails → **take the next candidate in lift order and repeat step 4;
   once the list is exhausted → `novel concept`**.

Every verdict carries a one-sentence justification in `uwagi`; for `renaming` and
`conceptual evolution`, the predecessor is recorded.

## 5. Second coder and agreement

Second coder: **60 terms (21%)**, stratified random sample by **`y₀` epoch** (2005–2012 /
2013–2019 / 2020+ → proportional allocation 6 / 36 / 18) **and n-gram length**. (A stratum on
"predecessor present" was rejected: at 95% coverage it is degenerate.) Same blinded view, same
procedure, no sight of the first coder's codes.

Agreement: **Cohen's κ, threshold ≥ 0.70**, reported alongside raw agreement and weighted κ
(five categories of markedly unequal frequency make κ alone unstable; the additional measures
supplement the threshold, they do not replace it). Below threshold: revise definitions, recode
the subsample, report both rounds. Disagreements resolved by discussion; pre-consensus codes
retained.

## 6. Post-coding controls and reporting

1. **Doubling time vs category** (technologies 2–3 years, methodology 8–15) — agreement
   reported; discordant cases discussed individually.
2. **Secondary field definition vs category**: `renaming` / `conceptual evolution` should
   reproduce there more often than `measurement artifact`. This control has value precisely
   because the secondary definition takes no part in coding.
3. **Category distribution by `y₀` epoch**, with a caution flag for `y₀ ≥ 2020`.

**Mandatory scope caveat in the Results:** the category distribution is measured on the 287-term
core — a set **pre-filtered for robustness across four text variants**. The proportion of
artifacts will be low by construction. A sentence of the form "X% of emergences are measurement
artifacts" describes robust emergences, **not** the full set of 7,662 — readers will assume the
wider generalisation unless it is explicitly ruled out.

**`y₀`:** primary-definition value with the secondary-definition value beside it, and a flag
where they differ by more than two years. The two are not averaged: each is correct with
respect to its own definition, and the divergence is an estimate of uncertainty, not a
correction.

## 7. Version history

- **v1.0** (2026-08-27, Polish) — first draft.
- **v1.1** (2026-08-27, Polish) — after VS Code review: substitution-test material added to the
  sheet; lift threshold unified at ≥ 3 and demoted to a search device; two `measurement artifact`
  indicators removed (the secondary-definition indicator broke blinding; the "disappears under
  S2/S3" indicator is empty by construction on the core); step-4 loop closed; second-coder
  stratification changed to epoch × n-gram length; weighted κ and raw agreement added;
  scope caveat added; corpus search restricted to the logged tool.
- **v1.2** (2026-08-27, English) — translation of v1.1. No operational rule changed.
