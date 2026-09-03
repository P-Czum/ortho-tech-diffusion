# Audyt `methods_v1.md` i `skeleton_v2.md`. Metody są w większości poprawne — ale mają cztery puste nawiasy i jedną liczbę, której nie da się obronić

Autor: sesja VS Code, 2026-09-03. Z własnej inicjatywy — nadal nie ma nowego briefu do mnie.

`methods_v1.md` nie ma następcy, więc jest żywym dokumentem Metod niezależnie od tego, czy `v1`
Wyników i szkieletu są jeszcze aktualne. `skeleton_v2.md` jest żywy z definicji. Domknięcie
audytu z 13:42.

**Najpierw dobra wiadomość, bo jest większa, niż się spodziewałem: aparat metodologiczny opisany
w `methods_v1.md` jest opisany poprawnie.** Progi detektora, definicja pola, reguły wyłączeń,
liczby MTIX, warstwa leków — wszystko zgadza się z kodem i danymi. Błędy są w liczbach materiału
i w czterech nawiasach do uzupełnienia.

---

## 1. `methods_v1.md` — co jest poprawne

| twierdzenie | weryfikacja |
|---|---|
| „56 descendants" | `field_orthopedic_procedures.csv`: **56** |
| „137 journals ... Broad Subject Term *Orthopedics*" | `journals_orthopedics.csv`: **137** |
| „five descriptors that also belong to the dentistry subtree" (D5a) | brama z drzew: **5** — Le Fort, orthognathic, sagittal split ramus, sinus floor augmentation, alveolar bone grafting |
| progi detektora: 5 × baza 2000–02, ≥ 0,1%, ≥ 5 prac, 3 lata z rzędu | zgodne ze stałymi w kodzie |
| „no phrase can emerge after 2023" | `Y0_MAX = 2023` |
| spaCy 3.8, `en_core_web_sm` | 3.8.16 / 3.8.0 |
| „80% of the registered 287-term core" | 229/287 = **79,8%** |
| „κ = 0.44 against a preregistered threshold of 0.70" | **0,442** / 0,70 |
| „Drugs (**seven** phrases) ... analysed separately" | `kontrast_leki.csv`: **7** wierszy |
| skróty wykluczone `ai`, `ha`, `cr`, `ka` | wszystkie cztery **nieobecne** w materiale |
| „median of 9% of papers per group" (braki kraju) | mediana **9,4%** |
| MTIX: „13.1 (2018) ... 8.7 (2022) ... 12.5 (2025)" | **13,14 / 8,70 / 12,48** — komplet zgodny |
| MTIX: „ρ = 0.14, p = 0.36, n = 43" | `mtix_mech.log`: **ρ = +0,143, p = 0,3601, n = 43** |
| „Two groups fitted neither" | zgodne: `femoral nerve block` (przesunięcie), `computer navigation` (wchłonięcie) |

## 2. `methods_v1.md` — poprawki

| w tekście | poprawnie |
|---|---|
| „yielded ⟨**1,294**⟩ candidate phrases" | **1 289** (`rdzen_d6.json`) |
| „removed ⟨n⟩ records, **9%** of the field, leaving ⟨N⟩" | **26 335** rekordów, **8,8%**, zostaje **271 332** |
| „the **eleven** deviations" | `deviations.md` ma **dziesięć** (D-1 … D-10) |
| „three ... as retronyms and **seven** as generic descriptions" | trzy retronimy i **sześć** generyków — siódmym był ACDF, który **zostaje w materiale** (patrz brief z 13:42 §1) |
| „**66** technology groups ⟨61 pending⟩" | **60** |
| doubling time „not computed ... (⟨n⟩ groups)" | **11** — szczyt < 2 lata po `y₀`: 8, nachylenie niedodatnie: 3 |
| „missing ... (maximum ⟨…⟩)" | **19,6%** |
| „vascular limb salvage entering through *Amputation, Surgical* and *Limb Salvage*" | brama D4 ma **cztery** deskryptory — dochodzą *Disarticulation* i *Hemipelvectomy* |

### Dwie rzeczy, które wymagają przeliczenia, a nie tylko przepisania

**(a) MTIX `n = 43` policzone na nieaktualnej liście terminów.** Statystyka jest poprawna, ale
zbiór testowy zawiera co najmniej dziewięć fraz, których w materiale 60 nie ma —
`primary hip arthroscopy`, `anatomic total shoulder arthroplasty`, `machine learning`,
`virtual reality`, `3d printing technology`, `oblique lateral interbody fusion`,
`primary unilateral total knee arthroplasty`, `unilateral anterior cruciate ligament
reconstruction`, `arcr`. W tekście stoi „n = 43" obok „60 grup" i recenzent to zestawi.
Przeliczenie to jeden przebieg `mtix_mechanizm.py`; wniosek („brak związku") prawie na pewno
się nie zmieni, ale liczba musi pasować do materiału.

**(b) Warstwa leków policzona przed filtrami pola.** `kontrast_leki.csv` jest z 2026-09-01
i **dwa z siedmiu leków mają `y₀` starsze o trzy lata** niż w obecnym detektorze:

| lek | `y₀` w pliku | `y₀` obecnie |
|---|---:|---:|
| `multimodal analgesia` | 2021 | **2018** |
| `local infiltration analgesia` | 2017 | **2014** |

Pozostałe pięć ma `y₀` zgodne; liczby prac różnią się o 1–14. Plik trzeba odtworzyć na
`emerging_d6_primary`.

### Jedna rzecz, którą można teraz wzmocnić, a nie poprawić

„We identified them one by one — **none by a planned test**" jest nadal prawdą co do tego, **jak
je znaleziono**. Ale od 2026-09-03 istnieje test planowy na całym materiale
(`audyt_skazenia.py`): **0 z 60 grup powyżej 20%**, mediana 0,6%, udział weterynaryjny dokładnie
0,0% wszędzie. Zdanie może zostać, jeśli dopiszesz drugie — bo z niego wypadło CBCT i to jest
argument, nie przyznanie się do słabości.

## 3. `skeleton_v2.md` — poprawki

Poza tymi z briefu z 12:18 (materiał 60, nie 66/76; 16 jeszcze rosnących; 11 jednokrajowych;
55 z 60 prowadzonych przez USA/Chiny):

| linia | w tekście | poprawnie |
|---:|---|---|
| 23 | „yielded **76** technology groups" | **60** |
| 23 | „For the **13** groups whose attention fell below half" | **12** — i sprzeczne z „Twelve" w linii 25 |
| 25 | „**76** technologies emerged" | **60** |
| 25 | „robotic assistance (**2020**)" | `y₀` **2019** |
| 25 | „ranged from 1.2 to **14.7**" | 1,2 do **12,8** |
| 25 | „**primary hip arthroscopy (89.0% USA)**" | po scaleniu: `hip arthroscopy`, **63,3%** USA |
| 25 | „**cone-beam CT**, short-stem hips, volar locking plates and PSI ... **12–15** countries" | CBCT usunięte; pozostała trójka **12,0–12,8** |
| 25 | „hip arthroscopy (doubling **1.7** years), robotic (**2.0**)" | hip arthroscopy **7,0**; robotic **2,2**; najszybsza jest **AI, 2,1** |
| 25 | „**61 of 66**" | **55 z 60** |
| 25 | „**Eleven of 24** apparent declines" | **10 z 22**, rozkład 5 + 5 |
| 29 | „has since had to learn, evaluate, or decline **76** technologies" | **60** |
| 42 | „**11 of 24** declines were renamings; **76** groups" | **10 z 22**; **60** |
| 45 | „**eleven** deviations tabulated in S1" | **dziesięć** |
| 48 | „Table 1: **76** groups" | **60** |
| 49 | „Table 4, **four rows**" | **trzy** — ACDF wypada |
| 50 | „USA: hip arthroscopy, **ATSA**, TMR, MUA, EMR" | **ATSA jest wykluczone jako retronim** — nie może być przykładem literatury jednokrajowej |
| 50 | „worldwide ones (**CBCT**, short stem, volar plate, PSI, MSC)" | CBCT usunięte |
| 51 | „**61 of 66** led by USA or China" | **55 z 60** |
| 61 | „three retronyms, **3–8 years** after the rival" | **2–8 lat** (single bundle 3, ATSA 8, mechanical alignment **2**) |
| 67 | „S5 full **76-group** table" | **60** |
| 77 | „The **13** declines by evidence state" | **12** |

### Linia 63 — jedno ograniczenie do skreślenia, jedno do zostawienia

> „MeSH-defined fields leak, and **no systematic test for it exists**"

**Już istnieje.** `audyt_skazenia.py`, cały materiał, wynik w §2 wyżej. To zdanie trzeba
przepisać z „nie mamy testu" na „test jest i pole go przechodzi, z jednym wyjątkiem, który
usunęliśmy". Reszta linii 63 zostaje bez zmian — PRP, BMP, VR, ACI/mikrozłamania, MSC są
wszystkie policzone i trafne.

### Uwaga do linii 25 i 52 — nie ruszaj pasm trwałości

„0.17–0.25 of peak at 3–5 years versus 0.35–0.73" jest **zgodne co do setnej**, tak samo jak
komplet pasm w `results_v2.md`. To jedyny akapit Wyników, który przeszedł oba audyty bez
poprawki.

## 4. Jedna liczba, której nie da się obronić w żadnym wariancie

„**no country above 24%**" w `results_v2.md` — `latarjet procedure` ma **USA 25,0%** przy eff 9,2.
Próg 24% wyklucza go, a jest jednym z dziesięciu. Napisz „poniżej 25%" albo „żaden powyżej jednej
czwartej".

## 5. Kontrole

| | |
|---|---|
| materiał | **60**, nietknięty |
| osie | nietknięte |
| manuskrypt | **nietknięty** — poprawki podaję, nie wprowadzam |
| manifest | **12/12** |
