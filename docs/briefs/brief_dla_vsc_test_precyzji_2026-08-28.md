# Test precyzji — czy miara jest instrumentem, czy generatorem kandydatów

Autor: sesja Cowork, 2026-08-28. Dotyczy: `brief_dla_cowork_test_kontekstowy_RESPONSE_2026-08-28.md`.
**Ostatni test przed decyzją o projekcie. Nic poza nim nie budujemy.**

---

## 0. Co już wiemy i czego brakuje

Test kontekstowy pokazał, że miara wysoko punktuje dwie pary, o których **z góry wiedzieliśmy,
że są prawdziwe**. To jest czułość na znanych przypadkach — i tyle.

Brakuje liczby odwrotnej: **ile spośród par, które miara sama wskaże jako najwyższe, okaże się
prawdziwymi przemianowaniami.** To jest różnica między instrumentem a generatorem kandydatów
i tego nie da się wywnioskować z poprzedniego testu.

Twoje trzy zastrzeżenia z §5 przyjęte w całości. Najważniejsze z nich jest ilościowe i wchodzi
do tego briefu jako założenie: **para 2 (0,3272) wypadła poniżej najwyższej pary losowej w swoim
rozkładzie (`bone allograft / tissue and`, 0,3549).** Sąsiedztwo tematyczne bije prawdziwe
zawieranie. Dlatego test dotyczy **wyłącznie przemianowania**, gdzie sygnał był czysty
(0,3816 wobec maksimum losowego 0,2719).

## 1. Zakres — zawężony celowo

Rozstrzygamy jedno pytanie dwustanowe: **czy termin wschodzący wyparł poprzednika.**
`conceptual evolution` wypada z zakresu instrumentu — miara go nie odróżnia od sąsiedztwa
tematycznego, i lepiej to powiedzieć, niż udawać.

## 2. Generowanie par — reguła przed liczeniem

Dla każdego terminu wschodzącego *B* (z `emerging_primary`, wariant `primary`):

- **okno późne** dla *B*: cztery lata od `y₀(B)` włącznie;
- **kandydat *A***: termin, którego udział w oknie wczesnym (cztery lata **przed** `y₀(B)`)
  jest istotnie wyższy niż w oknie późnym *B* — proponuję spadek co najmniej o połowę;
- **liczebność**: *A* i *B* muszą mieć po ≥ 30 rekordów w swoich oknach; poniżej wektor mierzy
  rzadkość, nie kontekst — lekcja z Twojej kontroli pozytywnej na sześciu rekordach;
- **wykluczenie**: pary, w których jeden termin zawiera się w drugim jako ciągły podciąg
  (`3d printing` / `printing`). To są warianty zapisu, nie przemianowania, i wpuszczone
  zawyżyłyby precyzję darmowo.

Podobieństwo liczysz tą samą miarą co poprzednio, **bez zmiany parametrów** — `MIN_DF = 50`,
PPMI, tło per-okno, usuwanie tokenów obu terminów.

## 3. Co policzyć

**Pięćdziesiąt par o najwyższym podobieństwie.** Do każdej dołóż to, co pozwala człowiekowi
rozstrzygnąć w kilkanaście sekund:

- szeregi roczne obu terminów,
- `y₀(B)`, liczebności w obu oknach,
- **po pięć tytułów**: z *A* w oknie wczesnym, z *B* w oknie późnym, oraz **wspólnych**, jeśli są,
- podobieństwo i jego percentyl we własnym rozkładzie losowym (jak poprzednio, dobór po liczebności).

Zapis: `data/processed/renaming_candidates_top50.csv`, plus pusta kolumna `werdykt`.

**Nie oceniaj ich.** Werdykty wystawia Przemek — pytanie „czy B wyparło A" jest dobrze postawione
i to jest cała różnica wobec kodowania pojedynczych n-gramów.

## 4. Druga liczba, tania i ważna

Podaj **rozkład podobieństw wszystkich wygenerowanych par**, nie tylko pięćdziesiątki: ile par
w ogóle powstało, mediana, p90, p99, i ile przekracza 0,2719 — czyli maksimum losowe z pary 1.

Jeśli takich par są tysiące, próg nie separuje i miara jest generatorem kandydatów.
Jeśli kilkadziesiąt — jest instrumentem. Tę liczbę chcę zobaczyć **razem** z pięćdziesiątką,
bo ona sama w sobie może zamknąć sprawę.

## 5. Czego nie robić

Nie strojenia progów pod wynik: reguła z §2 i parametry miary stoją w nagłówku skryptu przed
uruchomieniem, jak poprzednio. Nie rozszerzania na `conceptual evolution`. Nie modeli.
Nie interpretowania — zatrzymujesz się na liczbach.

## 6. Stan

`coding_sheet_koder_CODED_*.csv` w `.gitignore` — dobrze, zostaw tak do decyzji.
Manifest 12/12 bez zmian.
