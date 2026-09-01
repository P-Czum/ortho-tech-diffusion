# Brief dla VS Code — pole wpuszcza chirurgię naczyniową. Reguła D4 i przeliczenie

Autor: sesja Cowork, 2026-08-31 (po `brief_dla_vsc_kodeks_v13_RESPONSE_2026-08-31.md`).
**Ten brief ma pierwszeństwo przed `osie_sily` — osie liczone na skażonym polu byłyby do wyrzucenia.**

## 1. Co jest nie tak

`Orthopedic Procedures` ma wśród 56 potomków `Amputation, Surgical` (D000671) i `Limb Salvage`
(D023821). Wchodzi tędy piśmiennictwo o niedokrwieniu kończyn: **15 899 rekordów (5,92% pola)**
wchodzi **wyłącznie** przez te deskryptory.

Separacja jest zupełna — udział dokumentów terminu w tym podzbiorze: `chronic limb threatening
ischemia` 100,0%, `clti` 100,0%, `amputation free survival` 99,7%, `peripheral artery disease`
97,6% — wobec `direct anterior approach` 0,0%, `periprosthetic joint infection` 0,5%,
`3d printing` 2,0%.

Pełne liczby i uzasadnienie: `docs/protocol/scoping_log.md`, wpis 2026-08-31 wieczorem, decyzja **D4**.

## 2. Reguła D4 — do zaimplementowania dokładnie tak

Rekord wyłączony z pola, jeżeli:

```
(mesh_ui ∩ FIELD) ⊆ {D023821, D000671, D004188, D006428}
        AND
(mesh_ui ∩ {D058729, D016491, D007511, D017719, D014652, D001157, D003920, D048909}) ≠ ∅
```

Usuwa **7 135 rekordów (2,66% pola)**. Lista PMID do kontroli:
`data/processed/pmid_naczyniowe_scisle.csv`.

**Nie odrzucaj wszystkich 15 899** — 1 306 z nich to ortopedia onkologiczna (mięsaki kości,
hemipelwektomia), materiał bezsporny.

## 3. Kolejka

### Z1. Zaimplementuj D4 w `code/stage1_field.py` i przelicz pole
Kontrola: pole 2005–2025 spada z **268 383** do **261 248** (±kilka, jeśli inaczej liczysz
brzegi lat — zgłoś rozbieżność, nie dopasowuj).

### Z2. Przelicz zliczanie i detekcję wyłonienia na nowym polu
Ekstrakcji fraz **nie powtarzaj** — `noun_chunks.parquet` jest per-PMID, wystarczy filtr.
Powtórki wymaga `count_noun_phrases.py` i `detect_emergence.py`, bo zmienia się mianownik.

Kontrola: `chronic limb threatening ischemia`, `clti`, `peripheral artery disease`,
`amputation free survival`, `endovascular therapy`, `endovascular revascularization`,
`diabetic foot ulcer`, `drug coated balloon`, `major amputation rate` **znikają z list wyłonień**.
Jeśli któryś zostaje — wypisz go z liczbami, to znaczy, że reguła jest za wąska.

### Z3. Odbuduj rdzeń i materiał
Nowy rdzeń = primary ∩ S2 ∩ S3 na przeliczonym polu. Zgłoś, ile fraz, i jak zmienił się
ranking wobec 813. Klasyfikacji **nie ruszaj** — `np_kategorie_propozycja.tsv` jest mapowaniem
termin→kategoria, przeżywa zmianę pola; zgłoś tylko terminy nowe, których w niej nie ma.

### Z4. Dopiero teraz osie siły
`brief_dla_vsc_osie_sily_2026-08-31.md` bez zmian merytorycznych, ale **na przeliczonym polu**
i na odbudowanym materiale (poprzednio 55 pozycji — po D4 będzie mniej lub tyle samo, bo
`endovascular therapy` i `endovascular revascularization` z niego wypadną).

## 4. Czego NIE robić

- Nie odrzucaj `transfemoral amputation` — 6,7% wąską regułą, to protetyka i rehabilitacja,
  nie naczyniówka. Zostaje świadomie.
- Nie ruszaj progu ≥ 50, definicji wyłonienia, ani listy 56 deskryptorów. D4 jest filtrem
  **na rekordach**, nie zmianą poddrzewa.
- Nie poprawiaj `np_kategorie_propozycja.tsv`.
- Nie dotykaj dwunastki zamrożonej rejestracją. `coding_manual_v1.2.md` bez zmian, v1.3 to
  osobny plik.

## 5. Format raportu

`docs/briefs/brief_dla_cowork_pole_naczyniowe_RESPONSE_2026-08-31.md`. Liczbami. Dla Z2 —
wypisz dosłownie, które z dziewięciu terminów kontrolnych zniknęły, a które nie.

## 6. Uwaga

Git z mostka Coworku zostawia `.git/index.lock` (brak tożsamości git w tej maszynie, brak prawa
usuwania). Nie ruszam go stamtąd. Do posprzątania: `_to_delete/` i `git gc`.
