# S1, S2, S7, podpisy rycin — sprawdzone; S1 i S7 poprawione u źródła; S5 — pliki

Autor: sesja VS Code, 2026-10-29. Odpowiedź na `brief_dla_vsc_suplement_S1_S2_S7_2026-10-29`.
S3, S4 i S6 składam; przyjdą osobnym briefem.

## 1. S2 i podpisy rycin — bez uwag

- **S2:** tekst kodeksu v1.4 jest w S2 **dosłownie**. Sprawdziłem skryptem: cały plik
  `coding_manual_v1.4.md` zawiera się w S2.
- **`figure_legends.md`:** wszystkie liczby i opisy zgadzają się z danymi:
  - 36 z 48 przy zgodnych miarach, 12 bez słupka;
  - 9 bez czasu podwojenia, z trzema powodami;
  - dual mobility ma pięć lat po szczycie;
  - kifoplastyka: sama pierwsza nazwa (0,34 szczytu) wyglądałaby na zanik.

## 2. S1 — poprawiłem sześć wierszy rejestru bezpośrednio w pliku

S1 przekłada mój rejestr. W kilku miejscach skrót zmienił sens, więc przywróciłem brzmienie
z `deviations.md`:

| wiersz | było w S1 | jest (jak w rejestrze) |
|---|---|---|
| D-1, reguła z góry | „the protocol prescribed revision of the unit…” | **dwuczęściowe kryterium akceptacji** (brak szablonu w top 50; rodzina robotyki ≤ 3 wiersze) zapisane i wysłane przed przebiegiem; „eight rows” zamiast „non-overlapping fragments” |
| D-4, „Forced by” | „definicja klasyfikowała frazy, których żaden chirurg…” — tego zdania nie ma w rejestrze | **κ = 0,442 wobec progu 0,70; 6 z 17 niezgodności na luce w definicji** |
| D-6 | „No” | „No — a defect in the registered document, not a change of plan” |
| D-8 | „the registered research questions could not be answered…” | „96% of the material as registered was something else”; „No — the author's scoping decision, taken after seeing the composition” |
| D-10 | „a census cost less than a sampling design” | „a census was feasible” |
| D-11 | „branch abandoned (D-1)” | przywrócone **dlaczego nie było drugiej rundy**: koder widział osie, czasy podwojenia i trwałość, więc zaślepić dało się tylko stronę modelu; plus rozkład 229/20/20/18/0 |
| **D-12** | „secondary definition reported as a text-variant sensitivity (S8)”; „dictionary too small (see D-2)” | **błąd merytoryczny.** Druga definicja to definicja **pola** (137 czasopism), a nie wariant tekstu. Nie ma jej w S8, a D-2 dotyczy wariantu samych tytułów. Przywrócone: decyzja autora, a nie pomiar; tylko n-gramy 2005–2025; Jaccard ≈ 0,31; reumatologia i nauki podstawowe |

**D-9 — Twoje pytanie:** tak, `tdr` 28,8 → 50,2% się zgadza.

## 3. S7 — jedno zdanie poprawione

Było: klasyfikację odrzucono, *„when the classification could not be blinded to the curves
(S1, D-11)”*. D-11 dotyczy pięciu kategorii terminów, a nie zaników. Teza o dowodach zeszła
z trzech powodów łącznie (`ksztalt_artykulu` §4):
- n = 2,
- odstęp 0,003 w oknie +1–3,
- klasyfikacja znająca krzywe.

Teraz S7 mówi dokładnie to. Data 2026-09-02 jest prawdziwa: klasyfikacja jest w commicie
`852e9f1`, a okna względem szczytu powstały 2026-09-04. Zdanie nie sugeruje już jednak, że
kolejność dawała zaślepienie, bo ortopeda znał wtedy krzywe trwałości w oknach kalendarzowych.

## 4. S5 — z jakich plików

- **Człony grup:** `data/processed/material_48.csv` (term → grupa, klasa, źródło terminu). Zawiera
  to samo co `grupy_48.json` i dodatkowo klasy.
- **`warianty_odrzucone.csv` to nie są „odrzucone warianty” grup.** To 172 frazy odpadłe na
  przecięciu S2/S3, czyli S8.2. Do S5 nie wchodzi.
- **Wyłączenia z materiału** są w kilku plikach z kolejnych wersji:
  - `retronimy.csv`: trzy pierwsze wiersze to retronimy z Tabeli 3; czwarty, `primary ACL
    reconstruction`, był kandydatem, nie retronimem;
  - `material_wykluczenia.json`: pięć „zbyt ogólnych”;
  - `material_decyzje_koncowe.json`: wieloznaczne skróty `ha`, `cr`, `ka`, `ai` oraz dwa
    powikłania (`armd`, `squeaking`);
  - MUA z §4a.
  
  Jeśli chcesz, zbiorę je w jedną tabelę `wylaczenia_48.csv` ze źródłem każdego wiersza;
  napisz, a dołączę ją do briefu z S3, S4 i S6.

## 5. Błąd w `methods_v3` sprzed dwóch miesięcy, nigdy nie naniesiony

*„…and **seven** as generic descriptions of established procedures”* — poprawnie **sześć**.
Siódmym był ACDF, który został w materiale. Poprawka była w `brief_dla_cowork_audyt_methods_i_skeleton_2026-09-03` §2,
ale przeszła przez methods v1 → v2 → v3 nietknięta. Plik `material_wykluczenia.json` ma pięć
pozycji. Szóstą trzeba ustalić przy zbieraniu S5; zrobię to w tabeli z §4.

## 6. Inne

- `deviations.md`: Twój dopisek MTIX na materiale 48 zostaje. Przywróciłem tylko końce linii
  CRLF, bo przy zmianie na LF diff obejmował cały plik.
- Przypis Ryc. 1 w podpisie zamiast na rycinie: dobrze.

Manifest **12/12**.
