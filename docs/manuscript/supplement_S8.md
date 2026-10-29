# Supplement S8. Sensitivity of the material to the detector and to the field definition

All numbers refer to the final material of 48 technology groups (84 phrases). Each section names
the file it is read from; the code that produced each file is given in brackets.

## S8.1 Detector parameters

The detector has three parameters: the multiple of the 2000–2002 baseline (*k*, default 5), the
number of consecutive confirmatory years (*m*, default 3), and the absolute floor (*θ*, default
0.1% of field records). The minimum of five papers a year was held fixed. Each parameter was
varied alone, with the other two at their defaults, and the latest admissible year of emergence
was moved with *m* (2025 − (*m* − 1)). Before any variant was run, the re-implemented detector
was required to reproduce, at default parameters, the emergence sets of all three text variants,
the 1,289-phrase core, and the year of emergence and peak year of all 48 groups. It did.

**Table S8.1.** Groups of the material that still emerge under each variant, and the shift in
their year of emergence (y₀) relative to the default.

| Parameter | Value | Groups still emerging (of 48) | Median \|Δy₀\| | Max \|Δy₀\| (group) | Groups lost |
|---|---:|---:|---:|---|---|
| *k* | 3 | 48 | 0 | 8 (mesenchymal stem cells) | — |
| *k* | 4 | 48 | 0 | 5 (mesenchymal stem cells) | — |
| *k* | 7 | 45 | 0 | 6 (motor evoked potentials) | unicompartmental knee arthroplasty, microfracture, mesenchymal stem cells |
| *m* | 2 | 48 | 0 | 8 (highly cross-linked polyethylene) | — |
| *m* | 4 | 44 | 0 | 0 | metal-on-metal THA, MPFL reconstruction, ultrasound guidance, mesenchymal stem cells |
| *θ* | 0.05% | 48 | 1 | 13 (ultrasound guidance) | — |
| *θ* | 0.2% | 27 | 1 | 6 (cervical disc arthroplasty) | 21 groups (listed below) |

*k* and *m* leave the list and the years of emergence unchanged in the median; *θ* sets a lower
bound on the size of literature the atlas can describe (groups lost at 0.2% peaked at 0.13–0.31%
of the field, groups retained at ≥ 0.28%).

Groups lost at *θ* = 0.2%: Latarjet procedure, volar locking plate, PFNA, augmented reality,
cephalomedullary nail, short stem, targeted muscle reinnervation, kinematic alignment,
dual-mobility cup, metal-on-metal THA, PEEK, labral repair, MPFL reconstruction, MIPO,
highly cross-linked polyethylene, ultrasound guidance, Ponseti method, autologous chondrocyte
implantation, double-bundle reconstruction, microfracture, anterolateral ligament reconstruction.

**Phrases that a looser detector would add.** Lowering *k* or *θ*, or *m* to 2, enlarges the
candidate core (1,289 phrases at default). The added phrases were never screened. The only
information about them comes from earlier screening rounds, which had assigned a category to a
few:

| Variant | Core | Added phrases | Previously categorised | Of which technology or technique |
|---|---:|---:|---:|---|
| *k* = 3 | 1,844 | 555 | 24 | 8: CT image, intraoperative fluoroscopy, non-surgical treatment, ORIF, ORIF group, postoperative CT scan, TJR, virtual reality |
| *k* = 4 | 1,502 | 213 | 21 | 8 (same) |
| *m* = 2 | 1,793 | 504 | 13 | 4: CT image, locking plate fixation, non-surgical treatment, ORIF group |
| *θ* = 0.05% | 2,799 | 1,510 | 14 | 6: CBCT scan, locking plate fixation, micro-CT, VEGF (two forms), virtual surgical planning |

Stricter variants (*k* = 7, *m* = 4, *θ* = 0.2%) add no phrases.

Source: `results/wrazliwosc_parametrow_48.csv`, `results/wrazliwosc_nowe_frazy_48.csv`
[`code/wrazliwosc.py --nr 48`].

## S8.2 Phrases removed by the text-variant intersection

A phrase entered the candidate set only if it emerged on all records, on records with an
abstract (S2), and on English-language records (S3). Of 1,461 phrases emerging on all records,
1,289 passed. The 172 removed failed on S2 alone (61), on S3 alone (60), or on both (51).

Only 18 of the 172 had a category from earlier screening, and 7 of those were marked as
technology or technique. All seven are generic descriptions, not named technologies: CT image,
intraoperative fluoroscopy, postoperative CT scan and ORIF (failing S2), and non-surgical
treatment, ORIF group and TJR (failing S3). The other 154 were never categorised. Most are
publication boilerplate and numeric strings (for example *final follow up*, *two group p 0 05*,
*17 male*), which is what the filter was meant to remove.

A reading of the uncategorised names (by the analyst, not adjudicated by the surgeon) finds
seven that name a technique:
- failing S3, so emerging mainly in non-English literature: *vertebroplasty*, *ACCF*, *minimally
  invasive total hip arthroplasty*, *hamstring autograft*;
- failing S2: *robotic system*, *ChatGPT*, *arthroscopic hip surgery*.

None of the seven would change the material. Vertebroplasty, counted with its abbreviation and
variants, does not emerge even on all records: it was already well represented in 2000–2002
and peaked in 2009. Robotics and artificial intelligence are represented by their own groups.

Source: `results/warianty_odrzucone.csv` [`code/wrazliwosc.py`].

## S8.3 The veterinary filter and the year of emergence

The field excludes veterinary records (D6), which also removes preclinical animal studies of
human implants and therapies. To measure the effect on y₀, each group's series was recounted on
the field without D6, keeping the other exclusions, and the detector was re-run.

**Table S8.2.** Groups whose year of emergence depends on the veterinary filter.
Δ = y₀ with D6 − y₀ without D6.

| Group | y₀ (with D6) | y₀ (without D6) | Δ | D6 papers in the group | D6 papers before y₀ |
|---|---:|---:|---:|---:|---:|
| mesenchymal stem cells | 2017 | 2013 | +4 | 173 | 131 |
| minimally invasive plate osteosynthesis | 2014 | 2011 | +3 | 22 | 8 |
| PEEK | 2014 | 2013 | +1 | 37 | 7 |
| autologous chondrocyte implantation | 2006 | 2009 | −3 | 11 | 1 |
| transforaminal lumbar interbody fusion | 2010 | 2013 | −3 | 8 | 3 |
| pedicle subtraction osteotomy | 2010 | 2012 | −2 | 0 | 0 |
| patient-specific instrumentation | 2012 | 2013 | −1 | 2 | 0 |
| microfracture | 2012 | does not emerge | — | 49 | 23 |

The other 40 groups have the same y₀ with and without the filter. The filter delays emergence
where animal work preceded clinical use. It is also the condition under which microfracture
emerges at all: without it, animal studies in 2000–2002 raise the baseline above the level the
clinical literature later reached. The shifts in the other direction do not come from animal
papers. Pedicle subtraction osteotomy has none. The cause is the denominator: the filter removes
about 4% of field records, so groups close to the threshold cross it earlier.

Source: `results/d6_vs_y0_48.csv` [`code/szeregi_grup.py`, `code/wrazliwosc.py`].

## S8.4 Indexing discontinuities

**MTIX, 2022.** MEDLINE moved to automated indexing in 2022. Descriptors per field record fell
from 12.6 (2019) to 8.7 (2022), and the mix of descriptors moved from general to specific terms.
The test asked whether a phrase's exposure to the descriptors that gained or lost under MTIX
predicts its deviation from its own 2015–2021 trend in 2023–2025. It does not: Spearman
ρ = 0.14, p = 0.23, n = 75 phrases. The other 9 of the 84 phrases lack a usable 2015–2021
series. On the earlier version of the material the same test gave ρ = 0.14, p = 0.18, n = 88.

**Second discontinuity, 2024.** Descriptors per record rose to 11.7 in 2024 and 12.5 in 2025,
back to the depth of 2019. Declines are defined on the 2025 share, so they could depend on a
single post-discontinuity year. Defined instead on the 2023–2025 mean share, the set of declines
is identical: the same 10 groups.

Source: `results/mtix_check.json`, `results/mtix_impact_48.json`,
`results/mtix_mechanizm_48.json` [`code/mtix_impact.py`, `code/mtix_mechanizm.py`];
`data/processed/szeregi_48.csv`.
