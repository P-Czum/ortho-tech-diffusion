# Coding manual — emerging terms
## v1.3 (English) · 2026-08-31

**This is a revision, not a translation.** v1.3 changes one operational rule (§2, §4 step 2)
and retires one category (§2, `measurement artifact`). It is a **declared deviation** from the
OSF registration, which cites `coding_manual_v1.2.md` by hash. v1.2 is frozen and untouched;
this file is new. §8 records what changed and why, with the measurements that forced it.

Everything not restated below is unchanged from v1.2 and v1.2 remains the reference for it.

---

## 1. What triggered the revision

Second-coder agreement on the 60-term subsample: **Cohen's κ = 0.442** against a preregistered
threshold of **0.70**; raw agreement 71.7%; 17 disagreements. Brennan–Prediger κ = 0.646, also
below threshold — the conclusion does not depend on the choice of statistic.
(`results/agreement.json`; second coder `openai/gpt-5.6-sol` via OpenRouter, seed 20260827,
prompt hash `522edf5153f20fc6`.)

§5 of v1.2 prescribes exactly this path: below threshold — revise definitions, recode, report
both rounds. This is that revision.

**Eleven of the seventeen disagreements are two things, not seventeen.**

- **Six**: human `non-technological term`, model `novel concept` — `tranexamic acid`,
  `local infiltration analgesia`, `cephalomedullary`, `medial open wedge`, `pericapsular`,
  `lateral lumbar`. Both readings comply with the letter of v1.2 §2, which names "device,
  material, computational or operative technique" and settles neither a drug nor a
  periprocedural technique. This is a definitional gap, addressed in §2 below.
- **Five**: human `non-technological term`, model `measurement artifact` — `study from`,
  `in individual with`, `at minimum`, `development and validation`, `fracture a finite`.
  These are n-gram fragments, not terms; the dispute is about how to file rubbish, not about
  what the rubbish means. Addressed by the change of unit, not by definition (§8.3).

## 2. Technology — positive and negative definition

Replaces the parenthetical in v1.2 §4 step 2 and governs `non-technological term` in §2.

> **A technology** is an artefact or a specified technique that mediates diagnosis or treatment:
> a device, a material **together with its active substance**, a computational method, or an
> operative or periprocedural technique.
>
> **The following are not technologies**: research methodology, statistics, reporting
> convention, care organisation, **disease entity, complication, and outcome measure**.

The negative clause carries most of the work. In v1.2 the four positive items functioned as a
**stop rule**: anything outside the list had one obvious destination. Widening the positive
side without a matching negative side would have reopened the question at every row and left
nothing to close it with — and `non-technological term` holds **229 of 287 (79.8%)** of the
first coder's output, so the boundary being disputed is the one that carries the material.

**A term outside the technology definition is still coded and still reported.** "Not a
technology" is a classification, not an exclusion: disease entities and complications remain in
the material and in the results as their own stratum. What the negative clause forbids is
counting them **as technologies**.

## 3. Drugs are technologies, but they are not this paper's material

**Definition.** A drug is a technology. This is not a concession: health technology assessment
defines "health technology" to include medicines alongside devices, procedures and organisational
programmes, and the founding study of medical-innovation diffusion — Coleman, Katz and Menzel's
1966 work on tetracycline — is a study of a drug. Excluding drugs from the *definition* would
exclude the canonical case. §2 therefore names "a material together with its active substance",
and the six κ disagreements that turned on this point are settled: `tranexamic acid` and
`local infiltration analgesia` are technologies.

**Scope.** This paper's material is nevertheless restricted to the **device and technique
strata**: devices, materials, implants, imaging, computational methods, and operative and
periprocedural techniques. **55 terms** on the current phrase material (21 devices and
computational methods, 34 operative techniques).

The reason is mechanistic, not definitional. A drug diffuses by prescription: no learning curve,
no capital outlay, no training bottleneck, no ceiling set by the number of competent operators.
A device or an operative technique diffuses under all four constraints. A paper that claims
something about *how* surgical innovation spreads cannot put both in one table without the claim
dissolving. The drug stratum is 7 terms — too few to carry inference on its own, and enough to
blur the main one.

**Reporting.** The drug stratum is reported as a **contrast**, not dropped: it is the purest case
of diffusion in the material, because the technology is already finished and what the curve shows
is adoption alone. Tranexamic acid dates from the 1960s; its `y₀` of 2015 is the year
orthopaedics reached for it, not the year it was invented. Read against the device curves, it
shows what a competence barrier does to a diffusion curve by showing a curve that has none.

Strength axes are reported separately for drugs in any case: first-author and country
concentration measure something different for a generic substance with no owner than for an
implant tied to one manufacturer.

## 4. `measurement artifact` is retired

**Zero observations in 287** on the human coding; the model used it 5 times in 60, and all five
of those uses fell on n-gram fragments that do not arise under phrase chunking.

The category is removed from the decision tree. **This is a finding to be reported, not
housekeeping**: either the conjunction in v1.2 §2 was too strict for a human reading the
material, or the artifacts had already been removed before the sheet was frozen (three found in
Stage 1, `ml` = millilitres among them). Both readings are stated in the Results; the zero is
not silently dropped.

Step 1 of the decision tree is deleted; steps renumber 1–3.

## 5. Decision tree (revised)

1. Is the referent a technology, per the positive **and** negative definition in §2?
   → NO: `non-technological term`, **recording which negative-clause item applies**
   (methodology / statistics / reporting convention / care organisation / disease entity /
   complication / outcome measure), stop.
2. Is there a predecessor with a matching referent, on the list or found manually with the
   tool from v1.2 §1? → NO: `novel concept`, stop.
3. Substitution test: bidirectional → `renaming`; unidirectional → `conceptual evolution`;
   fails → next candidate in lift order and repeat; list exhausted → `novel concept`.

The sub-label required in step 1 is new. Without it `non-technological term` absorbs 80% of the
material into one undifferentiated bin, and the distribution of categories — which v1.2 §2
declares a primary finding — says nothing.

## 6. Agreement (revised)

**Weighted κ is dropped from the required reporting.** v1.2 §5 requires it but supplies no
weight matrix, and with five nominal categories there is no natural ordering from which weights
could follow; inventing one after the fact would be choosing a statistic to fit a result.
**Brennan–Prediger κ replaces it**, as the standard answer to the instability that same
sentence describes. Both κ Cohen and κ Brennan–Prediger are reported with raw agreement.
Threshold unchanged at **0.70 on Cohen's κ**.

**Round two is run on the phrase core, not on the n-gram set, and as a census rather than a
sample.** Tuning the manual against a unit already measured to fail would be fitting the
instrument to the material. Five of the seventeen disagreements disappear by the change of unit
alone, since those fragments do not arise under chunking.

## 7. What is unchanged

§1 (material and blinding, including the three post-coding controls the coder must not see),
§3 (lift as a search device, threshold ≥ 3), the substitution test, §6 of v1.2 (post-coding
controls, the mandatory scope caveat, the treatment of `y₀` under two definitions).

The blinding rule stands and applies with more force after the E1 incident: doubling time,
concentration axes and secondary-definition results stay closed until coding is complete.

## 8. Version history and deviation record

- **v1.0 / v1.1** (2026-08-27, Polish), **v1.2** (2026-08-27, English) — see v1.2 §7.
- **v1.3** (2026-08-31) — first revision of an operational rule after registration.
  Declared deviation. Three changes:
  1. **Technology redefined** (§2): drugs and periprocedural techniques admitted; explicit
     negative clause added. Forced by 6 of 17 disagreements falling on a gap in v1.2 §2 that
     both coders read defensibly.
  2. **`measurement artifact` retired** (§4). Forced by 0/287 observations.
  3. **Weighted κ replaced by Brennan–Prediger** (§6). Forced by v1.2 requiring a statistic
     without supplying the weight matrix it needs.
  Plus one procedural change: round two on the phrase core as a census (§6).

  **Not changed, deliberately**: the 0.70 threshold, the blinding rule, the lift threshold,
  the substitution test. Revising any of those in the same pass as a failed agreement result
  would be indistinguishable from tuning until the number passes.
