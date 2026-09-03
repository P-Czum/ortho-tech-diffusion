# Audyt wszystkich liczb w `results_v2.md`. Dwadzieścia poprawek — i wycofuję własne ACDF

Autor: sesja VS Code, 2026-09-03. Z własnej inicjatywy — nie ma nowego briefu do mnie.

Stałe liczby łapałem dotąd doraźnie (CBCT, 66/61, 19, 13, 76). To ta sama sytuacja co przed
audytem skażenia: seria wykryć ad hoc zamiast testu. Przeszedłem więc **każdą liczbę**
w `results_v2.md` wobec `osie_60.csv`, `grupy_61.json`, `retronimy.csv` i `trwalosc_wzgledna.csv`.

**Dwie wiadomości. Dobra: cały akapit „Why attention fades" jest liczbowo bezbłędny, łącznie
z pasmami trwałości — nie ruszaj go. Zła: pomyliłem się przy ACDF i wprowadziłem Cię w błąd,
przez co w Tabeli 4 stoi czwarty wiersz, który nie powinien istnieć.**

---

## 1. Najpierw moja pomyłka — ACDF nie jest retronimem

W briefie `nazwy_i_kontrole_RESPONSE` §5 napisałem: „**Odpowiedź na §6: ACDF kwalifikuje się** —
CDA obecna od 2009, cztery lata przed `y₀` ACDF. Czwarty wiersz powstaje." **To było błędne.**

Zastosowałem test w brzmieniu „rywal obecny przed `y₀`", a ten test nie odróżnia nazwy **ukutej**
dla kontrastu od nazwy **starej, której uwaga wzrosła późno**. `y₀` ACDF to 2013, ale nazwa
istnieje w polu od początku okna:

```
        2000  2001  2002  2003  2004
ACDF       7     0     8     4     7   prac
CDA        0     0     0     0     2   prac
```

**Dziewiętnaście prac o ACDF ukazało się, zanim powstała pierwsza praca o CDA.** Nazwa wyprzedza
rywala o co najmniej cztery lata i nie została dla niego ukuta — ACDF nazywa się ACDF od dekad.
Detektor wykrył wzrost uwagi, nie narodziny nazwy.

### Test poprawiony: obecność, zanim rywal w ogóle zaistniał

| domniemany retronim | rok 1. pracy rywala | prac retronimu do tego roku |
|---|---:|---:|
| single bundle | 2000 | **0** |
| anatomic total shoulder arthroplasty | 2006 | **0** |
| mechanical alignment | 2009 | 11 (w ciągu 9 lat, ~1,2/rok) |
| **anterior cervical discectomy fusion** | 2004 | **19 (w ciągu 4 lat, ~4,8/rok)** |

Warunek „rywal obecny przed `y₀`" zastępuję **„domniemany retronim praktycznie nieobecny, dopóki
rywal nie zaistnieje"**. Przy tym warunku ACDF odpada jednoznacznie, a pozostała trójka zostaje.
Zastrzeżenie uczciwe: przy `single bundle` okno jest ślepe, bo pierwsza praca rywala wypada
w 2000, czyli na krawędzi okna — rozstrzyga tam nie zero, lecz to, że fraza ma **1 pracę w 2000
i 1 w 2006**, a rusza dopiero razem z rywalem w 2007. `mechanical alignment` jest najsłabszą
z trójki i warto o tym wiedzieć.

**Konsekwencje:** materiał zostaje **60** (ACDF w nim był i pozostaje, `y₀` 2013, 1 672 prace).
Tabela 4 ma **trzy wiersze, nie cztery** — usuń wiersz ACDF.

To zresztą ciekawsze niż czwarty retronim: ACDF rośnie jako **ramię porównawcze w badaniach nad
CDA**. Uwaga napędzana przez rywala bez zmiany nazwy — inne zjawisko niż retronim i osobne zdanie
w Dyskusji, jeśli zechcesz.

## 2. Tabela 4 — brakujące „Rival present from"

| Nazwa ukuta dla istniejącego standardu | Emerged | Rywal | **Rival present from** |
|---|---:|---|---:|
| Single-bundle ACL reconstruction | 2010 | Double-bundle reconstruction | **2007** |
| Anatomic total shoulder arthroplasty | 2015 | Reverse shoulder arthroplasty | **2007** |
| Mechanical alignment | 2018 | Kinematic alignment | **2016** |
| ~~ACDF~~ | | | **wiersz do usunięcia** |

Wszystkie trzy spełniają Twoją definicję z nagłówka tabeli (pierwszy rok z ≥ 5 pracami, wyprzedza
`y₀`).

## 3. Audyt liczb — dwadzieścia pozycji

| # | w `results_v2.md` | poprawnie |
|---:|---|---|
| 1 | nagłówek: „material 66 (61 pending)", „Table 1 (76 rows)" | **60**, Tabela 1 ma **60 wierszy** |
| 2 | „**Sixty-six** technologies" | **Sixty** |
| 3 | „Eleven … **42** … **13** from 2020–2023" | 11 / **40** / **9** |
| 4 | „earliest were hip resurfacing, kyphoplasty, TDR (all 2005)" | pomija **`vertebral augmentation`** (`y₀` 2005) |
| 5 | „robotic assistance (**2020**)" | `y₀` **2019** |
| 6 | „**Nineteen** of the 66 — nearly a third" | **16 z 60** — nadal ponad czwarta część |
| 7 | „ranged from 1.2 to **14.7**" | 1,2 do **12,8** (CBCT usunięte) |
| 8 | „**Thirteen** single-country … China (**seven**) or USA (**six**)" | **11**; Chiny **6**, USA **5** |
| 9 | „**primary hip arthroscopy** (89% USA)" | patrz §4 — liczba nieaktualna po scaleniu |
| 10 | „**Twelve** technologies … nine or more … **no country above 24%**" | **10**; maksimum **25%** (Latarjet) |
| 11 | „cone-beam CT (14.7 countries)" | **usunięte z materiału** (82,5% stomatologii) |
| 12 | „**medial** unicompartmental knee arthroplasty (**9.5**)" | grupa to `unicompartmental knee arthroplasty`, eff **9,0** |
| 13 | „percutaneous kyphoplasty and cone-beam CT had 545 and **553** papers" | CBCT usunięte — potrzebna nowa para |
| 14 | „Doubling … for **55** technologies" | **49** |
| 15 | „the fastest were **primary hip arthroscopy (1.7)**, robotic (**2.0**), AI (2.1), OLIF (**2.2**), FNS (2.3), hip resurfacing (2.4)" | AI **2,1**, robotic **2,2**, OLIF **2,3**, FNS **2,3**, hip resurfacing **2,4**, FNB **2,6** — hip arthroscopy ma **7,0** i wypada z listy |
| 16 | Tabela 2: wiersze `primary hip arthroscopy`, `mechanical alignment`, `cone-beam CT` | dwa ostatnie **usunięte z materiału**; pierwszy z błędnymi liczbami |
| 17 | „**61 of the 66**" | **55 z 60** |
| 18 | „**Eleven of 24** … were changes of name" | **10 z 22**, rozkład 5 + 5 — brief z 12:30 |
| 19 | notatka: „**Fourteen** single-country literatures" | **11** — i sprzeczna z „Thirteen" w tekście głównym |
| 20 | notatka: „not computable for **15**" | **11** — i sprzeczna z „11" w tekście głównym |

### Co jest poprawne i czego nie ruszaj

| twierdzenie | stan |
|---|---|
| `y₀` wszystkich 24 technologii wymienionych z nazwy w akapicie 2 | **wszystkie zgodne** poza robotic (2019) |
| PKP 545 prac / 90% Chiny; PELD 81%; FNS 70%; PFNA 69%; OLIF 65% | **zgodne** |
| TMR 68% USA; manipulation under anaesthesia 67%; EMR 66% | **zgodne** |
| sześć technologii z podwojeniem > 20 lat (TDR, PEEK, short stem, CDA, total elbow, cephalomedullary) | **komplet zgodny** |
| pięć wyjątków narodowych (Francja 32%, Niemcy, Japonia, Korea ×2) | **zgodne** |
| „dwanaście technologii straciło ponad połowę" | **zgodne** |
| pasma trwałości 0,27–0,48 / 0,17–0,25 / 0,11–0,17 wobec 0,50–0,87 / 0,35–0,73 / 0,26–0,72 | **wszystkie sześć zgodne co do setnej** |
| computer navigation 0,66 w +3–5; MSC 0,73 | **zgodne** |
| szczyty: computer navigation 2007, dual mobility 2020 | **zgodne** |

**Cały rozdział „Why attention fades" przeszedł audyt bez jednej poprawki** poza zdaniem
o „11 z 24" na końcu. Dwanaście zaników to te same dwanaście pozycji w materiale 60 co w 66,
więc `trwalosc_wzgledna.csv` nie wymaga przeliczenia.

## 4. `primary hip arthroscopy` — scalenie zmieniło liczby drastycznie i występuje w trzech miejscach

To najgroźniejsza pozycja audytu, bo nie jest zwykłą literówką: fraza **została scalona**
do grupy `hip arthroscopy` i wszystkie jej liczby się zmieniły.

| | tekst (przed scaleniem) | materiał 60 (po) |
|---|---:|---:|
| prace | 222 | **1 318** |
| USA | 89% | **63,3%** |
| efektywnych krajów | 1,3 | **2,4** |
| czas podwojenia | 1,7 roku | **7,0 lat** |

Grupa nadal mieści się w progu jednokrajowości (2,4 ≤ 2,5), więc **zostaje na liście
jednokrajowych** — ale z udziałem 63%, nie 89%. Za to **wypada z listy najszybszych**, bo 7,0
zamiast 1,7. Fraza występuje w `results_v2.md` trzy razy i za każdym razem niesie stare liczby.

Najszybszą technologią jest teraz **sztuczna inteligencja (2,1 roku)**.

## 5. Czego nie zrobiłem

Nie ruszałem tekstu manuskryptu — to Twoja część i nie wiem, które zdania przetrwają wybór
wariantu (a)/(b) z poprzedniego briefu. Nie przeliczałem `trwalosc_wzgledna.csv`, bo zbiór
dwunastu zaników jest identyczny.

Nie audytowałem `results_v1.md`, `skeleton_v1.md` ani `methods_v1.md` — powiedz, czy v1 są żywe,
czy zastąpione. Jeśli żywe, zrobię to samo; jeśli nie, nie ma po co.

## 6. Kontrole

| | |
|---|---|
| materiał | **60**, nietknięty |
| osie | nietknięte |
| manuskrypt | **nietknięty** |
| manifest | **12/12** |
