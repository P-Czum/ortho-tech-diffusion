# Cztery decyzje wykonane — i jedno znalezisko przy okazji

Autor: sesja VS Code, 2026-08-28. Dotyczy: `brief_dla_vsc_ranking_rozstrzygniecia_2026-08-28.md`.

## 1. `virtual reality` — masz rację, 153

Moje 154 było błędem sortowania, nie danych: rankowałem pełną listę `sort_values()` z domyślnym
quicksortem, a dopiero potem filtrowałem do rdzenia. Przy remisie quicksort przestawia sąsiadów.
Zamrożony arkusz i stabilne sortowanie dają zgodnie **153**.

## 2. Ale powód jest ciekawszy niż pomyłka — i to jest znalezisko do metod

`virtual reality` **leży w trzyelementowym bloku remisowym, pozycje 152–154:**

```
152  secondary analysis    292 prace 2021-2025
153  virtual reality       292
154  to sport after        292
```

Remis jest **bitowo dokładny, nie „prawie równy"**: `prevalence_2021_2025` to liczba prac
podzielona przez mianownik wspólny dla wszystkich terminów, więc równa liczba prac daje
identyczną liczbę zmiennoprzecinkową.

Zmierzyłem skalę: **44 bloki remisowe obejmujące 95 z 287 pozycji.** Trzecia część rankingu ma
kolejność nierozstrzygniętą przez dane.

**Praktycznie:** to nie jest problem, bo zamrożony arkusz ustala kolejność raz na zawsze, i to
on jest rankingiem. Ale każde zdanie „termin X na pozycji N" musi się odwoływać **do kolejności
arkusza**, nie do „rankingu po prevalence" — powtórny przebieg z innym sortowaniem przestawi
sąsiadów w remisie i liczba w tekście przestanie się zgadzać. Dokładnie ten rodzaj drobiazgu,
przed którym ostrzegałeś, tylko szerszy: dotyczy 95 pozycji, nie jednej.

Zapisane w `docs/protocol/liczby_do_metod.md`.

## 3. Wykonane

| zadanie | stan |
|---|---|
| `virtual reality` 153 czy 154 | **153**, plus znalezisko z §2 |
| korekta datowana w v0.8 | wstawiona po linii 181, Twój blok bez zmian w treści |
| przemianowanie pliku | `emerging_top50_prevalence_PRZED_przesiewem.csv`, przez `git mv` |
| liczby z §4 i §5 | `docs/protocol/liczby_do_metod.md`, nowy plik |

Do przemianowania dołożyłem `data/processed/README.md` — tabelka, który plik jest którym
rankingiem, z jednym zdaniem, że ranking na rdzeniu **nie jest osobnym plikiem, tylko kolejnością
wierszy arkusza**. Plus przypis, że `detect_emergence.py` zapisuje natywnie pod starą nazwą, więc
przy odtwarzaniu pipeline'u plik przyjdzie jako `emerging_top_prevalence.csv` — ta sama treść.

`liczby_do_metod.md` zbiera: wyłonienia per wariant (607 w S1 wobec 7 662 w primary), 41/41 i 33/41
z Twojego §5, rodziny 46/140 i 8/23/35, remisy 44/95, oraz tabelę pozycji technologii — z nagłówkiem
**„nie do cytowania jako wynik"**, żeby liczba 28 nie wróciła tylnymi drzwiami.

## 4. Zgoda bez zastrzeżeń na §1

Że 143 nie zastępujemy liczbą 28 — tak, i to jest mocniejsze postawienie sprawy niż moje.
Zastąpienie jednej przedwczesnej liczby drugą zostawiłoby w tekście dokładnie ten sam błąd
w mniejszej skali.

## 5. Manifest

Sprawdzony po wszystkich zmianach: **12/12 OK**. Ruszałem wyłącznie pliki spoza manifestu —
plan v0.8, przemianowany CSV, dwa nowe pliki dokumentacji. Arkusz `bf065aadc07350bd…` bez zmian.
