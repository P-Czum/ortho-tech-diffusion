# Odpowiedź na `brief_dla_vsc.md` — sesja VS Code, 2026-08-26

Wykonawca: Claude Opus 5 w VS Code. Format wg §4 briefu: krótko, liczbami, konkretne komunikaty
błędów.

Dokument zawiera dwa raporty z tej samej sesji — pierwszy po zamknięciu zadań 1.1–1.3,
drugi po 1.4–1.6 i 3, wraz ze zmianą kierunku pracy.

---
---

# Raport 1 — zadania 1.1–1.3

## 1.1 medRxiv — ZROBIONE

**4 337 nowych preprintów v1.** Korpus 82 192 → **86 529** katalogów DOI; inwentarz
81 483 → 85 820 wierszy. Zasięg do **2026-07-29**. Transfer 12,21 GB w 50,8 min.

Nie użyłem `s3_tdm_full_pull.py`. Ten skrypt czyta wersję z `manifest.xml` dopiero po ściągnięciu
całej paczki, więc płaci pełny transfer za rewizje, które wyrzuca (32,5% obiektów), i za figury
spoza `KEEP_PATTERNS` (53% bajtów). Napisałem `code/s3_tdm_ranged_pull.py` — czyta central
directory ZIP-a z ogona obiektu (`Range: bytes=-16384`) i pobiera tylko potrzebne wpisy; nie-v1
odpada po ~20 kB. **43,2 GB → 12,2 GB.** Zwalidowane na 13 paczkach (v1 i v2, 0,89–455,73 MB):
sha256 każdego pliku, DOI i wersja zgodne 13/13. Każdy wpis weryfikowany CRC32, przy ZIP64
lub braku EOCD fallback na pełny download.

**Błędy:** 4 × `ResponseStreamingError: Connection broken: ConnectionResetError(10054)`.
Klucze z błędem nie trafiają do żadnego rejestru, więc ponowne odpalenie je podjęło —
4/4 odzyskane, 0 błędów.

**Czego nie da się pobrać:** 1 124 preprinty v1 są już w API medRxiv, ale nie ma ich w buckecie —
78 z lipca, 1 046 z sierpnia. Folderu `Current_Content/August_2026/` nie ma w ogóle.
**Feed S3 TDM ma ~miesiąc poślizgu wobec API.** „Do dziś" oznacza faktycznie do 2026-07-29,
niezależnie od skryptu.

**Audyt historyczny** (nie było w briefie, wyszło przy listowaniu bucketu): 26 016 kluczy spoza
inwentarza = 201,8 GB. Przesondowałem 20 463 historyczne po ~20 kB każdy (0,13 GB, 13,6 min):
19 570 to rewizje, 892 to v1 z katalogami już na dysku, **1 faktycznie brakujący** —
`10.1101/2021.06.06.21258253`, pełnoprawny v1 z JATS XML i PDF. Dociągnięty.
Podejrzany `August_2025` (619/1689 nieznanych) okazał się fałszywym alarmem.

**Nowe artefakty:** `code/s3_tdm_ranged_pull.py`, `data/processed/s3_tdm_skipped_nonv1.csv`
(1 471 wierszy — rejestr odrzuconych, dzięki czemu kolejne przebiegi ich nie dotykają).

## 1.2 Lustro MEDLINE — W TRAKCIE

Baseline 1 334 + updatefiles 267 = 1 601 plików.

**Korekta rozmiaru: nie 30–40 GB, tylko ~68 GB** (baseline ~59 + updates ~9). Zmierzone przez
HEAD: `n0001` 19,7 MB, `n0600` 35,5 MB, `n1000` 62,1 MB, `n1200` 76,1 MB. ETA raportowane przez
skrypt jest zaniżone, bo liczy pliki, nie bajty, a te w kolejce są ~3× cięższe od pobranych.

**MD5: weryfikowane przy każdym pliku, 0 niezgodności.**

**Błędy — 5 plików z wyczerpanymi próbami**, wszystkie w oknie 15:15–15:39:

```
pubmed26n0365.xml.gz: URLError: <urlopen error _ssl.c:1018: The handshake operation timed out>
pubmed26n0366.xml.gz: URLError: <urlopen error [Errno 11001] getaddrinfo failed>
pubmed26n0367.xml.gz: URLError: <urlopen error _ssl.c:1018: The handshake operation timed out>
pubmed26n0368.xml.gz: URLError: <urlopen error _ssl.c:1018: The handshake operation timed out>
pubmed26n0373.xml.gz: URLError: <urlopen error [Errno 11001] getaddrinfo failed>
```

Przyczyna nie leży po stronie NCBI. Kontrola na niezależnym hoście: AWS S3 spadło w tym samym
momencie z 5,6 do 0,16 MB/s, a `getaddrinfo failed` to padnięte DNS — throttling zdalnego
serwera tego nie powoduje. **Degradacja lokalnego łącza**, ~30×, później częściowo odbudowana.
rsync (zalecany przez NCBI do masowych pobrań) nic by nie dał i nie ma go w systemie.

**Poprawka w `medline_fetch.py`:** `http_get` nie miał retry. Skutki dwa: padnięty listing
zabijał cały run na starcie, a nieudane pobranie `.md5` powodowało, że `expected_md5` zwracało
`None` i **plik trafiał na dysk bez weryfikacji sumy**. Przy zmierzonej awaryjności NCBI ~1/3
żądań to była realna dziura. Teraz 3 próby z backoffem.

**Nie podnosiłem `--workers` powyżej 4.**

## 1.3 MeSH — ZROBIONE

**Poddrzewo `Orthopedic Procedures` (D019637, E02.718 + E04.555): 56 deskryptorów.**
Zapisane do `field_orthopedic_procedures.csv`.

**Kontrola 1 — PASS.** `Fractures, Bone` (D050723) nie wpadło. Mocniej: w całym poddrzewie jest
zero deskryptorów z jakimkolwiek drzewem `C*`, więc gałąź chorobowa nie przecieka boczną ścieżką.

**Kontrola 2 — PASS.** `Printing, Three-Dimensional` = `D066330`, rok wprowadzenia **2015**.

Kontrola 2 wymagała naprawy: `mesh_tree.py` czytał `DateEstablished/Year`, a tego pola nie ma
w obecnym DTD MeSH — wszystkie lata wychodziły puste. Właściwe to `DateIntroduced`, obecne
w 100% z 31 110 deskryptorów.

**Dwa ustalenia poza zakresem pytania:**

Trzy z czterech korzeni z v0.1 są zbędne — `Arthroplasty` (poddrzewo 14) i `Fracture Fixation`
(6) wnoszą **0** deskryptorów ponad `Orthopedic Procedures`, bo są jego potomkami. Po wyłączeniu
`Fractures, Bone` definicja pola redukuje się do jednego korzenia i 56 deskryptorów. Unia
czterech korzeni dałaby 107.

**28 z 56 deskryptorów pola wprowadzono w 2006 r. lub później** — dokładnie połowa. Dotyczy to
mianownika, nie licznika, więc §6 planu tego nie obejmuje. Efekt jest jednak w dużej mierze
wygaszany rozwijaniem poddrzewa wraz z przodkami: rekord z 2006 r. dostał wtedy istniejący
deskryptor nadrzędny, również należący do pola. Ryzyko resztkowe dotyczy rekordów, których
jedynym deskryptorem z pola jest deskryptor młodszy niż sam rekord — policzalne na Etapie 1.

---
---

# Raport 2 — zadania 1.4–1.6, 3 i zmiana kierunku

## 1.4 — test na reprezentatywnym pliku

Poprzednie liczby pochodziły z `n0001–0002` (roczniki 1975–79) i były bezużyteczne.
Powtórzone na `pubmed26n0794`, mediana rocznika **2014**:

| miara | wartość |
|---|---|
| rekordów | 30 000 |
| sito MSK | 1 179 (**3,93%**) |
| `status` = MEDLINE | 80,8% |
| `status` = PubMed-not-MEDLINE | **18,9%** |
| `status` = Publisher | 0,4% |
| ma abstrakt | 83,5% |
| `aff1` niepusty | **85,8%** |
| `citation_subset` niepusty | 78,1% |
| ma DOI | 91,4% |

**Diagnoza z §0 briefu potwierdzona liczbowo: prawie co piąty rekord baseline to nie-MEDLINE.**
Kolumna `status` była konieczna. `aff1` wypełnione w 85,8% nowoczesnych rekordów, więc kraj
pierwszego autora jest realną jednostką geograficzną.

Do sprawdzenia przy pełnym runie: `indexed` i `medline_indexed` wyszły identyczne co do promila.
Jeśli tak jest w całym korpusie, jedna jest redundantna — ale to wymaga porównania wiersz po
wierszu, nie średnich.

**Zrównoleglenie.** Parsowanie szło 1,15 s/MB jednym wątkiem, czyli ~22 h dla 68 GB. Dodałem
`ProcessPoolExecutor` (worker sam zapisuje parquet, żeby nie odsyłać ramek przez IPC) —
**~2 h na 8 procesach**. Wynik zwalidowany: 6/6 plików parquet bit-w-bit identycznych z wersją
sekwencyjną.

Uwaga: edycja `medline_extract.py` z 14:42 (nowe pola `status`/`medline_indexed`/
`citation_subset`/`aff1`) nadpisała to zrównoleglenie — zapis z bufora otwartego przed moimi
zmianami. Nowe pola zostawiłem nietknięte, zrównoleglenie nałożyłem ponownie. Gdyby nie to,
zakolejkowany `--workers 8` wywaliłby się na `unrecognized arguments`.

Stare parquety skasowałem, zanim brief dotarł. Kasowanie `parsed/` niepotrzebne.

## 1.6 BIBLIO → `docs/biblio_checklist.md`

**6 TAK, 5 CZĘŚĆ, 5 PLAN** (wymagalne dopiero w manuskrypcie), **3 LUKA**, 1 nie dotyczy.

Z trzech luk **tylko jedna ma konsekwencje dla liczb — poz. 10, deduplikacja.** Plan nie opisuje,
co zrobić z rekordami występującymi i w `baseline`, i w `updatefiles` (zaktualizowanymi po
wydaniu baseline) ani z `DeleteCitation`. Bez reguły „ostatnia wersja rekordu wygrywa" mianownik
będzie zawyżony. **Wymaga decyzji przed Etapem 1.** Pozostałe dwie są redakcyjne: typ badania
w tytule, diagram przepływu.

Twierdzenie o lukach w standardzie potwierdzone z numerami pozycji: poz. 7 wymaga opisania słów
kluczowych, ale nic nie wymaga PPV; poz. 13 wylicza same wielkości bezwzględne i nie wymaga
mianownika; żadna pozycja nie dotyczy niezmienniczości pomiaru w czasie.

## 1.5 scoping → `docs/scoping_log.md`

12 zapytań PubMed (E-utilities) + 8 OpenAlex, pełne ciągi w logu, 147 przesianych tytułów.
Scopus i WoS nieodpytane — brak subskrypcji. OpenAlex dołożony jako zamiennik: pokrywa
*Scientometrics* (8 493), *JASIST* (2 327), *Journal of Informetrics* (1 721), *QSS* (473) —
**13 014 prac praktycznie nieobecnych w PubMedzie**, czyli dokładnie tam, gdzie leżałaby praca
zajmująca lukę.

**Trzy zapytania zwróciły zero:** „bibliometric" + „proportion/share/percentage of publications";
„bibliometric" + „relative to all / normalized by"; „technology diffusion" + „bibliometric"
+ „clinical" w OpenAlex.

**Ustalenie mocniejsze niż „nie ma takiej pracy".** Obie połowy podejścia istnieją, ale
w rozłącznych nurtach:

- **„Technology diffusion" w bibliometrii to zjawisko patentowe** — wszystkie 10 trafień
  w czterech czasopismach metodologicznych mierzy dyfuzję przez cytowania patentów.
- **„Proportion of publications" występuje, ale w pytaniach dyscyplinarno-demograficznych** —
  wszystkie 12 trafień dotyczy udziałów wg dyscyplin, krajów, płci, modelu OA.

Te nurty się nie spotkały. Konsekwencja dla wstępu: zacytować nurt patentowy i uzasadnić wybór
publikacji zamiast patentów — merytorycznie, bo technologie chirurgiczne dyfundują też przez
zmianę techniki i wskazań, których się nie patentuje.

**Ostrzeżenie: nie wolno napisać „nikt nie normalizuje".** Normalizacja dziedzinowa cytowań
(MNCS, SNIP, Moed, Waltman) jest ugruntowana. My normalizujemy liczbę publikacji, nie cytowania —
inny konstrukt, ale rozróżnienie musi paść wprost, inaczej praca wygląda na nieświadomą dorobku.

## Zmiana kierunku — `plan_do_recenzji.md` v0.3

Przemek zauważył, że projekt zaczął być „pracą o pracy". Sprawdziłem to na dokumentach
i **zarzut się potwierdził, ale nie tam, gdzie się wydawało**.

Bibliometria z definicji jest badaniem publikacji i §1 już to poprawnie ramuje. Dryf był w tym,
**gdzie leżało twierdzenie o nowości**: z 11 zmian wyliczonych w §10 (recenzja v0.1→v0.2)
**dziewięć było metodologicznych**, a pytanie substantywne nie drgnęło.

Rozstrzygnął to scoping: **Q3 = 69 prac bibliometrycznych o technologiach w ortopedii**, w tym
co najmniej sześć o druku 3D i robotyce z osobna. Pytanie „jak rósł druk 3D w ortopedii" jest
zajęte wielokrotnie. **Nowe jest natomiast to, że wszystkie 69 są jednotechnologiczne
i raportują liczby bezwzględne** — żadna nie zestawia rodzin ani nie odnosi ich do produkcji pola.

**Decyzja Przemka: najpierw praca ortopedyczna (B), potem metodologiczna (A).**

v0.3 wprowadza:

1. **Nowość przeniesiona z metody na przedmiot** — pierwsze porównanie wielu rodzin na wspólnym
   mianowniku.
2. **Jawne „co z tego" dla klinicysty** (§1, trzy pytania). Najmocniejsze jest drugie — czy
   rodziny się wypierają — bo **da się je zadać wyłącznie na wspólnym mianowniku**; przy liczbach
   bezwzględnych wszystko rośnie i pytanie nie ma sensu. To lepsze uzasadnienie normalizacji dla
   ortopedy niż „bo baza rośnie".
3. **Nowa §1.1 z podziałem na dwie prace.** Do A odłożone: luki BIBLIO, wywód
   patenty-kontra-publikacje, warstwy epokowe jako *teza*, uogólnienie na inne specjalności.
   Z warunkiem: A nie może być „ta sama metoda opisana porządnie", bo dostanie zarzut uprzedniej
   publikacji — musi wnieść wiele specjalności, formalną walidację niezmienniczości albo
   pokazanie ilościowo, jak bardzo krzywa nienormalizowana myli.
4. **§§3–9 bez zmian merytorycznych.** Warstwy epokowe, PPV stratyfikowany, standaryzacja
   geograficzna, joinpoint zostają — są potrzebne do trafności B niezależnie od tego, gdzie leży
   nowość. Odkłada się budowanie z nich tezy, nie ich stosowanie.
5. **§11: który z trzech wątków uniesie pracę, rozstrzygnie Etap 1.** Jeśli rodziny rosną
   równolegle bez wypierania, wątek 2 odpada. Jeśli udziały wszystkich łącznie są płaskie,
   odpada cała ramka dyfuzji. Zapisane przed danymi, żeby potem nie dopasowywać pytania do wyniku.

## 3 porządki

`.git/_to_delete` usunięte (11 plików: `HEAD.lock`, `index.lock.5`, `tmp_obj_*`). Dangling bloby
po `fsck` są normalne, znikną przy `gc`.

**`~/repos/medrxiv-sync` — założenie z briefu było błędne.** Nie miało remote'a, commit nigdzie
nie wypchnięty, a `tools/audit_corpus.py` **nie istnieje w `code/`** — to nim policzono
kompletność korpusu cytowaną w planie §2 (82 192 wobec 82 350 z API = 0,19%). Skasowanie bez
migracji zniszczyłoby proweniencję tej liczby.

Przeniesione po weryfikacji sha256, dopiero potem skasowane: `audit_corpus.py` → `code/`,
`corpus-status-2026-08-24.md` → `docs/`. Porzucone świadomie: `LICENSE`, `README.md`,
`requirements.txt`, `medrxiv_sync.py` — ten ostatni realnie dublował `s3_tdm_full_pull.py`
i był jedyną rzeczą pasującą do opisu z briefu.

W `~/repos/` zostały `_pmc_repro`, `pmc-unicode-audit`, `pmc-unicode-audit_data_v1.0.0.zip` —
nie ruszałem, nie były w briefie.

**Commit `7f2ae16`**: 5 plików, 1053 wstawienia, wyłącznie `code/` (`s3_tdm_ranged_pull.py`,
`medline_fetch.py`, `medline_extract.py`, `mesh_tree.py`, `audit_corpus.py`). Poza `code/`
zostaje 249 niezacommitowanych zmian, nietknięte. **Push niewykonany.**

---

## Do rozstrzygnięcia

1. **Deduplikacja PMID baseline/updatefiles + `DeleteCitation`** — jedyna luka BIBLIO wpływająca
   na liczby, potrzebna przed Etapem 1.
2. **Commit `7f2ae16` poszedł na gałąź `blind-replication-2026-06-03`**, bo na niej jesteśmy.
   Nazwa nie pasuje do treści. Do przeniesienia na `main` albo nową gałąź.
3. **`docs/` jest w `.gitignore` (linia 15).** `plan_do_recenzji.md` v0.3, `biblio_checklist.md`,
   `scoping_log.md`, przeniesiony raport audytu i ten dokument **nie są wersjonowane**.
   Przy dokumentach idących do metod to prawdopodobnie niezamierzone.
4. **Scopus i WoS nieodpytane** — przy publikacji uzupełnić albo jawnie zadeklarować jako
   ograniczenie przeszukania. Do przesiania zostały większe zbiory: Q1 (192), Q5 (118), Q11 (63),
   O2 (32), O7 (28).
5. **Nie zweryfikowałem, czy `PREREG_DESIGN_DECISIONS.md` podaje N powiązane z korpusem
   medRxiv** — jeśli tak, 4 337 nowych rekordów wymaga aktualizacji rejestracji.
