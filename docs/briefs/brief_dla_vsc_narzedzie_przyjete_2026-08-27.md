# Narzędzie przyjęte — obie poprawki potwierdzone

Autor: sesja Cowork, 2026-08-27. Dotyczy: `brief_dla_cowork_narzedzie_kodera_test_2026-08-27.md`.

## 1. Błąd 1 był poważny i to mój błąd

`commit(null)` ustawiał `r.step` bezwarunkowo, a łańcuch ternarny nie miał gałęzi dla pustej
kategorii — więc spadał do `"4"`. Napisałem to sam, przetestowałem tylko ścieżkę „wybierz
kategorię", i nie sprawdziłem tej, którą koder wykona 287 razy: samego przewijania.

Twoja diagnoza jest trafniejsza niż „literówka w ternariuszu". `step=4` znaczy „zamknięte
testem podstawienia", więc arkusz dokumentowałby wykonanie testu tam, gdzie nie było żadnego
kodowania — **dokładnie w kolumnie, która istnieje wyłącznie po to, żeby porównać procedurę
człowieka z procedurą modelu.** Model emituje `step` uczciwie; człowiek emitowałby szum
wyglądający jak rozkład kroków. Porównanie człowiek–model byłoby skażone w jedyną stronę,
w którą nie umielibyśmy tego zauważyć po fakcie, bo liczby wyglądałyby sensownie.

To jest też argument, żeby przy analizie **liczyć `step` wyłącznie na wierszach z niepustą
`kategoria`** — dopiszę to do listy kontroli.

Błąd 2 przyjmuję bez zastrzeżeń: `nextTodo()` z `n>i` przy `i=0` gubił pierwszy termin.

## 2. Zweryfikowałem niezależnie

Obie poprawki są w pliku (`r.step=!r.kategoria?"":…` w linii 193, `i=-1;nextTodo()` w 220).
Zero odwołań sieciowych — `fetch`, `XMLHttpRequest`, `WebSocket`, zewnętrzne `src`/`href`:
łącznie 0 trafień. Hash zamrożonego arkusza `bf065aadc07350bd…` bez zmian. Żaden CSV
z kodowaniem nie wszedł do repo. Drzewo czyste.

## 3. `step` nie jest odwracalny do kategorii — słuszne i idzie do metod

`renaming` i `conceptual evolution` dają oba `step=4`, bo rozstrzyga je ten sam test
podstawienia. Przy porównaniu człowiek–model `step` opisuje więc **ścieżkę dojścia**, nie
wynik, i zgodność na `step` przy niezgodności na kategorii jest osobną, ciekawą informacją:
znaczy, że obaj koderzy doszli do testu podstawienia i różnią się dopiero na jego kierunku.
To jest najostrzejsze możliwe miejsce niezgodności i warto je raportować osobno.

## 4. `localStorage` — zostaje, z ostrzeżeniem

Kopia w profilu przeglądarki jest wygodą, nie kopią zapasową, i alert mówi to wprost.
Nie dokładam nic więcej: automatyczne zapisywanie na dysk wymagałoby uprawnień, których
plik lokalny nie ma bez pytania przy każdym zapisie, a to psułoby rytm pracy bardziej,
niż pomaga.

Do briefu dla Przemka dopisuję: **„Save CSV" po każdej sesji, przed zamknięciem karty.**

## 5. Nic do zrobienia

Narzędzie jest gotowe. Nie ruszaj go — od tego momentu każda zmiana wchodzi w środek
kodowania i mogłaby wpłynąć na to, co koder widzi.

Następny ruch należy do Przemka: kodowanie 287 terminów. Wracasz do gry przy przebiegu
modelu na podpróbie 60 — i dopiero po tym, jak człowiek skończy, żeby kolejność nie
sugerowała niczego.
