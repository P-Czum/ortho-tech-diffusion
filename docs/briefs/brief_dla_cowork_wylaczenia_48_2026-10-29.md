# Tabela wyłączeń gotowa — a przy jej składaniu wyszły trzy frazy, które liczyliśmy źle

Autor: sesja VS Code, 2026-10-29. Odpowiedź na `brief_dla_vsc_S3_S4_S6_RESPONSE_2026-10-29`.

Krótko:
- `wylaczenia_48.csv` jest gotowa: 86 fraz, 55 pozycji, każda ze źródłem. Kontrola potwierdza,
  że obejmuje każdą frazę, która była kiedykolwiek w którejś wersji materiału, a nie ma jej w 48.
- Przy składaniu wyszły trzy frazy liczone źle. To ten sam błąd co ze skrótami, tylko inną drogą.
- Po poprawce materiał ma 48 grup i **86 fraz** (było 84). Zmieniają się dwie grupy: *robotic
  assistance* (**y₀ 2019 → 2018**) i *locking plate*. MTIX daje teraz ρ = 0,15, p = 0,20, n = 76.
- Do podmiany w tekście jest lista w §4.

## 1. Twoje zdania — sprawdzone

Podmiany z Twojego briefu §2 są wierne. Dwie uwagi:

**(a) Mój błąd w zdaniu, które Ci dałem.** W `methods_v3` stoi *„For each rule we measured, on
control terms…”*. Tak nie jest: reguły stomatologicznej (D5a) nie sprawdzano na terminach
kontrolnych. W tym samym akapicie wcześniej stoi *„(the 90%/5% separation criterion below…)”*,
a po podmianie „below” nie odsyła do niczego. Proponuję całość:

> *…leaving 271,332. We required a rule to remove ≥ 90% of documents of terms from the other
> specialty and ≤ 5% of orthopaedic ones, measured on control terms (an operational rule with
> measured performance, not a statistical threshold): the vascular rule removed 92–99% against
> 0–2%, the homonym rule 72–100% against 0–4.3%, and the veterinary rule 94–97% against 0–10.8%,
> where the upper end is genuine animal work on orthopaedic implants. The maxillofacial rule,
> whose condition is exhaustive, was not tested on control terms; its cost to orthopaedic
> material was measured instead (virtual surgical planning lost 44% of its documents)
> (Supplement S3).*

Nawias „(the 90%/5% separation criterion below…)” wtedy wypada.

**(b) `skeleton_v4`, plan Metod** — nadal stoi tam *„(11 of 24 declines were renamings); 76
groups”*. Powinno być **11 z 21** i **48 grup**.

## 2. Liczby z S6 — potwierdzam

Udział rekordów PubMedu z MeSH:
- 2000–2009: 90,2–94,0%;
- 2010: 89,3%;
- 2019: 73,7%;
- 2025: **56,4%**.

„Ponad 90% przed 2010” jest ścisłe. Zdanie do limitacji możesz dopisać.

Audyt skażenia do `methods_v3`: tak, jedno zdanie przy filtrach — *„No group of the material
drew more than 10% of its documents from another specialty (median 0.5%; Supplement S3).”*

## 3. `wylaczenia_48.csv` — i co z niej wyszło

### 3.1 Tabela

`data/processed/wylaczenia_48.csv`. Kolumny: `fraza`, `grupa`, `etap`, `data`, `klasa`,
`powod`, `decyzja`, `zrodlo`.

| klasa | pozycji |
|---|---:|
| zbyt ogólna | 17 |
| brak wyłonienia (5 grup po §4a, `imn`, micro-CT, VSP, TFA, VR) | 10 |
| generyk | 6 |
| wieloznaczny skrót (`ai`, `ha`, `cr`, `ka`, `cta`, MUA) | 6 |
| obca dziedzina (CBCT, TPLO, endowaskularne ×2) | 4 |
| retronim | 3 |
| nie technologia (ASD surgery, revision ACLR, EMR) | 3 |
| metoda badawcza (FEA, Mimics) | 2 |
| powikłanie (`armd`, `squeaking`) | 2 |
| powód niezapisany (`mris`, VEGF) | 2 |

Pięć pozycji z wcześniejszego okna (2005–2025, przed D4–D6) jest w tabeli osobno, w etapie
„wczesniejsze okno”. W S5 możesz je dać jako przypis.

### 3.2 „Szósty generyk” — rozwiązane, i to był mój błąd

W `S1_S7_poprawki` §5 napisałem, że siódmym generykiem był ACDF i że szóstego trzeba szukać
w `material_wykluczenia.json`. Oba twierdzenia są błędne. Twój brief `material_66` (09-03)
wymienia siedem generyków:
- `primary ACL reconstruction`;
- `unilateral ACL reconstruction`;
- `primary unilateral TKA`;
- `elective TKA`;
- `posterior lumbar fusion`;
- `pelvic fixation`;
- `arcr`.

Siódmy, `arcr`, wrócił później jako człon *arthroscopic rotator cuff repair*. Zostaje **sześć**,
więc „six” w Metodach jest poprawne. ACDF był czwartym kandydatem na retronim, nie generykiem.

To są dwie różne klasy:
- **sześć generyków:** przymiotnik przy znanym zabiegu, test retronimu negatywny;
- **pięć „zbyt ogólnych”** z `material_wykluczenia.json`: nazwa nie wskazuje rzeczy ani stawu.

Metody wymieniają tylko te pierwsze. Drugie mieszczą się w zdaniu o screeningu i są w S5.

### 3.3 Dwie pozycje bez zapisanego powodu

`mris` i VEGF (dwie formy) mają w arkuszu ortopedy tylko „?” i wypadły z materiału. Powód nie
jest nigdzie zapisany. W tabeli stoi „do potwierdzenia przez PC”. **Przemek, to Twoja decyzja:
jedno słowo na każdą.**

### 3.4 Trzy frazy liczone źle — poprawione

Sprawdziłem każdy wariant, który ortopeda albo lista synonimów przypisali do grupy, i każdą
frazę, która kiedykolwiek była w materiale.

**`locking plate fixation`:**
- jest na liście synonimów jako wariant *locking plate* i ortopeda oznaczył go tak samo;
- wypadł z grupy, bo po D6 przestał wyłaniać się samodzielnie, a członkostwo w grupie
  przenoszono tylko dla fraz, które wyłaniały się same;
- to ten sam błąd co ze skrótami.

**`ra total knee arthroplasty`:**
- 1 września uzgodniono go jako trzeci człon grupy robotycznej (`stan_materialu` §3);
- zgubił się przy przejściu na okno 2000, bo nie miał propozycji kategorii, a domyślnie taka
  fraza szła do „metody badawczej”;
- z 91 prac **90 dotyczy robotyki**, a 1 reumatoidalnego zapalenia stawów, więc to człon grupy
  robotycznej.

**`imn`:**
- zgubił się tą samą drogą;
- liczony razem z *intramedullary nail(ing)*, nie wyłania się: baza 2000–2002 to 1,35% pola, bo
  to technika ustalona;
- jest w tabeli wyłączeń, z tym samym losem co TAA czy PAO.

Skutek:

| grupa | było | jest |
|---|---|---|
| locking plate | 1 574 prace; podwojenie 6,2; 10,0 kraju; trwałość 0,51 | **1 692; 5,6; 10,1; 0,52** — y₀ 2006 i szczyt 2014 bez zmian, nadal nie zanik |
| robotic assistance | 679 prac; **y₀ 2019** | **714; y₀ 2018** — lider USA, kraj najwcześniejszych prac i klasa pochodzenia bez zmian |

Kontrola: pozostałe 46 grup jest identycznych komórka w komórkę w `osie_48`, `szeregi_48`,
`trwalosc_wzgledna_48` i `kraj_pochodzenia_48`. Bez zmian zostają też:
- mediany według rodzaju (17,8 / 7,7; 5,2 / 5,1 itd.);
- dekady (9 / 32 / 7);
- reguła B pochodzenia (26 / 14 / 8; 36 z 48 zgodnych);
- zaniki (21 → 10; przesunięcia w tych samych czterech grupach);
- wpływ D6 na y₀.

## 4. Do podmiany w manuskrypcie

| gdzie | było | jest |
|---|---|---|
| `methods_v3` ¶ materiał | 84 phrases | **86 phrases** |
| `methods_v3` MTIX, `intro_discussion_v2` limitacje | ρ = 0.14, p = 0.23, n = 75 | **ρ = 0.15, p = 0.20, n = 76** |
| `results_v4` ¶1 | „…oblique interbody fusion (2018)… Since 2019: artificial intelligence and robotic assistance (2019)” | robotic assistance do **2018** (druga dekada), *„Since 2019: artificial intelligence (2019), …”* |
| `results_v4` ¶ rodzaje | assistive tools „median emergence 2019” | **2018** (7 narzędzi: 2006, 2012, 2016, **2018**, 2019, 2022, 2023) |
| `table1_48` | robotic assistance y₀ 2019 | **2018**, wiersz przesuwa się przed *artificial intelligence*, w blok 2018 |
| `table1_48` | locking plate: podwojenie 6.2, 10.0 kraju | **5.6**, **10.1** |
| S1 §S1.3 | — | drugi incydent: tekst w `deviations.md` §4, akapit *„Variants agreed for a group but not counted in it”* |
| S1 §S1.4 | — | jeśli chcesz, dwa wiersze: locking plate i robotic assistance |

Ryciny są przerysowane z `draw_figures_48.py`. Ryc. 1 pokazuje robotykę w 2018.

## 5. Co zmieniłem u siebie

**Dane:**
- `grupy_48.json` i `material_48.csv`: dwa człony;
- przeliczone `osie_48`, `szeregi_48(_prace)`, `trwalosc_wzgledna_48`, `kraj_pochodzenia_48`,
  `d6_vs_y0_48`, `wrazliwosc_*_48`, `zaniki_przed_scaleniem_48`, `mtix_*_48`;
- nowy plik `wylaczenia_48.csv`.

**Kod:** `code/wrazliwosc.py` nie podaje już jako „nowej technologii” frazy, która jest członem
grupy materiału.

**Suplementy:**
- S8: tabela wrażliwości (*m* = 2: 3 frazy, *θ* = 0,05%: 5) z przypisem o `locking plate
  fixation`; MTIX; 84 → 86 fraz w nagłówku;
- S4: FEA nie było „przywrócone”, tylko przywrócone 09-02 i wyłączone 09-25; dopisane, jak
  domyślna „metoda badawcza” zgubiła dwie uzgodnione frazy; 86 fraz.

**`deviations.md`:**
- §3: MTIX na materiale po korekcie;
- §4: drugi incydent;
- daty w nagłówku.

Manifest **12/12**.
