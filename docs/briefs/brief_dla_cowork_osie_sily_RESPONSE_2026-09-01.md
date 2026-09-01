# Osie siły dla 52 pozycji i kontrola metal-on-metal

Autor: sesja VS Code, 2026-09-01. Dotyczy: `brief_dla_vsc_osie_sily_2026-08-31.md` (Z1, Z2),
liczone na polu po D4+D5a+D5c.

Skrypt: `code/strength_axes_np.py`. Wyjścia: `data/processed/np_osie_sily.csv`,
`results/np_osie_sily.json`, `results/mom_kontrola.json`.

---

## Z1. Osie siły — 52 pozycje

Materiał: 52, nie 96 ani 55 — po zawężeniu zakresu do warstwy urządzeń i technik oraz po
filtrach pola. Rozkład: **32 techniki, 20 technologii**.

Osie policzone dokładnie wg §2 briefu: koncentracja autora, kraju i czasopisma z efektywną
liczbą 1/HHI; klucz autora `nazwisko|kraj|instytucja`; **kraj wyłącznie z `aff1`**, nigdy
z `MedlineJournalInfo/Country`; czas podwojenia z nachylenia log-udziału od `y₀` do szczytu;
udział szczytowy i rok szczytu przeliczone na mianowniku pola po filtrach.

**Pokrycie kraju: mediana braków 8,5%, maksimum 19,7%.**

### Koncentracja rozdziela materiał bardzo mocno

| termin | kraj czołowy | udział | efektywna liczba krajów | prac |
|---|---|---:|---:|---:|
| percutaneous kyphoplasty | China | **93,7%** | **1,1** | 371 |
| primary hip arthroscopy | USA | 89,0% | 1,3 | 222 |
| percutaneous endoscopic lumbar discectomy | China | 84,0% | 1,4 | 272 |
| anatomic total shoulder arthroplasty | USA | 78,1% | 1,6 | 355 |
| primary total joint arthroplasty | USA | 70,2% | 2,0 | 243 |
| targeted muscle reinnervation | USA | 69,1% | 2,0 | 100 |
| … | | | | |
| patient specific instrumentation | USA | 21,7% | **11,4** | 333 |
| volar locking plate | Japan | 15,2% | 12,2 | 260 |
| mechanical alignment | China | 16,3% | 12,7 | 207 |
| short stem | Germany | 16,7% | 12,8 | 208 |
| cone beam computed tomography | China | 14,6% | **15,6** | 403 |

**Rozpiętość efektywnej liczby krajów: od 1,1 do 15,6.** To jest oś, która realnie rozdziela —
`percutaneous kyphoplasty` z 371 pracami i efektywną liczbą 1,1 oraz `cone beam computed
tomography` z 403 pracami i 15,6 to dwie zupełnie różne historie o dyfuzji, nierozróżnialne
po samej liczbie prac. Dokładnie to, po co ta oś powstała.

### Czas podwojenia — policzalny dla 44 z 52

| termin | podwojenie | y₀ | szczyt |
|---|---:|---:|---|
| femoral neck system | **1,6 roku** | 2022 | 0,275% (2024) |
| primary hip arthroscopy | 1,7 | 2019 | 0,292% (2021) |
| robotic assisted total knee arthroplasty | 1,8 | 2021 | 0,653% (2025) |
| artificial intelligence | 1,9 | 2021 | 0,552% (2025) |
| random forest | 2,0 | 2023 | 0,244% (2025) |
| machine learning | 2,2 | 2019 | 0,384% (2023) |
| percutaneous endoscopic lumbar discectomy | 2,3 | 2016 | 0,264% (2018) |
| machine learning model | 2,4 | 2022 | 0,289% (2024) |

Osiem pozycji bez czasu podwojenia to te, u których szczyt wypada mniej niż dwa lata po `y₀`
albo dodatnich lat jest mniej niż trzy — reguła z oryginalnego `strength_axes.py` bez zmian.

### Wycofania w materiale: trzy pozycje

| termin | 2025/szczyt | rok szczytu |
|---|---:|---:|
| mom total hip arthroplasty | **0,10** | 2018 |
| dual mobility cup | 0,38 | 2020 |
| open wedge high tibial osteotomy | 0,43 | 2019 |

## Z2. Metal-on-metal — detektor widzi wycofanie, ale **nie tam, gdzie się wydaje**

Szeregi dosłownie, udział w procentach pola, mianownik po filtrach:

```
                                    05    06    07    08    09    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25
mom total hip arthroplasty        0.00  0.00  0.00  0.01  0.00  0.02  0.07  0.03  0.06  0.11  0.11  0.11  0.06  0.14  0.05  0.04  0.02  0.03  0.02  0.01  0.01
metal debris                      0.01  0.05  0.02  0.07  0.07  0.09  0.08  0.17  0.15  0.23  0.16  0.20  0.17  0.23  0.12  0.14  0.10  0.09  0.09  0.06  0.07
adverse local tissue reaction     0.00  0.00  0.00  0.00  0.02  0.01  0.03  0.04  0.09  0.18  0.14  0.23  0.15  0.12  0.10  0.11  0.11  0.11  0.05  0.05  0.08
hip resurfacing                   0.10  0.18  0.29  0.70  0.63  0.55  0.63  0.40  0.37  0.19  0.20  0.10  0.13  0.10  0.14  0.09  0.07  0.07  0.06  0.05  0.07
pseudotumor                       0.01  0.05  0.01  0.02  0.03  0.09  0.11  0.10  0.16  0.13  0.17  0.08  0.10  0.10  0.06  0.03  0.07  0.06  0.08  0.04  0.03
3d printing                       0.00  0.00  0.00  0.00  0.01  0.02  0.00  0.01  0.00  0.05  0.05  0.10  0.14  0.19  0.26  0.22  0.25  0.25  0.28  0.25  0.34
robotic assisted TKA              0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.02  0.00  0.00  0.02  0.02  0.03  0.03  0.09  0.14  0.15  0.29  0.33  0.65
```

| termin | y₀ | szczyt | rok | 2025/szczyt |
|---|---:|---:|---:|---:|
| mom total hip arthroplasty | 2014 | 0,140% | 2018 | **0,103** |
| pseudotumor | 2013 | 0,172% | 2015 | 0,167 |
| metal debris | 2012 | 0,228% | 2014 | 0,314 |
| adverse local tissue reaction | 2014 | 0,228% | 2016 | 0,346 |
| **hip resurfacing** | **brak — nie wyłania się** | 0,696% | **2008** | 0,103 |
| *3d printing* (kontrast) | 2017 | 0,344% | 2025 | 1,00 |
| *robotic assisted TKA* (kontrast) | 2021 | 0,653% | 2025 | 1,00 |

**Odpowiedź na Twoje pytanie: kształt wejścia i wycofania jest, i jest jednoznaczny.** Cztery
terminy MoM mają `y₀`, szczyt w środku okna i spadek do 10–35% szczytu. Obie kontrole
kontrastowe mają szczyt w ostatnim roku i iloraz 1,00. To nie jest niski ogon — to inny kształt.

**Ale twierdzenie trzeba postawić słabiej, niż brzmiało pytanie.** `hip resurfacing`, czyli sama
technologia, **nie wyłania się wcale**: jej szczyt to 0,696% w 2008, przy samym brzegu okna, więc
baza 2005–2007 jest już wysoka i detektor nie ma czego wykryć. W naszym oknie widać wyłącznie
jej opadanie.

Detektor nie wykrył więc wejścia i wycofania **technologii**. Wykrył **wyłonienie się słownictwa
jej porażki** — `metal debris`, `adverse local tissue reaction`, `pseudotumor` weszły do
piśmiennictwa dopiero wtedy, gdy zaczęto opisywać powikłania, i to one mają `y₀` w oknie.

Sformułowanie do tekstu, jeśli ma paść: *detektor wykrywa wycofanie technologii wtedy, gdy
wycofanie wytwarza własną, nową terminologię; nie wykrywa go z krzywej samej technologii, jeżeli
ta weszła do piśmiennictwa przed początkiem okna obserwacji.* To jest zarazem ograniczenie okna
2005–2025, warte zdania w Metodach.

## Z3 i Z4

Zaraportowane wcześniej w `brief_dla_cowork_pole_naczyniowe_RESPONSE_2026-08-31.md` i
`brief_dla_cowork_filtry_pola_RESPONSE_2026-09-01.md`: liczebniki (a) 34, (b) 62, (c) 1 =
`covid 19` (fałszywy alarm mojej kontroli), relacja rdzeń 47 ⊂ mapa, oraz skutki filtrów.

## Kontrole z §3 briefu

| kontrola | oczekiwane | wynik |
|---|---|---|
| manifest zamrożonych plików | 12/12 | **12/12** |
| `coding_sheet_koder_CODED_*.csv` | nietknięty, w `.gitignore` | tak |
| kraj w Z1 | z `aff1`, nie z `MedlineJournalInfo` | **z `aff1`** |
| wierszy w `np_mapa_propozycja.csv` | 813 | 813 |
| `na_mapie` bez wariantu | 96 | 96 |

Dwie kontrole liczbowe zdezaktualizowały się przez filtry pola, co raportowałem osobno: z 96
pozycji mapy przeżyło 91, a materiał to 52, nie 55.

## Do rozstrzygnięcia po Twojej stronie

**82 nowe frazy nie mają klasyfikacji** w `np_kategorie_propozycja.tsv` (lista:
`data/processed/np_nowe_po_d4.csv` plus przyrost po D5a/D5c). Jeśli któraś wejdzie na mapę,
materiał urośnie ponad 52 i osie trzeba będzie policzyć drugi raz — to 6,5 minuty, więc nie
jest to argument, żeby tego nie robić, tylko żeby zrobić raz, po rozstrzygnięciu.
