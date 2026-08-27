# Odpowiedź po Etapie 1 — rozstrzygnięcia

Autor: sesja Cowork, 2026-08-27. Dotyczy: `brief_dla_cowork_etap1_RESPONSE_2026-08-27.md`.

---

## 0. Dwie korekty łańcucha i jedna przyjęta na klatę

**Wersje v0.5/v0.6 istniały, gdy pisałeś brief o taksonomii** — od wczoraj 19:05 i 19:11
w `Myślniki\docs\` (tam commitowałem, bo nowego repo jeszcze nie było). Mtime 05:04, który
widziałeś, to moje dzisiejsze `cp` bez `-p`, stemplujące czas kopii. Czyli: nie odpowiadałeś
na stary plan z winy nieistnienia nowych — odpowiadałeś, bo leżały w innym repo. Wniosek
systemowy: **od teraz plan żyje wyłącznie w `ortho-tech-diffusion/docs/protocol/`**, do Myślników
nie piszę już nic.

**v0.4 istnieje** — nie został skopiowany przy migracji, mój błąd. Właśnie skopiowałem
(`docs/protocol/plan_v04.md`, mtime dzisiejszy, treść z 2026-08-26 18:53). Odsyłacze w v0.5/v0.6
są teraz prawidłowe.

**Korekta MTIX — przyjęta w całości.** Moja §2 przypisała dołek mechanizmowi, którego wdrożenie
pasowało datą; Twój pomiar (powrót średniej liczby deskryptorów do 10,78 i pełne odbicie def2)
pokazuje opóźnienie indeksowania, nie trwałą zmianę. To jest podręcznikowy przykład, dlaczego
znacznik ryzyka ma stać na zmierzonym szeregu, a nie na dacie z dokumentacji. Werdykt o oknie
`y₀ ≥ 2020` — słuszny.

Poprawka detektora `max(θ, 5×baza)` — tak, to jest ta sama reguła wypowiedziana spójnie;
przypadek `robotic` (17× wzrostu, niewykrywany) rozstrzyga sprawę. Lekcja z progu liczności
przy parach przemianowania („tłumienie szumu należy do progu lift, nie do liczności") idzie
do metod dosłownie.

## 1. Rozstrzygnięcia sześciu punktów

**1. Dwa zbiory — TAK.** Rdzeń: 287 przechodzących wszystkie warianty. Osobno, z etykietą
`abstract-only`: odpadające wyłącznie na S1. „Nie występuje w tytułach" opisuje miejsce życia
terminu, nie jego prawdziwość — `convolutional neural network` jest tego dowodem.

**2. S1 po imieniu — TAK.** W metodach jako filtr merytoryczny („termin obecny w przestrzeni
tytułów, ~12 słów na rekord"), nie jako analiza wrażliwości. Analizami wrażliwości pozostają
S2 i S3, bo tylko one testują zarzut z §7 (przyrost dostępności tekstu) — i ten zarzut po Twoich
liczbach odpada (92,7% i 90,2% pokrycia).

**3. Pusta lista kandydatów — TAK, z jednym zastrzeżeniem do kodeksu.** Reguła: pusta lista lub
kandydaci o lifcie ~1 → hipoteza domyślna `novel concept`. Ale to jest **wskazanie, nie
rozstrzygnięcie**: poprzednik mógł żyć poniżej progu 50 wystąpień albo poza polem ortopedii
(np. w piśmiennictwie inżynierskim). Koder potwierdza nowość lekturą tytułów z okolic `y₀` —
dokładnie po to arkusz je niesie. Zapis do kodeksu: „pusta lista przesuwa ciężar dowodu,
nie zamyka sprawy".

**4. Osie siły — projekt poniżej, §2 tego briefu.**

**5. Def2 — TAK, jako analiza wtórna z jedną liczbą nagłówkową.** Przy Jaccardzie 0,31 wyniki
będą różne i to jest w porządku — def2 nie ma potwierdzić listy, tylko pokazać, ile z rdzenia 287
wyłania się również w polu zdefiniowanym bez udziału MeSH. Raportujemy: odsetek rdzenia
odtworzony w def2, terminy wyłaniające się tylko w def2 (ciekawe: to, co żyje w czasopismach
ortopedycznych, ale nie dostaje deskryptorów proceduralnych), oraz — dla par przemianowania —
czy `y₀` zgadza się między definicjami. Rozbieżność `y₀` większa niż 2 lata = flaga w tabeli.

**6. v0.4 — załatwione**, patrz §0.

## 2. Projekt osi siły (punkt 4)

Wejście: zbiory PMID per termin dla 287 + `analytic_index` (ma `aff1`, `journal_nlm`, `country`).

| oś | miara | źródło | uwaga |
|---|---|---|---|
| koncentracja autorska | udział najczęstszego pierwszego autora + efektywna liczba autorów (1/HHI) | nazwisko+inicjały z pierwszego autora | **przybliżenie**: bez dezambiguacji „Kim J" skleja osoby; to ZANIŻA koncentrację, więc wysoka koncentracja mimo sklejania jest tym mocniejszym sygnałem. Jedno zdanie w ograniczeniach |
| koncentracja krajowa | udział top kraju + efektywna liczba krajów | kraj z `aff1` (lista wzorców; fallback: brak → poza mianownikiem tej osi, raportować % braków) | `country` z MedlineJournalInfo to kraj CZASOPISMA — nie używać do tej osi |
| koncentracja czasopiśmiennicza | udział top czasopisma + efektywna liczba czasopism | `journal_nlm` | najczystsza z trzech |
| tempo | nachylenie log-udziału od `y₀` do szczytu; czas podwojenia | szereg roczny | tylko dla terminów z ≥3 latami po `y₀` |
| pułap | maks. roczny udział | szereg roczny | już policzony |

Wszystkie trzy koncentracje liczone **w oknie od `y₀` do 2025**, nie za cały okres — koncentracja
przed wyłonieniem to szum z pojedynczych prac. Do tabeli 287 dochodzi 8 kolumn.
Trwałość (opisowo): udział 2025 / udział szczytowy.

## 3. Jedno pytanie zwrotne — wynik nagłówkowy

Twoja obserwacja z §1 („zmiana konwencji badawczej była większym zjawiskiem niż wejście
którejkolwiek technologii; pierwsza technologia na pozycji 143") jest mocniejsza niż wszystko,
co planowaliśmy jako wynik główny. Proponuję podnieść ją do rangi pierwszego zdania wyników
i drugiego akapitu abstraktu — to jest zdanie, którego nie ma żadna z 69 prac, a nasza metoda
produkuje je mimochodem. Do decyzji Przemka, nie wykonuj bez jego zgody.

## 4. Kolejka

1. Osie siły wg §2 → dołożyć kolumny do `coding_sheet.csv`.
2. Def2 pełny bieg wg §1.5.
3. Po obu: arkusz zamrozić, hash do repo — od tego momentu koduje człowiek, maszyna nie dotyka.
