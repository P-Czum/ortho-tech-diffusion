# Nowe repo dla projektu PubMed — brief dla VS Code

Data: 2026-08-26. **Wersja lekka: repo `myslniki` pozostaje nietknięte.**

---

## 1. Ustalenie

Praca o myślnikach jest **zamknięta** (OSF HFT8C, `CITATION.cff` v2.0.0, kod zamrożony
na `21b65fd`, README: *„a tool for reproducing the reported numbers — not a record of the
working process"*). Projekt PubMed/ortopedia to zupełnie inne badanie i dostaje własne repo.

**Czego NIE robimy:** nie cofamy `7f2ae16`, nie resetujemy gałęzi, nie usuwamy niczego z `myslniki`,
nie ruszamy jego `.gitignore` ani 249 niezacommitowanych zmian. Kopiujemy, nie przenosimy.

Konsekwencja uboczna: `docs/` jest w `.gitignore` myślników, więc nasze briefy i dokumenty
protokołu nigdy nie weszły do jego historii. Wystarczy je skopiować.

## 2. Nowe repo

`D:\Claude\Projects\ortho-tech-diffusion` (nazwa robocza — zmień, jeśli wolisz inną).

```
code/       docs/protocol/   docs/briefs/   data/processed/   logs/   results/
```

**`docs/` ma być wersjonowany od pierwszego commitu.** Wykluczaj co najwyżej `docs/internal/`.

### Kopiujemy z `myslniki`

**`code/`** — 4 pliki: `medline_fetch.py`, `medline_extract.py` (**wersja z dysku, z Twoim
zrównolegleniem**), `mesh_tree.py`, `medline_dedup.py`.

**`docs/` → `docs/protocol/`** — `plan_do_recenzji.md`, `related_work.md`, `biblio_checklist.md`,
`scoping_log.md`, `README_medline.md`. Do `docs/protocol/archiwum/`:
`protokol_mapowanie_innowacji.md` (v0.1).

**`docs/briefs/`** — w całości, razem z `README.md` (protokół wymiany między sesjami).

### Zostaje w `myslniki`, nie kopiujemy

`s3_tdm_full_pull.py`, `s3_tdm_ranged_pull.py`, `s3_tdm_data_quality.py`, `audit_corpus.py`,
`corpus-status-2026-08-24.md`. Należą do korpusu medRxiv, który obsługiwał tamtą pracę.
Nowy projekt sięga po ten korpus **tylko do odczytu** i tylko w opcjonalnej warstwie lead–lag.

## 3. Dane — bez zmian, poza repozytoriami

| ścieżka | rola w nowym projekcie |
|---|---|
| `D:\medline_2026` | źródło podstawowe |
| `D:\medrxiv_s3_tdm` | tylko odczyt, warstwa lead–lag (opcjonalna) |

**Korpusu medRxiv nie uzupełniamy.** Brakujące 1 124 preprinty z lipca i sierpnia były potrzebne
pracy o myślnikach, która czyta pełny tekst JATS. Nasza warstwa lead–lag potrzebuje tytułu
i abstraktu, a te API medRxiv zwraca dla całego okna, bez S3.

Dla protokołu: strona TDM medRxiv podaje, że *„The full set of processed PDF and XML files from
medRxiv is deposited each month with delivery completing typically a few days into the new month"* —
czyli brak `Current_Content/August_2026/` 26 sierpnia jest właściwością źródła, nie usterką.

## 4. Scaffolding

`README.md` (pytanie badawcze, gdzie leżą dane, jak uruchomić pipeline, odesłanie do
`docs/protocol/plan_do_recenzji.md`), `.gitignore` (poświadczenia, `__pycache__`, `parsed/`,
`*.xml.gz`, `data/raw/*` — **bez** `docs/`), `LICENSE`, `requirements.txt`,
`CITATION.cff` **nowy, nie kopiowany z myślników**.

## 5. Pierwszy commit i raport

```powershell
git init -b main
git add -A
git commit -m "Pierwszy commit: narzędzia i protokół badania dyfuzji technologii w ortopedii"
```

Zaraportuj: nazwę repo, hash commitu, potwierdzenie sha256 dla skopiowanych plików,
`git log --oneline -1` w obu repozytoriach (w `myslniki` ma być bez zmian: `7f2ae16`).

## 6. Osobna usterka w `myslniki` — tylko do sprawdzenia, nie do naprawy teraz

`CITATION.cff` podaje `repository-code: https://github.com/P-Czum/em-ergence-em-dash`,
a remote to `github.com/P-Czum/myslniki`. Jeśli ten link figuruje w depozycie OSF lub Zenodo,
prowadzi w nieistniejące miejsce. Zgłoś Przemkowi, **nie zgaduj i nie poprawiaj** — to jest
materiał depozytowy zamkniętej pracy.
