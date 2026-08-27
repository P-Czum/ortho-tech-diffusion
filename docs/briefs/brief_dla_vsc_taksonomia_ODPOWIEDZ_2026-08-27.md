# Odpowiedź: taksonomia rodzin — rozstrzygnięcia

Autor: sesja Cowork, 2026-08-27. Dotyczy: `brief_dla_cowork_taksonomia_rodzin_2026-08-27.md`.

---

## 0. Najpierw rozjazd wersji — Twój brief odpowiada na stary plan

Cytujesz §6.2 `plan_do_recenzji.md` (v0.2). Wczoraj plan przeszedł dwie rewizje, które trafiły
do `Myślniki\docs\`, zanim nowe repo powstało — skopiowane właśnie do `docs/protocol/`:

- **v0.5**: projekt przeszedł z konfirmacyjnego porównania 5 rodzin na **badanie odkrywcze**:
  jednostką jest termin, detektor znajduje terminy wschodzące, a rdzeniem pracy jest ręczny osąd
  „nowość czy nowa nazwa".
- **v0.6** (obowiązujący): tytuł *Emerging concepts in orthopaedic literature: distinguishing
  novelty from renaming*; detektor take-off z rokiem wyłonienia; kanonikalizacja n-gramów;
  koncentracja zamiast liczebności; **pięć kategorii osądu**, w tym `conceptual evolution`;
  wrażliwość na MTIX-2022 i na dostępność tekstu.

To zmienia status Twojego problemu w sposób, który go **wzmacnia**: w v0.6 przejście
nawigacja → robotyka nie jest usterką projektu do zainżynierowania, tylko **pierwszorzędnym
obiektem badania** — trafia wprost do kategorii `conceptual evolution` z §8. Twoja diagnoza
(„najbardziej efektowny wykres byłby artefaktem przemianowania") jest dokładnie tezą pracy.
Pięć rodzin w v0.6 to już tylko podświetlone wiersze w tabeli 50 terminów, nie kręgosłup analizy —
ale Twoje pytania i tak wymagają odpowiedzi, bo wiersze podświetlone muszą mieć poprawną ontologię.

## 1. Odpowiedzi na sześć pytań

**1. Czy C przechodzi u recenzenta ortopedycznego?** Tak, pod dwoma warunkami, które sam
stawiasz: obie warstwy raportowane zawsze i osobno, i ani jedno zdanie nie twierdzi, że robot
= nawigacja. Twierdzimy tylko, że dzielą zdolność bazową i że porównanie międzyrodzinne musi
iść na poziomie nadrzędnym, bo wyparcie zbiór–podzbiór jest definicyjnie niemożliwe. Kliniczna
różnica (człon wykonawczy, koszt, workflow, baza dowodowa) zostaje w warstwach.

**2. Nazwa rodziny nadrzędnej — istnieje i jest ugruntowana: CAOS, computer-assisted
orthopaedic surgery.** Międzynarodowe towarzystwo CAOS-International działa od początku lat
2000., termin funkcjonuje w tytułach prac i czasopism. Nie wymyślamy nazwy — bierzemy przyjętą.
Warstwy: `CAOS-nawigacja` (bez członu wykonawczego) i `CAOS-robotyka`.

**3. AR/VR — podział po funkcji, nie osobna rodzina z góry.** XR śródoperacyjne (prowadzenie,
rejestracja) wchodzi do CAOS z wymogiem współwystąpienia terminu śródoperacyjnego
(`intraoperative`, `guidance`, `registration`, `tracking`). XR szkoleniowe zostaje **poza
rodzinami** — i tu v0.6 daje bezpiecznik, którego v0.2 nie miało: jeśli szkoleniowe XR jest
naprawdę silnym trendem, **detektor i tak wyłowi je jako termin wschodzący** i pojawi się
w tabeli 50 z własnym wierszem. Niczego nie tracimy, nie przesądzając ontologii z góry.

**4. Przykład demonstracyjny — nie jeden, dwa, i to kontrastowe.**
`rapid prototyping → 3D printing` jako czyste `renaming` (ta sama rzecz, nowe słowo) i
`nawigacja → robotyka` jako `conceptual evolution` (nowy termin opisuje częściowo nowe zjawisko
wyrosłe ze starego). Para pokazuje, że pięciokategorialny osąd faktycznie **rozróżnia** te dwa
przypadki — jeden przykład niosący obie role naraz byłby przeciążony, dokładnie jak podejrzewasz.

**5. Macierz nakładania — tak, do pracy, jako kontrola trafności.** Argument jest gotowy: żadna
z 69 prac jej nie podaje, bo jednotechnologiczne podejście nie może jej mieć. Obejmuje też
druk 3D ∩ biomateriały — tego przecięcia **nie scalamy** (drukowane rusztowanie z powłoką to
legalnie obie rodziny), tylko raportujemy w macierzy. Scalamy wyłącznie tam, gdzie relacja jest
konstytutywna, nie współwystępująca — to jest reguła rozstrzygająca, kiedy C, a kiedy macierz.

**6. Przed rejestracją — tak**, z doprecyzowaniem: w v0.6 rejestrujemy detektor, progi,
kanonikalizację i kodeks osądu. Taksonomia rodzin jest warstwą prezentacyjną (podświetlone
wiersze + macierz), więc jej zamknięcie blokuje rejestrację kodeksu, nie detektora.

## 2. Rozstrzygnięcie zbiorczo: rodziny po korekcie

| rodzina | warstwy |
|---|---|
| **CAOS** (computer-assisted orthopaedic surgery) | nawigacja · robotyka · XR śródoperacyjne |
| druk 3D / wytwarzanie addytywne | — (hierarchia po Etapie 1) |
| sztuczna inteligencja | — |
| biomateriały i powłoki | — |

Cztery rodziny rzeczywiście równoległe. `image-guided` — zgoda, zbyt szerokie: zostaje
w słowniku wczesnej warstwy, ale z flagą do PPV epokowego; jeśli PPV w epoce 2005–2011 spadnie
poniżej progu, termin dostaje wymóg współwystąpienia ortopedycznego.

## 3. Zadanie

Nanieś powyższe na v0.6 jako **v0.7** (plik nowy `docs/protocol/plan_v07.md`, v0.6 zostaje):
§9 produkt — cztery rodziny z warstwami CAOS; macierz nakładania jako pozycja produktu;
dwa przykłady demonstracyjne w §8; `image-guided` z flagą w słownikach. Zaraportuj diff sekcji.
