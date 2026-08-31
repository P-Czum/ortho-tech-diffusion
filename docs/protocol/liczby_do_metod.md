# Liczby zmierzone, do wykorzystania w metodach i ograniczeniach

Zbierane na bieżąco, żeby nie trzeba było ich odtwarzać przy pisaniu. Każda z datą pomiaru
i sposobem policzenia.

## Rdzeń a pełna lista (2026-08-28)

Wyłonienia per wariant tekstowy, detektor z §4 bez zmian:

| wariant | kandydatów | wyłonionych |
|---|---:|---:|
| primary (tytuł + streszczenie) | 245 081 | 7 662 |
| S1 (tylko tytuł) | 17 583 | **607** |
| S2 (tylko rekordy ze streszczeniem) | 244 026 | 7 537 |
| S3 (tylko anglojęzyczne) | 228 644 | 7 569 |

`emerging_core.json` = dokładnie przecięcie czterech powyższych = **287**.

**S1 jest filtrem merytorycznym, nie analizą wrażliwości.** Z 41 terminów, które wypadają
z pierwszej pięćdziesiątki `primary` przy przejściu do rdzenia, **wszystkie 41 odrzuca S1**,
a **33 z 41 w ogóle nie istnieją w słowniku S1 — nigdy nie pojawiają się w tytule.**
Szablon streszczenia (`were included`, `95 ci`, `method this`, `result a total`) żyje
w streszczeniach, bo tytuł nie ma sekcji „Methods".

## Rodziny zawierania (2026-08-28)

Zawieranie = ciągły podciąg tokenów, domknięcie przechodnie.

- cały rdzeń 287: **46 grup, 140 terminów uwikłanych**
- pierwsza pięćdziesiątka rdzenia: **8 rodzin, 23 z 50 terminów; po scaleniu 35 odrębnych bytów**

Tabela główna pokazuje 50 wierszy surowych z kolumną przynależności do rodziny — scalanie
zmieniałoby prerejestrowaną regułę §3.1 pkt 6 (próg Jaccarda 0,90).

## Remisy w rankingu (2026-08-28)

`prevalence_2021_2025` = liczba prac 2021–2025 ÷ mianownik wspólny dla wszystkich terminów,
więc **równa liczba prac daje bitowo równą prevalence**. W rdzeniu:

**44 bloki remisowe obejmujące 95 z 287 pozycji; największy blok ma 3 wiersze.**

Kolejność wewnątrz bloku nie wynika z danych. Rozstrzyga ją zamrożona kolejność wierszy
`coding_sheet_koder.csv` — sortowanie stabilne po kolejności wierszy parquet. Każde zdanie
postaci „termin X na pozycji N" musi się do tej kolejności odwoływać, bo powtórny przebieg
z niestabilnym sortowaniem potrafi przestawić sąsiadów w remisie.

Przykład, na którym to wyszło: `virtual reality` leży w remisie pozycji **152–154**
(`secondary analysis`, `virtual reality`, `to sport after` — każdy 292 prace w 2021–2025).
Wiążąca jest pozycja **153** z zamrożonego arkusza.

### Granica pięćdziesiątki nie pada w remisie — obie osie (2026-08-28)

Pytanie pierwszorzędne przy jednej trzeciej rankingu nierozstrzygniętej przez dane: czy cięcie
„50 najsilniejszych" wypada w środku bloku równych wartości. **Nie wypada, na żadnej z osi.**

| oś | wierszy w remisach | wartość na pozycji 50 | granica |
|---|---:|---|---|
| prevalence (kolejność arkusza) | 51 nadmiarowych, 95 uwikłanych w 44 blokach | `limb threatening`, unikalna | ostra |
| exceedance (rdzeń, sort. stabilne) | 11 nadmiarowych | `retrospective observational`, unikalna | ostra |

Uwaga do sąsiedztwa granicy na osi prevalence: remis **jest** tuż obok, ale po właściwej stronie —
pozycje 48 (`cone`) i 49 (`md`) mają bitowo równą wartość. Blok kończy się na 49, pozycja 50 jest
jednoelementowa, więc tabela pięćdziesięciu nie zależy od stabilności sortowania.

Oś exceedance remisuje znacznie rzadziej (276 wartości unikalnych z 287 wobec 236 na prevalence),
bo jest ilorazem dwóch wielkości ciągłych, a nie liczbą prac przez wspólny mianownik.

### Sformułowanie do metod

> Ranking is defined as the row order of the frozen coding sheet. Because prevalence is a count
> divided by a shared denominator, 95 of 287 terms fall into 44 exact ties; a re-run with a
> different sort algorithm would permute neighbours within a tie. All positional statements in
> this paper therefore refer to the frozen sheet, not to a recomputed ranking. On both selection
> axes the boundary of the main table falls on a uniquely-valued position and is unaffected;
> ties are far rarer on the exceedance axis (276 of 287 values unique), which is a ratio rather
> than a count over a shared denominator.

## Pozycje wcześniej etykietowanych technologii (2026-08-28)

**Nie do cytowania jako wynik** — etykiety „technologia" nadano ręcznie w Etapie 1, bez kodeksu
i bez zaślepienia. Wielkość do tekstu jest wynikiem kodowania. Tabela poniżej służy wyłącznie
pokazaniu, że rdzeń przesuwa technologie w górę.

| poz. w pełnych 7 662 | termin | poz. w rdzeniu 287 |
|---:|---|---:|
| 143 | robotic | 28 |
| 159 | patient specific | 30 |
| 357 | 3d printed | 51 |
| 417 | robotic assisted | 58 |
| 557 | machine learning | 80 |
| 854 | 3d printing | 101 |
| 931 | artificial intelligence | 104 |
| 1437 | virtual reality | 153 |
| 2183 | deep learning | 197 |
| 2745 | augmented reality | 220 |
| 2950 | patient specific instrumentation | 228 |
| 6809 | convolutional neural network | poza rdzeniem |

Jedenaście z dwunastu przeżywa przejście do rdzenia.

## Test przemianowania w kontekstach (2026-08-28)

### Zakres okien — do diagramu przepływu

Reguła generowania par wymaga czterech lat przed `y₀` i czterech od `y₀`, więc oba okna mieszczą
się w obserwowanym zakresie 2005–2025 tylko dla **`y₀` w przedziale 2009–2022**. Odpada przez to
**1 053 z 7 662** wyłonień wariantu `primary`; pozostaje **6 609**. Wolałem stracić skrajne
roczniki niż porównywać okna różnej długości.

Reguła daje **8 384 866** par, z czego **13** odrzuca wykluczenie zawierania (jeden termin jest
ciągłym podciągiem tokenów drugiego) — zostaje **8 384 853**. Liczba wykluczeń policzona dwiema
niezależnymi metodami, zgodna co do jednej pary.

### Obserwacja post hoc: liczba wspólnych prac działa odwrotnie — NIEUŻYTA

**Zauważona po zobaczeniu danych, więc jest hipotezą do osobnej walidacji, nie filtrem.**
Nie została użyta do żadnego wyboru ani progu; zapisana, bo jest sprawdzalna na nowym materiale.

W pięćdziesiątce najwyżej punktowanych par liczba prac zawierających oba terminy ma medianę **8**
i zakres **0–331**. Wartości skrajnie wysokie mają pary, które przemianowaniami nie są:
`question purpose` → `ci` **331**, → `95 ci` **315**, → `level iii` **268**. Pary z rodziny
CLI → CLTI, czyli udokumentowanego przemianowania, mają **0–13**.

Kierunek jest odwrotny do intuicyjnego i ma wyjaśnienie: przemianowanie daje wspólne prace **tylko
w wąskim oknie przejściowym**, bo potem stara nazwa znika. Trwałe współwystępowanie w setkach prac
znaczy, że oba terminy żyją obok siebie, czyli nie są tą samą rzeczą. Gdyby użyć liczby wspólnych
prac jako potwierdzenia przemianowania, dostałoby się wynik odwrotny do zamierzonego.

### Reguła grupowania w zdarzenia perkoluje poniżej ~0,40 (2026-08-28)

Reguła: dwie pary należą do jednego zdarzenia, gdy dzielą token po stronie *A* **oraz** po stronie
*B*; domknięcie przechodnie. Na 50 najwyżej punktowanych parach działa poprawnie (14 zdarzeń,
dwie niezależne implementacje zgodne). **Na pełnym zbiorze powyżej 0,2719 załamuje się.**

| próg | par | zdarzeń | największa składowa | rozpiętość A × B |
|---:|---:|---:|---:|---|
| 0,2719 | 10 562 | 767 | 8 899 (84,3%) | 669 × 1615 |
| 0,31 | 3 299 | 423 | 2 309 (70,0%) | 288 × 581 |
| 0,35 | 1 040 | 200 | 451 (43,4%) | 71 × 131 |
| 0,40 | 292 | 65 | 122 (41,8%) | 18 × 21 |
| 0,45 | 78 | 20 | 45 (57,7%) | 9 × 13 |

Przy 0,2719 największa składowa obejmuje 669 terminów *A* i 1 615 *B* z `y₀` od 2009 do 2022,
łącząc CLI/CLTI z metodyką przeglądów Cochrane, bazą NIS i płatnościami pakietowymi. Każde ogniwo
łańcucha spełnia regułę z osobna; sklejka powstaje z domknięcia przechodniego.

**Wskaźnikiem perkolacji jest rozpiętość składowej, nie jej udział w parach.** Udział spada do 34%
przy 0,37 i potem rośnie, bo przy wysokich progach prawie wszystko, co zostaje, jest jednym
prawdziwym zdarzeniem. Rozpiętość spada monotonicznie i przechodzi do rozmiaru wiarygodnego dla
pojedynczego zdarzenia między 0,40 a 0,43.

Konsekwencja: liczba zdarzeń przy niskim progu jest **dolnym oszacowaniem** — składowa połyka
nieznaną liczbę odrębnych zdarzeń. Liczba par takiego zaniżenia nie ma i jest wiarygodna.
