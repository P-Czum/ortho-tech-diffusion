# `data/processed/` — który plik jest którym rankingiem

Dwa pliki wyglądają jak „tabela pięćdziesiątki" i **nie są tym samym zbiorem**. Notatka istnieje,
bo pomyliliśmy je 2026-08-28 i kosztowało to wstrzymanie kodowania.

| plik | zbiór | w manifeście |
|---|---|---|
| `coding_sheet_koder.csv` | **rdzeń 287**, posortowany malejąco po `prevalence_2021_2025_pct` | tak |
| `emerging_top50_prevalence_PRZED_przesiewem.csv` | top 50 z **pełnych 7 662** wyłonień wariantu `primary` | nie |
| `emerging_top_exceedance.csv` | top 50 z pełnych 7 662 po drugiej osi | nie |

**Ranking na rdzeniu nie jest osobnym plikiem — jest nim kolejność wierszy `coding_sheet_koder.csv`**
(`build_coding_sheet.py` kończy sortowaniem po prevalence). Zweryfikowane: 0 pozycji różnych.

Dwa pliki `PRZED_przesiewem` / `exceedance` to artefakt **kroku 2** porządku z planu v0.8 §5
(detektor → uszeregowanie → przesiew kodeksem → dopiero pięćdziesiątki). Wchodzą do pracy
dopiero po przesiewie, więc nie są wejściem do zamrożenia.

Nazwa `PRZED_przesiewem` jest nasza; `detect_emergence.py` zapisuje natywnie
`emerging_top_prevalence.csv` w katalogu roboczym. Przy odtwarzaniu pipeline'u plik przyjdzie
pod starą nazwą — to ta sama treść.
