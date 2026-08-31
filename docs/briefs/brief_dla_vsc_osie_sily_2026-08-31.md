# Brief dla VS Code — osie siły dla mapy klinicznej (96 pozycji) i kontrola metal-on-metal

Autor: sesja Cowork, 2026-08-31. Poprzedni: `brief_dla_cowork_frazy_rzeczownikowe_RESPONSE_2026-08-28.md`.

## 1. Stan wyjściowy

Twój brief z 28.08 zamknął pytanie o jednostkę: **frazy wygrywają** i wiadomo, że rdzeń 47
to skutek progu w S1, nie jednostki.

Od tego czasu, po stronie Coworku, bez liczenia niczego nowego na korpusie:

- **Rdzeń bez S1 = 813 fraz** (primary ∩ S2 ∩ S3). Decyzja D1 w `docs/protocol/scoping_log.md`,
  wpis z 2026-08-31, wraz z kosztem (32 gołe liczebniki, 3,9%) i kontrolą przeciwko naciąganiu.
- **Klasyfikacja wszystkich 813** na 11 kategorii — `data/processed/np_kategorie_propozycja.tsv`.
  Propozycja modelu; ortopeda rozstrzyga w `code/mapa_ui.html`. Decyzja D2.
- **Sklejenie skrótów** — `data/processed/np_synonimy.tsv`, 125 par.
- **Mapa kliniczna: 96 pozycji** (rozpoznanie / technika / technologia / lek, po sklejeniu):
  `data/processed/np_mapa_propozycja.csv`, kolumny `kategoria`, `wariant_do`, `na_mapie`.

Pliki wejściowe do zadań poniżej są w repo. Tabele `emerging_np_*` w `D:/medline_2026/parsed`.

## 2. Kolejka

### Z1. Osie siły dla 96 pozycji mapy — to jest właściwy pomiar z planu v0.4

Do tej pory mamy dla każdej frazy tylko `y0`, `prevalence_2021_2025` i `peak_share`. Plan v0.4
przewiduje osie siły, których nigdy nie policzyliśmy dla jednostki frazowej:

- **koncentracja**: udział czołowego autora, kraju i czasopisma; liczby efektywne = 1/HHI.
  Klucz autora `surname|country|institution`, kraj **wyłącznie z `aff1`**, nigdy
  z `MedlineJournalInfo/Country`.
- **czas podwojenia** udziału po `y0`.
- **udział szczytowy** i rok szczytu (są, ale przelicz spójnie na tym samym mianowniku).

Wejście: `data/processed/np_mapa_propozycja.csv`, wiersze z `na_mapie == True` i pustym
`wariant_do` (96). Wyjście: `data/processed/np_osie_sily.csv` + `results/np_osie_sily.json`.

### Z2. Kontrola metal-on-metal — krzywe roczne, nie agregaty

Wypisz pełne szeregi `y2005…y2025` (udział, nie liczby bezwzględne) dla:
`mom total hip arthroplasty`, `metal debris`, `adverse local tissue reaction`,
oraz dla kontrastu `3d printing` i `robotic assisted total knee arthroplasty`.

Pytanie do rozstrzygnięcia liczbami: czy MoM ma **kształt wejścia i wycofania** (wzrost, szczyt,
spadek do poziomu tła), czy tylko niski ogon. Jeśli tak, detektor widzi wycofania technologii,
a nie tylko wejścia — to osobne twierdzenie i trzeba je udokumentować, zanim padnie w tekście.
Wyjście: `results/mom_kontrola.json` + wykres, jeśli to tanie.

### Z3. Zliczenie klasy śmieci, którą wpuszcza D1

W 813 policz: (a) frazy będące wyłącznie liczbami, (b) frazy zawierające samodzielny token
liczbowy, (c) ile z nich wpada do 96 mapy klinicznej po klasyfikacji z `np_kategorie_propozycja.tsv`.
Spodziewam się (a)=32, (b)=60, (c)=0. Jeśli (c) > 0 — wypisz je, to błąd mojej klasyfikacji.

### Z4. Relacja rdzeń 47 ⊂ mapa 96

Ile z 47 rdzenia trafiło na mapę kliniczną, ile odpadło i do jakich kategorii. Kolumna
`w_rdzeniu_4` jest już w `np_mapa_propozycja.csv`. To jedna tabelka, ale wejdzie do metod.

## 3. Kontrole, które muszą przejść

| kontrola | oczekiwane |
|---|---|
| manifest zamrożonych plików | **12/12** |
| `coding_sheet_koder_CODED_*.csv` | nietknięty, w `.gitignore` |
| wierszy w `np_mapa_propozycja.csv` | 813 |
| `na_mapie == True` i pusty `wariant_do` | **96** |
| suma kategorii | 813 |
| kraj w Z1 | z `aff1`, nie z `MedlineJournalInfo` |

## 4. Czego NIE robić

- **Nie ruszać progu ≥ 50** ani definicji wyłonienia. D1 zmienia tylko to, które warianty
  współokreślają rdzeń.
- **Nie poprawiać klasyfikacji** w `np_kategorie_propozycja.tsv`. To plik do rozstrzygnięcia
  przez ortopedę; jeśli widzisz błąd — zgłoś w raporcie, nie popraw.
- **Nie dopisywać reguły na gołe liczebniki.** Zgłoszona w §6 Twojego briefu, świadomie
  nieprzyjęta; Z3 ma ją tylko zmierzyć.
- Nie dotykać dwunastki zamrożonej rejestracją.
- Nie oceniać list merytorycznie — od tego jest ortopeda.

## 5. Format raportu

`docs/briefs/brief_dla_cowork_osie_sily_RESPONSE_2026-08-31.md`. Liczbami, krótko, z pełnymi
komunikatami błędów. Dla Z2 — szeregi dosłownie, bez interpretacji.
