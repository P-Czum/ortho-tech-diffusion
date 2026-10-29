# Supplement S4. Category proposals and the surgeon's adjudication

## S4.1 What was proposed, and by whom

Every candidate phrase received a proposed category from a language model working as the
project's drafting assistant: Claude (Anthropic), in the desktop application. The model version
was not recorded at the time; this is a limitation of the record, not of the procedure. The
proposals are in `data/processed/np_kategorie_propozycja.tsv` (columns `term`, `kategoria`;
643 phrases). They span the candidate sets of successive versions of the material, so the file
is larger than the 84 phrases of the final material.

| Proposed category | Phrases |
|---|---:|
| scale or score | 102 |
| technique | 101 |
| diagnosis | 97 |
| outcome | 96 |
| parameter | 66 |
| organisation of care | 59 |
| technology | 53 |
| factor | 24 |
| artefact | 15 |
| unclear | 15 |
| drug | 10 |
| research method | 5 |

A phrase absent from the file was treated as *research method* and did not enter the material.

## S4.2 The record is the surgeon's

The orthopaedic surgeon (PC) reviewed the proposals in two sheets. Each sheet has, for every
phrase, the proposed category, the surgeon's category, an optional request to merge the phrase
into another (`wariant_do`), an optional rating of the proposal (`trafnosc`), and a free-text
note.

| Sheet | Phrases | Category changed | Merge requests | Rated: apt / doubtful / wrong |
|---|---:|---:|---:|---|
| `ocena_mapy_2026-09-01.csv` | 846 | 0 | 115 | 43 / 7 / 1 (51 rated) |
| `ocena_mapy_nowe_naprawiony.csv` | 506 | 0 | 43 | 30 / 11 / 0 (41 rated) |

The surgeon changed no proposed category. His work went into three other kinds of decision:
- merging variants of one name;
- removing phrases too general to name a specific thing (`material_wykluczenia.json`);
- the final exclusions: ambiguous abbreviations, complications, and the restoration of finite
  element analysis (`material_decyzje_koncowe.json`).

Ratings were given only to phrases proposed as technology or technique: 51 of 80 such phrases
in the first sheet and 41 of 68 in the second. No phrase with another proposed label was rated.
The 73 of 92 rated *apt* therefore describe the model's proposals in the stratum that became
the material, not its precision on the whole list.

## S4.3 What the proposals did not decide

- Membership of the material was decided by the surgeon's definition of a technology (coding
  manual v1.4 §2, S2), not by the proposed label.
- The six kinds were assigned by the surgeon.
- The context of each decline was recorded by the surgeon from external sources (S7).
- The three retronyms were identified from co-occurrence with a rival and confirmed by the
  surgeon from the clinical literature (Methods, Table 3).
