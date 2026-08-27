# Emerging concepts in orthopaedic literature: distinguishing novelty from renaming
## Plan v0.8 · 2026-08-27 · Przemysław Czuma · zastępuje v0.7

> **Pierwsza wersja pisana po zobaczeniu danych.** v0.1–v0.7 powstawały przed Etapem 1; ta nanosi
> to, czego pomiar nie potwierdził. Zmiany: §4 (próg `y₀` to `max(θ, 5×baza)`, nie samo `θ`),
> §5 (dwie osie selekcji zamiast jednej), §8 (kodeks jako przesiew przed wyborem, nie etykieta po),
> §9 (rozkład kategorii jako wynik pierwszorzędny, dwie tabele), §10 (zapisany wynik bramy).
> §§1–3, 6–7, 8.1 i 11 bez zmian merytorycznych.
>
> **Wszystko, co tu dopisano na podstawie danych, dotyczy aparatu, nie wyniku.** Progi, osie
> selekcji i kolejność kroków są rozstrzygnięciami konstrukcyjnymi; żadna liczba opisująca
> zjawisko nie została po ich zobaczeniu zmieniona. Preregistracja musi to rozgraniczyć wprost
> — Etap 1 jest jawnie eksploracyjny i jego rola w projekcie aparatu jest do zadeklarowania.

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

### 1.1. Zakres tej pracy a praca metodologiczna

Ortopedia jest poligonem, nie przedmiotem — ale **szczegółowa metodologia zostaje dla osobnej
pracy metodologicznej** (dalej **praca A**). Linia podziału biegnie wzdłuż rozróżnienia
opisowe / normatywne, nie wzdłuż stopnia szczegółowości opisu.

**Tutaj:** detektor **jako zastosowany**. Progi, listy zamknięte, reguły kanonikalizacji i kodeks
osądu podane w całości — bo bez nich praca nie jest odtwarzalna, a odtwarzalność jest warunkiem
brzegowym, nie wkładem. Twierdzenie ma postać: *w piśmiennictwie ortopedycznym 2005–2025 tyle
a tyle wyłonień to przemianowania, nie nowe pojęcia* — fakt o polu, z którego wynika ostrzeżenie
metodologiczne.

**Do pracy A:** detektor **jako narzędzie**. Wrażliwość na dobór progów `θ`, długości okna
potwierdzenia i mnożnika bazowego; zachowanie na innych specjalnościach; porównanie z algorytmem
Kleinberga, którego tu świadomie nie używamy (§4); formalna walidacja. Do A idzie też cały
argument normatywny: luki w wytycznej BIBLIO (`biblio_checklist.md`), rozróżnienie między
normalizacją cytowań a normalizacją liczby publikacji oraz ramka patenty-kontra-publikacje
(`scoping_log.md`).

**Warunek, żeby praca A pozostała publikowalna po tej.** Nie może być „ten sam detektor, opisany
porządnie" — dostałaby zarzut uprzedniej publikacji. Musi wnieść co najmniej jedno z:
zastosowanie na kilku specjalnościach, walidację niezmienniczości detektora, albo ilościowe
pokazanie, o ile myli analiza nieodróżniająca przemianowania od nowości. Metody tej pracy piszemy
kompletnie, ale **bez rozwijania ogólnego argumentu** — inaczej praca A nie zostanie z czym.

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
liczebności pola z jawnym testem nieciągłości, a terminy z rokiem wyłonienia **od 2020 wzwyż**
oznaczone w tabeli jako obarczone tym ryzykiem.

**Korekta po pomiarze (2026-08-27) — mechanizm to nie MTIX.** Średnia liczba deskryptorów MeSH
na rekord spadła z 11,13 (2019) przez 9,01 (2021) do 7,63 (2022), po czym **wróciła** do 9,91
(2024) i 10,78 (2025). Trwałe przejście na algorytm w 2022 r. dałoby spadek utrzymujący się,
a nie powrót; do tego spadek zaczyna się w 2020, dwa lata przed MTIX. To wygląda na **opóźnienie
indeksowania** — najświeższe roczniki są niedoindeksowane w chwili zamrożenia baseline'u.

Druga definicja pola potwierdza, że dołek jest artefaktem: pole wg MeSH spada o 21 % od szczytu
(16 811 w 2020 → 13 310 w 2023) i nie odrabia tego do 2025, a pole wg czasopism o 12,5 %
(17 462 → 15 276) i **wraca w pełni** do 17 221 w 2025. Definicja czasopiśmiennicza nie potrzebuje
deskryptorów, więc widzi rekordy, których definicja MeSH jeszcze nie widzi.

Znacznik ryzyka opieramy więc na **zmierzonym szeregu** — gęstości MeSH dla def1 i odsetku
zaindeksowanych dla def2 — a nie na dacie wdrożenia MTIX. Uwaga symetryczna: def2 ma własny
artefakt na prawej krawędzi, bo odsetek rekordów zaindeksowanych w MEDLINE spada w niej
z 92,7 % (2024) przez 85,2 % (2025) do 54,8 % (2026). Żadna z definicji nie jest stabilna na
prawej krawędzi; są niestabilne w przeciwnych kierunkach.

**Definicje pokrywają się słabiej, niż zakładano:** Jaccard ≈ 0,31 stabilnie przez cały okres.
To nie są dwa pomiary tej samej rzeczy — def1 łapie prace o procedurach ortopedycznych w dowolnym
czasopiśmie, def2 wszystko z czasopism ortopedycznych, łącznie z reumatologią i naukami
podstawowymi. **Podstawowa jest def1** (decyzja 2026-08-27); def2 pozostaje analizą wrażliwości
i jedynym oknem na rekordy niezaindeksowane.

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
5. rozwinięcie skrótów z zamkniętej, preregistrowanej listy (TKA, THA, ORIF, ACL…)

**Kryterium wpisu na listę skrótów (2026-08-27).** Rozwijamy tam, gdzie tożsamość jest bezsporna
i częstość wysoka; zostawiamy osądowi z §8 tam, gdzie tożsamość jest sporna. Wieloznaczność jest
własnością semantyczną, nie częstościową — test „skrót częstszy niż jego pełna forma" wskazywał
`ACDF` i `PRP` (jednoznaczne, tylko rzadko pisane w pełnej formie), a przepuszczał `HA` i `RSA`
(naprawdę wieloznaczne). Usunięte po pomiarze: `ml` (mililitr, 1249 trafień wobec 1 dla „machine
learning" w latach 2005–2010), `mr` (magnetic resonance, 419), `dl` (decylitr, 181), `ha`, `rsa`,
`ar`, `xr` oraz `psi` i `cas` — te dwa dlatego, że rozwijają się na frazy rodziny CAOS, więc błąd
kontaminowałby jednocześnie licznik i poziom bazowy, a przy progu `max(θ, 5×baza)` podnosiłby
próg wykrycia. Nierozwinięty skrót nie znika: zostaje osobnym wierszem i idzie do osądu.
6. **zwijanie zagnieżdżonych n-gramów**: jeśli krótszy n-gram zawiera się w dłuższym, a ich
   zbiory rekordów mają Jaccarda ≥ 0,90 — zostaje dłuższy, bardziej swoisty

Listy zamknięte są częścią preregistracji, nie są rozszerzane po zobaczeniu wyników.

## 4. Detektor — moment take-off, nie porównanie końców

Porównanie pierwszego i ostatniego pięciolecia nie odróżnia terminu, który wystrzelił w 2012 r.
i od dekady jest wysoko, od terminu, który ruszył w 2024. To dwa różne zjawiska.

Szukamy **momentu wyłonienia**. Dla terminu o rocznym udziale w polu `s(y)`:

- **próg obecności** `θ` = 0,1 % rekordów pola w danym roku, przy minimum 5 pracach bezwzględnie
- **poziom bazowy** = średnia `s(y)` z lat 2005–2007
- **próg wykrycia terminu** = `max(θ, 5 × poziom bazowy)`
- **rok wyłonienia `y₀`** = pierwszy rok, w którym `s(y)` przekracza ten próg **i** utrzymuje się
  powyżej przez co najmniej 3 kolejne lata
- `y₀ ≤ 2023`, żeby zmieściły się trzy lata potwierdzenia

Zmiana wobec v0.7 (2026-08-27). Poprzednio próg był stały (`θ`), a mnożnik 5× sprawdzany osobno
w punkcie `y₀`. To gubiło terminy o niskiej, ale niezerowej bazie: `y₀` przyklejało się do
pierwszego przekroczenia progu **obecności**, więc test 5× był liczony na początku szeregu, gdzie
z definicji nie mógł przejść. Zmierzone: `robotic` rośnie z 0,17 % (2005) do 2,90 % (2025),
siedemnastokrotnie, i **nie był wykrywany**.

To nie jest nowy warunek, tylko ten sam wypowiedziany spójnie — dotychczasowy wyjątek „albo
poziom bazowy poniżej `θ/5`" jest przypadkiem szczególnym, bo wtedy `5 × baza < θ` i `max` wynosi
dokładnie `θ`. Stary warunek ilorazowy jest przez to subsumowany i znika jako osobny.

Termin jest **wschodzący**, jeśli `y₀` istnieje w oknie. Detektor daje **odpowiedź dwustanową
plus rok wyłonienia** — a `year of emergence` staje się osobną, użyteczną zmienną.

Reguła jest preregistrowana i przeliczalna ręcznie. **Świadomie nie używamy algorytmu Kleinberga** —
jest standardem w tej literaturze, ale ma parametry, których nie da się zwalidować, i nie jest
dobrze dopasowany do strumienia piśmiennictwa naukowego.

## 5. Trzy rzeczy, które trzeba trzymać osobno

**Detektor ≠ miara siły ≠ ranking.** Detektor mówi tylko: wschodzący / nie. Siła to trzy osobne
osie, których nie sprowadzamy do jednej liczby, bo wagi dobralibyśmy my. A skoro nie ma jednej
liczby, to **„50 najsilniejszych" nie istnieje** — trzeba innego, jawnego kryterium wyboru.

**Wybór do analizy pogłębionej — dwie osie, dwie tabele, bez ważenia.** Skoro §6 raportuje trzy
osie siły obok siebie zamiast sprowadzać je do rankingu, to selekcja też nie musi iść po jednej
osi.

| oś | miara | nazwa w pracy |
|---|---|---|
| obecność | udział w latach 2021–2025 | *50 emerging terms with the highest 2021–2025 prevalence* |
| przekroczenie | szczytowy udział ÷ próg wyłonienia tego terminu, czyli `max(θ, 5×baza)` z §4 | *50 emerging terms with the highest exceedance of their own emergence threshold* |

Druga miara nie wprowadza żadnej nowej stałej — dzieli osiągnięty pułap przez poprzeczkę, którą
detektor postawił temu właśnie terminowi. Czyta się wprost: „ile razy termin przekroczył własny
próg". Termin o wysokiej bazie ma poprzeczkę wysoko i musi urosnąć proporcjonalnie.

**Pomiar z 2026-08-27 potwierdza, że osie są niezależne:** korelacja Spearmana 0,454, a obie
pięćdziesiątki mają **1 wspólny termin na 50**. Sam ranking po obecności dawał pięćdziesiątkę
w 100% metodologiczną, z pierwszą technologią na pozycji 143.

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

### Kodeks jest PRZESIEWEM, nie etykietą doklejaną po wyborze

Zmiana wobec v0.7, wymuszona pomiarem z Etapu 1. Pierwotnie kodeks miał opisywać 50 terminów już
wybranych. Okazało się, że **na obu osiach selekcji pięćdziesiątka jest zdominowana przez
metodologię** — PROM, PRISMA, propensity score, web of science, minimal clinically important
difference, level of evidence — i nie jest to artefakt: po usunięciu mililitrów, roczników
i zagnieżdżonych n-gramów lista jest czysta. W piśmiennictwie ortopedycznym 2005–2025 zmiana
konwencji badawczej była po prostu większym zjawiskiem niż wejście którejkolwiek technologii.

Rozróżnienie technologia / nie-technologia musi więc zostać zrobione **jawnie**, a nie liczone
na to, że wypadnie z rankingu. Kolejność:

1. detektor (§4) → pełna lista terminów wschodzących;
2. uszeregowanie po obu osiach (§5);
3. **przesiew kodeksem** rzędu tysiąca najwyżej notowanych terminów, z kategorią
   `non-technological term` jako pełnoprawnym rozstrzygnięciem;
4. dopiero z tego — pięćdziesiątki do analizy pogłębionej.

Znane technologie siedzą na pozycjach 143, 159, 357, 417, 557, 854, 931, 1437, 2183, 2745, 2950
i 6809 wg obecności, więc przesiew musi objąć rząd tysiąca terminów, nie pięćdziesiąt. Da się to
rozbić: mechaniczne odsianie oczywistego szablonu abstraktu, ręczne kodowanie reszty.

**Rozkład kategorii w tym przesiewie jest wynikiem pierwszorzędnym, nie kosztem.** Zdanie
„na tysiąc najsilniejszych wyłonień w abstraktach ortopedycznych X% to metodologia, Y% technologia"
jest policzalne, nikt tego nie policzył, i dowodzi tezy o odróżnianiu nowości od nowej nazwy
mocniej niż jakikolwiek pojedynczy przykład przemianowania.

### Dwa przykłady demonstracyjne — kontrastowe, nie jeden

Kodeks pięciokategorialny trzeba pokazać na parze, która dowodzi, że kategorie faktycznie
**rozróżniają**, a nie tylko istnieją na liście. Jeden przykład niosący obie role naraz byłby
przeciążony.

| przykład | oczekiwana kategoria | co pokazuje |
|---|---|---|
| `rapid prototyping` → `3d printing` | `renaming` | ta sama rzecz, nowe słowo: technologia i wskazania bez zmian, zmienia się wyłącznie etykieta |
| `computer assisted surgery` / `surgical navigation` → `robotic assisted` | `conceptual evolution` | nowy termin opisuje częściowo nowe zjawisko wyrosłe ze starego: zdolność bazowa (rejestracja, tracking, prowadzenie) ciągła, dochodzi człon wykonawczy |

Druga para jest tu kluczowa, bo **wyparcie jest w niej definicyjnie niemożliwe**: robot ortopedyczny
zawiera nawigację jako składową konstytutywną, a nie współwystępującą. Naiwna analiza dwóch
równoległych rodzin wyprodukowałaby najbardziej efektowny wykres w całej pracy — „robotyka wyparła
nawigację" — i byłby to artefakt przemianowania, zgodny z narracją już funkcjonującą w ortopedii,
więc tym trudniejszy do zakwestionowania. Kategoria `conceptual evolution` istnieje dokładnie po to,
żeby ten przypadek dało się opisać bez zmuszania kodera do fałszywego wyboru.

**Oczekiwane kategorie są zapisane przed kodowaniem i podlegają falsyfikacji.** Jeśli koderzy
przypiszą inne, raportujemy to jako wynik, a nie poprawiamy kodeks pod oczekiwanie.

### 8.1. Przypisanie rodzin — warstwa prezentacyjna

Rodziny **nie są jednostką analizy** — jednostką jest termin kanoniczny (§3). Rodziny służą
wyłącznie do podświetlenia wierszy w tabeli 50 i do porównania międzyrodzinnego. Ale skoro
podświetlamy, ontologia musi być poprawna.

**Reguła rozstrzygająca, kiedy scalać, a kiedy tylko raportować przecięcie:**

- relacja **konstytutywna** (jedna technologia zawiera drugą jako składową niezbywalną)
  → **rodzina nadrzędna z warstwami**;
- relacja **współwystępująca** (dwie technologie bywają użyte razem, ale żadna nie zawiera
  drugiej) → **osobne rodziny, przecięcie raportowane w macierzy**, nigdy scalane.

**Rodzina nadrzędna: CAOS — computer-assisted orthopaedic surgery.** Termin ugruntowany, nie ukuty
na potrzeby tej pracy: towarzystwo CAOS-International działa od początku lat 2000., a nazwa
funkcjonuje w tytułach prac i czasopism.

| warstwa CAOS | zakres |
|---|---|
| `CAOS-nawigacja` | prowadzenie bez członu wykonawczego |
| `CAOS-robotyka` | prowadzenie z członem ograniczającym lub wykonującym |
| `CAOS-XR śródoperacyjne` | AR/MR z **wymogiem współwystąpienia** terminu śródoperacyjnego: `intraoperative`, `guidance`, `registration`, `tracking` |

Warstwy są **zawsze raportowane osobno** i w żadnym miejscu pracy nie pada twierdzenie, że robot
jest nawigacją. Twierdzimy wyłącznie, że dzielą zdolność bazową, więc porównanie międzyrodzinne
musi iść na poziomie nadrzędnym. Różnica kliniczna — człon wykonawczy, koszt, workflow, baza
dowodowa — zostaje w warstwach.

**XR szkoleniowe zostaje poza rodzinami.** Znaczna część literatury AR/VR w ortopedii dotyczy
szkolenia, nie prowadzenia śródoperacyjnego. Nie przesądzamy jednak jego statusu z góry: jeśli
jest realnym trendem, **detektor z §4 wyłowi je jako termin wschodzący** i dostanie własny wiersz
w tabeli 50. Konstrukcja v0.6 sprawia, że niczego tu nie tracimy przez powściągliwość.

**`image-guided` — flaga ryzyka.** Termin zostaje w zakresie CAOS, ale oznaczony: w polu
ortopedycznym łapie także biopsje i radioterapię okołokostną, a w warstwie wczesnej (2005–2011)
jest jednym z głównych terminów. **Jeśli PPV epokowy dla `image-guided` spadnie poniżej progu
w którejkolwiek epoce, termin dostaje wymóg współwystąpienia z terminem ortopedycznym.** Reguła
jest zapisana przed sprawdzeniem, nie dobierana po wyniku.

## 9. Produkt

1. **Rozkład kategorii osądu** na przesianym zbiorze (§8): ile procent najsilniejszych wyłonień
   to metodologia, ile technologia, ile artefakt pomiaru. Wynik pierwszorzędny.
2. **Dwie tabele po 50**, po jednej na oś selekcji z §5 — obecność i przekroczenie własnego progu.
   W każdej: rok wyłonienia, pułap, tempo, koncentracja, trwałość, kategoria osądu, znacznik
   ryzyka niedoindeksowania dla `y₀` od 2020 wzwyż.
2. Krzywe udziału dziesięciu o najwyższej obecności 2021–2025.
3. Rycina par przemianowań: stary opada, nowy rośnie, okno współwystępowania.
4. Panel wrażliwości: primary vs S1–S3 plus szeregi tła.
5. Diagram przepływu rekordów i terminów.
6. **Macierz nakładania się rodzin** — ile terminów i ile rekordów trafia w ≥2 rodziny,
   dla wszystkich par. Kontrola trafności, nie ciekawostka: bez niej „rodzina X rośnie kosztem Y"
   jest nieweryfikowalne. **Żadna z 69 prac bibliometrycznych o technologiach w ortopedii
   znalezionych w przeszukaniu 2026-08-26 jej nie podaje** — bo wszystkie są jednotechnologiczne
   i problem u nich nie występuje.

**Cztery nazwane rodziny** wchodzą jako podświetlone wiersze — porównanie z v0.4 jest tu zawarte,
nie utracone:

| rodzina | warstwy |
|---|---|
| **CAOS** (computer-assisted orthopaedic surgery) | nawigacja · robotyka · XR śródoperacyjne |
| druk 3D / wytwarzanie addytywne | hierarchia dopiero po Etapie 1 |
| sztuczna inteligencja | — |
| biomateriały i powłoki | — |

Cztery, nie pięć: nawigacja i robotyka są warstwami CAOS, nie osobnymi rodzinami (§8.1). Dopiero
po tym scaleniu pozostałe rodziny są **rzeczywiście równoległe**, a pytanie o wypieranie się
nawzajem ma sens.

Przecięcia **niekonstytutywne pozostają nieruszone**. Druk 3D ∩ biomateriały będzie zapewne
znaczne — drukowane rusztowanie z powłoką bioaktywną należy zasadnie do obu — i właśnie dlatego
idzie do macierzy, a nie do scalenia. Reguła z §8.1 rozstrzyga, który przypadek jest który.

## 10. Etap 1 — brama

Pole w obu definicjach, kanonikalizacja, szeregi udziałów, detektor, lista terminów wschodzących
z latami wyłonienia. Bez osądu, bez kodowania, bez rycin.

**Jeśli lista okaże się zdominowana przez terminy niebędące technologiami i artefakty, albo jeśli
liczba terminów wschodzących będzie jednocyfrowa — pracy nie ma.** Zapisane przed danymi.

### Wynik bramy — 2026-08-27

**Brama nie odrzuca pracy, ale przesuwa jej przedmiot.**

| kryterium | wynik |
|---|---|
| liczba terminów wschodzących | **7 662** z 245 081 (3,13%) — daleko od jednocyfrowej |
| artefakty | **usunięte**: mililitry mylone z `machine learning`, roczniki cytowane w abstraktach, zagnieżdżone n-gramy |
| dominacja terminów niebędących technologiami | **potwierdzona** — ale na czystej liście, nie przez artefakty |

Warunek odrzucenia był koniunkcją: dominacja nie-technologii **i** artefaktów. Artefaktów nie ma,
więc brama jest przejdziona — ale dominacja metodologii jest realna i zmienia konstrukcję pracy
(§5, §8).

**Detektor jest zwalidowany na przypadkach znanych z góry:** `patient specific instrumentation`
2013, `3d printing` 2014, `3d printed` i `patient specific` 2015, `robotic assisted` 2018,
`machine learning` i `augmented reality` 2019, `robotic`, `artificial intelligence`, `deep learning`
i `virtual reality` 2020, `convolutional neural network` 2022. Najmocniejszym testem jest
**odrzucenie**: `navigation` przy bazie 1,56% i pułapie 2,16% nie jest wschodząca — poprawnie,
bo w tym oknie już istniała. To wprost wspiera §8.1.

Liczby podstawy: pole def1 w oknie 2005–2025 to **268 383 rekordy**, z tekstem wyciągniętym
z pełnego lustra (nie z tabeli `msk`, która pokrywała tylko 90,74% pola i gubiła systematycznie
rekordy ubogie w tekst). 65,8 mln tokenów, 245 081 terminów powyżej progu 50 wystąpień.

## 11. Poza tą pracą

Klastrowanie osadzeń, lead–lag preprintów medRxiv, odtworzenie opublikowanych zapytań
z literatury.

**Materiał pracy A** (§1.1), nie tej: uogólnienie detektora na inne specjalności, analiza jego
wrażliwości na dobór progów, porównanie z algorytmem Kleinberga, krytyka wytycznej BIBLIO
i rozróżnienie normalizacji cytowań od normalizacji liczby publikacji.
