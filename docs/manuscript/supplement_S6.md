# Supplement S6. Drift of field composition, 2000–2025

The paper measures each technology as a share of the field's records in the same year. A share
absorbs changes that affect a technology's papers and the field equally. It does not absorb
changes in *who* enters the field or *how much text* a record carries. This supplement reports
those changes year by year so that the reader can judge them.

**Table S6.1.** The field by year.
- *Field records (MeSH)*: records indexed to the subtree, before exclusions.
- *Field records (final)*: after the four exclusion rules (S3); the denominator of every share
  in the paper.
- *PubMed with MeSH*: share of all PubMed records of the year that carry any MeSH indexing.
- *Field share of PubMed*: field records (MeSH) ÷ all PubMed records of the year.
- *Descriptors per record*: mean number of MeSH descriptors on a field record.
- *With abstract* and *English*: shares of final field records.

| Year | Field records (MeSH) | Field records (final) | PubMed with MeSH, % | Field share of PubMed, % | Descriptors per record | With abstract, % | English, % |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2000 | 4,997 | 4,550 | 91.6 | 0.940 | 12.53 | 82.7 | 82.4 |
| 2001 | 5,346 | 4,873 | 93.0 | 0.980 | 12.75 | 85.0 | 84.6 |
| 2002 | 5,885 | 5,357 | 93.4 | 1.049 | 12.98 | 84.2 | 84.5 |
| 2003 | 6,313 | 5,750 | 94.0 | 1.073 | 13.09 | 84.0 | 84.3 |
| 2004 | 6,743 | 6,141 | 93.3 | 1.074 | 12.96 | 84.1 | 85.2 |
| 2005 | 7,858 | 7,138 | 93.0 | 1.152 | 12.83 | 85.8 | 86.4 |
| 2006 | 8,366 | 7,640 | 92.8 | 1.187 | 12.77 | 86.3 | 85.9 |
| 2007 | 8,536 | 7,765 | 92.6 | 1.179 | 13.12 | 86.6 | 85.7 |
| 2008 | 9,660 | 8,822 | 91.3 | 1.268 | 13.40 | 86.3 | 85.2 |
| 2009 | 10,264 | 9,351 | 90.2 | 1.294 | 13.84 | 86.7 | 87.3 |
| 2010 | 10,859 | 9,832 | 89.3 | 1.278 | 13.88 | 86.7 | 88.8 |
| 2011 | 11,945 | 10,796 | 87.6 | 1.320 | 13.96 | 87.5 | 89.9 |
| 2012 | 12,071 | 10,870 | 86.1 | 1.276 | 13.74 | 88.9 | 90.9 |
| 2013 | 13,346 | 12,139 | 85.7 | 1.329 | 13.61 | 87.6 | 91.0 |
| 2014 | 13,427 | 12,119 | 83.3 | 1.275 | 13.58 | 88.0 | 91.2 |
| 2015 | 13,515 | 12,325 | 80.3 | 1.233 | 13.44 | 89.4 | 91.9 |
| 2016 | 13,901 | 12,699 | 77.0 | 1.246 | 13.28 | 91.1 | 93.1 |
| 2017 | 14,377 | 13,112 | 75.2 | 1.266 | 13.35 | 91.9 | 93.3 |
| 2018 | 14,390 | 13,155 | 73.9 | 1.226 | 13.14 | 92.0 | 94.7 |
| 2019 | 15,504 | 14,226 | 73.7 | 1.252 | 12.61 | 92.1 | 94.9 |
| 2020 | 16,811 | 15,436 | 71.2 | 1.161 | 11.06 | 91.9 | 95.0 |
| 2021 | 16,018 | 14,685 | 68.2 | 1.033 | 9.63 | 92.7 | 95.1 |
| 2022 | 14,457 | 13,311 | 66.4 | 0.933 | 8.70 | 93.0 | 95.1 |
| 2023 | 13,310 | 12,259 | 63.4 | 0.896 | 9.02 | 92.7 | 95.6 |
| 2024 | 14,817 | 13,479 | 62.0 | 0.956 | 11.73 | 95.6 | 95.7 |
| 2025 | 14,951 | 13,502 | 56.4 | 0.885 | 12.48 | 99.9 | 95.5 |

Sources: `results/mtix_check.json` [`code/mtix_check.py`];
`D:/medline_2026/parsed/terms_d6_{primary,s2_abstract,s3_english}.denom.json`
[`code/count_noun_phrases.py`].

## S6.1 Indexing

**Records without MeSH.** The share of PubMed records carrying any MeSH indexing fell steadily,
from 90–94% before 2010 to 74% in 2019 and 56% in 2025. The likely cause of most of the fall
is PubMed taking in records that MEDLINE does not index. The lowest values (2024–2025) also include recent
records whose indexing is not finished. The field is defined by MeSH, so it contains only indexed
records, and every share in the paper is computed within them. A technology's share is
unaffected as long as its indexed and unindexed papers do not differ in kind. The data cannot
test that assumption.

**Descriptor depth.** Descriptors per field record held at 12.5–14.0 from 2000 to 2019.
- They fell to 8.7 in 2022, when MEDLINE moved to automated indexing (MTIX).
- They returned to 11.7 in 2024 and 12.5 in 2025.

Neither discontinuity moves the paper's results (S8.4):
- a phrase's exposure to the descriptors that gained or lost under MTIX does not predict its
  deviation from trend;
- the set of declines is the same whether it is defined on the 2025 share or on the 2023–2025
  mean.

**Field share of PubMed.** The share rose from 0.94% (2000) to 1.15% (2005), peaked at 1.33%
(2013), and fell to 0.89% (2025). Measured against MeSH-indexed records only, the field's share behaves differently. It rises
from 1.03% (2000) to 1.70% (2019), dips to 1.41% in 2022–2023 (the MTIX years), and recovers to
1.57% (2025). The fall in the share of all PubMed after 2013 therefore reflects the growth of
unindexed records, not a shrinking field. For the window decision (deviation D-3), the share of all PubMed was the
measure. Extending the window back to 2000 adds a drift of +23% (2000 → 2005), no larger than
the −23% already inside 2005–2025.

## S6.2 Abstracts and language

- The share of final field records with an abstract rose from 82.7% (2000) to 92.1% (2019).
  The values for 2024–2025 (95.6%, 99.9%) are probably an artefact of incomplete recent years and
  should not be read as a trend.
- The share of English-language records rose from 82.4% (2000) to 95.5% (2025).

Both trends raise the number of noun phrases per record over the window. The detector requires
a phrase to emerge on all records, on records with an abstract, and on English records
(Methods). A phrase whose rise came only from more abstracts, or from fewer non-English records,
would therefore fail one of the subsets (S8.2).
