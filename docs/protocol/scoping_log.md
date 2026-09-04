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

---

# 2026-08-31, dalej — audyt pozostałych 55 deskryptorów pola. Trzy kolejne wycieki (D5)

Po wykryciu wycieku naczyniowego (D4) sprawdzono wszystkie 56 deskryptorów def1: ile rekordów
wchodzi do pola **wyłącznie** przez każdy z nich, i o czym te rekordy są (najczęstsze frazy
tytułowe oraz sondy słowne na próbach).

## D5a. Stomatologia i chirurgia szczękowo-twarzowa — sygnał strukturalny, nie słowny

Pięć deskryptorów pola należy **jednocześnie do poddrzewa stomatologicznego** — E06 (Dentistry)
lub E04.545 (Oral Surgical Procedures):

| deskryptor | drzewa |
|---|---|
| Orthognathic Surgical Procedures | E04.545.562; E04.555.580.289; **E06.645.562** |
| Sinus Floor Augmentation | E04.545.668; E04.555.130.550; **E06.645.668** |
| Osteotomy, Le Fort | E04.545.575; E04.555.580.580; **E06.645.575** |
| Osteotomy, Sagittal Split Ramus | E04.545.637; E04.555.580.790; **E06.645.637** |
| Alveolar Bone Grafting | E04.545.562.500; E04.555.580.289.500; **E06.645.562.124** |

Są w poddrzewie ortopedycznym dlatego, że osteotomia i przeszczep kości to procedury wspólne
anatomicznie — nie dlatego, że to ortopedia.

**8 230 rekordów (3,07%) niesie któryś z nich; 6 178 (2,30%) wchodzi wyłącznie przez nie.**

Potwierdzenie w tytułach: `Orthognathic Surgical Procedures` — `orthognathic surgery` (837 na
próbie 2 516). `Sinus Floor Augmentation` — `maxillary sinus augmentation`, `sinus floor
elevation`, `dental implants`. To implantologia stomatologiczna.

## D5b. Ten sam wyciek bocznymi drzwiami — dwa deskryptory mieszane

Nie da się ich rozstrzygnąć strukturalnie, bo mieszczą materiał ortopedyczny i twarzoczaszkowy:

| deskryptor | wyłącznie tędy | twarzoczaszka | kończyny / ortopedia |
|---|---:|---:|---:|
| Osteogenesis, Distraction | 2 469 | **1 221 (49,5%)** | 136 (5,5%) |
| Bone Transplantation | 10 104 | **2 641 (26,1%)** | 792 (7,8%) |

`Osteogenesis, Distraction` to w połowie **dystrakcja żuchwy** i sekwencja Pierre'a Robina —
`mandibular distraction osteogenesis` 235, `pierre robin sequence` 82 na próbie. Wydłużanie
kończyn, czyli sens ortopedyczny, to 5,5%.

**Ostrzeżenie metodologiczne:** te dwie liczby pochodzą z sond słownych na tytułach, nie
z deskryptorów. Reszta (45,1% i 66,3%) nie trafiła w żadną sondę. To są **dolne oszacowania**,
nie pomiary. Regułę trzeba oprzeć na współwystępowaniu deskryptorów (A14 / C07), a nie na
słowach, i zmierzyć ją tak, jak zmierzono D4.

## D5c. `Traction` — homonim, nie wyciek dziedzinowy

MeSH `Traction` (D014143, E04.555.720) to **fizyczne pojęcie wyciągu**, nie wyciąg ortopedyczny.
Na 2 008 rekordów wchodzących wyłącznie tędy:

- **400 (19,9%)** dotyczy narządów poza układem ruchu — `endoscopic submucosal dissection`
  (103 na próbie), choroba Peyroniego (30), zabiegi przełykowe, okulistyczne;
- 347 (17,3%) to układ ruchu.

**Terminów naczyniowych to nie tłumaczy, ale tłumaczy klasę śmieci innego rodzaju.** W skali pola
to 0,15%, więc priorytet niski — ale jest to jedyny znaleziony przypadek, w którym deskryptor
pola oznacza w MeSH co innego, niż zakłada nazwa dziedziny.

## D5d. Sprawdzone i pozostawione bez zmian

`Manipulation, Orthopedic` — 827 wyłącznie tędy, z tego **57 (6,9%)** to terapia manualna,
chiropraktyka i osteopatia. Poniżej progu działania; odnotowane.

Pozostałe 30 deskryptorów z ogona (Kyphoplasty, Tenotomy, Laminoplasty, Meniscectomy,
Viscosupplementation, Acetabuloplasty i dalej) — łącznie poniżej 4% pola, każdy poniżej 0,4%,
żaden nie wykazuje obcej dziedziny w tytułach. Bez zastrzeżeń.

## D5e. Definicja alternatywna (def2, 137 czasopism) — praktycznie czysta

Przesiew tytułów: 118 ze 137 zawiera słowo ortopedyczne. Z pozostałych 19 szesnaście to
ortopedia w innym języku (`Acta ortopédica mexicana`, `Chirurgia narządów ruchu i ortopedia
polska`, `Nihon Seikeigeka Gakkai zasshi`). Wątpliwe trzy:

- **`Head & face medicine`** — chirurgia szczękowo-twarzowa. Ten sam wyciek co D5a, tą samą
  drogą, w drugiej definicji. To wzmacnia D5a: nie jest artefaktem jednej definicji, tylko
  granicą, którą obie odziedziczyły.
- `Gait & posture` — biomechanika chodu, na pograniczu neurologii.
- `Journal of clinical densitometry` — densytometria, bliżej endokrynologii.

Trzy na 137 to 2,2% listy czasopism. Bez działania; do odnotowania w Ograniczeniach.

## Skala łączna

| wyciek | rekordów | % pola |
|---|---:|---:|
| naczyniowy (D4, reguła zmierzona) | 7 135 | 2,66% |
| stomatologiczny strukturalny (D5a) | 6 178 | 2,30% |
| stomatologiczny bocznymi drzwiami (D5b, dolne oszacowanie) | ≥ 3 862 | ≥ 1,44% |
| homonim `Traction` (D5c) | ~400 | 0,15% |
| **razem** | **≥ 17 575** | **≥ 6,5%** |

Co najmniej jeden na piętnaście rekordów pola nie jest ortopedią. Po naprawie liczba idzie
do Metod jako charakterystyka pola, a mechanizm — do Ograniczeń.

---

# 2026-09-02 — D6 (weterynaria), reguła skrótów, martwe pole detektora, MTIX zamknięty

## D6. Piśmiennictwo weterynaryjne — największa z reguł pola

Znalezione ubocznie przez VS Code przy pytaniu o narzędzia badawcze w materiale:
**`tibial plateau leveling osteotomy` miało 66% prac o psach.** TPLO to zabieg na więzadło
krzyżowe u psów; u ludzi się go nie wykonuje. Siedziało w materiale.

> **D6.** Rekord wyłączony, jeżeli `mesh_ui` zawiera `Animals` (D000818) i **nie zawiera**
> `Humans` (D006801).

**11 749 rekordów, 3,95% pola — więcej niż D4 (2,62%) i D5a (2,15%).** Nakładanie się
z pozostałymi regułami minimalne (D4 16, D5a 144, D5c 13).

Walidacja: `cranial cruciate ligament` 97,1% w podzbiorze, `tplo` 94,9%, `tibial tuberosity
advancement` 94,6% — wobec `total knee arthroplasty` 0,2% i `reverse shoulder arthroplasty` 0,0%.
Trzy przekroczenia po stronie ortopedycznej (`polyetheretherketone` 10,2%, `spinal fusion` 10,8%,
`locking plate` 5,1%) **nie są błędami reguły**, tylko prawdziwym udziałem badań zwierzęcych
w tych tematach; reguła usuwa zwierzęcy ułamek terminu, nie termin.

W odróżnieniu od D4 i D5b, D6 **nie wymagał testu progowego**, bo używa własnych znaczników
kontrolnych NLM zamiast heurystyki współwystępowania.

Skutek uboczny: `micro computed tomography` ma 61,4% prac zwierzęcych i wypada pod D6 — nie było
więc pozycją do rozstrzygnięcia „czy warsztat badawczy wchodzi w zakres".

## D7. Skróty dwu- i trzyliterowe — czwarte wystąpienie tego samego błędu

Po `ml` = mililitry (Etap 1): `ha` (960 prac, brak dominanty — hydroksyapatyt 17,7%, kwas
hialuronowy 14,3%, hip arthroplasty 28,6%), `cr` (21,9%), `ka` (31,5%), `ai` (41,1%, przy
`acetabular index` 27,3%). `let` z 93,5% zostaje.

Reguła spisana jako **§4a kodeksu v1.4**. Uzasadnienie odrzucenia jest lepsze niż pierwotne:
grupa liczy dokumenty zawierające dowolny człon, więc skrót wnosi **wyłącznie** prace używające
samego skrótu (67–93% jego dokumentów). Część weryfikowalna jest już w grupie; odrzucamy
nieodzyskiwalną.

**Skutek dla liczb podanych wcześniej: grupa AI/ML była zawyżona.** W rdzeniu 163 takie skróty,
21 w materiale.

**Ryzyko tej reguły, zgłoszone i jeszcze niezmierzone:** odrzucenie skrótu jest zachowawcze dla
obecności terminu, ale nie jest neutralne dla `y₀`, jeżeli udział skrótu zmieniał się w czasie.
Do zamknięcia przed zamrożeniem materiału (§4a v1.4).

## Martwe pole detektora — nazwane, nie naprawione

Przy rozstrzygnięciu, że biotechnologia wchodzi w zakres, okazało się, że nie wpuszcza to nic
nowego, ale odsłania mechanizm:

- **`platelet rich plasma`** — baza 2000–02 0,151%, próg 0,756%, szczyt 0,386% (2024).
  Wzrosło dwukrotnie w dwadzieścia lat i weszło na plateau. **Detektor wykrywa starty, nie wzrost
  stopniowy.**
- **`bone morphogenetic protein`** — pełna krzywa wycofania (0,43% w 2010 → 0,09% w 2025,
  −79%, zgodnie z kontrowersjami wokół INFUSE po 2011), ale nie wyłania się, bo **rosło przed
  rokiem 2000**.

To ten sam mechanizm co przy `hip resurfacing`, przesunięty o jedno okno. Zdanie do Metod,
mocniejsze niż samo „okno zaczyna się w 2000": **przesuwanie okna przesuwa martwe pole,
nie usuwa go.**

## MTIX-2022 — sprawdzony, oś rankingu zostaje

Nieciągłość jest realna i duża. Odsetek rekordów PubMedu z jakimkolwiek MeSH: 93,4% (2003) →
56,4% (2025). Deskryptorów na rekord pola: stabilnie ~13 przez osiemnaście lat, **załamanie do
8,70 w 2022**, powrót do 12,48 w 2025. Skład deskryptorów przesunął się systematycznie
z ogólnych na szczegółowe (`Orthopedic Procedures` −2,94 pp, `Arthroplasty, Replacement, Knee`
+1,19 pp).

**Ale przesunięcie nie przekłada się na ranking.** Korelacja ekspozycji terminu na zyskujące
deskryptory z jego odchyleniem od trendu: Spearman 0,143 (p = 0,36), Pearson 0,126 (p = 0,42),
n = 43. Korelacja osi obecności z osią przekroczenia progu rośnie po przejściu (0,862 → 0,916),
więc zmiana osi niczego by nie naprawiła.

**Oś i mianownik bez zmian; całość idzie do Ograniczeń z liczbami.** Zastrzeżenie VS Code przyjęte:
43 terminy to mała moc i „nie zmierzyliśmy skrzywienia" nie znaczy „skrzywienia nie ma".

## Sprostowanie

Liczebników w 506 nowych frazach jest **72**, nie 86. Różnica to 14 fraz zawierających liczbę
obok słowa, w większości prawdziwych terminów (`srs 22`, `sf 12`, `l4 5`, `95 confidence
interval`, `minimum 2 year follow up`). Do tekstu idzie 72.

## Materiał po D6

132 kandydatów z obu ocen ortopedy → 110 po wyłączeniach → 82 po słowniku synonimów →
**75 grup po scaleniu wariantów.**

---

# 2026-09-03 — zaniki uwagi wyjaśnione stanem dowodów. Koniec liczenia

Źródło: `brief_dla_cowork_gradient_dowodow_2026-09-03.md` (zastępuje osiem mechanizmów
z briefu z 2026-09-02, które zachodziły na siebie, bo mieszały wymiar epistemiczny ze
strukturalnym).

## Wynik: trwałość uwagi porządkuje się według stanu pytania, nie losu technologii

Rama ortopedy: skoro mierzymy uwagę, jej spadek bierze się stąd, że pytanie się zamknęło.
Trzynaście zaników z materiału na pięciu stanach dowodów, trwałość 2021–22 / szczyt:

| stan dowodów | n | trwałość |
|---|---:|---|
| przeciw stosowaniu (MoM, resurfacing) | 2 | 0,10–0,17 |
| za alternatywą | 1 | 0,23 |
| brak rozstrzygnięcia | 6 | 0,20–0,39 |
| za + wchłonięcie przez następcę (nawigacja → robotyka) | 1 | 0,39 |
| za + rutyna (Ponseti, kyphoplasty) | 3 | 0,43–0,61 |

Trzy główne stany **nie zachodzą na siebie** (0,17 | 0,20 … 0,39 | 0,43). Wykładnia: gdy dowody
mówią „nie", piśmiennictwo umiera; gdy pytanie otwarte, tli się; gdy dowody mówią „tak",
technologia wchodzi do rutyny i generuje stały strumień prac. **Hipoteza na trzynastu
przypadkach** — postawiona tak, by dała się obalić na nowym materiale; tak ma być przedstawiona.

To rozstrzyga zastrzeżenie z 2026-09-02, że iloraz 2025/szczyt miesza trzy zjawiska: miesza,
i właśnie dlatego trzeba go czytać przez stan dowodów, a nie jako jedną oś.

## Cztery korekty VS Code na sobie — i zasada, która z nich wynika

1. Kolumna koncentracji względnej **wycofana**: waga `p²/p_tła` mierzyła koncentrację
   podwójnie ważoną, nie względną, i zbiegała do 1,0.
2. „Odpływ badań podstawowych" przy chondrocytach — błędny; ACI i mikrozłamania były kliniczne
   od początku okna (53% → 55%, 55% → 73%). Pasuje wyłącznie do MSC (10% → 41%).
3. „Szczyt współwystępowania jako sygnatura zastąpienia" — artefakt mianownika (udział liczony
   w pracach rosnącego następcy). Współwystępowanie **nie odróżnia** zastąpienia od rywalizacji.
4. Nazwy klas twierdziły o praktyce („jedna wygrywa"), gdy nic nie wygrało klinicznie — blokada
   udowa ma nadal 54 prace w 2022–25 wobec 105 o blokadzie kanału. Przesunęła się proporcja uwagi.

Cztery razy w jednej sesji obserwacja o piśmiennictwie została przebrana za wniosek o medycynie
i cztery razy korekta przyszła od ortopedy, nie z kontroli. **Zasada do Metod, nie siedem
ostrożności: pomiar pokazuje wzorzec uwagi; rozstrzyga rzecz.**

## Współwystępowanie po korekcie na przypadek

Krotność obserwacji do oczekiwania `nA·nB/pole`: pęczki ACL **458×** (warianty jednej operacji,
porównywane head-to-head), blokady 170×, chrząstka 92×, nawigacja/robotyka **12×**. Stabilne
w dwóch oknach. Miara odróżnia wyłącznie wchłonięcie (składnik przestaje być nazywany) od
reszty. Rozróżnienie wariant/metoda postawił ortopeda; liczba je potwierdza, nie zastępuje.

## Dwa nowe ograniczenia

- **Uwaga miesza wartość kliniczną z dostępnością.** ACI kosztowne, regulowane, w nielicznych
  ośrodkach — trwałość 0,13; mikrozłamania robi każdy artroskopista — 0,43; obie techniki
  w użyciu. Dotyczy każdej kosztownej lub skoncentrowanej technologii, więc łączy się z osią
  koncentracji.
- **Odpływ tematu z pola nieodróżnialny od zaniku tematu.** Definicja przez poddrzewo MeSH
  widzi tylko wnętrze pola. Co najmniej MSC (31% prac usuwa D6, udział klinicznych rośnie).

## Pęczki ACL

Spór nie wygasł: współwystępowanie single/double 20–38% do 2025, recentne tytuły to porównania.
Równolegle rosną LET (6 → 146) i ALL (8 → 77) — obserwacja współbieżna, wyparcia nie ustalono.

## Stan

Materiał **76 grup** (FEA przywrócone). Trzynaście zaników z przyczyną, klasą, poziomem
i adnotacją: `data/processed/wycofania_mechanizmy.csv`. **Po stronie liczenia nic otwartego.**

---

# 2026-09-03 — D8: retronimy i generyki w materiale. 76 → 66

Zauważone przez ortopedę przy czytaniu Wyników: `mechanical alignment` (y₀ 2018) nie jest nową
technologią, tylko czterdziestoletnim standardem osiowania, który dostał nazwę, gdy pojawiło się
`kinematic alignment`. **Retronim** — detektor złapał zdarzenie nazewnicze, nie technologiczne.
Zgodne z tym, że leży wśród „światowych" (12,7 kraju): jest domyślne wszędzie.

## Ta sama klasa, ten sam mechanizm

| retronim | y₀ | nazwany w kontraście do | y₀ rywala |
|---|---:|---|---:|
| mechanical alignment | 2018 | kinematic alignment | 2022 (w rdzeniu wcześniej) |
| single bundle | 2010 | double bundle reconstruction | 2007 |
| anatomic total shoulder arthroplasty | 2015 | reverse shoulder arthroplasty | 2007 |

`single bundle` był wśród 13 zaników — „zanik" standardu, który nie zanikł. Wypada z tabeli 3.

## Generyki — ogólne określenia ustalonych zabiegów, nie technologie

`primary anterior cruciate ligament reconstruction`, `unilateral anterior cruciate ligament
reconstruction`, `primary unilateral total knee arthroplasty`, `elective total knee arthroplasty`,
`posterior lumbar fusion`, `pelvic fixation`, `arcr`.

`arcr` oznaczone jako wątpliwe w drugą stronę: artroskopowa naprawa stożka w latach 2010.
mogła być realnym przesunięciem kosztem naprawy otwartej. Wypada z ortopedą do potwierdzenia;
wraca, jeśli ortopeda tak rozstrzygnie.

## Decyzja

Wszystkie dziesięć poza materiałem. **Materiał 76 → 66.** Zaniki 13 → 12.

Do Metod jedno zdanie: pojawienie się rywala nadaje nazwę dotychczasowemu standardowi,
a detektor widzi to jako wyłonienie; trzy takie przypadki usunięto po przeglądzie klinicznym.
To jest zmierzona własność metody, nie usterka — i zarazem powód, dla którego przegląd przez
specjalistę nie jest opcjonalny.

Osie do przeliczenia na 66 (VS Code, brief z 2026-09-03).

---

# 2026-09-03 — słownictwo powikłań nie zapowiada upadku. Wynik ujemny, zamknięty

Hipoteza (Cowork, potwierdzona przez ortopedę): frazy powikłań wyłaniają się przed szczytem
technologii, która potem upada (MoM: `pseudotumor` −7 lat, `metal debris` −6, ALTR −4).
Przypadek próbny postawiony z góry: `cement leakage` −2 lata przed szczytem `kyphoplasty`,
która **nie** upadła.

Test VS Code na 228 parach powikłanie–technologia, 61 grup, szczyt ≤ 2022 (żeby wyprzedzenie
nie było trywialne przy technologiach wciąż rosnących — pierwszy przebieg był tym obciążony
i sam go sprostował):

| pasmo | wyprzedza szczyt |
|---|---:|
| dowody przeciw | 50% |
| brak dowodów | 50% |
| dowody za + rutyna | 50% |

**Dokładnie po równo.** Kifoplastyka łamie wzorzec także po odsianiu wskazań (`vcf`, `ovcf`
to powody zabiegu, nie powikłania — kategoria `rozpoznanie` ich nie odróżnia, co jest
ograniczeniem testu, ale nie zmienia wyniku).

Do Dyskusji: **wyłonienie słownictwa powikłań jest cechą cyklu życia technologii, nie zapowiedzią
jej upadku.** Zdanie o „wczesnym ostrzeżeniu" usunięte ze szkieletu (Clinical relevance).

Uboczne: krotności współwystępowania technologia–powikłanie są ogromne i selektywne (146–191×
przy triadzie MoM). Powiązanie jest wykrywalne; jego chronologia nie niesie informacji o losie.
Możliwe zastosowanie — automatyczne wskazywanie par do przeglądu — poza zakresem tej pracy.

---

# 2026-09-03 — gradient dowodów upada; zostaje podział binarny. Materiał 66

**Błąd wychwycony przez ortopedę:** trwałość liczona w oknach kalendarzowych (2021–22, 2023–25)
porównywała technologię 14 lat po szczycie (nawigacja, szczyt 2007) z technologią 2 lata po
szczycie (dual mobility, 2020) jako jedną miarę. Stąd „separacja w 2021–22 i jej brak w 2023–25"
— to nie była zagadka, tylko artefakt.

Poprawnie: trwałość **względem własnego szczytu**, okna +1..3, +3..5, +5..7 lat.

| okno | odrzucona (n=2) | nieodrzucona (n=10) |
|---|---|---|
| +1..3 | 0,27–0,48 | 0,50–0,87 |
| +3..5 | 0,17–0,25 | 0,35–0,73 |
| +5..7 | 0,11–0,17 | 0,26–0,72 |

**Przeżyło:** odrzucona vs nieodrzucona — czysto we wszystkich trzech oknach.
**Nie przeżyło:** pięć pasm. „Brak dowodów" (0,35–0,73 w +3..5) pokrywa całe pasmo rutyny.

Do Wyników: piśmiennictwo odróżnia technologię odrzuconą od nieodrzuconej; dalszych stopni nie
odróżnia. Przy n = 2 po stronie odrzuconych — obserwacja, nie reguła.

Potwierdzenia uboczne: MSC 0,73 w +3..5 (temat wracający), nawigacja 0,66 (wchłonięcie).
`double bundle` przepisane: technika, wobec której ukuto retronim — klasa „warianty bez
zwycięzcy" upada razem z `single bundle`.

Zliczenia na 66: y₀ 2000–09: 11, 2010–19: 42, 2020–25: 13; kraj_eff ≤ 2,5: 13 grup, wyłącznie
Chiny (7) i USA (6); ≥ 9: 12 grup; bez czasu podwojenia 11; szczyt 2025: 19.
`arcr`: 466 prac, y₀ 2017, USA 44% — do decyzji ortopedy.
