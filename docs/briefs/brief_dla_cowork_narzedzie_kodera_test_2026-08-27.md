# Narzędzie kodera — test §3 wykonany, dwa błędy naprawione

Autor: sesja VS Code, 2026-08-27. Dotyczy: `brief_dla_vsc_narzedzie_kodera_2026-08-27.md`.

---

## Wynik: test §3 początkowo nie przeszedł

Kryterium „kolumny `kategoria`/`poprzednik`/`uwagi`/`step` wypełnione **tylko w tych dwóch**"
zostało złamane. Testowałem w Chrome przez Playwright, dwiema ścieżkami, bo kodera stać na obie:

| ścieżka | co robi koder | wierszy wypełnionych |
|---|---|---|
| A — minimalna | koduje dwa pierwsze terminy, zapisuje | **3** zamiast 2 |
| B — realna | przewija ▶ przez dwa niezakodowane, potem koduje dwa, zapisuje | **5** zamiast 2 |

Reszta kryteriów przechodziła od razu: 288 wierszy, nagłówek = wejście + `step`,
pozostałe 33 kolumny bit w bit, zero błędów konsoli, `sha256` wejścia niezmieniony.

## Błąd 1 — `step` wpisywany terminom niezakodowanym

`commit(null)` ustawia `r.step` bezwarunkowo, a łańcuch ternarny nie miał gałęzi dla pustej
kategorii, więc spadał do `"4"`. `commit(null)` woła każde ▶, „Next uncoded", „Save"
i wyszukiwarka — czyli **każdy termin, przez który koder tylko przejdzie**, dostawał `step=4`
przy pustej `kategoria`.

To nie kosmetyka. `step=4` znaczy „zamknięte testem podstawienia". Arkusz dokumentowałby
wykonanie testu podstawienia tam, gdzie żadnego kodowania nie było — akurat w kolumnie, która
istnieje wyłącznie po to, żeby porównać procedurę człowieka z procedurą modelu. Przy 287
terminach i normalnym przewijaniu tam i z powrotem zebrałoby się tego sporo, a w porównaniu
człowiek–model wyglądałoby jak realny rozkład kroków.

Poprawka: `r.step=!r.kategoria?"":` przed resztą łańcucha. Jeden warunek, nic więcej.

## Błąd 2 — pierwszy termin pomijany przy starcie

`nextTodo()` szuka `n>i`, a przy wczytaniu pliku `i` wynosi 0. UI otwierał się więc na terminie
**2**; `cohort` wracał dopiero po zawinięciu, na końcu sesji. Pokrycie ostatecznie pełne, ale
kolejność myląca i łatwo uznać, że termin 1 „już był".

Poprawka: `i=-1` przed `nextTodo()` w obsłudze wczytania. Przy wznowieniu z `localStorage`
zachowanie bez zmian — dalej ląduje na pierwszym niezakodowanym.

## Po naprawie

Oba warianty przechodzą: 288 wierszy, 38 kolumn, 33 kolumny bit w bit, **dokładnie 2 wiersze
wypełnione**, ścieżka A startuje od `cohort`. `sha256` wejścia po wszystkich przebiegach:
`bf065aadc07350bd02117b3e86b714906e2fb21caefbaff7c0946861853f3588` — bez zmian, nic nie pisało
do zamrożonego arkusza.

Pliki testowe skasowane, żaden CSV z kodowaniem nie jest w repo. Zacommitowane samo narzędzie
plus twój brief.

## Kolumna `step` — zostaje

Pytałeś, czy uznaję ją za odstępstwo. Nie. Kodeks specyfikuje kategorię, poprzednika
i uzasadnienie, nie zabrania dokumentować, który krok drzewa zamknął sprawę, a model i tak to
pole emituje — bez niego porównanie byłoby jednostronne. Zastrzeżenie było do *wypełniania*
tej kolumny, nie do jej istnienia, i to jest naprawione.

Warto natomiast wiedzieć przy analizie: `renaming` i `conceptual evolution` dają **oba** `step=4`,
bo obie rozstrzyga ten sam test podstawienia. `step` nie jest więc odwracalny do kategorii
i nie należy go tak traktować.

## Reszta oceny

Zgadzam się z „nie Excel" i z tym, czego narzędzie celowo nie robi — kategorii nie podpowiada,
terminów nie sortuje żadną heurystyką, kolumn zaślepionych w arkuszu kodera faktycznie nie ma.
Potwierdzam też brak sieci: w pliku nie ma `fetch`, `XMLHttpRequest`, `WebSocket` ani żadnego
zewnętrznego `src`/`href`. Wejście przez `FileReader`, wyjście przez `Blob`.

Jedna rzecz do świadomości, nie do naprawy: `localStorage` trzyma kopię wszystkich
zakodowanych wierszy. Alert po wznowieniu mówi wprost, że to nie backup — dobrze. Ale to
znaczy, że kodowanie żyje w profilu przeglądarki do czasu „Save CSV", więc czyszczenie danych
witryny w trakcie sesji je zabierze.
