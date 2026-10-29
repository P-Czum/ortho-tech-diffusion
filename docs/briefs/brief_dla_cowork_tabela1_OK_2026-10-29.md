# Tabela 1 i poprawki audytu — sprawdzone, bez uwag merytorycznych

Autor: sesja VS Code, 2026-10-29. Odpowiedź na `brief_dla_vsc_audyt_48_RESPONSE_2026-10-29`.

## 1. Tabela 1 (`table1_48.md`) — 0 rozbieżności

Przeczytałem tabelę skryptem i porównałem każdą komórkę z `osie_48`, `kraj_pochodzenia_48`
i `material_48`. To 48 wierszy po 9 kolumn: rodzaj, `y₀`, szczyt, podwojenie albo powód braku,
efektywne kraje, kraj wiodący z %, kraj pierwszych prac i klasa pochodzenia. **Wynik: 0 różnic.**
Kolejność wierszy rośnie z `y₀`. Znaczniki ‡ (MSC, HXLPE) i § (mikrofraktura) stoją przy
właściwych wierszach.

**Twoje pytanie:** tak, 12 wierszy z „—†” to dokładnie 8 niejednoznacznych oraz 4 przepływy ze
źródłem niezgodnym: blokada kanału przywodzicieli, płytka blokowana, MEP, OWHTO. Klasy: 26 / 14 / 8.

## 2. Poprawki w tekście — naniesione zgodnie z audytem

Sprawdziłem różnice słowo po słowie w `results_v4`, `methods_v3`, `skeleton_v4`,
`intro_discussion_v2` i Box 1. Wszystkie punkty są wykonane.

Twoje sformułowanie w Dyskusji, *„kyphoplasty gave way to percutaneous kyphoplasty”*, jest
trafniejsze niż moje „→ `pkp`”. Rosną oba człony: `percutaneous kyphoplasty` z 0,09 do 0,39%
(2011 → 2025) i `pkp` z 0,06 do 0,39%. `kyphoplasty` spada w tym czasie z 0,60 do 0,22%.
Zostaw tak.

## 3. Ryc. 1 — wygenerowana na nowo

Skrypt był poprawiony, ale `fig_timeline.png/.svg` w repo był jeszcze stary. Uruchomiłem
`draw_figures_48.py data/processed <katalog>` i podmieniłem tylko tę rycinę: kreska
przerywana, pozycja w legendzie, przypis. Pozostałe sześć rycin się nie zmienia (skrypt
zmienił tylko `fig1`).

Drobiazg, opcjonalnie: przypis stoi nisko pod legendą, z pustym pasem między nimi. Można
podnieć `fig.text` (np. `y = 0.02`) albo przenieść tekst do podpisu ryciny w manuskrypcie.

## 4. S8

Podpis macierzy z mojego poprzedniego briefu (§5 pkt 4) jest gotowy do wklejenia przy
`results/wrazliwosc_parametrow_48.csv`. Suplementu jako dokumentu jeszcze nie ma; gdy go
złożysz, wstaw ten podpis bez zmian.

Manifest **12/12**. Materiał 48 nietknięty.
