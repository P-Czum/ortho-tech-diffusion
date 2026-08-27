# Narzędzie do kodowania — `code/coding_ui.html` (plik nowy)

Autor: sesja Cowork, 2026-08-27. Do wiadomości, nie do wykonania — chyba że w §3.

## Co to jest

Jednoplikowy interfejs do kodowania 287 terminów, otwierany lokalnie w przeglądarce.
Czyta **zamrożony `coding_sheet_koder.csv`** przez okno wyboru pliku, niczego w nim nie zmienia,
a wynik eksportuje do **nowego** CSV (`..._CODED_RRRR-MM-DD.csv`).

Zero sieci, zero zależności, zero backendu.

## Dlaczego nie Excel

37 kolumn, w tym cztery z wielozdaniowymi blokami tytułów. W arkuszu koder przewija poziomo,
łatwo wpisuje kategorię w niewłaściwy wiersz i literówkę w nazwę kategorii, która potem
wywraca liczenie κ. Interfejs pokazuje jeden termin naraz, kategorie są przyciskami
(klawisze 1–5), a nazwy pochodzą ze stałej listy — literówka jest niemożliwa.

## Czego celowo NIE robi

- **Nie podpowiada kategorii i nie sortuje terminów według żadnej heurystyki.** Kodeks mówi
  „maszyna nie proponuje żadnej kategorii"; podpowiedź zniszczyłaby niezależność κ i trzy
  kontrole pokodowe.
- Nie pokazuje kolumn zaślepionych — bo ich w arkuszu kodera po prostu nie ma; zweryfikowane.
- Nie dotyka pliku wejściowego.

## Jedna rzecz ponad arkusz: kolumna `step`

Eksport ma dodatkową kolumnę `step` z numerem kroku drzewa decyzyjnego, który zamknął sprawę
(1 artefakt, 2 nie-technologia, 3 brak poprzednika, 4 test podstawienia). Wypełniana
automatycznie z wybranej kategorii.

Uzasadnienie: model-koder emituje pole `step`, więc bez niego porównanie człowiek–model
byłoby niepełne po stronie człowieka. To jest **dodatkowa dokumentacja tej samej procedury**,
nie zmiana procedury — kodeks nie specyfikuje formatu wyjścia poza kategorią, poprzednikiem
i uzasadnieniem. Jeśli uznasz to za odstępstwo, powiedz, wywalę kolumnę.

## Weryfikacja przed oddaniem

Sprawdziłem arkusz kodera pod UI: 287 wierszy, 37 kolumn, **wszystkie wymagane obecne**,
**zero kolumn zaślepionych** (`autor_*`, `kraj_*`, czas podwojenia, trwałość) — widok jest
faktycznie zaślepiony, zgodnie z §1 kodeksu.

## §3 — do zrobienia po Twojej stronie

1. Otwórz `code/coding_ui.html` w Chrome, wczytaj `data/processed/coding_sheet_koder.csv`,
   zakoduj **dwa dowolne terminy testowo**, zapisz CSV i sprawdź, czy:
   wynik ma 288 wierszy, kolumny `kategoria`/`poprzednik`/`uwagi`/`step` są wypełnione tylko
   w tych dwóch, a wszystkie pozostałe kolumny są **bit w bit** takie jak w wejściu.
2. Wyrzuć plik testowy. **Nie commituj żadnego CSV z kodowaniem** — kodowanie robi Przemek.
3. Zacommituj samo narzędzie.

Uwaga: hash `coding_sheet_koder.csv` musi po tym teście zostać `bf065aadc07350bd…`.
Jeśli się zmieni, coś zapisało do pliku wejściowego i trzeba to zatrzymać.
