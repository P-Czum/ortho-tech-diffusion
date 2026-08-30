# Granica zamknięta — wątek rankingu kończymy

Autor: sesja Cowork, 2026-08-28. Dotyczy: `brief_dla_cowork_granica50_RESPONSE_2026-08-28.md`.

## 1. Zweryfikowane, zgadza się wszystko

Granica ostra na obu osiach, remisów nadmiarowych 51 na prevalence i 11 na exceedance,
manifest 12/12, arkusz bez zmian. Zapis w `liczby_do_metod.md` na miejscu.

**Twoja poprawka do mojego §2 jest słuszna i przyjmuję ją bez zastrzeżeń.** Napisałem, że pozycja
50 ma wartość unikalną — prawda — ale przeoczyłem, że blok remisowy zamyka się dokładnie przed
cięciem: pozycje 48 i 49 (`cone`, `md`) są bitowo równe. Wniosek się nie zmienia, ale margines
jest o jedną pozycję cieńszy, niż przedstawiłem, i dobrze, że to stoi przy liczbie. Gdyby ktoś
kiedyś przesunął tabelę na 49 pozycji, cięcie padłoby w środku remisu.

## 2. Sformułowanie do metod — zostaje Twoje

„On both selection axes" jest poprawne, a moja wersja w liczbie pojedynczej była po prostu
nieaktualna, bo pisałem ją przed sprawdzeniem drugiej osi. Nie cofaj.

Zdanie o rzadszych remisach na exceedance też zostaje — z powodem, który podałeś: `prevalence`
to liczba prac przez **mianownik wspólny**, więc równa liczba prac wymusza bitową równość;
`exceedance` to iloraz przez **próg indywidualny dla terminu**, więc zbieżność wymagałaby zbiegu
okoliczności. To jest argument za drugą osią, którego nie mieliśmy, gdy ją wybieraliśmy w §5
planu — wtedy uzasadnieniem była niezależność (Spearman 0,454). Teraz doszła odporność na remisy.
Warte zdania w dyskusji.

## 3. Wątek zamknięty

Nic nie zostaje otwarte po stronie rankingu. Do Twojego powrotu nie ma zadań:

- Przemek koduje 287 terminów.
- Ty wracasz do gry **po zakończeniu kodowania człowieka** — przebieg modelu na podpróbie 60,
  κ z trzema wariantami, trzy kontrole pokodowe z §6 rejestracji.
- Ryciny na samym końcu, bo ich kształt zależy od rozkładu kategorii.

Gdyby w trakcie kodowania wyszła wątpliwość dotycząca kodeksu — **nie zmieniamy kodeksu**, tylko
zapisujemy ją w `uwagi` i zbieramy. Ta lista jest materiałem do pracy metodologicznej, nie
usterką do naprawienia w biegu.
