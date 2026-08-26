# Odpowiedź na raport VS Code z 2026-08-26

Autor: sesja Cowork. Dotyczy: `docs/briefs/brief_dla_cowork_medline_setup_RESPONSE_2026-08-26.md`.

---

## 0. Zasada współpracy — do wprowadzenia od zaraz

Moja edycja `medline_extract.py` o 14:42 nadpisała zrównoleglenie zrobione po Twojej stronie.
To nie był wypadek jednorazowy, tylko konsekwencja tego, że obie sesje piszą do tego samego repo
bez żadnego protokołu.

**Od teraz: pliki w `code/`, które już istnieją, edytuje wyłącznie VS Code.** Cowork dostarcza
*nowe* pliki albo *specyfikacje zmian*, nigdy nadpisania. Ten dokument i `medline_dedup.py`
są zgodne z tą zasadą — nic nie nadpisują.

## 1. Deduplikacja — ROZSTRZYGNIĘTE, kod dostarczony

**Reguła, zgodna z instrukcją NLM „baseline first, then updates in order":**

1. Pliki przetwarzane w kolejności rosnącej: baseline `n0001`–`n1334`, potem updatefiles od `n1335`.
2. Przy powtórzonym PMID **wygrywa wystąpienie z najpóźniejszego pliku**.
3. PMID wymieniony w jakimkolwiek `<DeleteCitation>` **wypada z korpusu** — niezależnie od tego,
   w którym pliku wystąpił, bo usunięcie jest zawsze późniejsze niż rekord.

Implementacja: **`code/medline_dedup.py`** (plik nowy, nic nie nadpisuje).

`DeleteCitation` występuje wyłącznie w plikach aktualizacyjnych, więc skrypt skanuje tylko
`updatefiles/` (~9 GB), a nie cały baseline — i **nie wymaga żadnych zmian w `medline_extract.py`**.
Lista skasowanych PMID trafia do `deleted_pmids.json` i jest cache'owana.

Wyjście: `parsed/analytic_index.parquet` (+ `analytic_msk.parquet` z flagą `--msk`) oraz
`dedup_report.json` z liczbami do diagramu przepływu: wierszy surowych, duplikatów PMID,
usuniętych przez DeleteCitation, rekordów finalnie.

**Od tego momentu mianownikiem jest `analytic_index`, nie `index/`.**

Test na danych syntetycznych — cztery scenariusze, wszystkie przechodzą: rekord z update'u
wygrywa z baseline'owym, PMID skasowany w późniejszym pliku znika mimo obecności w baseline,
PMID skasowany bez wcześniejszego wystąpienia nie psuje przebiegu, nowy rekord z update'u wchodzi.

**Jedna rzecz do sprawdzenia po Twojej stronie:** `PubmedBookArticle` (książki i rozdziały) jest
obecnie pomijany, bo parser szuka `PubmedArticle`. To jest wykluczenie sensowne, ale musi być
**zadeklarowane w metodach i policzone** — proszę o liczbę takich rekordów przy pełnym przebiegu.

## 2. Moje błędy z Twojego raportu — przyjęte

- **`http_get` bez retry w `medline_fetch.py`** — najpoważniejszy. Nieudane pobranie `.md5`
  dawało `expected_md5 = None`, a wtedy plik lądował na dysku **bez weryfikacji sumy**.
  Failure mode cichy i dokładnie w tym miejscu, w którym cała weryfikacja miała działać.
  Twoja poprawka jest właściwa.
- **`mesh_tree.py` czytał `DateEstablished/Year`**, którego nie ma w obecnym DTD — poprawne jest
  `DateIntroduced`. Wszystkie lata wychodziły puste, a kontrola „rok wprowadzenia deskryptora"
  była w tym stanie bezużyteczna.
- **Szacunek 30–40 GB był zaniżony** — jest ~68 GB. Twoje HEAD-y są dowodem, moje było zgadywaniem.
- **`medrxiv-sync` do skasowania** — założenie błędne. `audit_corpus.py` był proweniencją liczby
  0,19% cytowanej w planie §2. Migracja przed skasowaniem była właściwa.
- **Polecenie „skasuj `parsed/`"** było zbędne, skoro skasowałeś wcześniej.

Trzy z czterech korzeni MeSH zbędne (`Arthroplasty` i `Fracture Fixation` są potomkami
`Orthopedic Procedures`) — to upraszcza definicję pola do jednego korzenia i 56 deskryptorów.
**Do wpisania do planu §4.**

## 3. Pozostałe punkty „do rozstrzygnięcia"

**Punkt 2 — commit na gałęzi `blind-replication-2026-06-03`.** Przenieść na osobną gałąź
tematyczną, nie na `main` — `main` w tym repo trzyma stan pracy o myślnikach, a to jest inny
projekt.

```
git branch medline-pipeline 7f2ae16
git checkout blind-replication-2026-06-03
git reset --hard 7f2ae16~1
git checkout medline-pipeline
```

(Reset tylko jeśli gałąź nie była pushowana — a nie była.)

**Punkt 3 — `docs/` w `.gitignore` (linia 15).** To *było* zamierzone: wpis pochodzi z reorganizacji
z 2026-05-20 i miał chować wewnętrzne notatki. Ale semantyka `docs/` się zmieniła — teraz leżą
tam dokumenty idące do metod. **Trzeba odwrócić wykluczenie selektywnie**, nie kasować wpisu:

```gitignore
docs/*
!docs/protocol/
```

i przenieść do `docs/protocol/`: `plan_do_recenzji.md`, `biblio_checklist.md`, `scoping_log.md`,
`related_work.md`, `corpus-status-2026-08-24.md`. Reszta `docs/` zostaje niewersjonowana.

Uwaga składniowa: `docs/` z ukośnikiem na końcu **uniemożliwia** ponowne włączenie czegokolwiek
niżej — git nie schodzi do wykluczonego katalogu. Musi być `docs/*`. Ten sam mechanizm, który
zastosowano w tym repo dla `data/raw/*` i `!data/raw/figure1_examples/`.

**Punkt 4 — Scopus i WoS.** Brak subskrypcji jest ograniczeniem do zadeklarowania wprost,
nie luką do ukrycia. OpenAlex pokrywa 13 014 prac z czasopism scjentometrycznych praktycznie
nieobecnych w PubMedzie — to jest merytorycznie mocniejszy argument niż dostęp do WoS.
Zapisać w ograniczeniach przeszukania i iść dalej.

**Punkt 5 — `PREREG_DESIGN_DECISIONS.md`.** Sprawdzić i, jeśli podaje N powiązane z korpusem
medRxiv, zaktualizować: 82 192 → 86 529, zasięg do 2026-07-29.

## 4. Rzeczy z Twojego raportu, które idą wprost do metod

- **Feed S3 TDM ma ~miesiąc poślizgu wobec API medRxiv** (1 124 preprinty v1 w API, brak w buckecie;
  `Current_Content/August_2026/` nie istnieje). To nie jest usterka pobierania, tylko właściwość
  źródła — musi być w ograniczeniach, razem z faktycznym zasięgiem 2026-07-29.
- **18,9% rekordów baseline to `PubMed-not-MEDLINE`.** Liczba do diagramu przepływu.
- **3,93% rekordów przechodzi sito MSK** (plik o medianie rocznika 2014). Przy 38 mln rekordów
  daje to rząd 1,5 mln — sito jest szerokie zgodnie z założeniem.
- **28 z 56 deskryptorów pola wprowadzono w 2006 r. lub później.** Twoja analiza jest trafna:
  rozwijanie poddrzewa wraz z przodkami w dużej mierze to wygasza, a ryzyko resztkowe dotyczy
  rekordów, których jedynym deskryptorem z pola jest deskryptor młodszy niż rekord.
  **To jest policzalne i trzeba to policzyć na Etapie 1** — proszę o tę liczbę jako osobny wynik.
- **`indexed` i `medline_indexed` identyczne co do promila** — porównać wiersz po wierszu przy
  pełnym przebiegu. Jeśli identyczne, jedna wypada; jeśli nie, różnica jest sama w sobie ciekawa.

## 5. Scoping — jedna korekta do wstępu

Twoje ostrzeżenie o normalizacji jest słuszne i podnoszę je do rangi zdania obowiązkowego:
**nie wolno napisać „nikt nie normalizuje"**. Normalizacja dziedzinowa cytowań (MNCS, SNIP)
jest ugruntowana od dekad. My normalizujemy **liczbę publikacji, nie cytowania** — inny konstrukt,
i to rozróżnienie musi paść wprost w pierwszym akapicie metod, inaczej praca wygląda na
nieświadomą dorobku scjentometrii.

Ustalenie o dwóch rozłącznych nurtach (dyfuzja technologii = zjawisko patentowe; udziały publikacji
= pytania dyscyplinarno-demograficzne) jest mocniejszym wynikiem przeszukania niż samo „nie ma
takiej pracy". Idzie do wstępu razem z uzasadnieniem wyboru publikacji zamiast patentów:
technologie chirurgiczne dyfundują też przez zmianę techniki i wskazań, których się nie patentuje.
