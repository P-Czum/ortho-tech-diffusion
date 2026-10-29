# Supplement S3. Field definition, exclusion rules, and their measured separation

## S3.1 The field

The field is every MEDLINE record, 2000–2025, indexed to at least one of the 56 descriptors in
the MeSH subtree *Orthopedic Procedures* (`data/processed/field_orthopedic_procedures.csv`,
frozen in the registration). The local mirror holds 297,667 such records. Four record-level
rules remove 26,335 of them (8.8%), which leaves **271,332**. No rule changes the subtree: each
one acts on records, and only on records whose field descriptors all point to another specialty.

## S3.2 The rules

*FIELD* is the set of 56 descriptors. A record is excluded if:

| Rule | Condition | Why |
|---|---|---|
| **D4** vascular | its only field descriptors are among *Limb Salvage* (D023821), *Amputation, Surgical* (D000671), *Disarticulation* (D004188), *Hemipelvectomy* (D006428), **and** it carries a vascular or diabetic descriptor (D058729, D016491, D007511, D017719, D014652, D001157, D003920, D048909) | vascular surgery and diabetic-foot literature enters the subtree through amputation and limb salvage |
| **D5a** dental and maxillofacial | all its field descriptors also sit in the MeSH trees E06 or E04.545. The trees give five: *Alveolar Bone Grafting*, *Orthognathic Surgical Procedures*, *Osteotomy, Le Fort*, *Osteotomy, Sagittal Split Ramus*, *Sinus Floor Augmentation* | maxillofacial procedures sit in the subtree. The rule is written on trees rather than descriptor IDs, so it survives a change of MeSH version |
| **D5c** *Traction* homonym | its only field descriptor is *Traction* (D014143), **and** it carries a descriptor from C06, C12 or C11 | *Traction* is also used for gastrointestinal, urological and ophthalmic traction |
| **D6** veterinary | it carries *Animals* (D000818) and not *Humans* (D006801) | veterinary orthopaedics, and preclinical animal studies of human implants and therapies |

Code: `code/apply_field_filters.py`.

## S3.3 Records removed, 2000–2025

| Rule | Records hit | Hit by this rule only | Removed (assigned by priority) |
|---|---:|---:|---:|
| D4 | 7,784 | 7,768 | 7,784 |
| D5a | 6,402 | 6,258 | 6,402 |
| D5c | 573 | 560 | 573 |
| D6 | 11,749 | 11,576 | 11,576 |
| **Total** | 26,508 | | **26,335 (8.8%)** |

D6 overlaps the other rules by 173 records: 16 with D4, 144 with D5a and 13 with D5c. Each
record is removed once.

PMID lists:
- `data/processed/pmid_pole_wylaczone_d6.csv`: the final list of 26,335 records;
- `data/processed/pmid_filtry_pola_d6.csv`: every hit with the rule that made it, including the
  unapplied D5b.

## S3.4 Separation

Each rule was tested before adoption on control terms. For each term, the test measured the
share of its documents that the rule removes. Foreign terms should be removed almost entirely,
orthopaedic terms hardly at all. The criterion, set when D4 was proposed and applied to every rule
after it, was ≥ 90% of foreign and ≤ 5% of orthopaedic documents.

| Rule | Foreign terms (share removed) | Orthopaedic terms (share removed) |
|---|---|---|
| D4 | chronic limb-threatening ischaemia, peripheral artery disease, diabetic foot ulcer, endovascular revascularisation and others: **92–99%** | 3D printing, periprosthetic joint infection, tranexamic acid, direct anterior approach, robotic-assisted TKA, Latarjet procedure: **0.0–2.0%** |
| D5c | Peyronie disease, retinal detachment, vitrectomy, endoscopic submucosal dissection: **72–100%** | skeletal, halo and cervical traction, spinal fusion, femoral fracture: **0.0–4.3%** (cervical traction 4.3%) |
| D6 | cranial cruciate ligament, TPLO, tibial tuberosity advancement, tibial plateau levelling osteotomy: **94–97%** | reverse shoulder arthroplasty, TKA, ACL reconstruction, locking plate: **0.0–5.1%**; PEEK **10.2%**, spinal fusion **10.8%** |
| D5a | not measured on control terms | 3D printing 5.2%, patient-specific instrumentation 0.0%, distraction osteogenesis 0.9%; virtual surgical planning **44.0%** |

**Reading the table:**
- **D4** meets the criterion.
- **D5c** falls short on the foreign side only (endoscopic submucosal dissection, 72%). That error
  is the safe kind: such records stay in the field and are not removed from it.
- **D6** exceeds 5% on the orthopaedic side for PEEK and spinal fusion. These are not
  misclassified records. They are genuine animal studies of orthopaedic implants and fusion
  techniques, which the rule removes by design (Methods; S8.3 gives the effect on y₀).
- **D5a** was adopted without control terms, because its condition is exhaustive: a record goes
  only when every one of its field descriptors is maxillofacial. Its cost to orthopaedic material
  was measured instead. Virtual surgical planning lost 44% of its documents, and with them its
  emergence. In this corpus virtual surgical planning is in large part a craniofacial technology.

## S3.5 A rule that was measured and not applied

**D5b** (mixed dental): the only field descriptors are *Osteogenesis, Distraction* (D019857) or
*Bone Transplantation* (D016025), and the record carries a descriptor from A14 or C07. The rule
would hit 6,286 records (2.1%). It failed the criterion on both sides at once:
- foreign terms as low as 23.1% removed (alveolar bone graft);
- an orthopaedic term at 14.9% removed (bone graft).

It was not applied, so some dental literature remains in the field through these two
descriptors. A lower bound from title probes is ≥ 1.44% of the field. S3.6 measures how much of
it reaches the material.

## S3.6 Audit of the material for foreign-domain content

The rules act on records. A technology could still be described mostly by another specialty, as
cone-beam CT turned out to be: 82.5% of its documents were dental, and it was removed before this
audit was run.

The audit measured, for every group of the final material, the share of its documents carrying a
descriptor from a foreign domain. The domains are the ones the rules were written against:
- dental (A14, C07, E06, E04.545);
- digestive (C06);
- urogenital (C12);
- eye (C11).

Nervous-system, neoplasm and cardiovascular descriptors are reported but not counted as foreign,
because in orthopaedics they are indications: nerve transfer in targeted muscle reinnervation,
myelopathy in ACDF, metastatic fracture.

| | Material 48 |
|---|---|
| Groups above 20% foreign | 0 of 48 |
| Groups above 10% | 0 |
| Median | 0.5% |
| Maximum | 8.6% (ACDF, digestive) |
| Animal-only records | 0.0% in every group |

Source: `data/processed/audyt_skazenia_48.csv` [`code/audyt_skazenia.py`]. The vascular,
maxillofacial, veterinary and homonym leaks were each found by a different, unplanned route;
this audit is the systematic test that now stands behind them.
