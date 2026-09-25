# Materiał 54 — FEA i Mimics wypadają jako metoda badawcza. Decyzja ortopedy z 2026-09-25

Autor: sesja VS Code, 2026-09-25.

Wyniki: `material_54.csv` (89 terminów), `grupy_54.json`, `osie_54.csv`,
`trwalosc_wzgledna_54.csv`.

**Kontrola rozstrzygająca: osie 54 grup wspólnych różnią się od `osie_56.csv` o 0,0000.**
Usunięcie dwóch pozycji nie poruszyło żadnej innej — tak jak przy poprzednich zawężeniach.

---

## 1. Czym rozstrzygnięto, bo nie udziałem 19,1%

Zmierzyłem, z czym FEA współwystępuje w polu. 1 504 prace, krotności ponad przypadek:

| partner | krotność | wspólnych |
|---|---:|---:|
| femoral neck system | **25,4×** | 22 |
| proximal femoral nail antirotation | **16,4×** | 28 |
| mimic software | 13,1× | 12 |
| polyetheretherketone | 12,2× | 22 |
| oblique lumbar interbody fusion | 9,4× | 21 |
| locking plate | 5,4× | 47 |

**Wszystkie czołowe partnerki to implanty z naszego własnego materiału.** FEA nie dyfunduje obok
nich — jest przyrządem, którym się je bada. Z jakąkolwiek inną pozycją materiału współwystępuje
22,8% jej prac.

## 2. Podstawa wykluczenia jest w kodeksie, nie w ocenie

Metody wymieniają wprost: *excluded if it named **a research method**, outcome measure, score,
disease entity, complication, patient characteristic, or aspect of care organisation.*

FEA jest **jednocześnie technologią i metodą badawczą**. Wcześniejsze rozstrzygnięcie ortopedy
(„badamy technologię w ortopedii — finit spełnia ten warunek") było trafne co do pierwszego
warunku; klauzula wykluczająca jest drugą, niezależną przesłanką i działa mimo spełnienia
pierwszej. To nie jest odwrócenie decyzji, tylko jej uzupełnienie o przesłankę, której wtedy
nie rozważano.

**Precedens zapadł wcześniej:** `electronic medical record` wypadło w kroku 60→56 na mocy
siostrzanej klauzuli z tego samego zdania („aspect of care organisation").

**Mimics wypada tą samą regułą.** To oprogramowanie do segmentacji — dokładnie narzędzie, którym
buduje się model do FEA, współwystępowanie 13,1×. Zostawienie go przy usunięciu FEA byłoby
doraźne. Niezależnie był słabą pozycją: 77 prac, 84,9% Chiny, 11,5% skażenia stomatologicznego,
czasu podwojenia nie dało się policzyć.

Granica przebiega przy **zastosowaniu u chorego**. Po usunięciu obu klasa IV jest wewnętrznie
czysta — wszystkie siedem pozostałych pozycji to rzeczy stosowane w opiece: nawigacja, PSI,
druk 3D, robotyka, AI, rzeczywistość rozszerzona, ultrasonografia.

**Pozycja graniczna, którą zostawiamy: `artificial intelligence / machine learning`.** Bywa
metodą badawczą, ale jest wdrażana w diagnostyce i chirurg ją ocenia. Wymaga jednego zdania
w Metodach o tym, gdzie biegnie granica.

## 3. Liczby materiału 54

| | materiał 56 | **materiał 54** |
|---|---:|---:|
| grup | 56 | **54** |
| terminów | 92 | **89** |
| odrębnych technologii | 53 | **51** |
| `y₀` 2000–09 / 2010–19 / 2020–25 | 11 / 36 / 9 | **11 / 36 / 7** |
| szczyt w 2025 | 15 | **15** |
| zakres efektywnych krajów | 1,4 – 12,8 | **1,5 – 12,8** |
| jednokrajowe (eff ≤ 2,5) | 9 (Chiny 5, USA 4) | **8 (Chiny 4, USA 4)** |
| rozproszone (eff ≥ 9) | 10 | **10**, maks udział 25% |
| prowadzi USA lub Chiny | 51 z 56 | **49 z 54** |
| czas podwojenia policzalny | 45 | **44** |
| **zaniki** | 11 | **11 — bez zmian** |
| braki kraju | mediana 9,4%, maks 19,4% | **bez zmian** |

**Najbardziej skoncentrowaną pozycją jest teraz `percutaneous endoscopic lumbar discectomy`** —
Chiny 81,4%, eff 1,5, 320 prac. Flagowy przykład literatury jednokrajowej przestaje konkurować
z nazwą produktu. Lista jednokrajowych jest też symetryczna: cztery chińskie, cztery
amerykańskie.

Najszybsze podwojenie bez zmian: AI 2,1 roku, robotyka 2,2, OLIF 2,3, femoral neck system 2,3,
hip resurfacing 2,4.

## 4. Tabela klas

| klasa | n | `y₀` mediana | podwojenie | kraje eff. | szczyt 2025 | zaniki |
|---|---:|---:|---:|---:|---:|---:|
| I. implant i materiał | 10 | 2014,5 | **18,4** | **7,7** | 3 | 2 |
| II. endoprotezoplastyka | 7 | **2007** | 11,7 | 5,5 | 2 | 2 |
| III. technika operacyjna | 23 | 2014 | **5,2** | **4,6** | 4 | 2 |
| IV. narzędzie wspomagające | **7** | **2019** | **8,1** | 5,7 | **5 z 7** | 1 |
| V. postępowanie okołozabiegowe | 3 | 2014 | 17,2 | 5,3 | 1 | 1 |
| VI. terapia biologiczna | 3 | 2012 | 5,0 | 7,0 | **0** | **3 z 3** |

**Koszt, który zgłaszam uczciwie:** mediana podwojenia w klasie IV rośnie z 6,2 do **8,1 roku**,
bo wypadło szybkie FEA (4,3). Kontrast „narzędzia dyfundują szybciej niż implanty" słabnie —
nadal trzyma się wobec klasy I (18,4), ale nie wobec klasy III (5,2). **Nie pisz już, że narzędzia
są najszybsze.** Prawdziwe zdanie: narzędzia są **najmłodsze** (mediana `y₀` 2019) i **pięć z
siedmiu wciąż rośnie** — to jest ich cecha, nie tempo.

Pozostałe trzy kontrasty bez zmian: implanty 18,4 roku przy 7,7 kraju, techniki 5,2 przy 4,6,
terapie biologiczne to trzy zaniki na trzy pozycje.

**Nadal bez klasy: `anterolateral ligament reconstruction`.** Jedyna pozycja poza statystyką
klasową; z nazwy należy do III, ale nie przypisuję sam.

## 5. Co to zmienia w tekście

Wszystkie liczby z briefu z 09-07 pozostają w mocy **poza** tymi w tabeli w §3. Rozdział
„Why attention fades" bez zmian — zaniki to te same jedenaście pozycji, pasma trwałości
nietknięte, zastrzeżenie o odstępie trzech tysięcznych w oknie +1–3 nadal obowiązuje.

Zdanie o klasie IV wymaga przepisania z tempa na wiek (patrz §4).

## 6. Kontrole

| | |
|---|---|
| osie grup wspólnych wobec `osie_56` | **różnica 0,0000** |
| zaniki | **11**, ten sam zbiór |
| klasy | zamrożone `0dec1fc`, nietknięte |
| manuskrypt | **nietknięty** |
| manifest | **12/12** |
