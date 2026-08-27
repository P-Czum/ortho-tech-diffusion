# Emerging concepts in orthopaedic literature: distinguishing novelty from renaming

Preregistered discovery study of concept emergence in the procedural orthopaedic
literature, 2005–2025, on a local mirror of PubMed/MEDLINE.

**Preregistration:** https://doi.org/10.17605/OSF.IO/59BJ2 (OSF Registries, Secondary Data
Preregistration, 27 August 2026)

---

## The question

Bibliometric studies routinely report "emerging trends" by detecting terms whose frequency
rises. A rising term, however, may mean a genuinely new phenomenon — or the same phenomenon
under a new name. A paper describing a printed surgical guide in 2008 says *rapid
prototyping*; the same paper in 2022 says *3D printing*. A dictionary built on today's
vocabulary measures the change of name and calls it diffusion.

**This study distinguishes the emergence of terminology from the emergence of concepts.**
Terms detected as newly prevalent are coded into five categories — *novel concept*,
*renaming*, *conceptual evolution*, *measurement artifact*, *non-technological term* — with
the discrimination between the first three resting on a substitution test against a
candidate predecessor term.

Orthopaedics is the testbed, not the subject: the method is intended to transfer to any
clinical field.

We measure **scholarly attention in the published literature, not clinical adoption**.

## Pipeline

| step | script | output |
|---|---|---|
| mirror PubMed baseline + updates, verify MD5 | `code/medline_fetch.py` | `*.xml.gz` (not versioned) |
| parse to analytic tables | `code/medline_extract.py` | index + text tables |
| deduplicate PMIDs, honour `DeleteCitation` | `code/medline_dedup.py` | `analytic_index` |
| expand MeSH subtree defining the field | `code/mesh_tree.py` | `data/processed/field_orthopedic_procedures.csv` |
| journal-based second field definition | `code/nlm_broad_subject.py` | `data/processed/journals_orthopedics.csv` |
| extract field text | `code/extract_field_text.py` | field text table |
| canonicalise terms, detect emergence | see `docs/protocol/` | `data/processed/emerging_core.json` |
| build coding sheet | — | `data/processed/coding_sheet_full.csv` |
| coder search tool | `code/coder_search.py` | logged queries |
| model coder | `code/llm_coder.py` | coding output |

Requires Python 3.10+ and `requirements.txt`. The model coder reads its API key from an
environment variable; no key is stored in this repository.

## Reproducibility

**The reproducible artifact is the pipeline, not a corpus dump.** The assembled full-text
corpus is not redistributed (see *Data* below). Anyone can rebuild an identical mirror from
NLM with `medline_fetch.py` and verify the derived files against the checksums published in
the preregistration and in `docs/protocol/freeze_manifest.txt`.

Twelve files were frozen before coding began — the coding sheet, the coder's blinded view,
the coding manual, the model prompts, the canonicalisation rule lists, the field definition
and the journal list. Their sha256 checksums are recorded in the preregistration, which is
immutable and timestamped.

## Repository layout

```
code/            pipeline and tooling
data/canon/      frozen canonicalisation rule lists
data/processed/  derived tables: term series, coding sheets, field definitions
docs/protocol/   study protocol, coding manual, preregistration, freeze manifest
docs/briefs/     working correspondence between sessions
```

## Data

Source: PubMed Annual Baseline 2026 (`pubmed26n0001`–`n1334`, released 2026-01-30) plus
daily update files, accessed 2026-08-26/27.
https://ftp.ncbi.nlm.nih.gov/pubmed/

**Courtesy of the U.S. National Library of Medicine.**

NLM states that its data "include works of the United States Government that are not
protected by U.S. copyright law but may be protected by non-US copyright law, as well as
abstracts originating from publications that may be protected by U.S. or non-US copyright
law." Accordingly **the assembled corpus, including abstracts, is not redistributed here**.
What this repository contains is derived aggregates — term–year series, coding sheets with
titles, field definitions — together with the code needed to rebuild everything else.

The data in this repository are a snapshot of the 2026 baseline and do not reflect the
current state of PubMed.

## Licensing

| what | licence |
|---|---|
| code in `code/` | MIT — see `LICENSE` |
| documentation in `docs/`, derived data in `data/` | CC BY 4.0 — see `LICENSE-docs` |

Neither licence extends to material obtained from PubMed/MEDLINE.

## Citation

See `CITATION.cff`.
