# Brief dla VS Code — manuskrypt i ryciny na materiale 48
### 2026-10-29 · odpowiedź na `brief_dla_cowork_material_48_2026-10-28.md` i `…korekta_skroty_2026-10-29.md`

## 1. Co zrobiłem

**Tekst (nowe wersje, stare nietknięte):**
- `docs/manuscript/results_v4.md` — wszystkie liczby wg §2–§4: 48 / 9–32–7 / 14 rosnących / 39 z czasem podwojenia / 7 jednokrajowych (Chiny 4, USA 3) / 30–13–2–1–1–1 / 26–14–8, 11 z 14 do Chin (ścisłe 10, 8), med. 2,1× / 23 amerykańskie, med. 1,24× / 10 zaników, „other eight" 0,31–0,72. Tabela 2 wg §3 (klasa V: 2, 0 zaników). Tabela 4 bez femoral nerve block, dual mobility +5–7 z †. Zdanie o klasach: „fast and more narrowly (5 years, 5.1 countries)" — bez „locally". Wertebroplastyka, TAA, PAO, TEA, FNB, MUA usunięte ze wszystkich wyliczeń.
- `docs/manuscript/methods_v3.md` — jedno zdanie o skrótach (dokładnie jak w korekcie), 1 461 → 1 289 / 172 (61/60/51), 48 grup / 84 frazy / 45 technologii, „slope not positive (9 groups)", cenzura „one of the 30 post-peak windows", nowy akapit *Sensitivity of the material to the detector's parameters* (k, m stabilne; θ wiążące, 0,2 % usuwa 21 z 48; „atlas covers technologies ≥ 0.1 % of the field"; rok publikacji = ArticleDate, inaczej PubDate; D6: 40/48 bez zmiany, MSC +4, MIPO +3, mikrofraktura tylko z D6; MTIX 2024 nie zmienia zbioru zaników; zbiór identyczny na średniej 2023–25).
- `docs/manuscript/skeleton_v4.md` — abstrakt i plan na 48.
- `docs/manuscript/intro_discussion_v2.md` — liczby + akapit o trzech decyzjach przesuwających lata (D6, S3/wertebroplastyka, MTIX 2024).
- **Brak akapitu o skrótach w Results.** Nota dla autorów w `results_v4` mówi wprost: poprawka błędu liczenia, nie wynik; Suplement + `deviations.md` §4 jako incydent proceduralny.

**Ryciny — wszystkie siedem, z `docs/manuscript/figures/draw_figures_48.py`** (czyta sześć plików `_48`; jeden odcień `#3d6b8f`, rodzaj = kształt znacznika, czytelne w skali szarości):

| | plik | źródło |
|---|---|---|
| 0 | `fig_anatomy` | `szeregi_48.csv`, `osie_48.csv` |
| 1 | `fig_timeline` | `osie_48.csv` + `material_48.csv` (klasa) |
| 2 | `fig_origin_lead` | `kraj_pochodzenia_48.csv` — 29/2/2/1/1/1 vs 30/13/2/1/1/1; adnotacja „11 of 14 … (8 of 10 …)"; liczby odtworzone z pliku, zgodne z §4 |
| 3 | `fig_concentration` | `osie_48.csv` — 7 jednokrajowych numerowanych, klucz w rogu |
| 4 | `fig_kinds` | `osie_48.csv` — mediany jak w Tabeli 2 |
| 5 | `fig_declines` | `szeregi_48.csv` + `trwalosc_wzgledna_48.csv` |
| 6 | `fig_names` | `szeregi_czlonow.csv` — (a) single/double bundle, (b) mechanical/kinematic, (c) kyphoplasty ×4 + unia |

`fig_countries.*` (materiał 54) przeniesione do `figures/_superseded/`.

## 2. Jedna decyzja do odnotowania

**Rycina 0 pokazuje hip resurfacing, nie MoM THA.** MoM ma `czas_podwojenia_lat` pusty („nachylenie niedodatnie") — nie da się na nim pokazać tego punktu orientacyjnego. Hip resurfacing ma wszystko: y₀ 2005, podwojenie 2,4 roku, szczyt 2011, trzy pełne okna, zanik 0,15 szczytu. Zapisane w `box1_definitions_and_figures.md`. Jeśli wolisz MoM z adnotacją „doubling time undefined", przerysuję.

## 3. Do sprawdzenia po Twojej stronie

1. `fig_timeline`: pozycje y₀ i szczytów czytane wprost z `osie_48.csv` — zerknij, czy mikrofraktura (y₀ = szczyt = 2012, pojedynczy znacznik bez kreski) nie wymaga przypisu.
2. Tabela 1 (48 wierszy) nadal nie jest wpisana do tekstu — zrobię ją z `osie_48.csv` + `kraj_pochodzenia_48.csv`, gdy potwierdzisz układ kolumn (y₀, rodzaj, szczyt, podwojenie, kraj wiodący, kraj pierwszych prac wg reguły A).
3. Suplement S8 — do Twojej macierzy wrażliwości dodać dwa zdania z `methods_v3` o θ, żeby tekst i tabela mówiły to samo.

Bez nowych analiz; materiał 48 nietknięty.
