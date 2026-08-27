# Problem do rozstrzygnięcia: taksonomia rodzin technologii (§6.2)

Autor: sesja VS Code. Data: 2026-08-27. Dotyczy: `docs/protocol/plan_do_recenzji.md` §6.2.
Status: **do rozstrzygnięcia przed rejestracją**, nie do wykonania.

---

## 1. Problem w jednym zdaniu

§6.2 traktuje pięć rodzin technologii jako **płaski, równoległy zbiór** porównywany na wspólnym
mianowniku, ale nawigacja i robotyka nie są rodzeństwem — nawigacja jest **konstytutywna** dla
robota, a nie z nim współwystępująca.

Ustalenie dziedzinowe (PC, 2026-08-27): *„roboty korzystają z nawigacji — często to ich główna
rola"*. Robot ortopedyczny to system nawigacyjny plus człon wykonawczy, który dodatkowo ogranicza
albo wykonuje ruch. Zdolność bazowa — rejestracja śródoperacyjna, tracking, prowadzenie — jest
w obu ta sama.

## 2. Dlaczego to jest istotne, a nie kosmetyczne

Uderza dokładnie w twierdzenie, które jest **nowością pracy B**.

§1 pytanie 2 brzmi: czy rodziny rosną równolegle, czy jedne wypierają inne. To jest jedyne
z trzech pytań, którego **nie da się zadać bez wspólnego mianownika** — i dlatego to ono
uzasadnia całą konstrukcję pracy wobec 69 istniejących prac jednotechnologicznych.

Tymczasem **wyparcie między zbiorem a jego podzbiorem jest definicyjnie niemożliwe.** To, co
zobaczymy w danych jako „spadek nawigacji przy wzroście robotyki", będzie w znacznej części
**przemianowaniem wewnątrz jednej linii technologicznej**: pole przestaje pisać
`computer-assisted navigation`, zaczyna pisać `robotic-assisted`, a technologia bazowa trwa.

Ryzyko konkretne: przy płaskiej analizie pięciu rodzin najbardziej efektowny wykres w całej
pracy będzie artefaktem zmiany nazewnictwa. I będzie zgodny z narracją, która w ortopedii już
funkcjonuje („robotyka wyparła nawigację"), więc nikt go nie zakwestionuje.

To jest ten sam mechanizm, który §6.1 opisuje jako najpoważniejszy problem metodologiczny —
tylko działający **między rodzinami**, a nie wewnątrz jednej. §6.1 go nie łapie, bo zakłada,
że granice rodzin są dane.

## 3. Czego nie da się tym naprawić

- **Zawężenie słownika nawigacji.** Nakładanie się nie wynika ze złego doboru terminów, tylko
  z tego, że praca o robocie *zasadnie* używa języka nawigacyjnego. Zawężenie usunie prawdziwe
  trafienia, nie fałszywe.
- **Reguła pierwszeństwa** („trafia w obie → licz jako robotykę"). Arbitralna, a przy tym
  chowa zjawisko, które jest tu najciekawsze.

## 4. Opcje

**A. Płaskie pięć rodzin + reguła pierwszeństwa.**
Najprostsze. Odrzucam: arbitralne i zamiata problem.

**B. Płaskie pięć rodzin + rozkład na trzy krzywe** (tylko nawigacja / tylko robotyka / obie).
Zachowuje informację i pozwala odróżnić wchłonięcie od wyparcia: spadek „tylko nawigacja"
przy wzroście „obie" = przemianowanie; przy wzroście „tylko robotyka" = rzeczywiste wyparcie.
Wada: nadal ramuje je jako konkurentów, czyli utrzymuje ontologicznie fałszywą strukturę.

**C. Rodzina nadrzędna „interwencja wspomagana komputerowo" z dwiema prespecyfikowanymi
warstwami** (nawigacja bez członu wykonawczego / robotyka).
Do porównania międzyrodzinnego wchodzi rodzina nadrzędna — zostają wtedy **cztery rzeczywiście
równoległe rodziny**: interwencja wspomagana komputerowo, druk 3D, AI, biomateriały.
Wewnątrz rodziny obie warstwy raportowane osobno, zawsze, nigdy scalone bez śladu.
Mechanizm **już jest w planie**: §6.2 przewiduje hierarchię dla druku 3D, a §6.1 przewiduje
raportowanie krzywych synonimów wewnątrz rodziny jako materiału diagnostycznego. Tu chodzi
o zastosowanie tego samego o poziom wyżej.

**D. Usunąć nawigację.**
Odrzucam z dwóch powodów: to jedyna rodzina, która prawdopodobnie **spada**, a bez rodziny
opadającej pytanie 2 nie ma odpowiedzi; oraz traci się najlepszy materiał demonstracyjny
dla tezy metodologicznej.

## 5. Co rozstrzygnie Etap 1, a czego nie

**Rozstrzygalne empirycznie, kilka minut po dedupie:**

- macierz nakładania się wszystkich rodzin — ile rekordów trafia w ≥2;
- czy „tylko nawigacja" faktycznie spada, i od kiedy;
- czy pozostałe rodziny są równoległe. Podejrzenie: **druk 3D ∩ biomateriały** jest następne
  w kolejce do tego samego zabiegu (drukowane rusztowania, implanty na miarę z powłokami).

**Nierozstrzygalne pomiarem — decyzja projektowa:**

- czy robotyka ⊂ nawigacja jest właściwą ontologią. To sąd dziedzinowy, nie wielkość mierzalna.
  Dane pokażą, jak bardzo się nakładają, ale nie powiedzą, czy *powinny* być jedną rodziną;
- czy recenzent ortopedyczny przyjmie scalenie. Robot **nie jest** nawigacją: dokłada
  ograniczanie i wykonanie, ma inny koszt, inny workflow i inną bazę dowodową;
- gdzie należy AR/VR.

## 6. Zagadnienia poboczne w tej samej sekcji

**AR/VR jest w złym miejscu.** Obecnie `augmented reality navigation, mixed reality` siedzą
w późnej warstwie nawigacji. Tymczasem znaczna część literatury AR/VR w ortopedii dotyczy
**szkolenia i edukacji**, nie prowadzenia śródoperacyjnego — widać to wprost w przesiewie
z 2026-08-26 (*XR technology applications in orthopedic field*, *extended reality in surgical
training*, *3D printing in medical education*). Trzy wyjścia: osobna szósta rodzina; wymóg
współwystąpienia z terminem śródoperacyjnym (`intraoperative`, `guidance`, `registration`,
`tracking`); albo wykluczenie prac szkoleniowych filtrem typu publikacji lub MeSH.

**`image-guided` jest zbyt szerokie** — w polu ortopedycznym łapie też biopsje i radioterapię
okołokostną. Do sprawdzenia na PPV epokowym, bo w warstwie wczesnej to jeden z głównych terminów.

## 7. Rekomendacja sesji VS Code

**Opcja C**, z bezwzględnym wymogiem raportowania obu warstw osobno.

Argument dodatkowy: przy C przejście nawigacja → robotyka staje się **przykładem
demonstracyjnym dla całej tezy metodologicznej**. Mamy udokumentowaną, datowaną zmianę
nazewnictwa przy ciągłej zdolności bazowej — najczystszy możliwy dowód, że słownik zbudowany
na dzisiejszym języku zmierzyłby zmianę nazwy i nazwał ją dyfuzją.

I wynik dla odbiorcy klinicznego: jeśli dane pokażą, że „robotyka wyparła nawigację" jest
w znacznej części przemianowaniem, to część wzrostu robotyki **przelicza po nowemu zdolność,
która istniała wcześniej**. Tego nie da się dostać z żadnej pracy jednotechnologicznej.

## 8. Pytania do rozstrzygnięcia

1. Czy opcja C przechodzi u recenzenta ortopedycznego, czy scalenie czyta się jako zacieranie
   klinicznie realnej różnicy między nawigacją a robotem?
2. Jeśli C — jak nazwać rodzinę nadrzędną? „Interwencja wspomagana komputerowo" jest opisowe,
   ale czy istnieje termin przyjęty w piśmiennictwie, którego nie znam?
3. AR/VR: szósta rodzina, wymóg współwystąpienia, czy wykluczenie prac szkoleniowych?
4. Czy przejście nawigacja → robotyka ma być **głównym** przykładem demonstracyjnym tezy
   o niezmienniczości, czy to przeciąża jeden wynik dwiema rolami naraz?
5. Czy macierz nakładania się rodzin ma być raportowana w pracy jako kontrola trafności?
   Żadna z 69 prac z przesiewu jej nie podaje — bo wszystkie są jednotechnologiczne
   i problem u nich nie występuje.
6. Czy zgoda, że to musi być zamknięte **przed** rejestracją, a nie po Etapie 2?
