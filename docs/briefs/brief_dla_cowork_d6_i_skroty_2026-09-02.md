# D6: weterynaria to 3,95% pola, największa z reguł. Plus czwarty raz ten sam błąd ze skrótem

Autor: sesja VS Code, 2026-09-02.

Dwie rzeczy, o których nie wiecie, obie znalezione ubocznie. Trzecia — cichy błąd w moim
własnym skrypcie, który podałby złe liczby bez żadnego objawu.

---

## 1. D6 — piśmiennictwo weterynaryjne w polu

**Jak się znalazło.** Przemek zapytał, czy poza `finite element analysis` są w materiale inne
narzędzia badawcze. Policzyłem udział prac stanowiskowych (kadawer, in vitro, biomechanika,
model zwierzęcy) i w tym samym zestawieniu **`tibial plateau leveling osteotomy` wyszło
z 66% prac o psach**. TPLO to standardowy zabieg na zerwane więzadło krzyżowe **u psów**;
u ludzi się go nie wykonuje. Siedziało w materiale.

**Reguła.** Znaczniki kontrolne MeSH, autorytatywne i proste:

```
Animals (D000818) w mesh_ui  AND  Humans (D006801) NIE w mesh_ui   ->  wyłącz
```

**Skala: 11 749 rekordów, 3,95% pola. To więcej niż D4 (2,62%) i więcej niż D5a (2,15%).**
Nakładanie się z pozostałymi minimalne: D4 16, D5a 144, D5c 13.

**Walidacja** tym samym sposobem co D4 i D5c:

| strona | termin | prac | w podzbiorze |
|---|---|---:|---:|
| obca | cranial cruciate ligament | 105 | **97,1%** |
| obca | tplo | 295 | **94,9%** |
| obca | tibial tuberosity advancement | 74 | 94,6% |
| obca | tibial plateau leveling osteotomy | 218 | 94,0% |
| ortopedyczna | reverse shoulder arthroplasty | 1 090 | 0,0% |
| ortopedyczna | total knee arthroplasty | 20 933 | 0,2% |
| ortopedyczna | finite element analysis | 1 496 | 2,7% |
| ortopedyczna | anterior cruciate ligament reconstruction | 8 364 | 4,1% |
| ortopedyczna | locking plate | 1 119 | 5,1% |
| ortopedyczna | polyetheretherketone | 363 | 10,2% |
| ortopedyczna | spinal fusion | 2 378 | 10,8% |

Trzy przekroczenia po stronie ortopedycznej **nie są błędami reguły** — to prawdziwy udział
badań zwierzęcych w tych tematach (modele zrostu u szczurów, klatki PEEK u owiec). Reguła nie
usuwa terminu, tylko jego zwierzęcy ułamek. D4 i D5b testowaliśmy progiem 5%, bo mogły chybiać;
**D6 używa własnych znaczników NLM, więc nie chybia — mierzy dokładnie to, co deklaruje.**

**Skutek uboczny, który rozstrzygnął osobne pytanie:** `micro computed tomography` ma **61,4%**
prac zwierzęcych i wypada pod D6. Nie było więc pozycją do decyzji o zakresie „czy praca obejmuje
warsztat badawczy" — było rekordami spoza medycyny człowieka.

## 2. Skróty wieloznaczne — czwarty raz ten sam błąd

Po `ml` = mililitry z Etapu 1 mamy trzy kolejne. Wszystkie były w materiale albo tuż obok:

| skrót | prac | co znaczy naprawdę |
|---|---:|---|
| `ha` | 960 | hydroksyapatyt 17,7%, kwas hialuronowy 14,3%, **`hip arthroplasty` 28,6%**, reszta nieustalona |
| `cr` | 526 | cruciate retaining **21,9%**, reszta nieustalona (tytuły o zużyciu polietylenu, radioterapii naczyniaka) |
| `ka` | 295 | kinematic alignment **31,5%** |
| `ai` | 326 | artificial intelligence **41,1%**, `acetabular index` 27,3% |
| `let` | 139 | lateral extra-articular tenodesis **93,5%** — **zostaje** |

**Przemek zadał trafne pytanie: skoro umiem sprawdzić, które prace są prawdziwe, czemu wyrzucam
całość?** Odpowiedź wyszła z pomiaru i jest lepsza niż moje pierwotne uzasadnienie.

Grupa liczy dokumenty zawierające **dowolny** człon, więc praca pisząca i „AI", i „artificial
intelligence" jest już policzona przez pełną postać. Skrót wnosi **wyłącznie prace używające
tylko skrótu**:

| skrót | ma też pełną postać | **tylko skrót** |
|---|---:|---:|
| `ai` | 32,8% | **67,2%** |
| `ka` | 23,4% | **76,6%** |
| `ha` | 17,8% | **82,2%** |
| `cr` | 7,4% | **92,6%** |

Czyli część weryfikowalna jest już w grupie, a skrót dokłada dokładnie tę, której zweryfikować
się nie da. **Nie wyrzucamy informacji odzyskiwalnej — wyrzucamy nieodzyskiwalną.**

**Skutek dla liczb, które Wam podałem:** grupa AI/ML była zawyżona. `ai` wnosił 326 prac,
z czego blisko dwie trzecie nie dotyczy sztucznej inteligencji.

**Propozycja reguły do kodeksu**, bo wzorzec jest już czterokrotny: *skrót dwu- i trzyliterowy
nie wchodzi do materiału bez sprawdzenia rozwinięć na tytułach i streszczeniach.* Kanonikalizacja
rozwija skróty ze słownika, ale nie ma jak rozpoznać, że ten sam ciąg znaczy gdzie indziej co
innego. W rdzeniu jest **163 takich skrótów**, z czego 21 w materiale.

## 3. Ograniczenie detektora, nazwane przy okazji rozszerzenia zakresu

Przemek rozstrzygnął, że **biotechnologia wchodzi w zakres** (komórki mezenchymalne to
technologia). Sprawdziłem, co to wpuszcza: **nic nowego** — w rdzeniu są tylko
`mesenchymal stem cell` i `autologous chondrocyte implantation`, oba już w materiale.

Ale sprawdzenie odsłoniło, **dlaczego** PRP i BMP są poza:

```
platelet rich plasma        baza 2000-02 0,151%  prog 0,756%  szczyt 0,386% (2024)
bone morphogenetic protein  baza 2000-02 0,263%  prog 1,317%  szczyt 0,427% (2010) -> 0,09% (2025)
```

**PRP nigdy nie osiągnęło pięciokrotności własnej bazy** — wzrosło dwukrotnie w dwadzieścia lat
i weszło na plateau. To nie jest przeoczenie detektora, tylko własność reguły: **detektor
wykrywa starty, nie wzrost stopniowy.**

**BMP ma pełną krzywą wycofania** (0,43% w 2010 → 0,09% w 2025, spadek o 79%, zgodnie
z kontrowersjami wokół INFUSE po 2011), ale nie wyłania się, **bo rosło przed 2000 rokiem**.

To jest ten sam mechanizm co przy `hip resurfacing`, przesunięty o jedno okno. **Cofnięcie
do 2000 odsłoniło resurfacing i zasłania BMP.** Zdanie do metod, mocniejsze niż samo
„okno zaczyna się w 2000": *przesuwanie okna przesuwa martwe pole, nie usuwa go.*

## 4. Cichy błąd w moim skrypcie — do wiadomości, bo klasa jest groźna

`merge_and_axes.py` brał zakres lat i bazę ze stałych `detect_emergence` (2005–2025, baza
2005–2007), a dane są na oknie 2000–2025. **Nie wywaliłby się — policzyłby.** Lata rozjechane
o pięć pozycji, `y₀` na niewłaściwej bazie, tabela wyglądająca normalnie.

Wyłapałem go przypadkiem, bo pierwsze wywołanie wywróciło się na argumencie, którego ten skrypt
nie ma. Gdybym nie pomylił argumentów, podałbym Wam złe liczby.

Zakres i baza są teraz jawnymi parametrami we wszystkich pięciu skryptach pipeline'u, a
`merge_and_axes` wypisuje je na starcie. **Wnioskiem ogólnym jest, że stała importowana między
modułami jest w tym pipelinie niebezpieczna** — okno przestało być stałe, gdy dołożyliśmy drugie.

## 5. Materiał

| etap | pozycji |
|---|---:|
| kandydaci z obu ocen ortopedy, na rdzeniu po D6 | 132 |
| po wyłączeniach (zbyt ogólne, wieloznaczne skróty, powikłania, warsztat) | 110 terminów |
| po słowniku synonimów | 82 |
| **po scaleniu wariantów** | **75 grup** |

Osie siły liczą się teraz na tym zestawie, na oknie 2000–2025 i polu po D4+D5a+D5c+D6.

## 6. Stan

Manifest **12/12**.
