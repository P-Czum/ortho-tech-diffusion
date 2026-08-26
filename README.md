# ortho-tech-diffusion

Dyfuzja badań nad technologiami w ortopedii — pomiar udziału piśmiennictwa ortopedycznego
poświęconego poszczególnym rodzinom technologii, 2005–2025, na danych MEDLINE/PubMed.

## Pytanie badawcze

Które rodziny technologii zyskują, a które tracą udział w produkcji publikacyjnej ortopedii
zabiegowej — i czy rosną równolegle, czy wypierają się nawzajem.

Kluczowa różnica wobec istniejących przeglądów bibliometrycznych: **wspólny, znormalizowany
mianownik**. Przeszukanie z 2026-08-26 znalazło 69 prac bibliometrycznych o technologiach
w ortopedii; wszystkie są jednotechnologiczne i wszystkie raportują liczby bezwzględne, przez
co żadna nie potrafi odpowiedzieć, która technologia rośnie *kosztem* której.

Pełny protokół: **[`docs/protocol/plan_do_recenzji.md`](docs/protocol/plan_do_recenzji.md)**.
Rozpoznanie literatury: [`docs/protocol/related_work.md`](docs/protocol/related_work.md),
[`docs/protocol/scoping_log.md`](docs/protocol/scoping_log.md).
Zgodność z wytyczną BIBLIO: [`docs/protocol/biblio_checklist.md`](docs/protocol/biblio_checklist.md).

Mierzymy **dyfuzję badań i uwagę naukową**, nie adopcję kliniczną. Publikacja jest
przybliżeniem zainteresowania, nie dowodem wejścia technologii do praktyki.

## Dane — poza repozytorium

| ścieżka | rola |
|---|---|
| `D:\medline_2026` | źródło podstawowe: lustro PubMed baseline + updatefiles (~68 GB) |
| `D:\mesh\desc2026.xml` | deskryptory MeSH, do rozwijania poddrzewa definiującego pole |
| `D:\medrxiv_s3_tdm` | **tylko odczyt**, opcjonalna warstwa lead–lag |

W repo trafiają wyłącznie tabele pochodne w `data/processed/`. Lustro, pliki `.xml.gz`
i katalog `parsed/` są wykluczone — odtwarza się je skryptami.

## Pipeline

```powershell
# 1. lustro PubMed (baseline + updatefiles). NCBI prosi o umiar: nie podnosic --workers powyzej 4.
python code\medline_fetch.py --dest D:\medline_2026 --workers 4

# 2. parsowanie do parquet: index/ (mianownik) + msk/ (sito miesniowo-szkieletowe)
python code\medline_extract.py --src D:\medline_2026 --out D:\medline_2026\parsed --workers 8

# 3. tabela analityczna: dedup PMID + DeleteCitation
python code\medline_dedup.py --src D:\medline_2026 --parsed D:\medline_2026\parsed --msk
```

Po kroku 3 mianownikiem jest `parsed/analytic_index.parquet`, **nie** `index/`.
`dedup_report.json` zawiera liczby do diagramu przepływu.

Definicja pola, niezależnie od powyższych kroków:

```powershell
python code\mesh_tree.py --desc D:\mesh\desc2026.xml --root "Orthopedic Procedures" ^
    --out data\processed\field_orthopedic_procedures.csv
python code\mesh_tree.py --desc D:\mesh\desc2026.xml --intro "Printing, Three-Dimensional"
```

Kontrola negatywna do powtarzania przy każdej zmianie rocznika MeSH: w rozwiniętym poddrzewie
nie może wystąpić żaden deskryptor z numerem drzewa `C*` (gałąź chorobowa). Na `desc2026.xml`
poddrzewo liczy 56 deskryptorów i takich wpisów jest zero.

## Wymagania

`pip install -r requirements.txt`. Poza tym miejsce na dysku: ~68 GB na lustro plus ~5 GB
na tabele pochodne.

## Relacja do repo `myslniki`

To jest **osobne badanie**. Repo `myslniki` zawiera zamkniętą pracę o prewalencji myślnika
w preprintach medRxiv (OSF HFT8C) i jego korpus. Stąd sięgamy do tamtego korpusu wyłącznie
do odczytu, w opcjonalnej warstwie lead–lag, i niczego w nim nie zmieniamy.
