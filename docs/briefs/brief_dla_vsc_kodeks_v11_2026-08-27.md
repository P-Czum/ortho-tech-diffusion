# Kodeks v1.1 przyjęty — droga do zamrożenia

Autor: sesja Cowork, 2026-08-27. Dotyczy: `brief_dla_cowork_recenzja_kodeksu_2026-08-27.md`.

## Recenzja przyjęta w całości

Wszystkie punkty zasadne, v1.1 w `docs/protocol/kodeks_kodowania_v1.1.md` (v1.0 zostaje dla
historii; §7 wylicza zmiany). Najkrócej:

- **Test podstawienia**: masz rację, że w v1.0 był niewykonalny — pisałem regułę do materiału,
  którego koder nie miał. Twoje trzy kolumny to naprawiają; przykład „robotic navigation
  system" wszedł do definicji `conceptual evolution` jako wzorzec.
- **Lift**: próg **3 spójnie**, status zdegradowany do narzędzia wyszukiwania. Twoje pomiary
  (`we tested the`, lift 36,0) idą do kodeksu jako uzasadnienie — lepszego dowodu, że lift
  nie jest regułą decyzyjną, nie będzie.
- **Sprzeczności 3.1 i 3.2**: oba wskaźniki usunięte. Def2 zostaje wyłącznie w kontroli
  po kodowaniu — jej wartość bierze się dokładnie z tego, że nie uczestniczy w kodowaniu.
  `measurement artifact` opiera się teraz na **koniunkcji** daty (`y₀ ≥ 2020`) i treści
  (konwencja zapisu) — sama data nie wystarcza, bo dotyczy 86 terminów i większość to realne
  zjawiska.
- **Warstwowanie**: epoka × długość n-gramu, 6/36/18. Obecność kandydata odrzucona.
- **Pętla kroku 4**: kolejni kandydaci w kolejności liftu, po wyczerpaniu `novel concept`.
- **Zastrzeżenie zakresu z Twojego §4** — wpisane do kodeksu jako obowiązkowe zdanie wyników.
  To jest ważna uwaga: rozkład kategorii na rdzeniu opisuje wyłonienia odporne, nie wyłonienia
  w ogóle, i czytelnik założy szersze uogólnienie, jeśli mu wprost nie zabronimy.
- **κ**: ważone + zgodność surowa obok, próg 0,70 bez zmian.

## Zadania do zamrożenia

1. **Narzędzie przeszukiwania dla kodera** — tak, dostarcz. Wymagania minimalne: wejście
   termin kanoniczny (+ opcjonalnie zakres lat), wyjście tytuły z rokiem i PMID, każde
   zapytanie dopisywane do logu (`logs/coder_queries.log`: timestamp, zapytanie, liczba
   trafień). Bez rankingu, bez podpowiedzi — samo wyszukiwanie.
2. **Regeneracja kolumny kandydatów przy progu lift ≥ 3** (jeśli arkusz generował przy innym).
3. **Zamrożenie**: `coding_sheet_full.csv` + widok kodera (bez kolumn zaślepionych) + kodeks
   v1.1 → sha256 wszystkich trzech do `docs/protocol/freeze_manifest.txt`, commit.
4. Po zamrożeniu piszę rejestrację OSF (szablon analiz danych wtórnych; zadeklarowane, co już
   wykonano: detektor, warianty, arkusz — kodowanie nie ruszyło). Hashe z pkt 3 wchodzą do
   rejestracji.

Kodowanie rusza po rejestracji — pierwszy koder: Przemek.
