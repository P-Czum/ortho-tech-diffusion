# Granica 50/51 — ostra na obu osiach. Plus drobiazg tuż przy niej

Autor: sesja VS Code, 2026-08-28. Dotyczy: `brief_dla_vsc_remisy_i_granica50_2026-08-28.md`.

## 1. Odpowiedź na §3: nie pada w remisie

Sprawdzone na **surowych** wartościach, nie zaokrąglonych do trzech miejsc — bo zaokrąglenie
potrafi zarówno stworzyć remis, którego nie ma, jak i ukryć ten, który jest.

| oś | wierszy nadmiarowych w remisach | wartość na pozycji 50 | granica |
|---|---:|---|---|
| prevalence (kolejność arkusza) | 51 | `limb threatening` — unikalna | **ostra** |
| exceedance (rdzeń, sort. stabilne) | 11 | `retrospective observational` — unikalna | **ostra** |

Prerejestrowana reguła rozstrzygania nie jest potrzebna na żadnej osi. Wariant „50 plus wszystkie
remisujące z pozycją 50" nie wchodzi do gry.

## 2. Drobiazg, który zmienia Twoje §2 o jedną pozycję

Twój listing pokazuje pozycję 49 jako `md` 1,111 i pozycję 50 jako unikalną. Wniosek jest trafny,
ale **remis jest tuż obok, po lewej stronie granicy**:

```
 48  cone               0.011107636670156214
 49  md                 0.011107636670156214   <- bitowo równe, blok konczy sie tutaj
 50  limb threatening   0.011066849754598724   <- unikalna, granica
```

Blok remisowy 48–49 zamyka się dokładnie przed cięciem. Nic to nie psuje, ale gdyby ktoś kiedyś
przesunął tabelę na 49 pozycji, cięcie **padłoby w środku remisu**. Warto, żeby to było zapisane
przy liczbie, a nie odkrywane drugi raz.

## 3. Dlaczego exceedance remisuje pięciokrotnie rzadziej

276 wartości unikalnych z 287, wobec 236 na prevalence. Powód jest strukturalny i wart zdania
w metodach: `prevalence` to **liczba prac przez mianownik wspólny wszystkim terminom**, więc dwa
terminy o równej liczbie prac mają bitowo równą wartość — remis jest wymuszony arytmetyką, nie
przypadkiem. `exceedance` to iloraz pułapu przez próg **indywidualny dla terminu**, czyli dwie
wielkości ciągłe; zbieżność wymagałaby zbiegu okoliczności.

To wzmacnia Twój wybór drugiej osi z planu §5 z powodu, którego wtedy nie znaliśmy.

## 4. Zapisane

`liczby_do_metod.md`, sekcja o remisach, dwie nowe podsekcje: granica na obu osiach z tabelką
i przypisem o bloku 48–49, oraz Twoje sformułowanie do metod.

Sformułowanie wziąłem dosłownie z jedną zmianą, którą zgłaszam: Twoja wersja mówiła o granicy
w liczbie pojedynczej („the boundary of the main table"), a mamy dwie osie i obie sprawdzone,
więc jest „on both selection axes", plus zdanie o rzadszych remisach na exceedance z powodem.
Jeśli wolisz swoją wersję, cofam.

## 5. Stan

Manifest 12/12. Arkusz `bf065aadc07350bd…` bez zmian. Kodowanie niezakłócone.
