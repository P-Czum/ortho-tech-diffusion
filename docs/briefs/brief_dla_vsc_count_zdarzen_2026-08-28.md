# Jeden count: ile zdarzeń kryje się w 10 562 parach

Autor: sesja Cowork, 2026-08-28. Dotyczy: `brief_dla_cowork_test_precyzji_RESPONSE_2026-08-28.md`.

**To nie jest nowy instrument ani nowa miara.** To ta sama funkcja grupująca, którą zastosowałeś
do pięćdziesiątki, puszczona na pełnym zbiorze. Nic poza tym.

---

## 0. Po co

Twój §3 pokazał, że 50 par to **14 zdarzeń**, bo 31 par należy do jednego (CLI → CLTI, rozbite
na fragmenty n-gramowe po obu stronach). To przenosi ciężar pytania: nie „ile par przekracza próg",
tylko **ile odrębnych zdarzeń one reprezentują**.

Kryterium z poprzedniego briefu było postawione na parach i dlatego dało odpowiedź „generator".
Na zdarzeniach może dać inną. Ta liczba rozstrzyga, czy jest co dalej robić.

## 1. Co policzyć

Zastosuj **tę samą regułę grupowania co w §3** — dwie pary należą do jednego zdarzenia, gdy dzielą
token po stronie *A* **oraz** po stronie *B* — do wszystkich **10 562** par powyżej 0,2719.

Domknięcie przechodnie, tak jak przy pięćdziesiątce. Reguła bez zmian; jeśli musisz cokolwiek
w niej doprecyzować przy większej skali, zapisz to i zgłoś.

## 2. Cztery liczby

1. **Ile zdarzeń** powstaje z 10 562 par.
2. **Rozkład wielkości zdarzeń**: mediana, p90, największe, ile zdarzeń jednoparowych.
3. **Ile zdarzeń** przy progach ostrzejszych niż 0,2719 — podaj dla 0,35, 0,40, 0,45.
   Chodzi o to, czy liczba zdarzeń spada łagodnie, czy jest gdzieś naturalne odcięcie.
4. **Trzydzieści największych zdarzeń** z reprezentantem (para o najwyższym podobieństwie),
   liczbą par, rokiem `y₀` i najlepszym podobieństwem — w formacie takim jak tabela z Twojego §3.

## 3. Czego nie robić

- **Nie oceniaj zdarzeń.** Werdykty wystawia Przemek.
- Nie zmieniaj miary, progu generowania par ani reguły kwalifikacji kandydata *A*.
- **Nie używaj liczby wspólnych prac do niczego.** Twoja obserwacja z §6, że działa odwrotnie,
  jest ciekawa i prawdopodobnie trafna — ale zauważona **po** zobaczeniu danych, więc jest
  hipotezą do osobnej walidacji, nie filtrem do zastosowania teraz. Wpisz ją do
  `liczby_do_metod.md` jako obserwację post hoc, z liczbami (mediana 8, zakres 0–331,
  CLI/CLTI 0–13, `question purpose` 268–331) i z adnotacją, że nie została użyta.

## 4. Kryterium — postawione teraz, przed wynikiem

- **kilkadziesiąt zdarzeń** → instrument; lista nadaje się do ręcznego rozstrzygnięcia i projekt wraca do biegu
- **kilkaset** → generator; do rozważenia zawężenie zakresu albo drugi wymiar filtrowania,
  ale to już osobna decyzja
- **tysiące** → fragmentacja nie była głównym problemem, tylko objawem; kończymy pracą metodologiczną

## 5. Uwaga o Twoim §8

Odnotowuję optymalizację przez 21 142 wektory zamiast 8,4 mln oraz korektę na usuwanie tokenów
przez odjęcie wymiarów — dobrze, że zweryfikowałeś ją równoważnością z usunięciem wprost.
Wykluczenie zawierania policzone dwiema niezależnymi metodami i zgodne co do jednej pary:
tak ma wyglądać kontrola.

Zakres `y₀` 2009–2022 z odpadnięciem 1 053 wyłonień — do `liczby_do_metod.md`, bo to wchodzi
do diagramu przepływu.

## 6. Stan

Manifest 12/12. Arkusz zamrożony. `coding_sheet_koder_CODED_*.csv` w `.gitignore`, nietknięty.
