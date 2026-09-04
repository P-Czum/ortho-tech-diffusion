# Materiał: scalenie kifoplastyki, cztery usunięcia, podział na sześć klas

Autor: sesja Cowork, 2026-09-03. Zastępuje `brief_dla_vsc_liczby_do_tekstu_2026-09-03.md`
(punkt 1 tamtego briefu rozstrzygnięty — odpowiedź była w `results_v1.md`; punkty 2 i 3
rozstrzygnięte Twoim audytem; punkty 4 i 5 przeniesione tu jako §5).

Podstawa: `rozstrzygniecie_materialu_2026-09-03.md` i `podzial_materialu_2026-09-03.md`
w `docs/protocol/`. Decyzje Przemka, wykonanie Twoje.

**Kolejność ma znaczenie:** §4 (przypisanie klas) musi być zamrożone **przed** przeliczeniem
osi z §1–§3, inaczej klasy nie mogą być raportowane jako wynik.

*(Dokument wpłynął przez czat, nie przez dysk; zapisany przez sesję VS Code 2026-09-03 dla
kompletności rejestru. Treść bez zmian.)*

---

## 1. Scal — jedna para, ta najważniejsza

**`kyphoplasty` + `percutaneous kyphoplasty` → jedna grupa `kyphoplasty`**, człony:
`kyphoplasty | balloon kyphoplasty | percutaneous kyphoplasty | pkp`.

Kifoplastyka jest przezskórna z definicji. To ta sama procedura pod nazwą zachodnią i chińską;
skrót `pkp` w członach to potwierdza.

| | `kyphoplasty` | `percutaneous kyphoplasty` |
|---|---|---|
| prac | 1 263 | 573 |
| y₀ / szczyt | 2005 / 2011 | 2010 / 2024 |
| kraj czołowy | USA 25,1% (0,86) | Chiny 90,5% (6,05) |
| trwałość 2025/szczyt | 0,39 | 0,91 |

Do przeliczenia po scaleniu: wszystkie osie, trwałość względem szczytu, **status w zanikach**
(wypadnie między 0,39 a 0,91; jeśli > 0,5 — zaników jest 11 i pasmo „dowody za, adaptacja"
traci kifoplastykę). Kraj czołowy prawie na pewno przestaje być chiński — więc **flagowy
przykład literatury jednokrajowej z Wyników i streszczenia przestaje istnieć.** Wskaż następcę
spośród pozostałych dziesięciu (kandydaci: PELD 81,4%, Mimics 84,9% z zastrzeżeniem z §2).

**`vertebral augmentation` → przemianuj na `vertebroplasty`.** Człony (`pvp`,
`vertebral augmentation`) to wertebroplastyka, zabieg bez balonu — odrębna technika. Nazwa
grupy ma mówić to, co człony. Po przemianowaniu nie ma hierarchii z kifoplastyką.

## 2. Usuń — trzy pewne, jedna warunkowa, jedna do pomiaru

Zasada: *pozycja materiału to jedna rzecz, którą chirurg wybiera dla chorego*.

| usuń | prac | powód |
|---|---:|---|
| `adult spinal deformity surgery` | 440 | obszar chirurgii, nie zabieg |
| `revision anterior cruciate ligament reconstruction` | 457 | wskazanie, nie technika; **zostaje w tabeli retronimów** jako punkt odniesienia dla `primary ACL` |
| `electronic medical record` | 439 | system informatyczny |

**`anterolateral ligament` (158) — warunkowo.** Struktura anatomiczna. Sprawdź, czy
`anterolateral ligament reconstruction` istnieje jako fraza w słowniku. Jeśli tak —
**przemianuj**, pozycja zostaje jako technika. Jeśli nie — usuń.

**`finite element analysis` (1 504) — pomiar, nie decyzja.** Dwa desygnaty: model implantu
generycznego (warsztat) wobec modelu z tomografii konkretnego chorego (planowanie, jak Mimics).
Policz udział prac patient-specific. Do czasu pomiaru decyzja z 2026-09-02 obowiązuje i FEA
zostaje.

**`mimic software` zostaje**, ale w Tabeli 1 oznacz jako nazwę produktu (jedyna obok PFNA).

## 3. Oznacz — trzy hierarchie, kolumna `zawiera_sie_w`

| rodzaj | gatunek |
|---|---|
| `locking plate` | `volar locking plate` |
| `cephalomedullary nail` | `proximal femoral nail antirotation` |
| `total disc replacement` | `cervical disc arthroplasty` |

Obie strony zostają. W tekście: *N pozycji opisujących M odrębnych technologii*, M policzone.

`hip arthroscopy` / `labral repair` — **nie** hierarchia (narzędzie–procedura, jak ARCR wobec
artroskopii barku). Bez oznaczenia.

Osobno do Dyskusji: `cephalomedullary nail` (y₀ 2021) wyłonił się **dekadę po** PFNA (2011) —
nazwa rodzajowa po nazwie produktu.

## 4. Podział na sześć klas — ZAMROZIĆ PRZED §1–§3

Przypisanie zrobione z nazw, bez patrzenia na osie. Zapisz jako kolumnę `klasa` z datą
i hashem, **zanim** przeliczysz cokolwiek z §1–§3.

| klasa | pozycje (stan przed operacjami) |
|---|---|
| **I. implant i materiał** | cephalomedullary nail, proximal femoral nail antirotation, femoral neck system, dual mobility cup, short stem, locking plate, volar locking plate, polyetheretherketone, highly cross linked polyethylene, mom total hip arthroplasty |
| **II. endoprotezoplastyka** | reverse shoulder arthroplasty, unicompartmental knee arthroplasty, total ankle arthroplasty, total elbow arthroplasty, total disc replacement, cervical disc arthroplasty, hip resurfacing |
| **III. technika operacyjna** | direct anterior approach, latarjet procedure, ponseti method, open wedge high tibial osteotomy, pedicle subtraction osteotomy, periacetabular osteotomy, transforaminal / lateral / oblique lumbar interbody fusion, anterior cervical discectomy fusion, percutaneous endoscopic lumbar discectomy, kyphoplasty (scalona), vertebroplasty, arthroscopic rotator cuff repair, hip arthroscopy, labral repair, double bundle reconstruction, medial patellofemoral ligament reconstruction, lateral extra articular tenodesis, minimally invasive plate osteosynthesis, targeted muscle reinnervation, manipulation under anesthesia, kinematic alignment *(dopisek: strategia planowania)* |
| **IV. narzędzie wspomagające** | computer navigation, robotic assistance, patient specific instrumentation, 3d printing, augmented reality, mimic software, artificial intelligence / machine learning, ultrasound guidance, *finite element analysis jeśli zostaje* |
| **V. postępowanie okołozabiegowe** | femoral nerve block, adductor canal block, motor evoked potential |
| **VI. terapia biologiczna** | mesenchymal stem cell, autologous chondrocyte implantation, microfracture |

Na materiale 60 klasy różnią się na każdej osi (implanty: podwojenie 18 lat, 7,7 kraju;
techniki: 5 lat, 4,8 kraju; narzędzia: y₀ 2019, 5/8 rośnie; biologiczne: 3/3 w zanikach).
Po operacjach przelicz tabelę: y₀ mediana, podwojenie mediana, kraje efektywne mediana,
szczyt 2025, zaniki — per klasa. Klasy V i VI opisowo, bez statystyki.

## 5. Pozostałe z poprzedniego briefu

- **`D5b`** (6 286 rekordów) nie ma opisu w Metodach; cztery pozostałe reguły mają. Nazwij
  albo wyjaśnij.
- **Wariant „tylko tytuł"** — Metody mówią o trzech wariantach, zarejestrowany rdzeń był
  przecięciem czterech. Status na nowej jednostce?
- **Druga definicja pola** — plan v0.8 linia 70 obiecuje „każdy wynik w obu definicjach",
  linia 94 degraduje def2 do wrażliwości. Decyzja Przemka; jeśli zostaje degradacja — wiersz
  w S1 i poprawka linii 70.
- **Retronimy — zmiana zdania w Metodach**, nie decyzji: nie „nazwy nadane istniejącemu
  standardowi" (wyrównanie mechaniczne funkcjonuje od Insalla), tylko „nazwy, które weszły do
  piśmiennictwa jako kontrast wobec nowej". Usunięcia zostają.
- **MTIX `n = 43`** i **warstwa leków** — Twoje dwie pozycje do przeliczenia z audytu, nadal
  otwarte.

## 6. Po wszystkim

Przelicz każdą liczbę w `results_v2.md` i `methods_v2.md` na nowym materiale
(spodziewane: 55–56 pozycji, 51–52 odrębne technologie, zaników 11 lub 12). Manifest nie jest
dotknięty żadnym punktem.
