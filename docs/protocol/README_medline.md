# Lustro MEDLINE 2026 — pobranie i parsowanie

Dwa skrypty, w konwencji `s3_tdm_full_pull.py`: najpierw lustro, potem parsowanie do tabel.

## 1. `medline_fetch.py` — lustro

Źródło: `https://ftp.ncbi.nlm.nih.gov/pubmed/{baseline,updatefiles}/`
Baseline 2026 to `pubmed26n0001`–`pubmed26n1334` (wydany 2026-01-30), pliki aktualizacyjne
od `pubmed26n1335` w górę. Do każdego pliku jest suma `.md5` — skrypt ją weryfikuje i traktuje
jako warunek pominięcia przy wznowieniu.

```powershell
python code\medline_fetch.py --dest D:\medline_2026 --dry-run
python code\medline_fetch.py --dest D:\medline_2026 --limit 5      # próba
python code\medline_fetch.py --dest D:\medline_2026 --workers 4
```

Rząd wielkości: ~1,5 tys. plików, ~30-40 GB spakowane. NCBI prosi o umiar w równoległości —
domyślne 4 wątki są bezpieczne, nie podnoś bez potrzeby.

## 2. `medline_extract.py` — parsowanie

Z każdego `.xml.gz` robi dwa parquety:

| wyjście | zawartość | po co |
|---|---|---|
| `index/` | **wszystkie** rekordy, bez tekstu: pmid, rok, miesiąc, doi, czasopismo, kraj, język, typy publikacji, MeSH (UI), `indexed`, `has_abstract` | mianownik do normalizacji trendów |
| `msk/` | rekordy z szerokiego sita mięśniowo-szkieletowego + tytuł, abstrakt, MeSH słownie, słowa kluczowe | materiał analityczny |

```powershell
python code\medline_extract.py --src D:\medline_2026 --out D:\medline_2026\parsed --limit 3
python code\medline_extract.py --src D:\medline_2026 --out D:\medline_2026\parsed
```

Wznawianie: plik, dla którego istnieje już `index/<stem>.parquet`, jest pomijany.

### Decyzje, które trzeba znać przy interpretacji

**Data.** Pierwszeństwo ma `ArticleDate` (publikacja elektroniczna), potem `PubDate/Year`,
na końcu `MedlineDate` (np. „2019 Jan-Feb" → rok 2019, miesiąc pusty). To znaczy, że data
w tabeli jest datą pierwszego udostępnienia, nie datą numeru czasopisma — dla analizy trendu
to jest właściwy wybór, ale różni się od tego, co pokazuje interfejs PubMed.

**Kolumna `indexed`.** `True` gdy rekord ma MeSH. Rekordy z ostatnich kilkunastu miesięcy często
jeszcze go nie mają („in process"). Bez tej kolumny ostatni rok każdej krzywej opartej na MeSH
sztucznie spada. Sito tekstowe łapie je mimo braku MeSH — dlatego jest w sicie obok MeSH, a nie zamiast.

**Sito MSK jest celowo szerokie** — czułość przed swoistością. Zawężanie robimy później na tabeli
`msk/`, nie na etapie parsowania, żeby nie czytać 38 mln rekordów drugi raz. W sicie są zarówno
terminy MeSH (`MESH_MSK`), jak i wyrażenie regularne na tytule, abstrakcie, MeSH i słowach
kluczowych (`TEXT_MSK`).

**`Printing, Three-Dimensional` wszedł do MeSH w 2017.** Prace wcześniejsze nie mają tego
deskryptora. Każda krzywa druku 3D musi być liczona po tekście, nie po MeSH, albo mieć zaznaczony
moment wprowadzenia terminu — inaczej zmiana słownika wygląda jak eksplozja technologii.

## Status testów

Parser sprawdzony na syntetycznym `PubmedArticleSet` z czterema przypadkami brzegowymi:
rekord z MeSH i `ArticleDate`, rekord „in process" bez MeSH z `MedlineDate`, rekord niezwiązany
(poprawnie odrzucony) i rekord bez abstraktu. Normalizacja miesiąca (`12` vs `Jul`) potwierdzona.
**Na prawdziwych plikach NCBI nieuruchamiany** — pierwszy przebieg z `--limit 5` jest testem właściwym.
