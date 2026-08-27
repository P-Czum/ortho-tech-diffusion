# Emerging concepts in orthopaedic literature: distinguishing novelty from renaming
## Plan v0.6 · 2026-08-26 · Przemysław Czuma · zastępuje v0.5

> **We distinguish emergence of terminology from emergence of concepts.**

Bibliometria rutynowo myli pojawienie się nowego słowa z pojawieniem się nowego zjawiska.
Ortopedia jest poligonem, nie przedmiotem — teza jest metodologiczna i przenosi się na dowolną
specjalność.

---

## 1. Pytania

1. Które pojęcia w piśmiennictwie ortopedycznym **wyłoniły się** między 2005 a 2025 i **w którym roku**?
2. Jak silne było wyłonienie — jak szeroko, jak szybko, jak wysoko?
3. **Czy to była nowość, czy nowa nazwa starej rzeczy?**

Mierzymy uwagę naukową, nie adopcję kliniczną.

## 2. Dane i pole

PubMed Baseline 2026 + updatefiles, lustro lokalne, po deduplikacji (`analytic_index`).
Lata 2005–2025; 2026 wyłączony jako niekompletny. Mianownikiem jest zawsze pole w danym roku.

**Definicja podstawowa:** `Orthopedic Procedures` + potomne deskryptory MeSH (56, rozwijane
programowo z `desc2026.xml`).

**Zagrożenie strukturalne — przerwa w 2022.** MEDLINE przeszedł w 2022 r. na indeksowanie
automatyczne algorytmem MTIX (sieć neuronowa); ludzka kuratela obejmuje jedynie wybrane zbiory,
a NLM nie deklaruje zastosowania wstecznego. Zmienił się więc **mechanizm decydujący o tym,
czy rekord wpada do naszego pola** — dokładnie w okresie, w którym szukamy najświeższych trendów.

Stąd **obowiązkowa druga definicja pola, niezależna od indeksowania MeSH**: czasopisma z NLM
Broad Subject Term „Orthopedics". Każdy wynik raportowany w obu definicjach. Dodatkowo szereg
liczebności pola z jawnym testem nieciągłości w 2022 r., a terminy z rokiem wyłonienia
2021–2023 oznaczone w tabeli jako obarczone tym ryzykiem.

## 3. Jednostka: termin kanoniczny

N-gramy 1–3 z tytułu i streszczenia. Próg wejścia: ≥50 wystąpień w całym okresie.

Termin, nie klaster — całą wartość tej pracy daje to, że każde wykrycie da się przeczytać i osądzić.

### 3.1. Kanonikalizacja — preregistrowana, przed detekcją

Bez tego `3d printing`, `three dimensional printing`, `dimensional printing` i `printing`
policzą się jako cztery odrębne trendy, a praca o odróżnianiu nowego zjawiska od nowego słowa
zacznie klasyfikować fleksję jako innowację.

1. małe litery, usunięcie interpunkcji, dywiz → spacja
2. warianty cyfrowo-słowne z zamkniętej listy (`3d` = `3-d` = `three dimensional`)
3. liczba mnoga → pojedyncza, regułowo
4. warianty brytyjsko-amerykańskie z zamkniętej listy (`orthopaedic`/`orthopedic`)
5. rozwinięcie skrótów z zamkniętej, preregistrowanej listy (PSI, CAS, TKA…)
6. **zwijanie zagnieżdżonych n-gramów**: jeśli krótszy n-gram zawiera się w dłuższym, a ich
   zbiory rekordów mają Jaccarda ≥ 0,90 — zostaje dłuższy, bardziej swoisty

Listy zamknięte są częścią preregistracji, nie są rozszerzane po zobaczeniu wyników.

## 4. Detektor — moment take-off, nie porównanie końców

Porównanie pierwszego i ostatniego pięciolecia nie odróżnia terminu, który wystrzelił w 2012 r.
i od dekady jest wysoko, od terminu, który ruszył w 2024. To dwa różne zjawiska.

Szukamy **momentu wyłonienia**. Dla terminu o rocznym udziale w polu `s(y)`:

- **próg obecności** `θ` = 0,1 % rekordów pola w danym roku, przy minimum 5 pracach bezwzględnie
- **rok wyłonienia `y₀`** = pierwszy rok, w którym `s(y) ≥ θ` **i** utrzymuje się `≥ θ`
  przez co najmniej 3 kolejne lata
- dodatkowo `s(y₀) ≥ 5 ×` poziom bazowy (średnia 2005–2007), albo poziom bazowy poniżej `θ/5`
- `y₀ ≤ 2023`, żeby zmieściły się trzy lata potwierdzenia

Termin jest **wschodzący**, jeśli `y₀` istnieje w oknie. Detektor daje **odpowiedź dwustanową
plus rok wyłonienia** — a `year of emergence` staje się osobną, użyteczną zmienną.

Reguła jest preregistrowana i przeliczalna ręcznie. **Świadomie nie używamy algorytmu Kleinberga** —
jest standardem w tej literaturze, ale ma parametry, których nie da się zwalidować, i nie jest
dobrze dopasowany do strumienia piśmiennictwa naukowego.

## 5. Trzy rzeczy, które trzeba trzymać osobno

**Detektor ≠ miara siły ≠ ranking.** Detektor mówi tylko: wschodzący / nie. Siła to trzy osobne
osie, których nie sprowadzamy do jednej liczby, bo wagi dobralibyśmy my. A skoro nie ma jednej
liczby, to **„50 najsilniejszych" nie istnieje** — trzeba innego, jawnego kryterium wyboru.

**Wybór do analizy pogłębionej:** 50 terminów wschodzących o najwyższym **udziale w latach
2021–2025**. W pracy nazywane wprost: *50 emerging terms with the highest 2021–2025 prevalence*.

## 6. Siła — trzy osie, raportowane obok siebie

**Szerokość dyfuzji piśmienniczej** (nie „adopcji" — autor publikacji nie jest dowodem, że ktoś
tak operuje). Mierzona **koncentracją, nie liczebnością**: liczba autorów rośnie z liczbą prac
niemal automatycznie, więc 2 000 prac zawsze „pobije" 100. Raportujemy:

- udział najpłodniejszego pierwszego autora
- udział największego kraju
- udział największego czasopisma
- efektywna liczba krajów i czasopism (odwrotność HHI)

Różnica między „największy ośrodek odpowiada za 4 % prac" a „za 48 %" to jest różnica między
dyfuzją a dorobkiem jednej grupy.

**Tempo wzrostu.** Nachylenie udziału w fazie wzrostu, czas podwojenia.

**Osiągnięty pułap.** Maksymalny roczny udział w polu.

Dodatkowo, opisowo, nie jako składnik siły: **trwałość** — czy udział się utrzymuje, czy opada.

## 7. Analizy wrażliwości na dostępność tekstu

Szansa trafienia angielskiego n-gramu w `tytuł + streszczenie` **sama rośnie w czasie**:
udział rekordów ze streszczeniem rósł przez cały okres, a udział angielskiego wzrósł
z **90,44 %** (2005–2009) do **97,14 %** (2020–2023). Bez tego testu recenzent słusznie powie,
że część wyłonień to po prostu więcej tekstu do przeszukania.

| | podstawa tekstowa |
|---|---|
| primary | tytuł + streszczenie |
| S1 | tylko tytuł |
| S2 | tylko rekordy ze streszczeniem — **licznik i mianownik jednocześnie** |
| S3 | tylko rekordy anglojęzyczne |

Osobno raportujemy dla samego pola trzy szeregi tła: odsetek rekordów ze streszczeniem, udział
angielskiego, średnią długość streszczenia. Wniosek utrzymuje się tylko wtedy, gdy termin rośnie
we wszystkich czterech wariantach.

## 8. Rdzeń: nowość czy nowa nazwa

Dla wybranych 50 terminów szukamy **kandydata na poprzednika**: terminu, którego udział opada
w tym samym okresie i który **współwystępuje** z kandydatem w pracach z lat przejściowych.
Przemianowanie ma charakterystyczny kształt — stary wysoko i opada, nowy rośnie, a przez kilka
lat oba pojawiają się w tych samych pracach („rapid prototyping (3D printing)").

Problem jest realny także w słowniku kontrolowanym: NLM sam ostrzega, że nowe deskryptory MeSH
zwykle **nie są przypisywane wstecznie**, i zaleca sprawdzanie wcześniejszych terminów używanych
dla danego pojęcia.

Statystyka podaje kandydatów; **rozstrzygnięcie jest ręczne**, na podstawie przeczytanych prac
z lat przejściowych. **Pięć kategorii:**

| kategoria | znaczenie |
|---|---|
| `novel concept` | nowe zjawisko |
| `renaming` | ta sama rzecz pod nową nazwą |
| `conceptual evolution` | nowy termin opisuje częściowo nowe zjawisko wyrosłe ze starego |
| `measurement artifact` | zmiana indeksowania, dostępności tekstu, praktyk redakcyjnych |
| `non-technological term` | metoda statystyczna, typ badania, termin ogólny |

Kategoria trzecia jest konieczna: `custom implant → patient-specific implant` albo
`computer-assisted surgery → surgical navigation` nie są prostym przemianowaniem, a zmuszanie
kodera do wyboru „nowość albo przemianowanie" produkowałoby sztuczne rozstrzygnięcia.

Kodeks spisany, podpróba kodowana niezależnie przez drugą osobę, zgodność κ.
**To jest walidacyjny rdzeń pracy, nie dodatek.**

## 9. Produkt

1. Tabela 50 terminów: rok wyłonienia, pułap, tempo, koncentracja, trwałość, kategoria osądu,
   znacznik ryzyka MTIX dla `y₀` w latach 2021–2023.
2. Krzywe udziału dziesięciu o najwyższej obecności 2021–2025.
3. Rycina par przemianowań: stary opada, nowy rośnie, okno współwystępowania.
4. Panel wrażliwości: primary vs S1–S3 plus szeregi tła.
5. Diagram przepływu rekordów i terminów.

Pięć nazwanych rodzin technologii (druk 3D, robotyka, nawigacja, AI, biomateriały) wchodzi jako
podświetlone wiersze — porównanie z v0.4 jest tu zawarte, nie utracone.

## 10. Etap 1 — brama

Pole w obu definicjach, kanonikalizacja, szeregi udziałów, detektor, lista terminów wschodzących
z latami wyłonienia. Bez osądu, bez kodowania, bez rycin.

**Jeśli lista okaże się zdominowana przez terminy niebędące technologiami i artefakty, albo jeśli
liczba terminów wschodzących będzie jednocyfrowa — pracy nie ma.** Zapisane przed danymi.

## 11. Poza tą pracą

Klastrowanie osadzeń, lead–lag preprintów medRxiv, odtworzenie opublikowanych zapytań
z literatury, uogólnienie detektora na inne specjalności.
