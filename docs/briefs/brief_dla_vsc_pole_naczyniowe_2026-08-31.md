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

---

# UZUPEŁNIENIE tego samego wieczoru — audyt pozostałych 55 deskryptorów. Trzy kolejne wycieki

Pełne liczby: `docs/protocol/scoping_log.md`, wpis „audyt pozostałych 55 deskryptorów", D5a–D5e.
**Zrób to w tym samym przebiegu co D4 — nie ma sensu przeliczać pola dwa razy.**

## Z5. Reguła D5a — stomatologia, strukturalna

Pięć deskryptorów pola leży też w E06 lub E04.545: **D056948, D059546, D019340, D059229, D064728**.

```
(mesh_ui ∩ FIELD) ⊆ {D056948, D059546, D019340, D059229, D064728}   →  wyłącz
```

Oczekiwane: **6 178 rekordów (2,30%)**. Zgłoś, jeśli wyjdzie inaczej.

Regułę wyprowadź **z drzew, nie z listy** — `any(t.startswith("E06") or t.startswith("E04.545")
for t in trees)` — żeby przeżyła zmianę wersji MeSH i żeby dało się ją zapisać jednym zdaniem
w Metodach.

## Z6. Reguła D5b — dwa deskryptory mieszane, DO ZMIERZENIA, nie do przyjęcia w ciemno

`Osteogenesis, Distraction` (D019857) i `Bone Transplantation` (D016025) mieszczą materiał
ortopedyczny i twarzoczaszkowy. Moje liczby (49,5% i 26,1% twarzoczaszki) pochodzą z **sond
słownych na tytułach** i są dolnym oszacowaniem, nie pomiarem — 45% i 66% próbek nie trafiło
w żadną sondę.

Proponowana reguła, **do zmierzenia przed przyjęciem**:

```
(mesh_ui ∩ FIELD) ⊆ {D019857, D016025}
        AND
mesh_ui zawiera deskryptor z poddrzewa A14 (Stomatognathic System)
        lub C07 (Stomatognathic Diseases)
```

UI rozwiń sam z `desc2026.xml` — masz go, ja nie. **Zmierz rozdzielczość tak jak przy D4**:
udział dokumentów kilku terminów kontrolnych w podzbiorze objętym regułą. Terminy do kontroli:
`mandibular distraction osteogenesis`, `pierre robin sequence`, `dental implant`, `alveolar bone
graft` po stronie obcej; `limb lengthening`, `nonunion`, `spinal fusion`, `bone graft` po
stronie ortopedycznej. **Jeśli separacja nie wychodzi tak czysto jak przy D4 (obca ≥ 90%,
ortopedyczna ≤ 5%) — nie wdrażaj, zgłoś liczby.**

## Z7. Reguła D5c — homonim `Traction`, priorytet niski

`Traction` (D014143) w MeSH oznacza fizyczne pojęcie wyciągu. 400 z 2 008 rekordów wchodzących
wyłącznie tędy dotyczy narządów poza układem ruchu (`endoscopic submucosal dissection` 103
na próbie, choroba Peyroniego 30).

```
(mesh_ui ∩ FIELD) = {D014143}
        AND
mesh_ui zawiera deskryptor z C06 (Digestive), C12 (Urogenital) lub C11 (Eye)
```

~0,15% pola. Zrób, jeśli tanie; jeśli nie — zgłoś jako nienaprawione i idziemy dalej.

## Z8. Czego NIE ruszać

- `Manipulation, Orthopedic` — 6,9% chiropraktyki, poniżej progu działania. Zostaje.
- Pozostałe 30 deskryptorów ogona — sprawdzone, bez zastrzeżeń. Zostają.
- **def2 zostaje bez zmian.** 3 czasopisma ze 137 są wątpliwe (`Head & face medicine`,
  `Gait & posture`, `Journal of clinical densitometry`). Nie wycinaj ich — def2 ma być
  **niezależną** definicją, a przycinanie jej pod def1 niszczy jej wartość jako kontroli.
  Odnotuj w raporcie.

## Kontrola łączna po D4 + D5a

Pole 2005–2025: **268 383 → ok. 255 070** (−7 135 −6 178, minus ewentualne nakładanie się reguł
— podaj dokładną liczbę i wielkość części wspólnej).
