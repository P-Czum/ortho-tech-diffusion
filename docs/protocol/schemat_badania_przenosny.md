# Schemat badania — wersja przenośna
### 2026-10-28 · wyprowadzony z projektu ortopedycznego (2026-08-25 → 10-28) · do zastosowania w innej specjalności bez odtwarzania decyzji

**Pytanie, na które schemat odpowiada:** które technologie wyłoniły się w piśmiennictwie
danej specjalności w zadanym oknie, kiedy, skąd, kto je bada — i ile z „wyłonień" to nazwy,
a nie technologie.

**Czego schemat nie mierzy:** wdrożenia klinicznego. Mierzy uwagę piśmiennictwa. To zdanie
ma paść w pierwszym akapicie każdej pracy z niego.

**Role:** analityk (potok) + **jeden specjalista z danej dziedziny** (punkty decyzji D3–D6).
Bez specjalisty schemat zwraca listę nazw.

---

## Przebieg — osiem kroków, sześć punktów decyzji

| krok | co | stałe / do powtórzenia | wyjście | kontrola |
|---|---|---|---|---|
| **0. Definicja pola i okna** | poddrzewo MeSH *albo* lista czasopism NLM; okno obserwacji; lata bazy | **D1** — decyzja specjalisty: które poddrzewo, które okno | lista deskryptorów z numerami drzew; `N` rekordów | druga, niezależna definicja pola zachowana jako kontrola, **niefiltrowana** |
| **1. Korpus** | PubMed baseline + updatefiles, MD5, deduplikacja „ostatni wygrywa", `DeleteCitation` | stałe | `analytic_index`, tekst pola | liczba rekordów = suma po latach |
| **2. Audyt skażenia pola** | dla każdego deskryptora: rekordy wchodzące **wyłącznie** przez niego → próbka tytułów → sondy; dla podejrzanych reguła na współwystępowaniu MeSH (lub znacznik NLM, np. `Animals ∧ ¬Humans`); **test rozdzielczości** na terminach obu stron | **do powtórzenia w każdej dziedzinie** — wycieki są inne | reguły D4…Dn, listy PMID, % pola usunięty | reguła przyjęta tylko przy ≥ 90% obcych / ≤ 5% własnych; **D2** — specjalista zatwierdza każdą regułę |
| **3. Jednostka** | frazy rzeczownikowe (spaCy), lematyzacja, próg słownika ≥ 50 wystąpień; trzy warianty tekstu (wszystkie / ze streszczeniem / angielskie) | stałe; **nie** n-gramy, **nie** wariant tytułowy jako filtr rdzenia | `noun_chunks`, `terms_*` | kontrola na zdaniu testowym: fraza wielowyrazowa wychodzi w całości |
| **4. Detekcja wyłonień** | Box 1: baza, próg max(k·baza, θ), y₀ z m latami potwierdzenia; rdzeń = przecięcie trzech wariantów | stałe parametry: b = 3, k = 5, θ = 0,1% i ≥ 5 prac, m = 3 | lista kandydatów z y₀, szczytem, udziałami rocznymi | ile kandydatów to gołe liczebniki (spodziewane 3–4%) — zgłosić, nie filtrować |
| **5. Klasyfikacja** | model proponuje kategorię (11 klas: technologia, technika, lek, rozpoznanie, skala, wynik, parametr, czynnik, organizacja, metoda, artefakt); **specjalista rozstrzyga** — jego plik jest zapisem | schemat klas stały; granica „technologia" = *zastosowanie u chorego* (narzędzie badawcze wypada, AI w diagnostyce zostaje) | `kategorie.tsv` z kolumną `ocena_specjalisty` | **D3** — specjalista; raportować liczbę zmian wobec propozycji modelu |
| **6. Nazwy** | (a) skróty 2–3-literowe: rozwinięcia na tytułach, bez dominanty → wypada; **nigdy osobny wiersz obok pełnej formy**; (b) słownik synonimów i wariantów → grupy; (c) **retronimy**: nazwa standardu po pojawieniu się rywala (rywal obecny ≥ 5 prac wcześniej) → poza materiałem, do osobnej tabeli; (d) generyki (ogólne nazwy zabiegów) → poza | reguły stałe; słownik **do powtórzenia** | `synonimy.tsv`, `grupy.json`, `retronimy.csv`, materiał N grup | **D4** — specjalista; raportować: ile pozornych zaników znika po scaleniu (tu 10 z 22) |
| **7. Osie** | koncentracja (1/HHI kraj/autor/czasopismo, kraj z `aff1`), nadreprezentacja wobec tła, czas podwojenia, trwałość **względem własnego szczytu** (+1–3, +3–5, +5–7), pochodzenie dwiema miarami, ten-sam-kraj / przepływ | stałe | `osie.csv`, `trwalosc_wzgledna.csv`, `kraj_pochodzenia.csv` | osie policzone **raz**, po zamrożeniu materiału; test nieciągłości indeksowania (MTIX) raz na korpus |
| **8. Raport** | atlas (tabela N wierszy), ryciny 0–6, tabela retronimów, zaniki opisowo z kontekstem, rejestr odstępstw, ograniczenia jako zmierzone własności | stałe | manuskrypt | **D5** — specjalista: kontekst zaników ze źródeł zewnętrznych; **D6** — zakres pracy (które warstwy wchodzą) |

---

## Punkty decyzji — co rozstrzyga specjalista i co ma zapisać

| | decyzja | zapis |
|---|---|---|
| **D1** | poddrzewo MeSH, okno, lata bazy | powód wyboru; alternatywna definicja pola |
| **D2** | każda reguła skażenia: przyjąć / odrzucić | liczba usuniętych, rozdzielczość, co zostaje świadomie (tu: `transfemoral amputation`, onkologia) |
| **D3** | technologia czy nie, dla każdego kandydata | plik z oceną; zmiany wobec propozycji modelu |
| **D4** | scalenia, retronimy, generyki | tabela retronimów; liczba zaników przed/po scaleniu |
| **D5** | kontekst każdego zaniku | źródła; **jawnie**: czy klasyfikowano znając krzywe |
| **D6** | zakres pracy: które warstwy (urządzenia/techniki; leki; rozpoznania) wchodzą | decyzja zakresowa, nie wymuszona pomiarem — tak oznaczona w rejestrze |

---

## Czego nauczyliśmy się kosztem — lista do przeczytania przed startem

1. **N-gramy nie są jednostką znaczenia.** 80% zarejestrowanego rdzenia nie nazywało technologii. Od razu frazy.
2. **Wariant tytułowy nie ocenia, tylko obcina** (słownik 1 882 wobec 25 419). Nie używać go do definicji rdzenia.
3. **Pole przez poddrzewo MeSH przecieka** — tu 9% (naczyniowe, stomatologia, weterynaria, homonim). Znalezione czterema przypadkami; w nowej dziedzinie zrobić krok 2 systematycznie, deskryptor po deskryptorze.
4. **Skrót jako osobny wiersz zniekształca y₀** — udział skrótu zmienia się w czasie (−5 do +3 pp/rok). Scalać albo wyrzucać.
5. **Retronimy wyglądają jak wyłonienia.** Trzy na 57; w każdej dziedzinie będą.
6. **Okna kalendarzowe trwałości porównują różne punkty cyklu.** Tylko względem własnego szczytu.
7. **Scalenie zmienia wniosek o zanikach**, nie tylko liczebność (22 → 11).
8. **Okno obserwacji przesuwa martwe pole, nie usuwa go** — technologie sprzed okna i te o wzroście stopniowym są niewidoczne. Powiedzieć, nie przepraszać.
9. **Nieciągłość indeksowania sprawdzić, nie zakładać** (MTIX 2022: realna, bez wpływu na ranking — ale to trzeba zmierzyć na każdym korpusie).
10. **Model klasyfikuje, specjalista rozstrzyga** — i cztery razy w jednej sesji analityk przebrał obserwację o piśmiennictwie za wniosek o medycynie. *Pomiar pokazuje wzorzec uwagi; rozstrzyga rzecz.*
11. **Stałe importowane między modułami są niebezpieczne**, gdy okno przestaje być stałe. Zakres lat jako jawny parametr każdego skryptu.
12. **Zaślepienie łamie się raz.** Nie liczyć niczego dla kodera, zanim skończy.

---

## Koszt (orientacyjnie, z tego projektu)

Korpus i ekstrakcja: dni (pobranie ~68 GB; ekstrakcja fraz 25 min na 270 k rekordów). Audyt
skażenia: 1–2 dni analityka + godzina specjalisty. Klasyfikacja i nazwy: pół dnia modelu,
2–4 godziny specjalisty na ~1 300 kandydatów. Osie: minuty. **Czas specjalisty jest wąskim
gardłem i nie da się go zastąpić.**

## Co wziąć z repozytorium bez zmian

`code/`: `medline_fetch`, `medline_extract`, `medline_dedup`, `mesh_tree`, `extract_noun_phrases`,
`count_noun_phrases`, `detect_emergence`, `merge_and_axes`, `kraj_pochodzenia`, `strength_axes_np`
— wszystkie z zakresem lat jako parametrem. Narzędzia specjalisty: `mapa_ui.html` (builder
`build_mapa_ui.py`). Dokumenty: Box 1 (`box1_definitions_and_figures.md`), `coding_manual_v1.4.md`
§2 i §4a, ten schemat. **Nie brać:** reguł D4–D6, słownika synonimów, listy klas technologii —
to jest do powtórzenia.
