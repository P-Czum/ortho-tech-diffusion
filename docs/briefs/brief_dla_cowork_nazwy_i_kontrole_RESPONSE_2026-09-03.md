# CBCT wypada — 82,5% stomatologii. Materiał 60. Plus: `arcr` był źle zaklasyfikowany

Autor: sesja VS Code, 2026-09-03. Dotyczy: `brief_dla_vsc_nazwy_i_kontrole_2026-09-03.md`.

Wyniki: `osie_60.csv`, `material_61.csv`, `grupy_61.json`, `retronimy.csv`.

**§2 najpierw, zgodnie z prośbą — i wypada gorzej, niż zakładałeś.**

---

## 1. §2 — skażenie stomatologiczne

Udział dokumentów z deskryptorem z A14, C07, E06 lub E04.545:

| technologia | prac | stomatologicznych |
|---|---:|---:|
| **cone beam computed tomography** | 565 | **82,5%** |
| mimic software | 165 | 11,5% |
| 3d printing | 476 | 8,2% |

**CBCT przekracza Twój próg czterokrotnie.** To nie jest zanieczyszczenie marginesu — to
technologia, która w tym korpusie jest w przeważającej części narzędziem stomatologicznym
i twarzoczaszkowym. Wypada z materiału.

Boli podwójnie, bo CBCT było **sztandarowym przykładem technologii „światowej"** — 14,7
efektywnych krajów, pozycja ilustrująca rozproszony koniec osi koncentracji. Następcy w tej
roli poniżej.

**Uwaga ogólniejsza:** D5a wyłącza rekord tylko wtedy, gdy **wszystkie** jego deskryptory pola
są stomatologiczne. To ta sama luka, którą przy weterynarii zamknęło D6 — znacznik na poziomie
rekordu zamiast warunku na wyłączność. Sprawdziłem trzy technologie, które wskazałeś; **nie
wiem, czy nie ma czwartej i piątej.** Policzenie udziału dla wszystkich 60 to jeden przebieg
tej samej maszynerii. Nie robię, bo prosiłeś o trzy i o niedokładanie analiz — ale przy 82,5%
u pozycji sztandarowej ryzyko jest realne.

## 2. §3 — `cta` wypada, i to nie jest angiografia

| rozwinięcie | prac | udział |
|---|---:|---:|
| cuff tear arthropathy | 69 | **29,5%** |
| angiografia TK | 39 | 16,7% |
| jakiekolwiek „arthropathy" | 72 | 30,8% |

Brak dominanty, a **częstsze jest rozpoznanie, nie technologia**. Wypada wedle §4a.

## 3. §4 — szczyt przed wyłonieniem: reguła trwałości, nie usterka

Oba przypadki mają ten sam mechanizm: **szczyt należy do wcześniejszego zrywu, który nie
utrzymał się trzech lat.**

`highly cross linked polyethylene` — nad progiem w 2005, **2006 poniżej**, 2007, 2008; pierwsza
seria nigdy nie ma trzech lat pod rząd. Szczyt 0,170% w 2008 należy do niej. `y₀` 2015 pochodzi
z drugiego, trwałego wzrostu.

`mesenchymal stem cell` — nad progiem 2010, potem 2013–2014 (para, za krótka), pierwszy ciąg
trzyletni to 2017–2019. Szczyt 0,338% w 2013.

**Twoja diagnoza trafna: `y₀` to drugi start.** Do Metod jednym zdaniem: `y₀` jest rokiem
pierwszego wzrostu **trwałego**, nie pierwszego wzrostu.

## 4. §1 — scalenia. Wychodzi 60, nie 61

`arcr` był już usunięty w materiale 66, więc jego przywrócenie jako członu nie dodaje grupy.
66 − 4 scalenia − CBCT − `cta` = **60**.

Hierarchie oznaczone kolumną `nadrzedny`: `percutaneous kyphoplasty` → `kyphoplasty`,
`proximal femoral nail antirotation` → `cephalomedullary nail`, `volar locking plate` →
`locking plate`. Wszystkie sześć pozycji w materiale.

### `arcr` — Wasza klasyfikacja była błędna, i to dwukrotnie

Ortopeda zapytał, czy to na pewno stary termin. Sprawdziłem — **nie jest.**

```
                                    00    05    10    15    20    24    25
arthroscopic rotator cuff repair  0.09  0.13  0.26  0.42  0.70  0.79  0.66
open repair                       0.07  0.20  0.12  0.14  0.08  0.10  0.06
```

Naprawa artroskopowa rośnie **dziewięciokrotnie**, 1 198 prac, `y₀` 2014, trwałość 0,84.
Naprawa otwarta spada do **29% szczytu** z 2002. To jest **para zastąpienia**, jak blokada udowa
i blokada kanału — nie generyk. Wasze przypuszczenie ze `scoping_log`, że artroskopia była
realnym przesunięciem kosztem naprawy otwartej, potwierdza się w danych.

Scalenie jest słuszne, ale **powód był zły**: to nie porządkowanie nazw, tylko dołączenie
skrótów do prawdziwej pozycji materiału. `open repair` nie wyłania się (wysoka baza 2000–02),
więc widzimy tylko rosnącą połowę pary — ta sama ślepa plamka co przy `hip resurfacing`.

## 5. §7 — tabela retronimów, dziesięć pozycji

**Mocne kandydatury** (rywal obecny wcześniej, wysoka krotność):

| pozycja | y₀ | rywal | obecny od | krotność |
|---|---:|---|---:|---:|
| single bundle | 2010 | double bundle reconstruction | 2007 | 458× |
| mechanical alignment | 2018 | kinematic alignment | 2016 | 429× |
| primary anterior cruciate ligament reconstruction | 2012 | **revision** ACL reconstruction | 2005 | 111× |
| anterior cervical discectomy fusion | 2013 | cervical disc arthroplasty | 2009 | 60× |
| anatomic total shoulder arthroplasty | 2015 | reverse shoulder arthroplasty | 2007 | 39× |

**Odpowiedź na §6: ACDF kwalifikuje się** — CDA obecna od 2009, cztery lata przed `y₀` ACDF.
Czwarty wiersz powstaje. Domysł o `primary ACL ← revision ACL` potwierdza się: rywal od 2005.

**Trzy kandydatury to kontekst, nie rywalizacja** — i to jest granica miary, którą stawiam jawnie:

- `primary unilateral total knee arthroplasty` ← `adductor canal block` (45×)
- `elective total knee arthroplasty` ← `adductor canal block` (32×)
- `pelvic fixation` ← `adult spinal deformity surgery` (65×)

Blokada kanału nie jest rywalem endoprotezoplastyki kolana, tylko znieczuleniem **wykonywanym
podczas niej**. Fiksacja miednicy jest **elementem** chirurgii deformacji, nie jej konkurentem.
Współwystępowanie mierzy „występują razem" i obejmuje zarówno rywalizację, jak i zawieranie.

`posterior lumbar fusion` ← `transforaminal lumbar interbody fusion` (12×) jest graniczne —
TLIF to realnie alternatywne podejście, ale krotność najniższa w tabeli.

### `unilateral anterior cruciate ligament reconstruction` — jedyna bez kandydata, i wiadomo dlaczego

Ortopeda zapytał, co „jednostronna" tu w ogóle znaczy. Sprawdzone na 175 pracach: **to zwykłe
ACL.** 30% prac porównuje ze stroną zdrową, 22% liczy wskaźnik symetrii kończyn, 21% wspomina
obustronność. Tytuły są zwyczajne — *quadriceps versus patellar autograft*, *techniques for
reducing anterior knee symptoms*.

Fraza jest **artefaktem chunkowania zdania o doborze chorych**, nie nazwą zabiegu. Dlatego jako
jedyna nie ma rywala: nie ma z czym konkurować, bo nie jest osobną rzeczą. Zostaje generykiem —
z powodem zmierzonym, nie założonym.

## 6. Materiał 60 — liczby do tekstu

| | |
|---|---|
| `y₀` po dekadach | 2000–09: **11**, 2010–19: **40**, 2020–25: **9** |
| `kraj_eff_n ≤ 2,5` | **11 grup** — Chiny 6, USA 5; nadal wyłącznie te dwa kraje |
| `kraj_eff_n ≥ 9` | **10 grup** |
| bez czasu podwojenia | **11** — szczyt < 2 lata po `y₀`: 8, nachylenie niedodatnie: 3 |
| szczyt w 2025 | **16 grup** |
| zaniki (trwałość < 0,5) | **12** |
| mediana braków kraju | 9,4% |

### Następca CBCT na rozproszonym końcu osi

| grupa | kraj | udział | tło | eff. krajów | prac |
|---|---|---:|---:|---:|---:|
| volar locking plate | Japonia | 16% | 5,0% | **12,8** | 363 |
| short stem | Niemcy | 17% | 5,5% | **12,8** | 258 |
| patient specific instrumentation | USA | 18% | 27,9% | 12,0 | 569 |
| locking plate | Chiny | 20% | 13,8% | 10,0 | 1 574 |

**`volar locking plate` i `short stem` są lepszymi przykładami niż CBCT**, bo ich kraj czołowy
jest spoza pary Chiny/USA i mimo to mają udział poniżej 20% — czyli rozproszenie jest tam
własnością technologii, a nie skutkiem tego, że nikt się nią szczególnie nie zajmuje.

## 7. Kontrole

Materiał **60**. Manifest **12/12**. Słownik synonimów i klasyfikacja nietknięte.
