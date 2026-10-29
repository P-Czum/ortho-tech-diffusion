# Audyt manuskryptu i rycin na materiale 48 — odpowiedź na `brief_dla_vsc_manuskrypt_48_RESPONSE_2026-10-29`

Autor: sesja VS Code, 2026-10-29. Sprawdziłem `results_v4`, `methods_v3`, `skeleton_v4`,
`intro_discussion_v2` oraz ryciny 1 i 2 względem plików `_48`.

**Zgadza się co do liczby:**
- Wyniki: wyłonienia i lata, 14 rosnących, podwojenie 2,1–57 przy 39 policzalnych;
- Tabela 2: wszystkie komórki poza zaokrągleniem z pkt 4;
- kraje: 30/13/2/1/1/1, siedem jednokrajowych z udziałami, 10 rozproszonych z maksimum 25%,
  PELD 320 przy 1,5 i płytka dłoniowa 307 przy 12,8;
- pochodzenie: 26/14/8, 11 z 14 do Chin z listą źródeł, mediana 2,11 i minimum 1,45;
  wariant ścisły 10 i 8; strona USA 1,24 i 6 z 23;
- Tabela 4: wszystkie 30 wartości trwałości i oba zakresy „other eight”;
- Ryc. 2: 29/2/2/1/1/1 wobec 30/13/2/1/1/1, 12 bez słupka „started”.

Poniżej to, co trzeba poprawić, od najważniejszego.

## 1. „10 z 22 zaników” to liczba z materiału 60 — na materiale 48 jest **11 z 21**

Policzone tą samą regułą (`udział 2025 / szczyt < 0,5`), termin po terminie wobec grup ze
zliczaniem unijnym. Skrypt: `code/zaniki_przed_scaleniem.py --nr 48`, wynik:
`results/zaniki_przed_scaleniem_48.csv`.

| | |
|---|---:|
| zaniki termin po terminie | **21** |
| zaniki grupami | **10** |
| usuwa scalenie | **11** |
| — druga nazwa technologii, która zanika naprawdę (`aci`, `computer assisted navigation`, `hip resurfacing arthroplasty`, `tdr`) | **4** |
| — nazwy, których spadek to przesunięcie wewnątrz grupy, która jako całość nie zanika | **7**, w czterech technologiach: kifoplastyka, płytka blokowana, OWHTO, PSO |

Zmiana wobec materiału 60: kifoplastyka nie zanika (0,81), bo grupa zawiera teraz rosnący `pkp`.
Dlatego `balloon kyphoplasty` przechodzi z „drugiej nazwy” do „przesunięcia”, a `kyphoplasty`
dochodzi jako siódmy termin.

**Do poprawienia w czterech miejscach:**
- `results_v4`, akapit „The same confusion…”: *„Of 21 phrases first identified as declining,
  11 disappeared once variants of one name were merged: four were a second name for the same
  declining technology, and seven — in four technologies — were names whose fall was a shift of
  usage within a group that, as a whole, did not decline. Without merging, the paper would have
  reported twice as many declines as there were.”* (21 wobec 10, więc „twice” zostaje.)
- `skeleton_v4`, abstrakt (3) i plan: „10 of 22” → **„11 of 21”**.
- `intro_discussion_v2`, akapit „The same confusion operates at decline”: 22 → **21**;
  „Five… five…” → **„Four… seven…”**. Popraw też przykłady. Chondrocyte implantation i jej skrót
  to **druga nazwa**, a nie przesunięcie, i tak było już na materiale 60. Przykłady przesunięcia:
  kifoplastyka (uwagę przejmuje `pkp`), PSO (pełna nazwa spada, skrót rośnie) oraz OWHTO
  (przejmuje modyfikowana OWHTO).

## 2. Dwie grupy mają rok wyłonienia **po** szczycie — tekst i Ryc. 1 muszą to wyjaśnić

| grupa | `y₀` | szczyt | dlaczego |
|---|---:|---:|---|
| mesenchymal stem cell | 2017 | 2013 | powyżej progu (0,21%) tylko w latach 2013–14, a pierwsza trójka kolejnych lat to 2017–19 |
| highly cross-linked polyethylene | 2015 | 2008 | pojedynczy rok 2008 (0,17%), a pierwsza trójka to 2015–17 |

To jest zgodne z regułą (`y₀` wymaga trzech kolejnych lat), ale bez wyjaśnienia czytelnik
zobaczy sprzeczność. W `results_v4` komórki macierzyste występują jako wyłonienie z 2017 roku,
a w Tabeli 4 mają szczyt w 2013. Na Ryc. 1 kreska tych dwóch grup biegnie w lewo od znacznika,
a legenda mówi „emergence → peak year”.

**Proponuję:**
- **Ryc. 1:** kreska przerywana dla `szczyt < y₀` oraz przypis: *„For two technologies attention
  peaked in a short spike before the first three consecutive years above threshold (mesenchymal
  stem cells, 2013; highly cross-linked polyethylene, 2008).”* Mikrofraktura (`y₀` = szczyt =
  2012) mieści się w tym samym przypisie: *„microfracture peaked in its year of emergence”*.
- **Tabela 1:** ten sam przypis przy obu wierszach.
- **`methods_v3`, podwojenie:** *„…where the peak came less than two years after emergence
  (or, in two groups, before it)…”*.

## 3. `methods_v3` — pięć poprawek

1. **Odwołania do tabel są zamienione.** Retronimy są w `results_v4` w Tabeli 3, a nie 4 („The
   retronyms are reported in Table 4”). Kontekst zaników jest w Tabeli 4, a nie 3 („external
   sources named in Table 3”).
2. **„all its papers before emergence (median 43)”** → **median 44.5**
   (`kraj_pochodzenia_48.csv`, `przed_y0_n`).
3. **D6 — brakuje czterech grup.** Tekst opisuje 40 bez zmian, 3 opóźnione i mikrofrakturę, co
   daje 44 z 48. Pozostałe cztery D6 **przyspiesza** o 1–3 lata: ACI −3, TLIF −3, PSO −2, PSI −1.
   Dzieje się to przez mniejszy mianownik; przy PSO bez żadnej pracy weterynaryjnej przed `y₀`
   (`results/d6_vs_y0_48.csv`). Dopisz: *„…and brought it forward by one to three years for
   four, through the smaller denominator alone.”*
4. **MTIX przeliczony na materiale 48:** **ρ = 0.14, p = 0.23, n = 75 phrases** (było 0,14,
   0,18 i 88 na materiale 61; odtworzyłem to dokładnie przed przeliczeniem: 0,1426 i 0,185).
   Wnioski bez zmian. Test jest na frazach, nie na grupach: „a group's exposure” → **„a
   phrase's exposure”**. Dziewięć z 84 fraz odpada przez istniejące filtry skryptu, bo nie ma
   wiersza w tabeli wyłonień albo ma mniej niż pięć niezerowych lat w 2015–2021. Pliki:
   `results/mtix_impact_48.json`, `mtix_mechanizm_48.json`. Ta sama liczba stoi w
   `skeleton_v4` (Limitations) i w `intro_discussion_v2`.
5. **Rok publikacji:** *„…otherwise from the print date, or the MEDLINE date where neither is
   structured”* (`medline_extract.py:89-90`).

## 4. Drobne

- **`results_v4`, pierwszy blok „Notes for the authors”:** jest nieaktualny (29/16/9, 13 z 16,
  12 i 10). Usuń go; blok v4 pod nim jest poprawny.
- **Tabela 2, mediana `y₀`:** klasy I i V mają 2014,5, a w tabeli stoi 2014. Wpisz 2014.5 albo
  zaokrąglaj jednolicie.
- **„Only for dual-mobility cups is the leading country also the country of the earliest
  papers”:** przy short stem Niemcy są najczęstsze wśród dziesięciu najwcześniejszych prac.
  Wystarczy dopisać *„under both measures”*.
- **Podpis Tabeli 4:** „marked † (†)” → „marked †”.
- **`skeleton_v4`:**
  - Methods: „yielding 54 technologies” → **48** (45 odrębnych);
  - „eleven deviations” → **twelve**;
  - „each at 1.5–4 times China's share” → **1.45–4.6** (maksimum to PELD, 4,60);
  - punkt „Classifying evidence state. Three states…” jest pozostałością po wycofanej tezie — usuń.
- **`intro_discussion_v2`, „Three choices of ours move individual years”:** przykład
  wertebroplastyki już nie działa. Grupa po scaleniu z pełną nazwą w ogóle się nie wyłania
  (szczyt w 2009, obecna w bazie), więc to nie filtr S3 ją „kosztuje”. Do tego S3 usuwa frazy,
  a nie przesuwa lat. Usuń tę część zdania i zostaw D6 oraz MTIX 2024.

## 5. Odpowiedzi na Twoje pytania

1. **Ryc. 0 z hip resurfacing:** tak, zostaw. MoM bez czasu podwojenia nie pokaże tego punktu
   orientacyjnego.
2. **Mikrofraktura na Ryc. 1:** tak, przypis, połączony z pkt 2 powyżej.
3. **Tabela 1, układ kolumn:** zgoda, z dwiema zmianami.
   - Kolumna „kraj pierwszych prac” wypełniona **tylko tam, gdzie obie miary się zgadzają**
     (36 grup), a w pozostałych 12 „—” z przypisem. Tak samo liczy Ryc. 2; „reguła A” w Twoim
     opisie oznacza właśnie to.
   - Dodać **efektywną liczbę krajów** i **klasę pochodzenia** (ten sam kraj / przepływ /
     niejednoznaczne), bo tekst używa obu.

   Proponowany układ: *technology · kind · y₀ · peak · doubling (or reason) · effective
   countries · leading country (%) · country of earliest papers · origin class.* Przy pustym
   podwojeniu pokaż powód z `powod_braku_podwojenia`.
4. **S8:** dwa zdania o θ z `methods_v3` pasują do macierzy bez zmian; liczby się zgadzają
   (θ = 0,2% → 27 z 48, czyli 21 wypada). Proponuję podpis macierzy: *„k and m leave the list
   and the years of emergence unchanged in the median; θ sets a lower bound on the size of
   literature the atlas can describe (groups lost at 0.2% peaked at 0.13–0.31% of the field,
   groups retained at ≥ 0.28%).”*

## 6. Kontrole

| | |
|---|---|
| materiał 48, osie, kraje, trwałość | nietknięte |
| nowe wyniki | `zaniki_przed_scaleniem_48.csv`, `mtix_impact_48.json`, `mtix_mechanizm_48.json` |
| manifest | **12/12** |
