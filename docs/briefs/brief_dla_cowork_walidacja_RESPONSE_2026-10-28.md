# Walidacja po recenzji — Z1–Z5, szeregi do rycin, Box 1. Plus jedna wada materiału (§6)

Autor: sesja VS Code, 2026-10-28. Odpowiedź na `walidacja_po_recenzji` i `szeregi_do_rycin`.

**Najważniejsze najpierw:** testy wrażliwości pokazują, że lista jest stabilna wobec *k* i *m*,
a zależy od *θ*. Przy okazji Z3 wyszła jednak rzecz poważniejsza niż którykolwiek parametr:
**w dziewięciu grupach etykieta jest pełną nazwą, a szereg liczy tylko skrót.** Po dołączeniu
pełnej nazwy **cztery grupy przestają się wyłaniać, a jednej `y₀` przesuwa się o 12 lat** (§6).
Zgłaszam, nie poprawiam — materiał 54 jest nietknięty, decyzja należy do Przemka.

**Kontrola, bez której nic poniżej nie ma wartości:** jedna funkcja detektora z parametrami
w argumentach (`code/wrazliwosc.py`) przy wartościach domyślnych odtwarza **dokładnie** wyłonienia
wszystkich trzech wariantów tekstu (1 461 / 1 465 / 1 550), rdzeń (1 289) oraz `y₀` i rok szczytu
**54 z 54** grup z `osie_54.csv`. Skrypt kończy się błędem, jeśli którakolwiek z tych zgodności
pęknie.

---

## Z1. Macierz wrażliwości — `results/wrazliwosc_parametrow.csv`

Jeden parametr na raz, reszta domyślna. Przy *m* ≠ 3 granica `y₀` = 2025 − (*m* − 1), tak jak
w Box 1.

| parametr | grup z 54 | mediana \|Δy₀\| | max \|Δy₀\| | nowe frazy w rdzeniu | w tym tech./technika wg istniejącej kategorii |
|---|---:|---:|---:|---:|---:|
| *k* = 3 | 54 | 0 | 8 (komórki macierzyste) | +555 | 8 |
| *k* = 4 | 54 | 0 | 5 (komórki macierzyste) | +213 | 8 |
| ***k* = 5** | **54** | — | — | — | — |
| *k* = 7 | **51** | 0 | 6 (MEP) | 0 (−256) | — |
| *m* = 2 | 54 | 0 | 8 (HXLPE) | +504 | 4 |
| *m* = 4 | **50** | 0 | 8 (PFNA) | 0 (−235) | — |
| *θ* = 0,05% | 54 | 0,5 | 13 (ultrasonografia) | +1 510 | 6 |
| *θ* = 0,2% | **30** | 1,0 | 9 (PAO) | 0 (−703) | — |

Wypadają: przy *k* = 7 — UKA, mikrozłamania, komórki macierzyste; przy *m* = 4 — MoM THA, MPFL,
ultrasonografia, komórki macierzyste; przy *θ* = 0,2% — 24 grupy.

**Sześć zdań:**

1. Przy zmianie mnożnika *k* (3–7) i liczby lat potwierdzenia *m* (2–4) wyłania się nadal
   50–54 z 54 grup, a mediana przesunięcia `y₀` wynosi 0 lat w każdym wariancie.
2. Duże przesunięcia dotyczą pojedynczych grup o długim, płaskim narastaniu: komórki macierzyste
   przekraczają trzykrotność poziomu bazowego osiem lat przed pięciokrotnością.
3. **Parametrem wiążącym jest próg bezwzględny *θ*:** przy 0,2% zostaje 30 z 54 grup. Odpadające
   mają szczytowy udział 0,13–0,31% pola, zachowane co najmniej 0,28%. Decyduje więc wielkość
   literatury, a nie kształt krzywej.
4. *θ* nie przestawia więc kolejności ani lat, tylko wyznacza dolną granicę wielkości literatury,
   którą atlas obejmuje. W Metodach trzeba to napisać wprost: atlas opisuje technologie, które
   osiągnęły co najmniej 0,1% piśmiennictwa pola.
5. Obniżenie progów wprowadza do rdzenia 213–1 510 nowych fraz. Istniejącą kategorię ma tylko
   13–24 z nich, a jako technologia lub technika oznaczonych jest 4–8: głównie nazwy ogólne
   (CT image, intraoperative fluoroscopy, ORIF, TJR) oraz nazwane `virtual reality` (*k* ≤ 4),
   `virtual surgical planning`, `locking plate fixation`, `cbct scan`, `micro computed
   tomography` i `vegf` (*θ* = 0,05%). Wszystkie nowe frazy bez klasyfikacji są w
   `results/wrazliwosc_nowe_frazy.csv`.
6. Próg słownika (≥ 50 wystąpień) **nie był testowany** — wymaga powtórzenia zliczania fraz.

## Z2. Ucięte okna trwałości — `trwalosc_wzgledna_54.csv`

Dopisane kolumny `po_1_3_status`, `po_3_5_status` i `po_5_7_status`. **Wartości są bajt
w bajt identyczne z poprzednim plikiem.** Jedyne ucięte okno to **dual mobility cup, okno
+5–7: 1 z 3 lat** (2025). Pozostałe 32 okna są pełne. Grupy ze szczytem w 2025 (15) nie mają
okien po szczycie i nie wchodzą do porównania trwałości. Żadna z nich nie jest zanikiem.

## Z3. Wyłonienia odrzucone na przecięciu — `results/warianty_odrzucone.csv`

**Korekta liczb w `methods_v2.md`:** 1 468 → 1 294 pochodzi z pola sprzed filtra D6. Na obecnym
polu jest **1 461 → 1 289, odrzucone 172**.

| wypada w | n |
|---|---:|
| S2 (tylko ze streszczeniem) | 61 |
| S3 (tylko angielskie) | 60 |
| oba | 51 |

Istniejącą kategorię ma 18 z 172. Jako technologia lub technika oznaczonych jest 7: CT image,
intraoperative fluoroscopy, postoperative CT scan i ORIF (wypadają w S2) oraz non-surgical
treatment, ORIF group i TJR (wypadają w S3). Pozostałe 154 to głównie szablon i liczby.

**Technologie, które wypadają przez S3, czyli w piśmiennictwie nieangielskim** (odczyt nazw,
nie klasyfikacja — do oceny ortopedy): **`vertebroplasty`**, `accf`, `minimally invasive total
hip arthroplasty`, `hamstring autograft`. Przez S2: `robotic system`, `chatgpt`, `arthroscopic
hip surgery`.

**Cztery zdania:**

1. Przecięcie z S2 i S3 odrzuciło 172 z 1 461 wyłonień (12%), w podobnych proporcjach przez brak
   streszczenia (61), przez język (60) i przez oba warunki (51).
2. Odrzucone frazy to w przeważającej części szablon publikacyjny i ciągi liczbowe, czyli to,
   co filtr miał usuwać.
3. Przecięcie usunęło też kilka nazw technologii wyłaniających się głównie w piśmiennictwie
   nieangielskim. Najważniejsza z nich to `vertebroplasty`, o czym dalej w §6.
4. Warianty są zagnieżdżone, więc przecięcie jest filtrem, a nie replikacją. Tak to opisują już
   Metody v2 i tak zostaje.

## Z4. Czy filtr D6 przesuwa `y₀` — `results/d6_vs_y0.csv`

Δ = `y₀` (pole z D6) − `y₀` (pole bez D6). Dodatnia Δ oznacza, że D6 opóźnia wyłonienie.

| Δ | grup |
|---:|---:|
| 0 | **44** |
| +1 … +4 (D6 opóźnia) | 3 — komórki macierzyste **+4** (131 prac D6 przed `y₀`), MIPO **+3** (8), PEEK +1 (7) |
| −1 … −3 | 6 — TLIF −3, MUA −3, ACI −3, PSO −2, TAA −1, PSI −1 (0–3 prac D6 przed `y₀`) |
| wyłania się tylko z D6 | 1 — **mikrozłamania** (bez D6 prace zwierzęce podnoszą poziom bazowy 2000–2002) |

**Trzy zdania:**

1. Filtr weterynaryjny nie zmienia `y₀` w 44 z 54 grup.
2. Opóźnia je tam, gdzie literatura zwierzęca poprzedza kliniczną: przy komórkach macierzystych
   o 4 lata (131 prac usuniętych przed `y₀`), przy MIPO o 3. Przy mikrozłamaniach działa
   odwrotnie: bez filtra prace zwierzęce z lat 2000–2002 podnoszą próg i technika w ogóle
   się nie wyłania.
3. Przesunięcia w przeciwną stronę (do −3 lat) nie wynikają z prac zwierzęcych, tylko
   z mianownika: filtr zmniejsza pole o 4%, więc grupy blisko progu przekraczają go wcześniej.

Przewidywanie z briefu sprawdza się częściowo: klasa VI tak (komórki macierzyste, mikrozłamania),
klasa I tylko PEEK +1, a doszło MIPO z klasy III.

## Z5. Dwa sprawdzenia

- **Rok publikacji:** pierwszeństwo ma `ArticleDate` (data elektroniczna), potem `PubDate`, potem
  `MedlineDate` (`code/medline_extract.py:89-90`). Zdanie do Metod: *„Publication year was
  taken from the electronic publication date where available, otherwise from the print date.”*
- **MTIX 2024:** rekordy z lat 2024–2025 są w korpusie. Test H2 (deskryptory na rekord pola)
  odczytany z istniejącego `results/mtix_check.json`, bez nowego liczenia:

  | | 2019 | 2020 | 2021 | 2022 | 2023 | **2024** | **2025** |
  |---|---:|---:|---:|---:|---:|---:|---:|
  | deskryptory / rekord pola | 12,61 | 11,06 | 9,63 | 8,70 | 9,02 | **11,73** | **12,48** |

  **Rok 2024 to drugie złamanie, w przeciwnym kierunku:** indeksowanie wraca do głębokości sprzed
  2020. Dla wyników ważne jest jedno: zanik liczymy z udziału w 2025, a na średniej z lat
  2023–2025 zbiór zaników jest **identyczny (11 = 11, te same grupy)**. Nie zależy więc od
  pojedynczego roku po zmianie indeksowania.

## §6. Wada materiału: dziewięć grup mierzy skrót, nie technologię

Brief z 09-02 (`skroty_po_latach` §2) zakładał, że skrót i pełna postać są w tej samej grupie.
W `grupy_54.json` **dziewięć grup ma pełną nazwę tylko jako etykietę**, a liczy wyłącznie skrót.
Pełna postać nie weszła do rdzenia, bo się nie wyłania: ma wysoki poziom bazowy 2000–2002,
a rośnie tylko użycie skrótu. Tak samo było w `grupy_56`, `grupy_61` i `grupy_66`, więc to nie
jest skutek ostatnich zmian.

Analiza wrażliwości: ten sam przebieg z pełną nazwą dołączoną do grupy (materiał nietknięty).

| grupa | człony | prac teraz → z pełną nazwą | `y₀` teraz → z pełną nazwą | szczyt |
|---|---|---|---|---|
| total ankle arthroplasty | taa, tar | 853 → 1 212 | **2007 → 2019** | 2023 |
| periacetabular osteotomy | pao | 404 → 700 | **2012 → brak** | 2024 |
| total elbow arthroplasty | tea | 321 → 605 | **2013 → brak** | 2025 → **2005** |
| femoral nerve block | fnb | 188 → 411 | **2014 → brak** | 2016 |
| vertebroplasty | pvp, vertebral augmentation | 886 → 2 601 | **2005 → brak** | 2025 → **2009** |
| motor evoked potential | mep | 592 → 642 | 2013 → 2013 | 2025 |
| PFNA | pfna | 308 → 345 | 2011 → 2011 | 2025 |
| anterolateral ligament reconstr. | anterolateral ligament | 158 → 231 | 2016 → 2016 | 2017 → 2025 |
| manipulation under anesthesia | mua | 242 → — | nie da się sprawdzić¹ | — |

¹ Fraza rzeczownikowa nie obejmuje przyimka, więc „manipulation under anesthesia” nigdy nie jest
jedną frazą i grupa z konieczności liczy sam skrót.

**Co to znaczy:**

- **Cztery z 54 „wyłonień” to wyłonienia skrótu**, nie technologii: PAO, endoproteza łokcia,
  blokada nerwu udowego, wertebroplastyka. Jedno `y₀` (TAA) jest o 12 lat za wczesne.
  Wertebroplastyka ma szczyt w 2009, a nie w 2025 — to technologia w odwrocie, a nie rosnąca.
- **Wynik o przepływach:** wertebroplastyka i blokada nerwu udowego są wśród 13 „przepływów do
  Chin”. Przy wertebroplastyce skrót `pvp` jest typowy dla piśmiennictwa chińskiego, więc
  „przepływ” może być po prostu nawykiem zapisu. Nie liczyłem krajów na pełnych nazwach.
- **Zanik blokady nerwu udowego** zostaje (2025/szczyt 0,28 → 0,42), ale grupa traci `y₀`.
- To jest **ta sama lekcja o języku, którą praca stawia w centrum** — tyle że zadziałała
  w naszym własnym materiale. Raczej wzmacnia tezę, niż ją podważa, pod warunkiem że ujawnimy to
  sami.

**Do decyzji Przemka (nie dostrajam):**

- **(a)** Zastosować regułę §4a dosłownie („skrót wchodzi scalony z pełną postacią”): dołączyć
  pełne nazwy, wtedy cztery grupy wypadają z atlasu, a TAA ma `y₀` 2019. Materiał spada do 50
  grup; trzeba przeliczyć osie i kraje. To wykonanie istniejącej reguły, a nie nowa decyzja.
- **(b)** Zostawić 54 i opisać dziewięć grup jako ograniczenie, z tą tabelą w suplemencie.

Moja rekomendacja to **(a)**. Reguła §4a była spisana, zanim ten wynik był znany, a (b) zostawia
w atlasie cztery wyłonienia, o których sami wiemy, że są artefaktem nazwy.

## Szeregi do rycin

| plik | zawartość |
|---|---|
| `data/processed/szeregi_54.csv` | 54 × `grupa, y2000…y2025`, udział w % (zliczanie unijne, pole D6) |
| `data/processed/szeregi_54_prace.csv` | te same szeregi w liczbie prac |
| `data/processed/szeregi_czlonow.csv` | `panel, czlon, y2000…y2025` w %: 4 człony kifoplastyki, single bundle / double bundle reconstruction, mechanical / kinematic alignment |

Kontrole: z tych szeregów odtwarza się `y₀` i rok szczytu 54/54 z `osie_54.csv` oraz wartości
`trwalosc_wzgledna_54.csv`.

**`szeregi_jednoterminowe.json` ma nieaktualny mianownik:** te same liczby prac, ale rekordy pola
sprzed filtra D6 (4 843 w 2000 zamiast 4 550). Udziały wychodzą tam o ~3,5% za niskie, lata się
nie zmieniają. **Rycinę 0 (`fig_anatomy`) trzeba przerysować z `szeregi_54.csv`.**

## Box 1 — poprawiony do kodu (kod nietknięty)

| punkt | było | jest |
|---|---|---|
| **Decline** | persistence < *d* w pierwszym oknie | **udział w 2025 ÷ szczyt < 0,5** — tak liczy kod; okna po szczycie są opisowe. (Ponseti ma w oknie +1–3 dokładnie 0,500, a jest zanikiem.) |
| Threshold | „minimum paper count” | ≥ 5 prac **w każdym roku** |
| y₀ | ≤ koniec − 2 | ≤ koniec − (*m* − 1) = 2023 |
| Doubling | „growth not sustained” | nachylenie niedodatnie |
| Origin | *n* najwcześniejszych | *n* najwcześniejszych **ze znanym krajem** |
| Over-representation | „same years” | te same lata, od `y₀` do końca okna |
| Fig 0 / 5 / 6 | dane zablokowane / json | `szeregi_54.csv`, `szeregi_czlonow.csv`; Fig 0 do przerysowania |

## Kontrole

| | |
|---|---|
| materiał 54, osie | **nietknięte** |
| `trwalosc_wzgledna_54.csv` | wartości identyczne, dopisane 3 kolumny statusu |
| detektor wrażliwości przy parametrach domyślnych | odtwarza 3 warianty, rdzeń, 54/54 `y₀` |
| manifest | **12/12** |
| nowe skrypty | `code/szeregi_grup.py`, `code/wrazliwosc.py` |
