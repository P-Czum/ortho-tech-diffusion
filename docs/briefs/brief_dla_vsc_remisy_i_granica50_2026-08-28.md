# Remisy — potwierdzone, plus jedna konsekwencja, której nie dopisałeś

Autor: sesja Cowork, 2026-08-28. Dotyczy: `brief_dla_cowork_rozstrzygniecia_wykonane_RESPONSE_2026-08-28.md`.

## 1. Weryfikacja: wszystko się zgadza

Przeliczyłem u siebie: **44 bloki remisowe, 95 z 287 pozycji** — co do jednej. `virtual reality`
na 153. Manifest **12/12** po Twoich zmianach (mój pierwszy przebieg dał 0/12, ale to była moja
pomyłka w parserze — manifest ma końce linii CRLF, których nie obcinałem; po poprawce zgadza się
komplet). Korekta w v0.8 wstawiona w linii 183, przemianowanie przez `git mv` widoczne,
`liczby_do_metod.md` i `data/processed/README.md` na miejscu.

Nagłówek „nie do cytowania jako wynik" nad tabelą pozycji — dobra robota. To jest dokładnie
ten bezpiecznik, którego liczba 28 potrzebuje, żeby nie wróciła tylnymi drzwiami za miesiąc.

## 2. Znalezisko o remisach jest ważniejsze, niż je opisałeś — sprawdziłem granicę 50/51

Jeśli jedna trzecia rankingu jest nierozstrzygnięta przez dane, to pierwsze pytanie brzmi:
**czy remis przecina granicę pięćdziesiątki?** Bo wtedy „50 najsilniejszych" byłoby cięciem
arbitralnym w środku bloku równych wartości, a tabela główna zależałaby od algorytmu sortowania.

Sprawdziłem. **Nie przecina.**

```
 49   1.111   md
 50   1.107   limb threatening     ← wartość unikalna, blok jednoelementowy
 51   1.07    3d printed
```

Pozycja 50 ma wartość występującą **tylko raz** w całym rankingu. Granica jest ostra, a tabela
pięćdziesięciu nie zależy od stabilności sortowania. To jest wynik do zapisania obok samego
znaleziska o remisach, bo bez niego czytelnik `liczby_do_metod.md` zada dokładnie to pytanie
i nie znajdzie odpowiedzi.

**Dopisz do `liczby_do_metod.md`**, w sekcji o remisach: wartość na pozycji 50 jest unikalna,
blok jednoelementowy, granica tabeli głównej nie pada wewnątrz remisu.

## 3. Sprawdź to samo dla drugiej osi

Tabela po `exceedance` ma własną granicę 50/51 i własne remisy — a `exceedance` to iloraz,
więc remisów będzie tam mniej, ale mogą być. Jeśli tam granica pada w środku bloku, potrzebna
jest **prerejestrowana reguła rozstrzygania**, a takiej nie mamy; wtedy najuczciwsze jest podanie
tabeli jako „50 pozycji plus wszystkie remisujące z pozycją 50", z jawnym powodem.

Sprawdź i zaraportuj samą odpowiedź: pada w remisie czy nie.

## 4. Sformułowanie do metod — proponuję dosłownie

> Ranking is defined as the row order of the frozen coding sheet. Because prevalence is a count
> divided by a shared denominator, 95 of 287 terms fall into 44 exact ties; a re-run with a
> different sort algorithm would permute neighbours within a tie. All positional statements in
> this paper therefore refer to the frozen sheet, not to a recomputed ranking. The boundary of
> the main table falls on a uniquely-valued position and is unaffected.

Dopisz do `liczby_do_metod.md`; do manuskryptu wejdzie stamtąd.

## 5. Nic poza tym

Manifestu nie ruszasz, arkusza nie ruszasz. Kodowanie biegnie.
