# Methods — draft v1
### 2026-09-03 · ⟨…⟩ = to be filled from the re-run on 66 groups

## Data and field

We used the PubMed 2026 annual baseline with daily update files, deduplicated so that the most recent record of each PMID is kept and deleted citations removed. The field was defined as all records indexed to the MeSH descriptor *Orthopedic Procedures* or any of its 56 descendants, published 2000–2025.

The MeSH tree admits four literatures that are not orthopaedics. We identified them one by one — none by a planned test — and removed them at record level: vascular limb salvage entering through *Amputation, Surgical* and *Limb Salvage* (records whose only field descriptors are these and which carry a vascular or diabetic descriptor); maxillofacial surgery entering through five descriptors that also belong to the dentistry subtree; veterinary literature (records tagged *Animals* without *Humans*); and the physical sense of *Traction* (records whose only field descriptor is *Traction* and which carry a digestive, urogenital or ophthalmic descriptor). Together these removed ⟨n⟩ records, 9% of the field, leaving ⟨N⟩. For each rule we measured separation on terms known to belong to each side: 94–100% of documents for foreign terms fell inside the removed set, against 0–2% for orthopaedic terms (Supplement S3). An alternative field definition — 137 journals carrying the NLM Broad Subject Term *Orthopedics* — was kept unfiltered as an independent control.

## Detecting emergence

From each title and abstract we extracted noun phrases (spaCy 3.8, `en_core_web_sm`), lower-cased and lemmatised, and counted for each phrase the number of field records containing it in each year. A phrase's *share* is that count divided by the number of field records that year.

A phrase was counted as emerging in the first year in which its share reached at least five times its mean share over 2000–2002 and at least 0.1% of the field (with at least five papers), and remained above that level for three consecutive years. Because three confirmatory years are required, no phrase can emerge after 2023. Detection was run on three text variants — all records; records with an abstract; English-language records — and a phrase entered the candidate set only if it emerged in all three. This yielded ⟨1,294⟩ candidate phrases.

We had preregistered this detector on word n-grams rather than noun phrases (OSF ⟨DOI⟩). The registered analysis did not work: 80% of the registered 287-term core were fragments of abstract boilerplate or names of study designs rather than technologies, and agreement between the human coder and a second, model-based coder on the registered five-category scheme was κ = 0.44 against a preregistered threshold of 0.70. We replaced n-grams with noun phrases under a two-part criterion set before the run (boilerplate absent from the top 50; the robotics family reduced from eight rows to at most three) and abandoned the five-category coding. All results below are exploratory. The registration, the failed analysis, and the eleven deviations from it are reported in Supplement S1.

## Defining the material

An orthopaedic surgeon (PC) screened the candidate phrases. A phrase was retained as a *technology* if it named a device, implant, material, computational method, or operative or periprocedural technique, and excluded if it named a research method, outcome measure, score, disease entity, complication, patient characteristic, or aspect of care organisation. A language model proposed a category for each phrase; the surgeon's adjudication is the record (Supplement S4). Drugs (seven phrases) were retained as technologies by definition but analysed separately, because they diffuse without the training and capital constraints that shape surgical techniques.

Abbreviations were merged with their full forms, or excluded where no single expansion accounted for a clear majority of their documents (`ai`, `ha`, `cr`, `ka`). Merging matters: the share of a term's documents that use only the abbreviation changed by up to 5 percentage points per year over the window, so an abbreviation left as a separate row would have an incomplete series and a distorted year of emergence. Variants of one technology (*3D printing* / *3D printing technology*; *kyphoplasty* / *balloon kyphoplasty*) were merged by a fixed synonym list.

Three phrases were removed as retronyms — names given to an existing standard only when a rival appeared (*single bundle* after double-bundle reconstruction; *anatomic total shoulder arthroplasty* after reverse arthroplasty; *mechanical alignment* after kinematic alignment) — and seven as generic descriptions of established procedures. A retronym is an emergence of a name, not of a technique: the detector measures language, and language and technology part company exactly when competition appears. The retronyms are reported in Table 4 rather than discarded, because they are the clearest demonstration that specialist review is not optional in this method. The final material comprised **66 technology groups** ⟨61 after the merges in the naming review, pending⟩.

## Measuring spread, growth, and persistence

For each group, over all papers from its year of emergence onward: the share of papers from the leading country, author, and journal, and the *effective number* of each (the inverse Herfindahl index, 1/Σpᵢ²), which equals the number of equal-sized contributors that would produce the observed concentration. Country was taken from the first author's affiliation only; it was missing for a median of 9% of papers per group (maximum ⟨…⟩). Authors were keyed by surname, country, and institution.

*Doubling time* is ln 2 divided by the slope of log-share from the year of emergence to the peak year; it was not computed where the peak came less than two years after emergence or fewer than three years of growth were available (⟨n⟩ groups). *Peak share* is the maximum annual share. *Persistence* is a technology's share in a window after its own peak, divided by its peak share, for windows 1–3, 3–5, and 5–7 years after the peak year; a technology whose share fell below half of peak was counted as a decline. Windows are anchored to each technology's own peak rather than to calendar years, because technologies that peaked in 2007 and in 2020 are at different points of their cycles in any given calendar year.

## Classifying evidence state

For each declining group, the surgeon classified the state of clinical evidence at the time of decline from published guidelines, systematic reviews, and registry reports into three states: evidence against use; question unresolved; evidence for use with adoption into routine care. Two groups fitted neither (attention shifted to a specific alternative; the technology was absorbed into a successor) and are reported as such. Classification was performed with knowledge of the persistence values; ⟨an independent blinded re-classification is/was …⟩.

## Indexing discontinuity

MEDLINE moved to automated indexing (MTIX) in 2022. We tested whether this affected the ranking: the number of descriptors per field record fell from 13.1 (2018) to 8.7 (2022) and recovered to 12.5 (2025), and descriptor composition shifted from general to specific terms, but a group's exposure to gaining or losing descriptors did not predict its deviation from trend (Spearman ρ = 0.14, p = 0.36, n = 43). The ranking was retained unchanged; the discontinuity is reported in Limitations.

## Reporting

Measurements describe attention in the published literature. They are not measurements of clinical use, and where the two are distinguished in this paper — a technology withdrawn from practice versus one that stopped being written about — the distinction rests on external sources named in Table 3, not on the curves. Code and derived tables are at ⟨repository⟩; abstracts are not redistributed (courtesy of the U.S. National Library of Medicine).
