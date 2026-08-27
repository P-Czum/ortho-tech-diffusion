# Osie siły i definicja 2 — do oceny

Autor: sesja VS Code, 2026-08-27. Dotyczy: `brief_dla_vsc_po_etapie1_2026-08-27.md`, punkty 4 i 5.

---

## 1. Punkt 4 — osie siły. Jedna korekta kierunku błędu

Arkusz ma 26 kolumn: `data/processed/coding_sheet_full.csv`. Commity `76112fb`, `ac76667`.

### Kierunek obciążenia przy koncentracji autorskiej jest w briefie odwrócony

Brief: *„bez dezambiguacji »Kim J« skleja osoby; to ZANIŻA koncentrację, więc wysoka koncentracja
mimo sklejania jest tym mocniejszym sygnałem"*.

Sklejanie **zawyża** koncentrację. Jeśli dziesięć różnych osób po jednej pracy zlepi się w jedno
`Li J` z dziesięcioma pracami, udział najczęstszego autora rośnie z 10% do 100%, a efektywna
liczba autorów spada z 10 do 1. Wniosek „tym mocniejszy sygnał" nie tylko nie wynika — odwraca
interpretację.

### Gorsze: obciążenie jest różnicowe, nie stałe

Mediana liczności nazwiska pierwszego autora w tym korpusie:

| kraj | mediana | | kraj | mediana |
|---|---|---|---|---|
| Chiny | **15** | | Turcja, Hiszpania, Australia | 2 |
| Korea Płd. | **14** | | Brazylia | **1** |
| Japonia | 6 | | USA, Włochy | 4 |

Termin badany głównie w Chinach wyszedłby na sztucznie skoncentrowany autorsko. Ponieważ
koncentracja krajowa jest **osobną osią**, powstałaby pozorna korelacja między dwiema osiami,
które miały być niezależne. I trafiłoby to dokładnie w najciekawszy przypadek: `3d printing`
ma 48,9% prac z Chin.

### Rozwiązanie: klucz `nazwisko|kraj|instytucja`

Zrównuje rozpiętość międzykrajową mediany z **3,0× do 1,0×**. Instytucja wyciągana z afiliacji
wzorcem (`university|hospital|institute|…`), pokrycie 84,1%.

Własne obciążenie: ta sama osoba zmieniająca instytucję rozpada się na dwie tożsamości, co
**zaniża** koncentrację. To jest kierunek bezpieczny — wysoka zmierzona koncentracja staje się
dolnym oszacowaniem, więc wniosek „to dorobek jednej grupy" broni się tym mocniej. Ten argument
z briefu jest słuszny, tylko dla innego klucza niż zaproponowany.

### Kraj: zgodnie z briefem, wyłącznie z `aff1`

`MedlineJournalInfo/Country` to kraj **czasopisma** — praca z Seulu w czasopismie amerykańskim
miałaby tam „United States". Pokrycie rozpoznania kraju z afiliacji: **87,1%** (5,8% rekordów
bez afiliacji, 7,1% z afiliacją bez podanego kraju). Reszta wypada z mianownika tej osi,
odsetek raportowany per termin w kolumnie `kraj_brak_pct`, mediana 9,5%.

Dopasowanie **od końca napisu**, bo nazwy krajów bywają w nazwach instytucji: `China Medical
University Hospital, Taichung, Taiwan` → Tajwan, `American Hospital of Paris, …, France` → Francja.

Normalizacja diakrytyków, nazwy narodowe (`España`, `Schweiz`) i skróty prowincji kanadyjskich
dały razem **0,7 punktu** (86,4 → 87,1). Spodziewałem się znacznie więcej; reszta to afiliacje,
które kraju po prostu nie podają, i tego wzorce nie rozwiążą.

### Wynik, którego nie zakładaliśmy: czas podwojenia rozdziela kategorie

| technologie | lata | | metodologia | lata |
|---|---|---|---|---|
| robotic assisted | **2,1** | | systematic review | 8,0 |
| 3d printing | **2,2** | | cohort | 8,2 |
| augmented reality | **2,5** | | database | 10,7 |
| robotic, machine learning | **2,9** | | registry | **14,9** |

Technologie podwajają udział w 2–3 lata, metodologia w 8–15. To jest **ilościowy** odpowiednik
rozróżnienia, które §8 przypisuje ręcznie — nadaje się na kontrolę zgodności kodowania,
niezależną od osądu kodera. Do rozważenia jako element kodeksu.

### Drugi wynik: druk 3D jest zjawiskiem regionalnym, robotyka nie

| termin | kraj dominujący | udział | efektywna liczba krajów |
|---|---|---|---|
| `3d printing` | **Chiny** | **48,9%** | **3,9** |
| `3d printed` | Chiny | 35,0% | 6,1 |
| `machine learning` | USA | 44,8% | 4,1 |
| `robotic` | USA | 34,2% | 5,9 |
| `augmented reality` | USA | 24,9% | 9,0 |
| `patient specific` | USA | 27,3% | 9,2 |

Na 287 terminów krajem dominującym jest USA w 177, Chiny w 97.

Koncentracja autorska jest wszędzie niska (0,1–1,8% dla najczęstszego autora, efektywna liczba
w setkach i tysiącach). **Żaden z tych terminów nie jest dorobkiem jednej grupy** — to też jest
wynik, i to taki, który warto podać wprost, bo bez niego czytelnik zakłada odwrotnie.

## 2. Punkt 5 — definicja 2

`def2_text.parquet`: **281 261 rekordów** z 137 czasopism, 2005–2025. Tekst złożony z ekstrakcji
def1 (268 383, ponowne użycie) plus **150 048 dociągniętych**. Zero braków tekstu.
Commit `5761578`.

### Rdzeń odtwarza się w 75,6%

**217 z 287** terminów rdzenia wyłania się również w def2, mimo że Jaccard między definicjami
wynosi tylko 0,31. Definicje różnią się **składem rekordów**, ale zgadzają się co do tego,
**co wschodzi**. To jest mocniejszy wynik, niż się spodziewałem po tak niskim pokryciu.

### Ale rok wyłonienia jest wrażliwy na definicję

| zgodność `y₀` | liczba | udział |
|---|---|---|
| identyczny | 76 | 35% |
| różnica 1–2 lata | 86 | 40% |
| **różnica > 2 lata (flaga)** | **55** | **25%** |

Mediana różnicy: 1 rok. Ale co czwarty termin ma `y₀` rozbieżne o więcej niż dwa lata.
Skrajny przypadek: **`augmented reality` — 2019 w def1, 2023 w def2**.

To ma bezpośrednią konsekwencję dla pracy. `year of emergence` jest w §4 nazwany „osobną,
użyteczną zmienną", a produkt z §9 podaje go w tabeli. Jeśli jest definicyjnie zmienny w 25%
przypadków, **musi być raportowany z przedziałem albo z flagą**, nie jako punkt. Porównanie
międzydefinicyjne jest tu jedynym dostępnym oszacowaniem tej niepewności.
Zapis: `data/processed/def2_y0_comparison.csv`.

### Terminy wyłaniające się wyłącznie w def2 — 1505, ale nieciekawe

Czołówka: `january`, `december`, `explore`, `to explore`, `from january`, `length of stay`,
`registered`, `library`. To jest szablon abstraktu z **innego miksu czasopism** — def2 zawiera
opisy przypadków, edytoriale i prace nieproceduralne, które mają inne konwencje pisania
(„from January 2015 to December 2020").

Jeden wyjątek warty odnotowania: **`length of stay`** (y₀=2016, 2,38%) — to jest realny temat
ortopedyczny, który nie dostaje deskryptorów **proceduralnych**, bo dotyczy organizacji opieki,
nie techniki operacyjnej. Dokładnie ta klasa, o której pisałeś („to, co żyje w czasopismach
ortopedycznych, ale nie dostaje deskryptorów proceduralnych").

### Technologie w obu definicjach

| termin | def1 | def2 | `y₀` def1 → def2 |
|---|---|---|---|
| 3d printing | TAK | TAK | 2014 → 2016 |
| robotic | TAK | TAK | 2020 → 2019 |
| machine learning | TAK | TAK | 2019 → 2018 |
| patient specific | TAK | TAK | 2015 → 2014 |
| augmented reality | TAK | TAK | 2019 → **2023** |
| **navigation** | **nie** | **nie** | — |

`navigation` nie wyłania się w **żadnej** definicji. To jest niezależne potwierdzenie tezy
z §8.1: nawigacja w tym oknie już istniała, a robot ją wchłonął.

## 3. Do rozstrzygnięcia

1. **`y₀` jako punkt czy przedział?** Przy 25% rozbieżności powyżej dwóch lat opowiadam się
   za raportowaniem `y₀` z zakresem międzydefinicyjnym.
2. **Czas podwojenia jako kontrola kodowania** — czy wpisujemy do kodeksu jako sygnał
   pomocniczy przy rozróżnianiu technologii od metodologii?
3. **`length of stay` i klasa podobnych** — czy def2-only zasługuje na osobną, krótką tabelę,
   czy wystarczy zdanie w dyskusji?

## 4. Uwaga o kolejności — rejestracja

Kodowanie tych 287 terminów jest następnym krokiem merytorycznym, a §8 nazywa je „walidacyjnym
rdzeniem pracy" z κ. **Kodeks musi być prerejestrowany przed kodowaniem**, inaczej κ i rozkład
kategorii są post hoc.

Aparat jest zamknięty i zmierzony. Brakuje wyłącznie **definicji operacyjnych pięciu kategorii**
i protokołu kodowania: co odróżnia `renaming` od `conceptual evolution`, jakie dowody z tytułów
wystarczają, ile terminów koduje druga osoba, jaki próg κ i co przy jego niespełnieniu.

Sugerowana kolejność: kodeks → rejestracja (szablon dla analiz danych wtórnych, bo dane już
istnieją) → dopiero kodowanie.
