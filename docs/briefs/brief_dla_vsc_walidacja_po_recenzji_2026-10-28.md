# Cztery tanie testy walidacyjne po recenzji zewnętrznej (ChatGPT, 2026-10-28)

Autor: sesja Cowork, 2026-10-28. Recenzja w całości u Przemka; tu tylko to, co z niej wynika
dla **tej** pracy (atlas). Praca o metodzie — później, osobno.

**Zasada:** nic z tego nie zmienia materiału 54 ani osi. To są analizy wrażliwości i kontrole,
raportowane obok. Jeśli któraś pokaże, że lista 54 jest niestabilna — zgłoś, nie dostrajaj.

---

## Z1. Macierz wrażliwości parametrów detektora — PRIORYTET

Zarzut: k = 5, θ = 0,1%, m = 3, próg słownika 50 są arbitralne; bez analizy wrażliwości nie wiadomo,
czy atlas opisuje specjalność, czy konfigurację.

Przelicz detekcję (`detect_emergence.py`, okno 2000–2025, pole po D4+D5a+D5c+D6) dla:

| parametr | wartości |
|---|---:|
| k | 3, 4, **5**, 7 |
| m | 2, **3**, 4 |
| θ | 0,05%, **0,1%**, 0,2% |

Pogrubione = obecne. Nie pełny iloczyn — **jeden parametr na raz** przy pozostałych
domyślnych (8 przebiegów). Dla każdego: ile z 54 grup nadal wyłania się; ile **nowych** grup
wchodziłoby (po istniejącym słowniku synonimów i klasyfikacji — nowe nieznane frazy wypisz
osobno, nie klasyfikuj); mediana |Δy₀| dla wspólnych; max |Δy₀| i która grupa.

Wyjście: `results/wrazliwosc_parametrow.csv` + 6 zdań. Próg słownika 50 **nie ruszaj** —
wymaga powtórzenia zliczania; zgłoś jako nieprzetestowany.

## Z2. Trwałość: oznaczenie obserwacji uciętych

Zarzut słuszny i to jest błąd w Tabeli 4: `dual mobility cup` szczyt 2020 → okno +5–7 =
2025–2027, niepełne. Dla każdej z 11 grup i każdego okna: `pelne` / `czesciowe (n lat)` /
`brak`. Grupy ze szczytem 2025 (15) — jawnie poza porównaniem trwałości.

Wyjście: `trwalosc_wzgledna_54.csv` z kolumnami `okno_X_status`. Nie zmieniaj wartości.

## Z3. Zagnieżdżenie wariantów tekstu

Zarzut: S2 (ze streszczeniem) i S3 (angielskie) to podzbiory primary, więc przecięcie jest
filtrem, nie replikacją. Mamy 1 468 wyłonień primary → 1 294 w rdzeniu. Dla **174 odrzuconych**:
w którym wariancie wypadają (S2 / S3 / oba), kategoria wg `np_kategorie_propozycja.tsv` (jeśli
mają), ile z nich to technologie/techniki. Jeśli jakaś technologia wypada przez S3 (nieanglojęzyczna
literatura) — wypisz z nazwą, to jest wynik do ograniczeń.

Wyjście: `results/warianty_odrzucone.csv` + 4 zdania.

## Z4. Czy filtr weterynaryjny (D6) opóźnia y₀?

Nowy punkt, nie widzieliśmy go: technologia bywa najpierw w badaniach na zwierzętach;
`Animals ∧ ¬Humans` usuwa te prace i może **przesuwać wykryte y₀ w późno**.

Dla 54 grup: y₀ na polu **bez D6** (z D4+D5a+D5c) obok obecnego. Rozkład Δy₀; grupy z |Δ| ≥ 2
z nazwą. Spodziewam się efektu przy implantach i materiałach (klasa I) i terapiach biologicznych
(klasa VI).

Wyjście: `results/d6_vs_y0.csv` + 3 zdania. Materiał i osie **bez zmian** — to jest analiza
wrażliwości filtra, nie nowa definicja pola.

## Z5. Dwa drobne sprawdzenia, po jednym zdaniu w raporcie

- Który rok publikacji używamy: `PubDate` drukowany czy elektroniczny (`ArticleDate`)? Jedno
  zdanie do Metod.
- Czy w korpusie są rekordy indeksowane po przejściu na **MTIX 2024** (NLM podaje dwa punkty:
  automatyczne indeksowanie IV 2022, algorytm MTIX 2024)? Nasz test obejmuje 2022; jeśli 2024
  jest w danych, powtórz test H2 (deskryptorów na rekord) z punktem 2024.

## Czego nie robić

- Nie zmieniać parametrów domyślnych, nawet jeśli inny zestaw „wygląda lepiej".
- Nie klasyfikować nowych fraz z Z1 — tylko wypisać.
- Nie dotykać materiału 54, osi, manifestu.

## Format

`brief_dla_cowork_walidacja_RESPONSE_2026-10-28.md`, liczbami. Z1 na początku.
