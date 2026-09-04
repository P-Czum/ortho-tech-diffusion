# Materiał 56. Kifoplastyka nie zanika — zaników jest 11. **Ale znalazłem błąd w tabeli trwałości i muszę wycofać własny audyt sprzed trzech godzin**

Autor: sesja VS Code, 2026-09-03. Dotyczy: `brief_dla_vsc_material_scalenie_i_klasy_2026-09-03.md`.

Wyniki: `material_56.csv`, `grupy_56.json`, `osie_56.csv`, `trwalosc_wzgledna_56.csv`,
`klasy_60.csv` (+ `.meta.json`). Nowe skrypty: `code/trwalosc_wzgledna.py`,
`code/kontrast_leki.py`.

**Kolejność z §4 dotrzymana:** klasy zamrożone osobnym commitem `0dec1fc`, sha256
`3c08fafb…`, **przed** jakąkolwiek operacją na materiale. W historii git jest to bezsporne —
w tamtym commicie nie ma żadnego innego pliku.

---

## 1. Najpierw to, co muszę odwołać

W audycie z 13:42 napisałem: *„Dwanaście zaników to te same dwanaście pozycji w materiale 60
co w 66, więc `trwalosc_wzgledna.csv` nie wymaga przeliczenia"* i *„wszystkie sześć pasm zgodne
co do setnej — nie ruszaj tego akapitu"*.

**Sprawdziłem tożsamość grup, ale nie sposób liczenia. To był błąd.** Po przeliczeniu:

| grupa | członów | stare `+1..3` | nowe `+1..3` |
|---|---:|---:|---:|
| mom total hip arthroplasty | 1 | 0,2654 | 0,2654 |
| double bundle reconstruction | 1 | 0,7353 | 0,7353 |
| femoral nerve block | 1 | 0,5474 | 0,5474 |
| dual mobility cup | 1 | 0,5854 | 0,5854 |
| ponseti method | 1 | 0,5002 | 0,5002 |
| microfracture | 1 | 0,7632 | 0,7632 |
| mesenchymal stem cell | 1 | 0,6891 | 0,6891 |
| **hip resurfacing** | **2** | 0,4768 | **0,4973** |
| **total disc replacement** | **2** | 0,6858 | **0,7317** |
| **computer navigation** | **2** | 0,7653 | **0,7539** |
| **autologous chondrocyte implantation** | **2** | 0,6287 | **0,8593** |

**Każda grupa jednoczłonowa zgadza się co do czwartego miejsca po przecinku. Każda dwuczłonowa
się różni.** Stary plik sumował szeregi członów zamiast liczyć unię dokumentów — dokładnie ten
sam błąd, który rano znalazłem w liście zaników (22 → 12). Nowy plik liczy unijnie, zgodnie
z `merge_and_axes.py`.

## 2. Konsekwencja: separacja w pierwszym oknie jest teraz na włosku

| okno | **odrzucone** (2) | **nieodrzucone** (9) | odstęp |
|---|---|---|---:|
| +1..3 lata | 0,27–**0,50** | **0,50**–0,86 | **+0,0029** |
| +3..5 lat | 0,17–0,26 | 0,35–0,79 | +0,088 |
| +5..7 lat | 0,11–0,17 | 0,26–0,72 | +0,085 |

`hip resurfacing` ma **0,4973**, `ponseti method` **0,5002**. Twierdzenie „odrzucone spadają
głębiej w każdym oknie" **formalnie się utrzymuje**, ale w pierwszym oknie odstęp wynosi trzy
tysięczne. W poprzedniej wersji było 0,023 — dziesięć razy więcej.

**Do Wyników w tej postaci: rozdzielenie jest czyste w oknach +3..5 i +5..7, a w +1..3 graniczne.**
Napisanie „w każdym oknie" bez tego zastrzeżenia byłoby nieuczciwe wobec liczby, którą recenzent
odczyta z tabeli sam.

### Dodatkowo: szczyt ACI jest remisem i chwieje wynikiem

Unia grupy ma 0,2746% w 2010 (27 prac) i 0,2554% w 2013 (**31 prac**) — różnica 7% względnych,
a liczba prac jest większa w 2013. `argmax` wybiera 2010. Gdyby szczytem było 2013, ACI ma
0,738 / 0,624 / 0,556 zamiast 0,859 / 0,786 / 0,689.

Nie zmieniam reguły — podaję, że górna granica pasma nieodrzuconych (0,79 w oknie +3..5)
wisi na siedmioprocentowej różnicy między dwoma latami jednej grupy. W tekście lepiej podać
pasmo bez ostatniej cyfry znaczącej.

## 3. §1 — kifoplastyka po scaleniu: Twoja przepowiednia trafna, poza krajem

| | wartość |
|---|---|
| `y₀` / szczyt | 2005 / 2011 |
| prace od `y₀` | **1 666** |
| **trwałość 2025/szczyt** | **0,81 → NIE zanika** |
| kraj czołowy | **Chiny 41,6%** (tło 13,6%, nadreprezentacja 3,07×) |
| efektywnych krajów | **4,5** |

**Zaników jest 11**, jak przewidywałeś, i pasmo „dowody za, rutyna" traci kifoplastykę —
zostają w nim `ponseti method` i `dual mobility cup`.

**Ale kraj czołowy NIE przestaje być chiński** — wbrew Twojemu „prawie na pewno". Chiny mają
41,6% scalonej grupy, bo 573 prace o `percutaneous kyphoplasty` (90,5% chińskie) przeważają nad
1 263 pracami o `kyphoplasty` (USA 25,1%) mocniej, niż wynikałoby z samych liczebności. Grupa
przestaje natomiast być literaturą jednokrajową: efektywnych krajów **4,5**, daleko powyżej
progu 2,5.

### Następca flagowego przykładu literatury jednokrajowej

Rekomenduję **`percutaneous endoscopic lumbar discectomy`: Chiny 81,4%, efektywnych krajów 1,5,
320 prac.** Odrzucam `mimic software` mimo wyższego udziału (84,9%): ma tylko **77 prac**, jest
nazwą produktu i ma najwyższe skażenie stomatologiczne w materiale (11,5%). PELD jest czystą
techniką operacyjną z czterokrotnie większą liczebnością.

## 4. §2 — pomiary

**`anterolateral ligament reconstruction` istnieje** — 96 prac, plus `allr` 48. Warunek
spełniony, **pozycja zostaje**, grupa przemianowana. Przemianowałem **samą nazwę grupy, bez
dodawania członów**, bo brief rozróżnia „scal" (§1) od „przemianuj" (§2), a przy wertebroplastyce
przemianowanie jawnie zachowuje człony. Dołączenie `anterolateral ligament reconstruction`
i `allr` jako członów byłoby scaleniem i zmieniłoby szereg — powiedz, jeśli o to Ci chodziło.

**`finite element analysis`: 2 662 prace, 19,1% ma jakąkolwiek przesłankę modelu konkretnego
chorego.**

| przesłanka | prac | udział |
|---|---:|---:|
| fraza od „patient specific" / „subject specific" / „personalized" | 146 | **5,5%** |
| tomografia jako źródło geometrii | 399 | **15,0%** |
| którakolwiek | 508 | **19,1%** |

Pierwszy przebieg dał mi 9,1% i **zaniżał** — chunker produkuje złożenia (`patient specific
factor`, `patient specific implant`), a nie samo `patient specific`; powtórzyłem z dopasowaniem
po prefiksie. Wynik: **około 81% to warsztat generyczny.** Pomiar nie potwierdza dwóch
równorzędnych desygnatów — potwierdza metodę badawczą z marginesem planowania. Decyzja Wasza;
do jej podjęcia FEA zostaje i jest wliczone w liczby poniżej.

## 5. Materiał 56 — komplet liczb

| | |
|---|---|
| pozycji (grup) | **56** |
| terminów | 92 |
| **odrębnych technologii** (po odjęciu 3 gatunków) | **53** |
| `y₀` po dekadach | 2000–09: **11**, 2010–19: **36**, 2020–25: **9** |
| szczyt w 2025 (nadal rosną) | **15** |
| zakres efektywnych krajów | **1,4 – 12,8** |
| jednokrajowe (eff ≤ 2,5) | **9** — Chiny 5, USA 4 |
| rozproszone (eff ≥ 9) | **10**, żaden kraj powyżej **25%** |
| prowadzi USA lub Chiny | **51 z 56** |
| czas podwojenia policzalny | **45**, brak 11 |
| **zaniki** | **11** |
| mediana braków kraju | 9,4% (maks 19,4%) |

Najszybsze podwojenie: **AI/uczenie maszynowe 2,1 roku**, robotyka 2,2, OLIF 2,3, femoral neck
system 2,3, hip resurfacing 2,4.

## 6. §4 — tabela per klasa. Podział przeżył operacje

| klasa | n | `y₀` mediana | podwojenie mediana | kraje eff. mediana | szczyt 2025 | zaniki |
|---|---:|---:|---:|---:|---:|---:|
| I. implant i materiał | 10 | 2014,5 | **18,4** | **7,7** | 3 | 2 |
| II. endoprotezoplastyka | 7 | **2007** | 11,7 | 5,5 | 2 | 2 |
| III. technika operacyjna | 23 | 2014 | **5,2** | **4,6** | 4 | 2 |
| IV. narzędzie wspomagające | 9 | **2019** | 6,2 | 4,9 | **5 z 9** | 1 |
| V. postępowanie okołozabiegowe | 3 | 2014 | 17,2 | 5,3 | 1 | 1 |
| VI. terapia biologiczna | 3 | 2012 | 5,0 | 7,0 | **0** | **3 z 3** |

**Wszystkie cztery kontrasty, które podałeś z materiału 60, odtwarzają się na 56**: implanty
podwajają się w 18 latach przy 7,7 kraju, techniki w 5 latach przy 4,6; narzędzia mają medianę
`y₀` 2019 i pięć z dziewięciu wciąż rośnie; terapie biologiczne to trzy zaniki na trzy pozycje.
Klasy V i VI opisowo, jak prosiłeś.

**Jedna pozycja bez klasy:** `anterolateral ligament reconstruction`. Przeżyła warunek z §2, ale
w liście z §4 jej nie ma. **Nie przypisałem klasy sam** — to złamałoby sens zamrożenia. Jest poza
statystyką klasową do Twojej decyzji; z nazwy należy do III.

## 7. §5 — pozostałe punkty

**D5b.** Brama: rekord, którego wszystkie deskryptory pola należą do `{Osteogenesis, Distraction
(D019857), Bone Transplantation (D016025)}`, przy jednoczesnym deskryptorze z A14 lub C07.
Wyłapuje **6 286 rekordów**. **Nie jest stosowana**, bo wdrożenie wymaga dowodu separacji jak
przy D4 (obca ≥ 90%, ortopedyczna ≤ 5%), a tego nie zmierzono. Zdanie do Metod: reguła
zaproponowana i zmierzona, niewdrożona z braku dowodu separacji; jej rekordy **nie wchodzą**
do 26 335 wyłączeń. Mogę domierzyć separację — powiedz.

**Wariant „tylko tytuł".** Na nowej jednostce zachowuje się tak samo jak na starej:

| | słownik fraz | wyłonień |
|---|---:|---:|
| primary | 25 071 | 1 461 |
| **S1 tytuł** | **1 892** | **128** |
| S2 abstrakt | 24 940 | 1 465 |
| S3 angielski | 23 267 | 1 550 |

Rdzeń trzech wariantów **1 289**; z S1 zostałoby **83** — S1 usuwa **93,6%** rdzenia i wyciąłby
**36 z 56** grup materiału. Na n-gramach było 94,2%. **D-2 nie był artefaktem starej jednostki**
i to warto napisać, bo wzmacnia uzasadnienie.

**Druga definicja pola.** Wyceniona dokładnie: def2 dla 2000–2025 to **316 091 rekordów**,
z czego 281 261 ma już pobrany tekst (2005–2025), a **34 830 wymaga dociągnięcia** za 2000–2004.
Nakładanie się z def1: 45,8%. Reszta to ekstrakcja fraz rzędu wielkości def1. Przypominam
z briefu z 13:06, że rejestracja §114 zobowiązuje do `y₀` w obu definicjach niezależnie od
losu def2 jako „wrażliwości" — to nie to samo pytanie.

**MTIX i leki** — zrobione przed Twoim briefem, szczegóły w `brief_dla_cowork_mtix_i_leki_
przeliczone_2026-09-03.md`. Skrót: ρ = 0,14 przy **n = 88** (było 43), p = 0,18; dwa `y₀` leków
poprawione.

**Retronimy** — Twoja zmiana zdania w Metodach jest słuszna i niezależnie od niej **wycofałem
ACDF z Tabeli 4** (brief z 13:42): 19 prac o ACDF przed pierwszą pracą o CDA, więc nazwa nie
została ukuta jako kontrast. Tabela ma trzy wiersze.

## 8. Kontrole

| | |
|---|---|
| klasy zamrożone przed operacjami | **tak**, commit `0dec1fc`, sha256 `3c08fafb…` |
| materiał | **56** grup, 92 terminy, 53 odrębne technologie |
| zaniki | **11** |
| manuskrypt | **nietknięty** |
| manifest | **12/12** |
