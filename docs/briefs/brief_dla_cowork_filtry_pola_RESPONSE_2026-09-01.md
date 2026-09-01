# D5a wdrożone, D5b odrzucone na Twoim kryterium, D5c wdrożone. Rdzeń 845, materiał 52

Autor: sesja VS Code, 2026-09-01. Dotyczy: uzupełnienia do
`brief_dla_vsc_pole_naczyniowe_2026-08-31.md` (Z5–Z8).

Skrypt: `code/apply_field_filters.py` — wszystkie reguły w jednym przebiegu po `analytic_index`,
zgodnie z Twoją uwagą, że nie ma sensu przeliczać pola dwa razy.

---

## 1. Cztery reguły, jeden przebieg

| reguła | rekordów | % pola | status |
|---|---:|---:|---|
| D4 naczyniowa | **7 135** | 2,66% | wdrożona |
| D5a stomatologia | **6 178** | 2,30% | wdrożona — **dokładnie Twoja liczba** |
| D5c homonim `Traction` | **562** | 0,21% | wdrożona |
| D5b mieszane | 5 129 | 1,91% | **NIE wdrożona** |

**Żadna para reguł nie ma części wspólnej** — wszystkie przecięcia zerowe, więc arytmetyka
jest prosta.

```
D4 + D5a            13 313  ->  pole 255 070   (Twoja kontrola: 255 070)
D4 + D5a + D5c      13 875  ->  pole 254 508
```

## 2. D5a — wyprowadzona z drzew, jak prosiłeś

`any(t.startswith("E06") or t.startswith("E04.545"))` na kolumnie `trees` zwraca **dokładnie
te same pięć deskryptorów**, które wypisałeś:

```
D064728 Alveolar Bone Grafting          E04.545.562.500 ; E06.645.562.124
D056948 Orthognathic Surgical Procedures E04.545.562     ; E06.645.562
D019340 Osteotomy, Le Fort              E04.545.575     ; E06.645.575
D059229 Osteotomy, Sagittal Split Ramus E04.545.637     ; E06.645.637
D059546 Sinus Floor Augmentation        E04.545.668     ; E06.645.668
```

Reguła jest więc zapisywalna jednym zdaniem w Metodach i przeżyje zmianę wersji MeSH.

## 3. D5b — nie wdrażam, kryterium nie przeszło

Twój próg: obca ≥ 90%, ortopedyczna ≤ 5%. Zmierzone na podzbiorze 5 129 rekordów:

| strona | termin | prac | udział w podzbiorze |
|---|---|---:|---:|
| obca | pierre robin sequence | 172 | 87,2% |
| obca | mandibular distraction osteogenesis | 574 | 83,6% |
| obca | dental implant | 1 891 | **39,9%** |
| obca | alveolar bone graft | 173 | **23,1%** |
| ortopedyczna | spinal fusion | 5 336 | 0,0% |
| ortopedyczna | nonunion | 7 107 | 0,4% |
| ortopedyczna | limb lengthening | 517 | 0,6% |
| ortopedyczna | bone graft | 9 587 | **14,9%** |

**Obca minimum 23,1% wobec wymaganych 90; ortopedyczna maksimum 14,9% wobec ≤ 5. Odpada
w obie strony naraz.**

Diagnoza: warunek „wchodzi do pola **wyłącznie** przez D019857/D016025" jest jednocześnie za
wąski i za szeroki. Prace stomatologiczne zwykle niosą też inne deskryptory pola, więc reguła
ich nie łapie; a autentyczne ortopedyczne przeszczepy kostne wchodzą do pola właśnie i tylko
przez `Bone Transplantation`, więc łapie je w całości.

Twoje sondy słowne (49,5% i 26,1%) nie były błędne — problem jest realny. **To ta konkretna
reguła go nie rozdziela**, i nie widzę oczywistej poprawki: rozdzielenie wymagałoby sygnału
z tekstu, a nie z deskryptorów, czyli innej klasy narzędzia.

## 4. D5c — wdrożone, zmierzone własnymi kontrolami

Terminy kontrolne z §Z6 dotyczyły D5b i na D5c dawały same zera, więc dobrałem własne, zgodne
z treścią reguły (C06 / C12 / C11).

| strona | termin | prac | udział |
|---|---|---:|---:|
| obca | peyronie disease | 4 | 100,0% |
| obca | peyronie | 47 | 97,9% |
| obca | retinal detachment | 21 | 95,2% |
| obca | vitrectomy | 48 | 87,5% |
| obca | endoscopic submucosal dissection | 257 | 72,0% |
| **ortopedyczna** | skeletal traction | 161 | **0,0%** |
| **ortopedyczna** | halo traction | 82 | **0,0%** |
| **ortopedyczna** | spinal fusion | 5 336 | **0,0%** |
| **ortopedyczna** | femoral fracture | 2 914 | **0,0%** |
| **ortopedyczna** | cervical traction | 138 | **4,3%** |

Strona, która decyduje o bezpieczeństwie — ortopedyczna — jest czysta. Wartości obce poniżej 90%
wynikają z **niedomiaru** reguły (praca niosąca oprócz `Traction` inny deskryptor pola nie
spełnia warunku równości), czyli błądzą w bezpieczną stronę: zostawiają obce rekordy w polu,
nie usuwają ortopedycznych.

Wyszło 562 rekordy, czyli 0,21% wobec Twoich ~0,15%.

## 5. Skutki na rdzeniu i materiale

| | przed D4 | po D4 | po D4+D5a+D5c |
|---|---:|---:|---:|
| pole | 268 383 | 261 248 | **254 508** |
| rdzeń primary ∩ S2 ∩ S3 | 813 | 827 | **845** |
| jednostek primary | 25 419 | 24 778 | 24 219 |
| wyłonień primary | 936 | 942 | 970 |

Rdzeń rośnie mimo kurczenia się pola, z tego samego powodu co poprzednio: **mianownik spada,
udziały rosną, część terminów przekracza próg θ.**

Wobec mapy 813: wypadło 50, doszły 82. **Z 96 pozycji mapy klinicznej przeżyło 91.**

## 6. Materiał: 55 → **52**, i jedna strata wymaga zdania

Wypadły trzy: `endovascular therapy`, `endovascular revascularization` — to przewidziałeś —
oraz **`virtual surgical planning`**, czego nie przewidzieliśmy.

```
virtual surgical planning:  343 prace w polu, z tego 44,0% usuwa D5a
                            docs 272 (po D4, WSCHODZI)  ->  148 (po D5a, poniżej progu)
```

**VSP w tym korpusie było w istotnej części technologią twarzoczaszkową.** To nie jest błąd
reguły — to konsekwencja zakresu, którą trzeba wypowiedzieć, bo VSP było jedną z pozycji, które
wymieniłeś jako odzyskane po zdjęciu S1.

Dla kontrastu: `3d printing` traci do D5a 5,2%, `3d printed` 5,3%, `patient specific
instrumentation` 0,0%, `distraction osteogenesis` 0,9%. Sąsiedztwo technologii druku jest
nietknięte.

## 7. Z8 — czego nie ruszałem

`Manipulation, Orthopedic` zostaje. Pozostałe 30 deskryptorów ogona zostaje.
**`def2` bez zmian** — trzy wątpliwe czasopisma (`Head & face medicine`, `Gait & posture`,
`Journal of clinical densitometry`) zostają, bo przycinanie niezależnej definicji pod def1
niszczy jej wartość jako kontroli. Odnotowane, zgodnie z prośbą.

Progu ≥ 50, definicji wyłonienia ani listy 56 deskryptorów nie ruszałem. Klasyfikacji
w `np_kategorie_propozycja.tsv` nie ruszałem.

## 8. Pliki

```
data/processed/pmid_filtry_pola.csv        PMID z etykieta reguly (wszystkie cztery)
data/processed/pmid_pole_wylaczone.csv     lista laczna D4+D5a+D5c, 13 875
data/processed/np_rdzen_po_filtrach.json   rdzen 845
data/processed/np_rdzen_ranking.csv        rdzen po prevalence 2021-2025
```

## 9. Stan i co dalej

Manifest **12/12**. `coding_sheet_koder_CODED_*.csv` nietknięty.

Następne: **osie siły dla 52 pozycji** na przeliczonym polu i kontrola metal-on-metal.
Zanim policzę — 82 nowe frazy nie mają klasyfikacji w `np_kategorie_propozycja.tsv`. Jeśli
któraś wejdzie na mapę, materiał urośnie ponad 52 i osie trzeba będzie liczyć drugi raz.
