# Test precyzji — miara jest generatorem kandydatów, i to z jednym zastrzeżeniem gorszym niż sama ta liczba

Autor: sesja VS Code, 2026-08-28. Dotyczy: `brief_dla_vsc_test_precyzji_2026-08-28.md`.

Skrypt: `code/renaming_precision_test.py`. Wyniki: `data/processed/renaming_candidates_top50.csv`
(z pustą kolumną `werdykt`), `results/renaming_precision_stats.json`. Reguła generowania par
i parametry miary zapisane w nagłówku skryptu przed uruchomieniem, jak poprzednio.

---

## 1. Odpowiedź na §4 — rozkład wszystkich par

| | |
|---|---:|
| par ogółem | **8 384 853** |
| mediana | 0,0954 |
| p90 | 0,1366 |
| p99 | 0,2047 |
| maksimum | 0,5968 |
| **powyżej 0,2719** | **10 562** |

Twoje kryterium brzmiało: tysiące → generator, kilkadziesiąt → instrument. Wychodzi **10 562**,
czyli **generator kandydatów**.

Podaję też mianownik, bo sama liczba myli: to **0,126% par, jedna na 800**. Próg separuje bardzo
ostro w ujęciu względnym. Problem jest w skali przestrzeni — górne 0,13% z ośmiu milionów to wciąż
dziesięć tysięcy pozycji, o trzy rzędy wielkości za dużo na ręczne rozstrzygnięcie.

## 2. Ale ważniejsze jest to: percentyl saturuje

**Wszystkie 50 par mają percentyl 100,0.** Co do jednej.

To wywraca moją własną uwagę z poprzedniego briefu. Pisałem, że próg globalny 0,2719 jest niesłuszny,
bo pochodzi z rozkładu jednej pary o liczebnościach 108/470, a tło rośnie z liczebnością — i że
percentyle liczone osobno dla każdej pary są uczciwą miarą. **Są uczciwsze, ale bezużyteczne
jako narzędzie rankingu**: na górze rozkładu wszystkie saturują na 100. Nie odróżniają
`critical limb ischemia → limb threatening` od `question purpose → 95 ci`.

Nie ma więc drugiego kryterium do filtrowania czoła listy. Zostaje samo podobieństwo, a ono miesza
typy — o czym niżej.

## 3. Pięćdziesiątka to nie pięćdziesiąt kandydatów, tylko **14 zdarzeń**

Pogrupowałem mechanicznie: dwie pary należą do tego samego zdarzenia, gdy dzielą token po stronie
*A* **oraz** po stronie *B*. To pomiar, nie ocena.

| par | zdarzenie (reprezentant) | y₀ | najlepsze |
|---:|---|---:|---:|
| **31** | `critical limb ischemia` → `limb threatening` | 2021 | 0,5968 |
| 3 | `nationwide inpatient sample` → `regression` | 2019 | 0,4931 |
| 2 | `critical limb ischemia` → `freedom from` | 2022 | 0,5133 |
| 2 | `nationwide inpatient sample` → `comorbidity` | 2019 | 0,5029 |
| 2 | `critical limb ischemia` → `free survival afs` | 2020 | 0,4950 |
| 2 | `question purpose` → `ci` | 2016 | 0,4750 |
| 1 | `restenosis` → `target lesion` | 2019 | 0,4899 |
| 1 | `femoral nerve block` → `canal block acb` | 2019 | 0,4685 |
| 1 | `nationwide inpatient sample` → `insurance` | 2018 | 0,4847 |
| 1 | `question purpose` → `level iii` | 2016 | 0,4844 |
| 1 | `nationwide inpatient sample` → `or 1` | 2018 | 0,4724 |
| 1 | `the nationwide inpatient` → `code` | 2017 | 0,4659 |
| 1 | `cli` → `free survival afs` | 2020 | 0,4655 |
| 1 | `the nationwide inpatient` → `odd ratio` | 2017 | 0,4645 |

**31 z 50 par to jedno zdarzenie.** CLI → CLTI, rozbite na fragmenty n-gramowe: po stronie
wczesnej `cli`, `with cli`, `cli patient`, `patient with cli`, `limb ischemia cli`,
`critical limb ischemia`, `for critical limb`; po późnej `clti`, `with clti`, `clti patient`,
`limb threatening`, `limb threatening ischemia`, `threatening ischemia clti`,
`chronic limb threatening`, `for clti`, `for chronic limb`, `clti and`.

**To jest ten sam problem jednostki analizy, który wywrócił kodowanie ręczne, tylko w nowym
instrumencie.** N-gram nie był jednostką znaczenia przy kodowaniu i nie jest nią przy generowaniu
par. Iloczyn kartezjański fragmentów po obu stronach jednego zdarzenia zajmuje czoło listy.

## 4. Miara znalazła przemianowanie, którego nie było na liście znanych

CLI → CLTI to udokumentowana zmiana nazewnictwa (*critical limb ischemia* → *chronic limb-threatening
ischemia*, wytyczne 2019). Nie podawaliśmy jej miary; znalazła ją sama, z najwyższym wynikiem
w całym rozkładzie ośmiu milionów par. To jest realna czułość na nieznanym przypadku i tego
poprzedni test nie pokazywał.

Drugie zdarzenie tego typu w pięćdziesiątce: `femoral nerve block` → `canal block acb`.

**Werdyktów nie wystawiam** — kolumna `werdykt` jest pusta, zgodnie z §3.

## 5. Trzy typy trafień w tym samym paśmie podobieństwa

Podaję jako obserwację o strukturze listy, nie jako ocenę poszczególnych par.

- **Fragmenty jednego przemianowania** — 31 par.
- **Terminy metodologiczne z jednego rodzaju badań**: rodzina `nationwide inpatient sample` →
  `comorbidity` / `regression` / `insurance` / `odd ratio` / `code` / `or 1`, 9 par. Baza danych
  i jej aparat statystyczny, w tym samym paśmie 0,46–0,50 co CLI/CLTI.
- **Szablon streszczenia**: `question purpose` → `ci`, `95 ci`, `level iii`, 3 pary.

## 6. Liczba wspólnych prac nie rozdziela typów — a intuicyjnie powinna

Mediana 8, zakres 0–331, trzy pary z zerem.

Najwyższe wartości mają pary **niebędące przemianowaniami**: `question purpose` → `ci` ma 331
wspólnych prac, `95 ci` 315, `level iii` 268. Prawdziwe pary CLI/CLTI mają 0–13.

Kierunek jest odwrotny do oczekiwanego i ma sens: przemianowanie daje wspólne prace **tylko
w wąskim oknie przejściowym**, bo potem stara nazwa znika. Trwałe współwystępowanie w setkach prac
znaczy, że oba terminy żyją obok siebie, czyli **nie są tą samą rzeczą**. Gdyby ktoś chciał użyć
liczby wspólnych prac jako potwierdzenia, dostałby wynik odwrotny do zamierzonego.

## 7. Podsumowanie w jednym zdaniu

Miara zawęża osiem milionów par do dziesięciu tysięcy, wynosi na sam szczyt prawdziwe
przemianowanie, którego nie znaliśmy — ale czoło listy to w 62% fragmenty jednego zdarzenia,
percentyl saturuje i nie filtruje, a odrębnych zdarzeń w pięćdziesiątce jest **14**.

Zatrzymuję się tutaj, zgodnie z §5. Decyzja o projekcie należy do Przemka.

## 8. Stan

Manifest **12/12**. Arkusz zamrożony bez zmian. `coding_sheet_koder_CODED_*.csv` nadal
w `.gitignore`, nietknięty.

Uwaga techniczna na wypadek odtwarzania: reguła z §2 daje 8,4 mln par, ale tylko **21 142 różne
wektory** — kwalifikacja kandydata *A* zależy wyłącznie od `y₀`, nie od konkretnego *B*, więc
wszystkie *B* z tego samego rocznika dzielą oba okna. Liczę wektory raz na rocznik i mnożę macierze.
Usuwanie tokenów obu terminów, które zależy od pary i nie daje się wpiąć w mnożenie, realizuję przez
odjęcie wkładu usuwanych wymiarów od pełnych iloczynów, z korektą na część wspólną tokenów —
wynik identyczny z usunięciem wprost.

Zakres `y₀` zawężony do **2009–2022**, żeby oba okna mieściły się w całości w 2005–2025; odpada
przez to 1 053 z 7 662 wyłonień. Wykluczenie zawierania odrzuciło **13 par** — policzone drugą,
niezależną metodą (enumeracja podciągów zamiast macierzy wspólnych tokenów) i zgodne co do jednej.
