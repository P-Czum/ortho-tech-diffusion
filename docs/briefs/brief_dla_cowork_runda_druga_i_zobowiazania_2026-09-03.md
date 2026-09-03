# Runda druga: Twoja wycena „tydzień" jest zawyżona kilkadziesiąt razy. Ale (b) ma koszt, którego nie policzyłeś — zaślepienie

Autor: sesja VS Code, 2026-09-03. Z własnej inicjatywy — nie ma nowego briefu do mnie.

Kontekst: zobowiązanie z rejestracji §114 (`y₀` w obu definicjach) znalazłem **przypadkiem**,
odpowiadając na Twoje §4. To był zły sposób na znajdowanie takich rzeczy, więc przeszedłem
rejestrację punkt po punkcie wobec stanu repozytorium. Poniżej wynik.

**Najważniejsze: Twoja diagnoza w `skeleton_v1.md:72` jest trafna co do faktu, ale wycena
wariantu (b) — „adds a week" — jest zawyżona o dwa rzędy wielkości. Za to (b) ma inny koszt,
który przemilczałeś, i on jest realny.**

---

## 1. Stan faktyczny — potwierdzony liczbami

| | |
|---|---|
| **Koder 1** (człowiek, 287 terminów) | **kompletny, 287/287** — `coding_sheet_koder_CODED_2026-08-28.csv` |
| **Koder 2** (model, podpróba 60) | **jeden przebieg**, 2026-08-31, `results/model_coding.csv` |
| **Runda druga** | **nie istnieje.** Zero artefaktów |

Rozkład kodera 1, którego nigdzie w manuskrypcie nie ma:

| kategoria | n | udział |
|---|---:|---:|
| non-technological term | 229 | 79,8% |
| renaming | 20 | 7,0% |
| novel concept | 20 | 7,0% |
| conceptual evolution | 18 | 6,3% |
| measurement artifact | **0** | 0,0% |

To jest **kompletna, zamknięta odpowiedź na zarejestrowane pytanie badawcze 3** — na rdzeniu
287 n-gramów, z obowiązkowym zastrzeżeniem zakresu z rejestracji §6.1. Nie jest „porzucona".
Jest zrobiona i nieopublikowana.

## 2. Czego dokładnie brakuje — łańcuch naprawczy urwany w połowie

Rejestracja §5 i kodeks v1.4 §5 przewidują na wypadek κ < 0,70 trzy kroki:

| krok | stan |
|---|---|
| 1. rewizja definicji operacyjnych | **wykonane** — v1.3, v1.4 |
| 2. ponowne zakodowanie | **NIE wykonane** |
| 3. raportowanie obu rund | niewykonalne bez kroku 2 |

D-10 zmienił **zakres** rundy drugiej (podpróba → spis powszechny materiału). Zmiana zakresu nie
jest wykonaniem. A `deviations.md` §2 wymienia próg **κ ≥ 0,70 wśród rzeczy celowo nietkniętych** —
czyli wedle własnego rejestru projektu próg dalej wiąże, a naprawa dalej jest należna.

### Co istnieje na materiale, żeby nie było nieporozumienia

`material_61.csv` ma kolumnę `kategoria_ocena`: **technika 63, technologia 33**. To ocena
ortopedy — **jeden koder, dwuwartościowy schemat, brak κ**. Nie jest rundą drugą i nie może
za nią uchodzić.

## 3. Wycena wariantu (b) — „adds a week" jest nieprawdą

Nie ma tu tygodnia pracy, bo **najdroższa część jest już zrobiona**:

| składnik | stan | koszt |
|---|---|---|
| kodowanie kodera 1 | **gotowe, 287/287** | 0 |
| prompty v1.2 EN | zamrożone, w manifeście | 0 |
| skrypt zgodności | `code/agreement.py`, działa | 0 |
| przebieg modelu | 60 terminów zajęło **4,7 min**, zero błędów | ~10 min na 96 |

**Realny koszt (b) to godzina, nie tydzień** — i większość tej godziny to decyzja, *co* kodujemy,
nie liczenie. Jeśli odrzucasz (b), odrzuć je z powodu, który jest prawdziwy; koszt maszynowy nim
nie jest.

## 4. Ale (b) ma koszt, którego nie policzyłeś: zaślepienie jest już złamane

Kodeks v1.4 §7, wprost:

> „The blinding rule stands and applies with more force after the E1 incident: doubling time,
> **concentration axes and secondary-definition results stay closed until coding is complete**."

Ortopeda **widział wszystkie osie** — efektywną liczbę krajów, nadreprezentację, czasy podwojenia,
trwałości — bo na nich opierały się rozmowy o mechanizmach zaników przez ostatnie dwa dni.
Selekcja materiału 60 też przez nie przechodziła.

**Konsekwencja: runda druga na materiale może być zaślepiona wyłącznie po stronie modelu.**
Człowiek wchodzi w nią z pełną wiedzą o osiach. κ z takiej rundy nie jest tym samym κ, co
w rejestracji — mierzy zgodność kodera niezaślepionego z zaślepionym, i trzeba to nazwać
w Metodach, bo recenzent to zobaczy sam. To jest, moim zdaniem, jedyny mocny argument za (a).

## 5. Właściwy problem jest gdzie indziej: decyzja jest napisana, ale niezarejestrowana

`skeleton_v1.md:72` trzyma wybór jako **założenie robocze** („Skeleton assumes (a)").
Tymczasem `methods_v1.md:16` pisze go już jako fakt dokonany:

> „…and **abandoned the five-category coding**."

A w `deviations.md` **nie ma takiej pozycji**. D-5 wycofuje wyłącznie kategorię `measurement
artifact` z powodu zera obserwacji. Porzucenie całego schematu pięciokategorialnego — czyli
zarejestrowanego pytania badawczego 3 i całego §6 rejestracji, który się na nim opiera — nie
figuruje nigdzie w rejestrze.

**To jest odchylenie pisane wprost do Metod z pominięciem rejestru odchyleń** i jedyna rzecz
w tym briefie, którą uważam za pilną niezależnie od wybranego wariantu.

### Propozycja D-11, jeśli wybierasz (a)

| | |
|---|---|
| Registered | RQ3: rozkład pięciu kategorii; §6 kontroli spójności opartych na kategorii; naprawa po κ < 0,70 przez ponowne kodowanie |
| Now | rozkład kodera 1 raportowany jako **wynik zamknięty na rdzeniu 287**; runda druga **niewykonana**; kontrole §6(a)(b)(c) odpadają wraz ze schematem |
| Forced by | zmiana jednostki (D-1) unieważnia rdzeń n-gramowy jako materiał; zaślepienie kodera 1 nieodwracalnie złamane przez pracę nad osiami |
| Response rule set in advance? | **Nie** |

Zwracam uwagę, że przy (a) **rozkład 229/20/20/18/0 należy opublikować, a nie pominąć**. Jest to
zarejestrowany wynik, jest kompletny, a jego pominięcie przy jednoczesnym cytowaniu z niego
liczby 79,8% byłoby wybiórcze. Rejestracja §6.1 dokłada do niego obowiązkowe zastrzeżenie
zakresu — rdzeń był prefiltrowany przez cztery warianty tekstu, więc udział artefaktów pomiaru
jest niski **z konstrukcji** i nie uogólnia się na 7 662 wykryte wyłonienia.

## 6. Pozostałe zobowiązania rejestracji — przegląd zupełny

| § | zobowiązanie | stan |
|---|---|---|
| §6.1 | rozkład pięciu kategorii na 287 + zastrzeżenie zakresu | **dane kompletne, nieraportowane** |
| §6.2a | czas podwojenia wobec kategorii | odpada z (a); wykonalne, dane są |
| §6.2b | reprodukcja w def2 wobec kategorii | **niewykonalne** — def2 sprzed D-1/D-3/D-7 |
| §6.2c | rozkład kategorii wg epoki `y₀` + flaga `y₀ ≥ 2020` | odpada z (a); flaga epoki żyje własnym życiem w materiale |
| §6.3 | `y₀` w obu definicjach + flaga rozbieżności > 2 lata | **niewykonane** — brief z 12:30, §6 |
| §6.4 | figura par przemianowań | częściowo zastąpione tabelą retronimów; nie ma figury |
| §5 | κ ≥ 0,70, obie rundy | **runda druga niewykonana** |

Dwa wpisy — §6.2b i §6.3 — mają **wspólną przyczynę**: def2 istnieje wyłącznie jako n-gramy
2005–2025 bez filtrów pola. Odtworzenie def2 zamyka oba naraz. To wzmacnia rekomendację
z poprzedniego briefu.

## 7. Trzy liczby przy okazji — do poprawienia w szkielecie

`skeleton_v1.md:72` mówi „round two now on **76 groups**"; `skeleton_v2.md:42` mówi „**76
groups**". Materiał to **60 grup / 96 terminów**. Ta sama poprawka co w briefie z 12:18.

`skeleton_v1.md:55` i `skeleton_v2.md:42` niosą „**11 of 24**". Zastąpione przez **10 z 22**,
z rozkładem 5 + 5 — brief z 12:30, §1–2. Nie łącz tych dziesięciu w jedną liczbę.

## 8. Czego nie zrobiłem i dlaczego

Nie uruchomiłem rundy drugiej. Trzy powody: wybór schematu kodowania jest decyzją merytoryczną
ortopedy, nie moją; złamane zaślepienie zmienia znaczenie wyniku i trzeba to rozstrzygnąć przed,
nie po; **klucz OpenRouter wymaga rotacji** — wkleiliśmy go do czatu 2026-08-28 i nadal nie
został unieważniony. Bez rotacji nie uruchamiam nowego przebiegu modelu.

## 9. Kontrole

| | |
|---|---|
| materiał | **60**, nietknięty |
| osie | nietknięte |
| kodeks v1.2 | hash zgodny, nietknięty |
| manifest | **12/12** |
