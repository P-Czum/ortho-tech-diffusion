# Etap 1 wykonany — raport zwrotny

Autor: sesja VS Code, 2026-08-27. Dotyczy: `brief_dla_vsc_taksonomia_ODPOWIEDZ_2026-08-27.md`
oraz całego Etapu 1 z §10 planu.

Format wg §4 briefu z 2026-08-26: krótko, liczbami, konkretne komunikaty błędów.

---

## 0. Zadanie z twojego briefu — wykonane, plus jeden krok dalej

v0.7 naniesione zgodnie ze zleceniem: dwa przykłady demonstracyjne w §8, nowa §8.1 z rodziną
nadrzędną CAOS i regułą konstytutywne/współwystępujące, macierz nakładania jako pozycja produktu,
`image-guided` z flagą. Diff: 118 linii dodanych, 4 usunięte, §§2–7 i 10 nietknięte.

Po nim powstało **v0.8** — pierwsza wersja pisana **po zobaczeniu danych**. Zmiany w §2, §4, §5
i §8 są wymuszone pomiarem i opisane niżej.

**Rozjazd wersji, dla porządku.** Twój brief mówi, że v0.5 i v0.6 „trafiły do `Myślniki\docs\`
zanim nowe repo powstało". Daty modyfikacji obu plików to **05:04 dzisiaj**, a mój brief
o taksonomii powstał o 05:00. Nie odpowiadałem więc na stary plan — tych wersji nie było, gdy
pisałem. Bez znaczenia dla treści, ale niech łańcuch będzie prawdziwy. Osobno: **nie ma pliku
v0.4**, choć v0.5 deklaruje, że go zastępuje, a v0.6 §9 się na niego powołuje.

## 1. Werdykt bramy z §10

**Brama nie odrzuca pracy, ale przesuwa jej przedmiot.**

| kryterium odrzucenia | wynik |
|---|---|
| liczba terminów wschodzących jednocyfrowa | **nie** — 7 662 z 245 081 (3,13%) |
| dominacja terminów niebędących technologiami **i** artefaktów | artefaktów **nie ma**, dominacja nie-technologii **jest** |

Warunek był koniunkcją, więc brama przechodzi. Ale dominacja metodologii jest realna i na czystej
liście: po usunięciu wszystkich znalezionych artefaktów pierwsza pięćdziesiątka to `cohort`,
`were included`, `95 ci`, `systematic review`, `retrospective cohort`, PROM, PRISMA. **Pierwsza
technologia lądowała na pozycji 143.**

W piśmiennictwie ortopedycznym 2005–2025 zmiana konwencji badawczej była po prostu większym
zjawiskiem niż wejście którejkolwiek technologii. To jest wynik, nie usterka.

## 2. Pole — liczby i jedna korekta merytoryczna

**Definicja podstawowa (MeSH):** 406 309 rekordów, **0,99% całego PubMedu**. W oknie 2005–2025:
**268 383**. Rocznie od 7 858 (2005) do 16 811 (2020).

**Definicja druga (czasopisma):** 137 tytułów z Broad Subject Term „Orthopedics", zapytanie
`orthopedics[st]` w NLM Catalog, odtwarzalne przez `code/nlm_broad_subject.py`.

**Definicje pokrywają się znacznie słabiej, niż zakładano: Jaccard ≈ 0,31, stabilnie przez cały
okres.** To nie są dwa pomiary tej samej rzeczy — def1 łapie prace o procedurach ortopedycznych
w dowolnym czasopiśmie, def2 wszystko z czasopism ortopedycznych, łącznie z reumatologią
i naukami podstawowymi. **Przemek rozstrzygnął: def1 podstawowa.**

### Korekta: mechanizm dołka po 2020 to NIE MTIX

§2 przypisywała nieciągłość automatycznemu indeksowaniu wdrożonemu w 2022. Pomiar temu przeczy.

**Średnia liczba deskryptorów MeSH na rekord:** 11,13 (2019) → 9,01 (2021) → **7,63 (2022)** →
9,91 (2024) → **10,78 (2025)**.

Trwałe przejście na algorytm dałoby spadek **utrzymujący się**, a nie powrót. Do tego spadek
zaczyna się w **2020**, dwa lata przed MTIX. To wygląda na **opóźnienie indeksowania** — najświeższe
roczniki są niedoindeksowane w chwili zamrożenia baseline'u.

Potwierdza to druga definicja, niezależna od deskryptorów: pole wg MeSH spada o **21%** od szczytu
(16 811 → 13 310) i nie odrabia tego do 2025, a pole wg czasopism o **12,5%** (17 462 → 15 276)
i **wraca w pełni** do 17 221.

**Konsekwencja:** znacznik ryzyka w §2 był skalibrowany na lata 2021–2023. To jest źle w obie
strony — zaczyna rok za późno i kończy się, zanim zniekształcenie wygasa. W v0.8 opiera się
na **zmierzonym szeregu**, nie na dacie wdrożenia, i obejmuje `y₀` **od 2020 wzwyż**.

**Uwaga symetryczna:** def2 ma własny artefakt na prawej krawędzi — odsetek rekordów
zaindeksowanych w MEDLINE spada w niej z 92,7% (2024) przez 85,2% (2025) do **54,8% (2026)**.
Żadna z definicji nie jest stabilna na prawej krawędzi; są niestabilne w przeciwnych kierunkach.

### Trzy liczby, o które prosiłeś

**`indexed` kontra `medline_indexed` — nie są identyczne.** Na 41 mln wierszy: 4 767 rekordów ma
MeSH bez statusu MEDLINE, a **353 ma status MEDLINE bez ani jednego deskryptora**. Razem 5 120,
czyli 0,012%. Kolumny nie są redundantne, choć wybór między nimi praktycznie nie zmienia
mianownika. Te 353 to anomalia warta osobnego spojrzenia.

**Odsetek z abstraktem — artefakt na końcu szeregu.** W polu: 86,4% (2005) → 92,1% (2019) →
95,6% (2024) → **99,9% (2025)**. Skok o cztery punkty w jednym roku i wartość praktycznie
stuprocentowa to właściwość świeżych rekordów, nie trend.

**`PubmedBookArticle`: zero.** W próbce 210 000 rekordów rozłożonej po całym baseline, od `n0001`
do `n1201`. Moja wcześniejsza hipoteza, że siedzą w wysokich PMID-ach, była błędna — w tym wydaniu
baseline ich po prostu nie ma. Pominięcie przez parser jest bezkosztowe.

## 3. Tekst pola — dlaczego osobny przebieg

Tabela `msk` pokrywa tylko **90,74%** pola; brakujące **9,26% (24 860 rekordów)** nie ma tekstu.

**Te braki nie są losowe.** Sito MSK zbudowano ze słownika dzisiejszego języka, więc rekordy,
które przez nie nie przeszły, to nieproporcjonalnie te o nietypowej terminologii — czyli populacja,
w której żyją terminy wschodzące. Detektor oparty na `msk` byłby obciążony **w stronę słownictwa
ugruntowanego**, czyli miałby dokładnie tę wadę, której praca dotyczy.

Stąd `code/extract_field_text.py`: 268 383 rekordy z pełnego lustra, 0 braków wobec celu.
Konstrukcja warta odnotowania — `analytic_index` niesie kolumnę `_src`, więc **każdy worker czyta
tylko PMID-y, dla których jego plik jest zwycięski po dedupie**. Zero etapu scalania i zero ryzyka,
że ekstrakcja rozjedzie się z dedupem w wyborze wersji rekordu.

Wynik: 9,10% rekordów pola bez abstraktu — liczba niemal identyczna z 9,26% wypadających z sita,
co potwierdza diagnozę.

## 4. Cztery poprawki wymuszone pomiarem (v0.8)

### §4 — próg `y₀` to `max(θ, 5 × baza)`, nie samo `θ`

Stara reguła gubiła terminy o niskiej, ale niezerowej bazie: `y₀` przyklejało się do pierwszego
przekroczenia progu **obecności**, więc test 5× był liczony na początku szeregu, gdzie z definicji
nie mógł przejść.

**Zmierzone: `robotic` rośnie z 0,17% (2005) do 2,90% (2025), siedemnastokrotnie — i NIE był
wykrywany.**

To nie jest nowy warunek, tylko ten sam wypowiedziany spójnie. Dotychczasowy wyjątek „albo baza
poniżej `θ/5`" jest przypadkiem szczególnym: wtedy `5×baza < θ` i `max` wynosi dokładnie `θ`.

### §5 — dwie osie selekcji zamiast jednej

Ranking po obecności strukturalnie gwarantuje tabelę szablonów: technologie żyją przy 0,2–2%
obecności, szablon abstraktu przy 4–18%. Druga oś to **przekroczenie własnego progu wyłonienia**,
czyli pułap dzielony przez `max(θ, 5×baza)` — bez żadnej nowej stałej.

**Osie są niezależne: Spearman 0,454, jeden wspólny termin na 50.**

### §8 — kodeks jako przesiew PRZED wyborem, nie etykieta po

Rozróżnienie technologia / nie-technologia musi być zrobione jawnie. Znane technologie siedzą na
pozycjach 143, 159, 357, 417, 557, 854, 931, 1437, 2183, 2745, 2950 i 6809, więc etykietowanie
pięćdziesiątki po wyborze nie dotknęłoby żadnej.

**Rozkład kategorii w przesiewie jest wynikiem pierwszorzędnym, nie kosztem.**

### §2 — opisane wyżej

## 5. Trzy artefakty znalezione i usunięte

**Skrót `ml` rozwijany na `machine learning`.** W latach 2005–2007 **zero** dosłownych „machine
learning", za to 524 rekordy z „ml", w tym 416 z liczbą — mililitry. Termin miał przez to fałszywe
2,19% w 2005 i nie był wykrywany jako wschodzący.

Usunięte po pomiarze: `ml` (1249 trafień skrótu wobec 1 pełnej formy w latach 2005–2010),
`mr` (magnetic resonance, 419 wobec 0), `dl` (decylitr, 181), `ha`, `rsa`, `ar`, `xr`.
Osobno `psi` i `cas` — te dlatego, że rozwijają się na frazy rodziny CAOS, więc błąd
kontaminowałby **jednocześnie licznik i poziom bazowy**, a przy nowym progu podnosiłby próg
wykrycia. Szkoda szłaby w dwie strony naraz.

**Metodologiczna uwaga, którą warto zapisać:** mój automatyczny test wieloznaczności („skrót
częstszy niż jego pełna forma") **mylił się w obie strony**. Wskazywał `ACDF` i `PRP` jako
podejrzane — a są jednoznaczne, tylko rzadko pisane w pełnej formie — i przepuszczał `HA` oraz
`RSA`, naprawdę wieloznaczne. **Wieloznaczność jest własnością semantyczną, nie częstościową.**

**Cytowane roczniki jako terminy.** 15 z 50 pozycji to `2020`, `2019`, `2018`…; 28,2% wszystkich
wschodzących zawierało samodzielną liczbę. Reguła: tokeny czterocyfrowe z zakresu 1900–2100 jako
**separator**, nie wycinane ze sklejeniem sąsiadów — inaczej „published in 2015 and followed"
produkuje nieistniejący bigram. Objęło 176 181 wystąpień.

**Zagnieżdżone n-gramy** (reguła 6 z §3.1, wcześniej niezaimplementowana): 8 334 zwinięte.
Uproszczenie warte odnotowania — jeśli krótszy n-gram zawiera się w dłuższym, to każdy dokument
z dłuższym zawiera krótszy, więc `docs(dłuższy) ⊆ docs(krótszy)` i **Jaccard redukuje się do
ilorazu liczby dokumentów**. Dokładnie, bez trzymania w pamięci ~100 mln par termin–dokument.

## 6. Detektor — zwalidowany

| termin | `y₀` | | termin | `y₀` |
|---|---|---|---|---|
| patient specific instrumentation | 2013 | | machine learning | 2019 |
| 3d printing | 2014 | | augmented reality | 2019 |
| 3d printed, patient specific | 2015 | | robotic, AI, deep learning, VR | 2020 |
| robotic assisted | 2018 | | convolutional neural network | 2022 |

**Najmocniejszym testem jest odrzucenie:** `navigation` przy bazie 1,56% i pułapie 2,16% **nie
jest wschodząca** — poprawnie, bo w tym oknie już istniała. To wprost wspiera §8.1: nawigacja nie
wyłoniła się, ona była, a robot ją wchłonął.

## 7. Warianty wrażliwości z §7 — wynik bardzo dobry

| wariant | rekordów | terminów | wschodzących |
|---|---|---|---|
| podstawowy | 268 383 | 245 081 | 7 662 |
| S1 tylko tytuły | 268 383 | 17 583 | **607** |
| S2 tylko z abstraktem | 243 966 | 244 026 | 7 537 |
| S3 tylko angielski | 248 159 | 228 644 | 7 569 |

**Część wspólna czterech wariantów: 287 terminów.**

**Przyrost dostępności tekstu nie napędza wykryć** — S2 i S3 pokrywają się z podstawowym w 92,7%
i 90,2%. To był największy zarzut przewidziany w §7 i odpada.

**Wszystkie główne technologie przechodzą wszystkie cztery warianty.** Odpadają wyłącznie
`convolutional neural network`, `prom` i `prisma` — i tylko na S1, bo nie występują w tytułach.

Zmiana konstrukcyjna: **mianownik jest teraz zapisywany jawnie** przez kanonikalizację i czytany
przez detektor. Dla S2/S3 podstawa jest zawężona i gdyby licznik szedł po podzbiorze, a mianownik
po całym polu, oba rozjechałyby się dokładnie w wariantach, które ten rozjazd wykrywają.

**Dwa zastrzeżenia do §7.** S1 nie jest kontrolą odporności, tylko **istotnym filtrem
merytorycznym** — wymaga 0,1% *tytułów*, a tytuł ma ~12 słów. Trzeba to nazwać po imieniu
w metodach. I ma fałszywie negatywne: `convolutional neural network` to prawdziwa technologia
wschodząca, tylko opisywana w abstrakcie. Proponuję raportować dwa zbiory — 287 przechodzących
wszystko oraz osobno odpadające wyłącznie na S1.

## 8. Arkusz do kodowania — gotowy

`data/processed/coding_sheet.csv`: **287 terminów, 274 z kandydatem na poprzednika (95%)**.
Na termin: szereg, `y₀`, szczyt, obecność, kandydaci z liftem, po trzy tytuły z okolic `y₀`
i z lat 2023–2025, puste kolumny `kategoria` / `poprzednik` / `uwagi`. **Maszyna nie proponuje
żadnej kategorii.**

Kandydat wybierany przez **lift**, nie przez sam spadek — najsilniej opadają słowa ogólne
(`degree`, `because`, `problem`), które współwystępują ze wszystkim i mają lift ~1.

**Algorytm sam znalazł oba przykłady demonstracyjne z §8, nie wiedząc, że ma ich szukać:**

| termin | najsilniejszy kandydat | lift |
|---|---|---|
| `3d printing` | **rapid prototyping** | **52,1** |
| `robotic` | `computer navigation`, `navigated total knee` | 15,9 / 20,7 |
| `augmented reality` | `the navigation system`, `computer assisted surgery` | 73,4 / 44,8 |

**Błąd, który przy tym naprawiłem, i lekcja z niego.** Pierwsza wersja nie znalazła
`rapid prototyping` dla `3d printing` — odrzucił go mój próg `MIN_CO=10`, bo współwystąpień jest
tylko **5**. Przy liftcie 52,1, najwyższym w zbiorze.

Powód jest strukturalny i wart zapisania w metodach: **prawdziwa para przemianowania jest z natury
rzadka w liczbach bezwzględnych**, bo stary termin umiera dokładnie wtedy, gdy nowy się rodzi —
okno nakładania jest cienkie z definicji. Próg liczności ustawiony dla tłumienia szumu wyciął
najsilniejszy sygnał w badaniu. **Tłumienie szumu należy do progu lift, nie do liczności.**

**Interpretacja pustej listy kandydatów.** `machine learning`, `virtual reality`, `deep learning`
i `artificial intelligence` dostają kandydatów bezwartościowych albo żadnych. To jest poprawne —
te technologie **nie mają poprzednika**, bo są nowe. Pusta lista jest sygnałem wskazującym na
`novel concept`, nie brakiem danych. Warto zapisać jako regułę interpretacyjną w kodeksie.

## 9. Stan repo

`D:\Claude\Projects\ortho-tech-diffusion`, gałąź `main`, drzewo czyste.

| commit | zakres |
|---|---|
| `c2d8956` | pierwszy commit, narzędzia i protokół |
| `858a018` | Etap 1: pole, kanonikalizacja, detektor, plan v0.8 |
| `ea26ad5` | warianty wrażliwości S1–S3 |
| `af4dda4` | arkusz do kodowania z kandydatami na poprzednika |

Repo `myslniki` nietknięte: `7f2ae16`, wszystkie 249 niezacommitowanych zmian na miejscu.

## 10. Do rozstrzygnięcia

1. **Czy raportujemy dwa zbiory** — 287 przechodzących wszystkie warianty oraz osobno odpadające
   wyłącznie na S1? Argument za: „nie ma go w tytułach" znaczy co innego niż „to artefakt".
2. **Nazwanie S1 po imieniu w metodach** jako filtru merytorycznego, nie analizy wrażliwości.
3. **Reguła interpretacyjna dla pustej listy kandydatów** w kodeksie z §8.
4. **Osie siły z §6** wymagają zbiorów rekordów per termin — do zaprojektowania, wykonalne dla
   287 terminów jednym przebiegiem.
5. **Pełny bieg na def2** — §2 wymaga raportowania w obu definicjach, a przy Jaccardzie 0,31 to
   będą realnie inne listy, nie potwierdzenie.
6. **Brak pliku v0.4** i odsyłacze do niego w v0.5 i v0.6 §9.
