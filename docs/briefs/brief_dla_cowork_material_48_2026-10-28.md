# Materiał 48 — skróty scalone z pełnymi nazwami (§4a). Zastępuje liczby materiału 54

Autor: sesja VS Code, 2026-10-28. Decyzja Przemka po `walidacja_RESPONSE` §6: *„skróty i całe
nazwy powinny być razem”*.

**Kontrola rozstrzygająca: 45 grup, których zmiana nie dotyczy, ma osie, szeregi, trwałość i kraje
pochodzenia identyczne z materiałem 54 co do komórki (0 różnic).** Zmieniło się dokładnie to,
co miało się zmienić.

---

## 1. Co zrobiono i dlaczego to nie jest nowa decyzja

Reguła §4a (v1.4, 2026-09-02): *skrót wchodzi do materiału scalony z pełną postacią albo wypada,
nigdy jako osobna pozycja.* Dziewięć grup tę regułę łamało: etykieta była pełną nazwą, a szereg
liczył sam skrót. Liczyliśmy więc prace, które **użyły skrótu**, a nie prace o technologii. Ta
krzywa rośnie razem z nawykiem pisania skrótów w streszczeniach. Teraz każda grupa zawiera
rozwinięcie swojego skrótu i frazę, od której ma nazwę.

**Zapisane w `docs/protocol/deviations.md` §4 jako incydent proceduralny** (błąd wykonania §4a),
nie jako odchylenie. Rejestr zostaje przy *„Two of twelve”*.

| grupa | było | po scaleniu | wynik |
|---|---|---|---|
| total ankle arthroplasty | taa, tar — 853 prace, `y₀` 2007 | + total ankle arthroplasty, total ankle replacement — 1 498 | **brak `y₀` → wypada** |
| periacetabular osteotomy | pao — 404, `y₀` 2012 | + pełna nazwa — 700 | **wypada** |
| total elbow arthroplasty | tea — 321, `y₀` 2013 | + pełna nazwa — 605, szczyt 2005 | **wypada** |
| femoral nerve block | fnb — 188, `y₀` 2014 | + pełna nazwa — 411 | **wypada** |
| vertebroplasty | pvp, vertebral augmentation — 886, `y₀` 2005 | + vertebroplasty, percutaneous vertebroplasty — 2 601, szczyt **2009** | **wypada** |
| manipulation under anesthesia | mua — 242 | pełnej nazwy nie da się policzyć¹ | **wypada** (§4a) |
| motor evoked potential | mep — 592 | 642 | zostaje, `y₀` 2013 bez zmian |
| PFNA | pfna — 308 | 345 | zostaje, `y₀` 2011 bez zmian |
| anterolateral ligament reconstruction | anterolateral ligament — 158 | 231 | zostaje, `y₀` 2016; szczyt 2017 → **2025** |

¹ Fraza rzeczownikowa kończy się przed przyimkiem, więc „manipulation under anesthesia” nigdy
nie jest jedną frazą.

**To nie jest wynik** (korekta 2026-10-29, zob. `brief_dla_cowork_korekta_skroty_2026-10-29`).
Skrót i pełna nazwa to ta sama technologia, a §4a od początku kazało liczyć je razem. Pięć grup
wypada, bo przy poprawnym liczeniu nigdy się nie wyłaniały — był to błąd zliczania, a nie zjawisko
w piśmiennictwie. Do Wyników nic; tabela powyżej → suplement jako zapis korekty.

## 2. Liczby — tabela zastępcza

| | materiał 54 | **materiał 48** |
|---|---:|---:|
| grup / terminów | 54 / 89 | **48 / 84** |
| odrębnych technologii | 51 | **45** |
| `y₀` 2000–09 / 2010–19 / 2020–25 | 11 / 36 / 7 | **9 / 32 / 7** |
| szczyt w 2025 | 15 | **14** |
| zakres efektywnych krajów | 1,5 – 12,8 | **1,5 – 12,8** |
| jednokrajowe (eff ≤ 2,5) | 8 (Chiny 4, USA 4) | **7 (Chiny 4, USA 3)** |
| rozproszone (eff ≥ 9) | 10, maks 25% | **10, maks 25% (Latarjet)** |
| najbardziej skoncentrowana | PELD | **PELD** — Chiny 81,4%, eff 1,5, 320 prac |
| prowadzi USA lub Chiny | 49 z 54 | **43 z 48** |
| pięć wyjątków krajowych | — | **bez zmian** |
| czas podwojenia policzalny | 44 | **39** |
| najszybsze podwojenie | AI 2,1; robotyka 2,2; OLIF 2,3; FNS 2,3; hip resurfacing 2,4 | **bez zmian** |
| **zaniki** | 11 | **10** — wypada blokada nerwu udowego |

Trwałość względna (`trwalosc_wzgledna_48.csv`) dla 10 zaników jest identyczna z poprzednią,
łącznie z pasmami i odstępem 0,003 w oknie +1–3. Jedyne ucięte okno to nadal dual mobility
+5–7.

## 3. Klasy

| klasa | n | `y₀` | podwojenie | kraje eff. | rośnie | zaniki |
|---|---:|---:|---:|---:|---:|---:|
| I. implant i materiał | 10 | 2014,5 | **17,8** | **7,7** | 3 | 2 |
| II. endoprotezoplastyka | **5** | **2007** | 11,7 | 5,5 | 1 | 2 |
| III. technika operacyjna | **21** | 2014 | **5,2** | **5,1** | 4 | 2 |
| IV. narzędzie wspomagające | 7 | **2019** | 8,1 | 5,7 | **5 z 7** | 1 |
| V. postępowanie okołozabiegowe | **2** | 2014,5 | 18,4 | 6,7 | 1 | **0** |
| VI. terapia biologiczna | 3 | 2012 | 5,0 | 7,0 | 0 | **3 z 3** |

Zdanie o klasach trzyma się: **implanty wolno i szeroko** (17,8 roku, 7,7 kraju), **techniki
szybko i węziej** (5,2 roku, 5,1 kraju). „Lokalnie” jest teraz za mocne — techniki straciły trzy
grupy (PAO, MUA, wertebroplastykę) i mediana krajów wzrosła z 4,8 do 5,1. Klasa V ma dwie
pozycje: nie pisz o niej osobno.

## 4. Pochodzenie i propagacja — reguła B (Box 1)

| | materiał 54 | **materiał 48** |
|---|---:|---:|
| ten sam kraj zaczął i prowadzi | 29 (USA 26) | **26 (USA 23)** |
| przepływ | 16 | **14** |
| niejednoznaczne | 9 | **8** |
| przepływów kończących się w Chinach | 13 z 16 | **11 z 14** |
| Chiny nadreprezentowane we wszystkich | min 1,45×, med 2,23× | **min 1,45×, med 2,11×** |
| wariant ścisły (zgodne źródło) | 12, w tym 10 do Chin | **10, w tym 8 do Chin** (min 1,63×, med 2,66×) |
| strona USA (ten sam kraj) | med 1,25×, 6 z 26 poniżej tła | **med 1,24×, 6 z 23 poniżej tła** |

Z przepływów wypadają wertebroplastyka i blokada nerwu udowego. **Przy wertebroplastyce
podejrzenie z poprzedniego briefu się potwierdza:** jej „chińskość” (57,9%, nadreprezentacja
4,3×) pochodziła ze skrótu `pvp`. Po dołączeniu pełnej nazwy grupa w ogóle się nie wyłania.

Zdania do tekstu z briefu `regula_przeplywu` zostają, z nowymi liczbami:

> Twenty-six groups were led by the country that started them and 14 by another country; 11 of
> the 14 flows ended in China. Requiring both measures to agree on the source country as well
> leaves 10 flows, 8 of them to China.

**Rycina 2 — nowe słupki:** zaczął (źródło zgodne w obu miarach) USA 29, Chiny 2, Korea 2,
Francja 1, Niemcy 1, Japonia 1; prowadzi USA 30, **Chiny 13**, Korea 2, Francja 1, Niemcy 1,
Japonia 1. Adnotacja: „11 of 14 flows end in China (8 of 10 when both measures must agree on
the source)”.

## 5. Wrażliwość na materiale 48 (zastępuje Z1 i Z4 z `walidacja_RESPONSE`)

| parametr | grup z 48 | mediana \|Δy₀\| | max \|Δy₀\| |
|---|---:|---:|---:|
| *k* = 3 / 4 | 48 / 48 | 0 / 0 | 8 / 5 (komórki macierzyste) |
| *k* = 7 | 45 | 0 | 6 (MEP) |
| *m* = 2 | 48 | 0 | 8 (HXLPE) |
| *m* = 4 | 44 | 0 | 0 |
| *θ* = 0,05% | 48 | 1,0 | 13 (ultrasonografia) |
| *θ* = 0,2% | **27** | 1,0 | 6 (CDA) |

Przy *θ* = 0,2% odpadają grupy o szczycie 0,13–0,31% pola, a zachowane mają co najmniej 0,28%.
Wniosek bez zmian: *k* i *m* nie ruszają listy, a *θ* wyznacza dolną granicę wielkości
literatury.

**D6:** `y₀` bez zmian w **40 z 48** grup. D6 opóźnia wyłonienie przy komórkach macierzystych
(+4), MIPO (+3) i PEEK (+1); mikrozłamania wyłaniają się tylko z D6. Z3 (172 odrzucone) nie
zależy od materiału — bez zmian.

## 6. Pliki

| nowe (obowiązujące) | |
|---|---|
| `data/processed/material_48.csv`, `grupy_48.json` | materiał |
| `data/processed/osie_48.csv` | osie |
| `data/processed/trwalosc_wzgledna_48.csv` | trwałość + status okien |
| `data/processed/kraj_pochodzenia_48.csv` | pochodzenie |
| `data/processed/szeregi_48.csv`, `szeregi_48_prace.csv` | szeregi do rycin (Ryc. 0, 5, 1) |
| `results/wrazliwosc_parametrow_48.csv`, `d6_vs_y0_48.csv`, `wrazliwosc_nowe_frazy_48.csv` | wrażliwość |

`szeregi_czlonow.csv` się nie zmienia (kifoplastyka i oba retronimy nie były dotknięte).
Box 1 wskazuje już pliki `_48`. Pliki `_54` zostają jako historia.

## 7. Do zrobienia w manuskrypcie

1. Podmienić liczby wg §2–§4 (wszędzie, gdzie stoi 54, 51, 49, 11 zaników, 13 z 16).
2. ~~Wyniki, część o języku: akapit o wyłonieniach skrótu~~ — **skreślone** (korekta 2026-10-29).
3. Metody: jedno zdanie — *„Each abbreviation was counted together with its full form; one
   abbreviation whose full form is not a noun phrase was excluded.”* Bez numeru odchylenia:
   to poprawka błędu wykonania, zapisana w rejestrze jako incydent proceduralny.
4. Zdanie o klasach: „techniki szybko i węziej”, bez „lokalnie”.

## 8. Kontrole

| | |
|---|---|
| 45 grup nietkniętych: osie, szeregi, trwałość, kraje | **0 różnic** wobec 54 |
| detektor wrażliwości przy parametrach domyślnych | odtwarza 3 warianty, rdzeń 1 289, `y₀` **48/48** |
| `klasy_60.csv`, manifest | nietknięte, **12/12** |
