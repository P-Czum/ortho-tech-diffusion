# Log scoping search

Zapis odtwarzalny — idzie do metod. Każde zapytanie z bazą, datą i liczbą trafień.

## Pytanie

> Czy istnieje praca porównująca **wiele technologii** w **jednej specjalności klinicznej**
> na **wspólnym, znormalizowanym mianowniku** (udział w polu, nie liczby bezwzględne)?

Data przeszukania: **2026-08-26**. Wykonał: sesja VS Code (Claude Opus 5).

## Bazy — co odpytano, czego nie

| baza | status | uwagi |
|---|---|---|
| **PubMed** | **odpytana programowo** | NCBI E-utilities `esearch.fcgi`, `db=pubmed`. Pełna odtwarzalność: ciągi zapytań poniżej dają te same liczby przy powtórzeniu. |
| **Wyszukiwanie otwarte (web)** | **wykonane** | Uzupełnienie o literaturę metodologiczną spoza PubMedu. Nie jest to przeszukanie bazy bibliograficznej i nie może być tak raportowane. |
| **Scopus** | **NIE odpytana** | Brak dostępu subskrypcyjnego w tym środowisku. |
| **Web of Science** | **NIE odpytana** | Brak dostępu subskrypcyjnego. |
| **Google Scholar** | **NIE odpytana** | Blokuje zapytania automatyczne; ręczne przeszukanie nie byłoby odtwarzalne w tym logu. |
| **Dimensions** | **NIE odpytana** | Wymaga konta do API; interfejs webowy nie daje zapisywalnego ciągu zapytania. |
| **OpenAlex** | **odpytana programowo** | REST API, `api.openalex.org/works`. Otwarta, bez subskrypcji, pełne ciągi zapytań odtwarzalne. Dodana jako zamiennik dla nieodpytanych baz — pokrywa czasopisma metodologiczne bibliometrii, których PubMed nie indeksuje. |

**Status: rozpoznanie wstępne wzmocnione, nadal nie pełne.** Scopus i WoS pozostają nieodpytane
i przy publikacji trzeba je uzupełnić lub jawnie zadeklarować ich brak jako ograniczenie.
Natomiast kluczowa dziura pierwszej wersji tego logu — brak pokrycia literatury metodologicznej
bibliometrii — została zamknięta przez OpenAlex, który indeksuje *Scientometrics* (8 493 prace),
*JASIST* (2 327), *Journal of Informetrics* (1 721) i *Quantitative Science Studies* (473),
łącznie 13 014 prac praktycznie nieobecnych w PubMedzie.

## Zapytania PubMed

Wszystkie: `db=pubmed`, bez ograniczenia daty i języka, `retmax` wg potrzeby.

| # | ciąg zapytania | trafień |
|---|---|---|
| Q1 | `bibliometric[tiab] AND (technolog*[tiab] OR innovation[tiab]) AND (diffusion[tiab] OR adoption[tiab])` | 192 |
| Q2 | `bibliometric[tiab] AND ("proportion of publications"[tiab] OR "share of publications"[tiab] OR "percentage of publications"[tiab])` | **0** |
| Q3 | `(bibliometric[tiab] OR scientometric[tiab]) AND (orthopaedic*[tiab] OR orthopedic*[tiab]) AND (technolog*[tiab] OR innovation[tiab])` | 69 |
| Q4 | `(bibliometric[tiab] OR scientometric[tiab]) AND "technology diffusion"[tiab]` | 1 |
| Q5 | `(bibliometric[tiab] OR scientometric[tiab]) AND (denominator[tiab] OR normali*[tiab]) AND (specialty[tiab] OR field[tiab])` | 118 |
| Q6 | `(bibliometric[tiab] OR scientometric[tiab]) AND ("multiple technologies"[tiab] OR "emerging technologies"[tiab]) AND (surger*[tiab] OR surgical[tiab])` | 18 |
| Q7 | `bibliometric[tiab] AND ("relative to all"[tiab] OR "as a proportion"[tiab] OR "normalized by"[tiab])` | **0** |
| Q8 | `(bibliometric[tiab] OR scientometric[tiab]) AND ("comparative analysis"[tiab]) AND technolog*[tiab] AND (specialty[tiab] OR speciality[tiab])` | 1 |
| Q9 | `(bibliometric[tiab] OR scientometric[tiab]) AND (robot*[tiab] AND "3D printing"[tiab] AND (artificial intelligence[tiab] OR navigation[tiab]))` | 2 |
| Q10 | `"innovation diffusion"[tiab] AND (publication*[tiab] OR literature[tiab]) AND (medicine[tiab] OR surgical[tiab] OR clinical[tiab])` | 5 |
| Q11 | `(bibliometric[tiab] OR scientometric[tiab]) AND "share of"[tiab] AND (field[tiab] OR discipline[tiab])` | 63 |
| Q12 | `bibliometric*[ti] AND (multiple[ti] OR comparative[ti] OR across[ti]) AND technolog*[ti]` | 2 |

## Przesiew

Tytuły przejrzano w całości dla Q3 (69), Q6 (18), Q4 (1), Q8 (1), Q9 (2), Q10 (5), Q12 (2).
Q1, Q5 i Q11 nie były przesiewane tytuł po tytule — do zrobienia przy pełnym przeszukaniu.

**Żadna praca nie spełnia wszystkich trzech warunków pytania.** Trafienia rozkładają się na
cztery powtarzalne typy, z których żaden nie zajmuje luki:

1. **Jedna technologia w jednej specjalności** — zdecydowana większość. Przykłady: *Global
   research hotspots and emerging trends in orthopedic robotic surgery* (2026), *The impact of
   3D printing in orthopedics and traumatology* (2025), *Artificial intelligence in shoulder and
   elbow surgery* (2026), *XR technology applications in orthopedic field* (2025). Wszystkie
   raportują liczby bezwzględne i mapy współwystępowania, żadna nie liczy udziału w polu.
2. **Rankingi „top-N najczęściej cytowanych"** — np. *Top 100 most-cited systematic reviews on
   robotic-assisted orthopaedic surgery* (2026), *Top 50 Spine Surgery Publications Most Cited
   by Patents* (2024). Mianownik z definicji nie występuje.
3. **Mapowanie hotspotów / knowledge mapping** — VOSviewer i CiteSpace, wynik jakościowy.
4. **Analizy sieci cytowań innowacji** — najbliższy pojęciowo: *Network analysis of surgical
   innovation: measuring value and the virality of diffusion in robotic surgery*
   (PMID 28841648, 2017). Mierzy dyfuzję, ale jednej technologii i przez sieć cytowań,
   nie przez udział w produkcji pola.

**Q2 = 0 i Q7 = 0** są najmocniejszym pojedynczym sygnałem: w całym PubMedzie nie ma rekordu,
który w tytule lub abstrakcie łączyłby „bibliometric" z „proportion / share / percentage of
publications" albo z „relative to all / as a proportion / normalized by". Zerowa liczba trafień
nie dowodzi nieistnienia takich prac — dowodzi, że nie nazywają tego w tytule ani abstrakcie.

## Zapytania OpenAlex

API: `https://api.openalex.org/works`, parametr `mailto` dla polite pool. Identyfikatory źródeł
rozwiązane z ISSN: Scientometrics `S148561398` (0138-9130), JASIST `S4210197613` (2330-1635),
Quantitative Science Studies `S4210195326` (2641-3337), Journal of Informetrics `S205292342`
(1751-1577). Skrót `BIB` niżej oznacza `primary_location.source.id:` z tymi czterema
połączonymi znakiem `|`.

| # | filtr | trafień |
|---|---|---|
| O1 | `BIB,title_and_abstract.search:"technology diffusion"` | 10 |
| O2 | `BIB,title_and_abstract.search:"share of publications"` | 32 |
| O3 | `BIB,title_and_abstract.search:"proportion of publications"` | 12 |
| O4 | `BIB,title_and_abstract.search:"medical specialty"` | 7 |
| O5 | `BIB,title_and_abstract.search:"innovation diffusion"` | 9 |
| O6 | `title_and_abstract.search:"share of publications" AND specialty` | 11 |
| O7 | `title_and_abstract.search:"emerging technologies" AND bibliometric AND surgery` | 28 |
| O8 | `title_and_abstract.search:"technology diffusion" AND bibliometric AND clinical` | **0** |

Przesiano tytuł po tytule: O1, O3, O4, O5, O6 (49 rekordów). O2 i O7 do przesiewu przy
pełnym przeszukaniu.

### Ustalenie mocniejsze niż samo „nie ma takiej pracy"

Przesiew O1 i O3 pokazuje, że obie połowy naszego podejścia **istnieją w literaturze
bibliometrycznej, ale w rozłącznych nurtach**:

**„Technology diffusion" w bibliometrii to zjawisko patentowe.** Wszystkie 10 trafień O1 mierzy
dyfuzję przez **cytowania patentów**: *Exploring the patterns of international technology
diffusion in AI from the perspective of patent citations* (Scientometrics 2021), *Does prior
knowledge affect patent technology diffusion?* (J Informetrics 2023), *Dynamic patterns of AI
technology diffusion: focusing on time series clustering and patent analysis* (Scientometrics
2025). Ani jedna nie mierzy dyfuzji przez udział w produkcji publikacyjnej pola.

**„Proportion of publications" występuje, ale w pytaniach dyscyplinarno-demograficznych.**
Wszystkie 12 trafień O3 dotyczy udziałów w podziale na dyscypliny, kraje, płeć albo model
otwartego dostępu: *Changing publication patterns in the Social Sciences and Humanities*
(2012), *Gender gap in medical research* (2020), *A big picture: bibliometric study of academic
publications from post-Soviet countries* (2021). Normalizacja udziału publikacji jest więc
w bibliometrii narzędziem znanym — ale nie stosuje się jej do adopcji technologii.

**O8 = 0.** W całym OpenAlex nie ma pracy łączącej „technology diffusion" z „bibliometric"
i „clinical" w tytule lub abstrakcie.

O4 dał jedno trafienie warte odnotowania jako sąsiedztwo historyczne — *A bibliometric analysis
of collaboration in a medical specialty* (Scientometrics 1991) — ale mierzy współautorstwo,
nie technologie. O6 zwrócił wyłącznie szum (edytoriale, teksty niezwiązane).

**Wniosek.** Luka polega nie na tym, że nikt nie liczył udziałów ani nikt nie badał dyfuzji
technologii, tylko na tym, że **te dwa nurty się nie spotkały**: dyfuzję technologii mierzy się
patentami, a udziały publikacyjne liczy się dla dyscyplin i demografii. Zastosowanie udziału
w polu jako miary dyfuzji technologii wewnątrz specjalności klinicznej nie ma precedensu
w żadnym z nich.

To ma bezpośrednią konsekwencję dla wstępu: trzeba zacytować nurt patentowy i uzasadnić, czemu
mierzymy publikacjami, a nie patentami. Uzasadnienie jest merytoryczne, nie wygodnościowe —
technologie chirurgiczne dyfundują też przez zmianę praktyki, techniki operacyjne i wskazania,
których się nie patentuje, więc patent jako jednostka pomiaru systematycznie pomija część
zjawiska.

## Zastrzeżenie, które recenzent podniesie

Bibliometria **ma** ugruntowaną normalizację dziedzinową — MNCS, SNIP, prace Moeda i Waltmana.
Twierdzenie „nikt nie normalizuje" byłoby wobec tego łatwe do obalenia i **nie należy go
formułować**.

Rozróżnienie jest takie: standardowa normalizacja dziedzinowa normalizuje **liczbę cytowań**
publikacji względem średniej w dziedzinie, żeby porównywać wpływ między dziedzinami o różnej
kulturze cytowania. Tutaj normalizujemy **liczbę publikacji** — udział produkcji pola poświęcony
technologii X — żeby oddzielić dyfuzję technologii od wzrostu samego pola i bazy. Inny licznik,
inny mianownik, inne pytanie. To rozróżnienie musi paść wprost we wstępie, bo bez niego praca
wygląda na nieświadomą istniejącego dorobku.

## Do dokończenia

- Przeszukać Scopus i Web of Science (wymaga dostępu instytucjonalnego) albo zadeklarować
  ich brak jako ograniczenie przeszukania.
- Przesiać tytuły Q1 (192), Q5 (118), Q11 (63), O2 (32), O7 (28).
- Sprawdzić, czy nurt patentowy dyfuzji technologii ma odpowiednik dla technologii
  medycznych — zapytanie o patenty w ortopedii, jako kontrapunkt dla naszej miary.

---

# 2026-08-31 — rdzeń bez S1 i klasyfikacja fraz. Zapis decyzji projektowych

Gałąź frazowa jest **eksploracyjna** — powstała po odstąpieniu od kodowania ręcznego i nie jest
objęta rejestracją OSF. Dwunastka zamrożonych plików nietknięta. Poniższe decyzje trzeba mimo to
zapisać, bo zapadły **po zobaczeniu wyników**, a nie przed.

## D1. S1 (wariant tytułowy) przestaje współokreślać rdzeń

**Było:** rdzeń = część wspólna czterech wariantów (primary ∩ S1 ∩ S2 ∩ S3) = **47 fraz**.
**Jest:** rdzeń = primary ∩ S2 ∩ S3 = **813 fraz**; S1 raportowany jako czułość.

**Powód.** S1 nie ocenia trwałości terminu, tylko obcina słownik. Tytuł daje 4,2 chunku,
streszczenie 61,7. Przy niezmienionym progu ≥ 50 słownik S1 ma 1 882 frazy wobec 25 419
w primary i wyłania 85 wobec 936. Część wspólna czterech wariantów nie może przekroczyć 85.
S1 usuwał 94,2% rdzenia — mechanicznie, nie merytorycznie.

**Koszt decyzji, zmierzony.** Rezygnacja z S1 wpuszcza z powrotem klasę śmieci, którą S1 odsiewał
przy okazji: gołe liczebniki jako chunki (`0 0`, `10 1`, `13 9`) — 32 pozycje na 813 (3,9%),
fraz z samodzielną liczbą 60 (7,4%). Zgłoszone przez VS Code w §6 briefu z 28.08.

**Kontrola przeciwko naciąganiu.** Rozszerzenie rdzenia z 47 do 100 pozycji po rankingu **nie
wpuszcza technologii** — pozycje 48–100 to `p value`, `iqr`, `hazard ratio`, `auc`,
`propensity score matching`, `prisma guideline`, `google scholar`. Decyzja D1 nie została podjęta,
żeby dołożyć technologie do listy; technologie leżą głęboko (3d printing 287, PSI 411, VR 513,
AR 559) i wchodzą dopiero przez D2.

## D2. Klasyfikacja fraz: model proponuje, ortopeda rozstrzyga

Po odstąpieniu od kodowania ręcznego (287 terminów, kompletność załamała się) rola człowieka
zmienia się z kodera na **rozjemcę**. Sesja Cowork przypisała kategorię wszystkim 813 frazom;
ortopeda poprawia i to jego wersja jest zapisem. Narzędzie: `code/mapa_ui.html` (offline,
dane wbudowane, eksport CSV).

Kategorie i liczności propozycji:

| kategoria | n | na mapie |
|---|---:|:--:|
| metoda badawcza / artefakt | 450 | nie |
| skala, kwestionariusz, PROM | 67 | nie |
| wynik, punkt końcowy | 46 | nie |
| parametr radiologiczny | 42 | przełącznik |
| czynnik pacjenta | 12 | przełącznik |
| organizacja opieki | 28 | przełącznik |
| niejasne (skróty wieloznaczne) | 10 | przełącznik |
| **rozpoznanie** | **63** | tak |
| **technika operacyjna** | **56** | tak |
| **technologia** | **30** | tak |
| **lek** | **9** | tak |

Kryterium mapy postawione przez ortopedę: *nazwy badań, skal i metod badawczych wykluczone;
zostają terminy medyczne i ortopedyczne — rozpoznanie, leczenie, technologia.*

Skróty sklejone z pełnymi formami przez ręczną tabelę `data/processed/np_synonimy.tsv`
(125 par: `clti` = chronic limb threatening ischemia, `txa` = tranexamic acid itd.).

**Mapa kliniczna po odsianiu i sklejeniu: 96 pozycji** — 34 rozpoznania, 34 techniki,
21 technologii, 7 leków.

## D3. Obserwacja, która wymaga własnego sprawdzenia

Trzy pozycje mapy tworzą jedną historię: `metal debris` (y₀ 2012), `adverse local tissue reaction`
(y₀ 2014), `mom total hip arthroplasty` (y₀ 2014, prevalence 2021–25 = 0,018%). Metal-on-metal:
technologia wchodzi, pojawiają się powikłania, technologia wypada. Detektor złapał wejście
i wycofanie bez podpowiedzi. Jeśli to się potwierdzi na krzywych rocznych, jest to mocniejsze
twierdzenie niż sama mapa nowości — metoda widzi **wycofania**, nie tylko wejścia.
Do sprawdzenia przed użyciem w tekście.

## Pliki

`data/processed/core813_np_ranking.csv`, `np_kategorie_propozycja.tsv`, `np_synonimy.tsv`,
`np_mapa_propozycja.csv`, `code/build_mapa_ui.py`, `code/mapa_ui.html`.

---

# 2026-08-31, wieczorem — chirurgia naczyniowa w polu ortopedycznym. Defekt definicji D1

Zauważone przez ortopedę przy oglądaniu list: nieproporcjonalnie dużo terminów dotyczy
niedokrwienia kończyn — `chronic limb threatening ischemia` stała na **13. pozycji rdzenia 47**,
`peripheral artery disease` na 21. To jest chirurgia naczyniowa, nie ortopedia.

## Mechanizm — pole dziedziczy strukturę MeSH razem z jej granicami

Definicja pola (def1) to `Orthopedic Procedures` (D019637) i potomkowie — 56 deskryptorów.
Wśród nich MeSH umieszcza **`Amputation, Surgical` (D000671, E04.555.080)** i
**`Limb Salvage` (D023821, E04.555.400)**. Tymi dwoma wrotami wchodzi całe piśmiennictwo
o ratowaniu kończyny niedokrwionej.

| | rekordów 2005–2025 | udział pola |
|---|---:|---:|
| pole ogółem | 268 383 | 100% |
| z deskryptorem amputacyjnym/limb salvage | 17 137 | 6,39% |
| **wchodzące wyłącznie przez nie** | **15 899** | **5,92%** |

Rozbicie tych 15 899 po współwystępujących deskryptorach: naczyniowe lub cukrzycowe **7 135
(44,9%)**, onkologiczne **1 306 (8,2%)**, urazowe 183 (1,2%), żadne z powyższych 7 361 (46,3%).

## Pomiar rozdzielczości — separacja jest zupełna

Udział dokumentów danego terminu, które leżą w podzbiorze wchodzącym wyłącznie przez amputację
lub limb salvage:

| termin | dok. | w podzbiorze |
|---|---:|---:|
| chronic limb threatening ischemia | 688 | **100,0%** |
| clti | 628 | **100,0%** |
| major amputation rate | 148 | **100,0%** |
| drug coated balloon | 90 | **100,0%** |
| amputation free survival | 724 | 99,7% |
| endovascular revascularization | 308 | 99,4% |
| peripheral artery disease | 670 | 97,6% |
| diabetic foot ulcer | 380 | 97,4% |
| — kontrola ortopedyczna — | | |
| 3d printing | 639 | 2,0% |
| periprosthetic joint infection | 2 360 | 0,5% |
| tranexamic acid | 1 443 | 0,2% |
| direct anterior approach | 786 | **0,0%** |
| robotic assisted total knee arthroplasty | 162 | **0,0%** |
| latarjet procedure | 464 | **0,0%** |

Nie ma tu strefy przejściowej. To dwa rozłączne piśmiennictwa w jednym worku.

## Reguła naprawcza (D4) — wąska, nie szeroka

Odrzucenie wszystkich 15 899 usunęłoby **ortopedię onkologiczną** — limb salvage w mięsakach
kości, hemipelwektomia (233 rekordy) — czyli materiał bezspornie ortopedyczny.

> **D4.** Rekord jest wyłączony z pola, jeżeli jego jedynymi deskryptorami pola są
> `Amputation, Surgical`, `Limb Salvage`, `Disarticulation` lub `Hemipelvectomy`
> **i jednocześnie** niesie deskryptor naczyniowy lub cukrzycowy (D058729, D016491, D007511,
> D017719, D014652, D001157, D003920, D048909).

Usuwa **7 135 rekordów = 2,66% pola**. Skuteczność zmierzona: 92–99% dokumentów każdego terminu
naczyniowego, przy 0,0–2,0% dla terminów ortopedycznych. `limb salvage` jako termin spada
z 81,4% do 46,9% — czyli reguła zabiera połowę naczyniową, a zostawia onkologiczną, i o to
chodziło.

Jeden termin reguła omija: `transfemoral amputation` (6,7% wąską regułą, 90,3% szeroką).
To piśmiennictwo protetyczno-rehabilitacyjne, nie naczyniowe. Zostaje świadomie.

## Co trzeba przeliczyć

Ekstrakcji fraz nie trzeba powtarzać — `noun_chunks.parquet` jest per-PMID. Powtórki wymaga
zliczanie i detekcja wyłonienia, bo **zmienia się mianownik**: udziały rosną o ok. 2,7%
względnie, a terminy naczyniowe powinny wypaść z list wyłonień w całości.

## Do zaraportowania niezależnie od naprawy

To jest **ograniczenie metody, nie tylko usterka tego przebiegu**. Definicja pola oparta
na poddrzewie MeSH dziedziczy granice, które MeSH wytyczył do innych celów. Amputacja jest
procedurą ortopedyczną w sensie anatomicznym i procedurą naczyniową w sensie wskazania;
poddrzewo nie odróżnia jednego od drugiego. Każde badanie definiujące dziedzinę kliniczną
przez poddrzewo MeSH ma ten problem i większość go nie sprawdza. Zmierzyliśmy go, więc idzie
do Ograniczeń wraz z liczbą.

Pliki: `data/processed/pmid_tylko_naczyniowe.csv` (15 899),
`data/processed/pmid_naczyniowe_scisle.csv` (7 135).
