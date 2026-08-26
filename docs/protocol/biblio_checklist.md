# Zgodność z BIBLIO

Lista kontrolna BIBLIO — *Preliminary guideline for reporting bibliometric reviews of the
biomedical literature*, Montazeri i wsp., **Syst Rev 2023;12:239**, DOI
[10.1186/s13643-023-02410-2](https://doi.org/10.1186/s13643-023-02410-2).
Pozycje pobrane z wersji na PMC ([PMC10722750](https://pmc.ncbi.nlm.nih.gov/articles/PMC10722750/));
listę kontrolną wydaje też EQUATOR Network.

20 pozycji: tytuł 2, abstrakt 1, wprowadzenie 2, metody 7, wyniki 4, dyskusja 4.

Oceniany dokument: `docs/plan_do_recenzji.md` **v0.2** (2026-08-25).
Data oceny: 2026-08-26.

**Zastrzeżenie interpretacyjne.** BIBLIO jest wytyczną *raportowania gotowego przeglądu*, a
oceniany dokument jest planem sprzed analizy. Pozycje dotyczące wyników i dyskusji nie mogą być
„spełnione" na tym etapie — oceniam je jako *czy plan przewiduje ich zaraportowanie*. Rozróżnienie
jest istotne: „DO ZROBIENIA" nie znaczy „brak", tylko „wymagalne dopiero w manuskrypcie".

Legenda: **TAK** — spełnione · **CZĘŚĆ** — spełnione niepełnie · **PLAN** — wymagalne dopiero
w manuskrypcie, plan to przewiduje · **LUKA** — nie przewidziane, wymaga decyzji.

---

## Tytuł

| # | Pozycja | Ocena | Uwagi |
|---|---|---|---|
| 1 | Identyfikacja raportu jako przeglądu bibliometrycznego w tytule | **LUKA** | Obecny tytuł („Dyfuzja badań nad technologiami w ortopedii") nie zawiera określenia typu badania. Manuskrypt musi mieć w tytule „bibliometric review" albo równoważne. |
| 2 | Kluczowe zagadnienia i pokrycie okresu | **CZĘŚĆ** | Zagadnienie jest, zakresu czasowego brak. Tytuł manuskryptu powinien nieść „2005–2025". |

## Abstrakt

| # | Pozycja | Ocena | Uwagi |
|---|---|---|---|
| 3 | Ustrukturyzowane streszczenie: tło, metody, wyniki, wnioski | **PLAN** | Plan nie ma abstraktu i nie musi. Wymagalne w manuskrypcie. |

## Wprowadzenie

| # | Pozycja | Ocena | Uwagi |
|---|---|---|---|
| 4 | Przegląd istniejącej wiedzy i informacji epidemiologicznych | **CZĘŚĆ** | `docs/related_work.md` istnieje, ale rozpoznanie nie ma jakości publikacyjnej (zablokowany dostęp do PMC, ScienceDirect, LWW). Domknie to zadanie 1.5. |
| 5 | Sformułowanie celu / pytania badawczego | **TAK** | §1. |

## Metody

| # | Pozycja | Ocena | Uwagi |
|---|---|---|---|
| 6 | Źródła informacji | **TAK** | §2–3: MEDLINE/PubMed baseline 2026 (`pubmed26n0001`–`n1334`, wydany 2026-01-30) + updatefiles. Lustro lokalne, nie interfejs wyszukiwania — to warto w metodach powiedzieć wprost, bo zmienia odtwarzalność na korzyść. |
| 7 | Strategia wyszukiwania: słowa kluczowe i kryteria systematyzacji (data wyszukiwania, język, typ dokumentu) | **TAK** | §6.2 warstwy epokowe słownika, §8 typy publikacji, brak ograniczenia językowego. **Data wyszukiwania = data wydania baseline (2026-01-30) plus zakres pobranych updatefiles**, nie data uruchomienia skryptu — do zapisania jawnie. |
| 8 | Okres objęty przeglądem i uzasadnienie | **TAK** | §5: 2005–2025, uzasadnienie przez okres przedwzrostowy; 2026 wyłączony jako niekompletny; rozszerzenie do 1990 jako wrażliwość. |
| 9 | Kryteria włączenia i wykluczenia | **TAK** | §8. |
| 10 | Oczyszczanie danych, usunięcie duplikatów i rekordów nieistotnych | **LUKA** | Plan nie opisuje deduplikacji. W lustrze MEDLINE ten problem ma inną postać niż w wyszukiwarce: duplikaty PMID między `baseline` a `updatefiles` (rekord zaktualizowany po wydaniu baseline) oraz `DeleteCitation`. Bez reguły „ostatnia wersja rekordu wygrywa" mianownik będzie zawyżony. Wymaga decyzji przed Etapem 1. |
| 11 | Ocena jakości (opcjonalna) | **n/d** | Pozycja dotyczy oceny jakości włączonych prac przez trzech autorów. W przeglądzie bibliometrycznym mierzącym udziały nie ma zastosowania. Plan ma w zamian walidację precyzji klasyfikatora (PPV per rodzina, per epoka) — to jest mocniejsze, ale **BIBLIO tego nie wymaga ani nie przewiduje**, patrz sekcja „Luki w samym standardzie". |
| 12 | Synteza danych: metody podsumowania, tabelaryzacji, analizy | **TAK** | §7: regresja segmentowa/joinpoint jako primary, krzywa logistyczna i model Bassa wyłącznie eksploracyjnie i tylko przy nasyceniu, standaryzacja bezpośrednia przy stałych wagach krajów. |

## Wyniki

| # | Pozycja | Ocena | Uwagi |
|---|---|---|---|
| 13 | Wyniki opisowe: przebieg wyszukiwania i selekcji na diagramie przepływu; statystyki publikacji, lat, typów dokumentów, krajów, autorów, czasopism | **LUKA** | Plan nie przewiduje **diagramu przepływu**. Dla lustra lokalnego jest on nietypowy, ale możliwy i sensowny: rekordy w baseline → po deduplikacji → w polu → po filtrze typu publikacji → w oknie 2005–2025. Warto go zaplanować, bo to jedyna pozycja BIBLIO wymagająca konkretnej formy graficznej. |
| 14 | Mapy schematyczne i trendy | **CZĘŚĆ** | §9 Etap 1 przewiduje krzywe udziałów. Map bibliometrycznych (współwystępowanie terminów, sieci współautorstwa) plan nie przewiduje — i słusznie, bo pytanie badawcze ich nie wymaga. Warto to w metodach uzasadnić, zamiast pominąć milczeniem. |
| 15 | Tabelaryzacja i podsumowanie wyników | **PLAN** | Forma tabel nie jest jeszcze ustalona; BIBLIO daje cztery dopuszczalne układy. Do rozstrzygnięcia po Etapie 1, gdy będą znane liczebności. |
| 16 | Synteza wyników, wskazanie luki, propozycja modelu lub hipotezy | **CZĘŚĆ** | Luka jest sformułowana w §1 i doprecyzowana w zadaniu 1.5. Model dyfuzji celowo pozostaje eksploracyjny (§7). |

## Dyskusja

| # | Pozycja | Ocena | Uwagi |
|---|---|---|---|
| 17 | Podsumowanie głównych ustaleń w przystępnych kategoriach | **PLAN** | Wymagalne w manuskrypcie. |
| 18 | Interpretacja spójna z wynikami | **PLAN** | Wymagalne w manuskrypcie. |
| 19 | Mocne strony i ograniczenia | **CZĘŚĆ** | §11 i rozproszone zastrzeżenia (m.in. „publikacja ≠ adopcja kliniczna") dają solidną podstawę, ale nie są zebrane w jednej sekcji. Przy pisaniu manuskryptu skonsolidować. |
| 20 | Wnioski: ogólna interpretacja wobec pytań i celów, implikacje | **PLAN** | Wymagalne w manuskrypcie. |

---

## Podsumowanie ilościowe

| ocena | liczba pozycji |
|---|---|
| TAK | 6 |
| CZĘŚĆ | 5 |
| PLAN | 5 |
| LUKA | 3 |
| n/d | 1 |

Trzy luki wymagające decyzji przed Etapem 1 lub przy pisaniu: **poz. 1** (typ badania w tytule),
**poz. 10** (deduplikacja PMID między baseline a updatefiles), **poz. 13** (diagram przepływu).
Z nich tylko poz. 10 ma konsekwencje dla liczb — pozostałe dwie są redakcyjne.

---

## Luki w samym standardzie

Trzy elementy krytyczne dla trafności tego badania **nie mają odpowiednika w żadnej z 20 pozycji
BIBLIO**. Nie jest to przeoczenie po naszej stronie — to ograniczenie wytycznej, i jeden
z argumentów pracy.

**1. Walidacja strategii wyszukiwania.** Poz. 7 wymaga *opisania* słów kluczowych, a poz. 11
dotyczy oceny jakości włączonych prac, nie trafności zapytania. Żadna pozycja nie wymaga
podania precyzji ani czułości klasyfikatora. Przegląd bibliometryczny może zatem być w pełni
zgodny z BIBLIO, opierając się na zapytaniu o nieznanym PPV. Plan raportuje PPV per rodzina
i per epoka (§6.1) — ponad wymóg.

**2. Normalizacja.** Poz. 13 wylicza „liczby publikacji, lata, typy dokumentów, kraje, metryki
wpływu" — same wielkości bezwzględne. Żadna pozycja nie wymaga podania mianownika ani
uzasadnienia jego wyboru. Ponieważ PubMed rośnie sam z siebie, liczby bezwzględne rosną zawsze,
a przegląd raportujący wyłącznie je jest zgodny z BIBLIO i jednocześnie nieinformatywny.
Plan liczy udział w polu i osobno udział pola w zadeklarowanym podzbiorze (§7).

**3. Zmiana terminologii w czasie.** Żadna pozycja nie odnosi się do niezmienniczości pomiaru.
Poz. 7 traktuje słowa kluczowe jako zbiór statyczny. Dla przeglądu obejmującego dwie dekady jest
to założenie fałszywe — słownik zbudowany na dzisiejszym języku zmierzy zmianę nazewnictwa i
nazwie ją zmianą zjawiska. Plan wprowadza warstwy epokowe synonimów i PPV liczony osobno
w epokach (§6.1).

Dodatkowo, ale słabiej: BIBLIO nie odnosi się do **dryfu samego słownika kontrolowanego**.
Deskryptory MeSH wchodzą do słownika w różnych latach i rekordy zwykle nie są reindeksowane
wstecz. Dotyczy to nie tylko licznika (co plan rozpoznaje w §6), lecz także **definicji pola**:
z 56 deskryptorów poddrzewa `Orthopedic Procedures` **28 wprowadzono w 2006 r. lub później**.
Efekt jest w dużej mierze wygaszany przez to, że rozwijamy całe poddrzewo wraz z przodkami —
rekord z 2006 r. dostał wtedy istniejący deskryptor nadrzędny, również należący do pola.
Ryzyko resztkowe dotyczy rekordów, których jedynym deskryptorem z pola jest deskryptor młodszy
niż sam rekord. Jest to policzalne na Etapie 1 i tam należy to zaraportować.
