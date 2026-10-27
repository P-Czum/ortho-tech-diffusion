# Wymyślenie i propagacja — dwa etapy w jednych danych. Zastępuje §3 briefu `ksztalt_artykulu` z dziś

Autor: sesja VS Code, 2026-10-27. Na podstawie uwagi ortopedy: *„można oba — wymyślenie
i propagacja, trochę jak z adaptacją innowacji"*.

Dane: `data/processed/kraj_pochodzenia_54.csv` (bez nowego liczenia — test policzył kraj
najwcześniejszych prac dla wszystkich 54 grup), nadreprezentacja z `osie_54.csv`.

**W briefie sprzed godziny postawiłem to jako albo–albo: „przywództwo pokazuje miejsce
kliniczne, *a nie* wynalezienie". Ortopeda ma rację, że to dwa etapy jednego cyklu, a nie
konkurencyjne odpowiedzi — i w tym ujęciu wynik obejmuje całą pracę, nie pięć wyjątków.**

---

## 1. Reguła klasyfikacji

Dwie miary kraju najwcześniejszych prac: (a) najczęstszy wśród 10 najwcześniejszych prac,
(b) najczęstszy w całym okresie przed `y₀` (mediana 43 prace). Grupa jest klasyfikowana tylko
wtedy, gdy **obie miary się zgadzają**; inaczej — niejednoznaczna.

| typ | grup |
|---|---:|
| **ten sam kraj zaczął i prowadzi** | **29** |
| **przepływ** — zaczął jeden kraj, prowadzi inny | **16** |
| niejednoznaczne (miary się rozchodzą) | 9 |

## 2. Wynik: dwa kraje dominują z dwóch różnych powodów

**Trzynaście z szesnastu przepływów kończy się w Chinach.** Źródła: głównie USA (kifoplastyka,
wertebroplastyka, TLIF, PSO, blokada udowa, MPFL, ultrasonografia), ale też Korea (PELD,
femoral neck system), Japonia (OLIF), Dania (blokada kanału przywodzicieli).

**Kontrola na przesunięcie się całego pola:** udział Chin w całym piśmiennictwie ortopedycznym
rósł przez 25 lat, więc „przepływ do Chin" mógłby być tylko tym. Nie jest: **we wszystkich
13 przypadkach Chiny są nadreprezentowane względem tła pola z tych samych lat — mediana
2,2×, minimum 1,45×.** Chiny prowadzą tu ponad swoją wagę.

Po drugiej stronie: z 29 grup „ten sam kraj" **26 to USA**.

> Para USA–Chiny dominuje piśmiennictwo z dwóch różnych powodów: Stany Zjednoczone najczęściej
> technologię zaczynają i utrzymują, Chiny najczęściej przejmują technologię zapoczątkowaną
> gdzie indziej i stają się głównym ośrodkiem jej badań.

### Zastrzeżenie, które musi stać obok — strona USA nie jest skontrolowana

Strona chińska przechodzi kontrolę tła. **Strona amerykańska nie:** nadreprezentacja USA
w 26 grupach „zaczął i prowadzi" ma medianę zaledwie **1,25×**, a w **6 z 26 jest poniżej
tła**. Do tego w latach 2000. USA było największym producentem piśmiennictwa, więc „najwcześniejsze
prace są amerykańskie" jest częściowo po prostu efektem wielkości. Bezpieczne brzmienie:
*„USA zaczyna i prowadzi"* jako obserwacja, a nie teza o amerykańskiej innowacyjności.

## 3. Pięć wyjątków — korekta briefu sprzed godziny

W §3 briefu `ksztalt_artykulu` zaliczyłem MIPO do „przejęć". **Przy wymogu zgodności obu miar
MIPO jest niejednoznaczne** — pierwsza praca jest szwajcarska, ale okres przed `y₀` (2000–2013)
już koreański. To samo dotyczy short stem.

| technologia | 10 najwcześniejszych | przed `y₀` | prowadzi | typ |
|---|---|---|---|---|
| dual mobility cup | Francja | Francja | Francja | **ten sam kraj** |
| volar locking plate | USA | USA | Japonia | **przepływ** |
| open wedge HTO | Australia | Niemcy | Korea Płd. | **przepływ** |
| MIPO | Tajlandia | Korea Płd. | Korea Płd. | niejednoznaczne |
| short stem | Niemcy | USA | Niemcy | niejednoznaczne |

Czysto: **jeden kraj, który wymyślił i prowadzi (Francja), dwa przepływy (płytka dłoniowa
USA → Japonia, OWHTO Europa → Korea), dwa niejednoznaczne.** Przy dwóch ostatnich nie piszemy
o pochodzeniu.

Dwa przypadki spoza piątki dobrze nadają się do ilustracji, bo dane zgadzają się z historią
techniki: **blokada kanału przywodzicieli** — najwcześniejsze prace duńskie, prowadzą Chiny;
**zabieg Latarjeta** — najwcześniejsze prace francuskie (choć przed `y₀` już amerykańskie,
więc formalnie niejednoznaczne).

## 4. Rama teoretyczna

Rogers, *Diffusion of Innovations* — wynalezienie i rozprzestrzenianie jako odrębne etapy.
Daje pracy ramę, której dotąd nie miała, i jest kanoniczna.

**Jedno zastrzeżenie w duchu całej pracy:** Rogers opisuje przyjmowanie innowacji przez
użytkowników. My mierzymy **uwagę badawczą**, nie wdrożenie kliniczne. Pisać „propagacja
uwagi badawczej" albo „przejęcie piśmiennictwa", nie „adopcja technologii" — to ta sama
granica, której pilnowaliśmy przy zanikach („wyparcie dotyczy zainteresowania w literaturze").

## 5. Co to zmienia w kształcie artykułu

W briefie `ksztalt_artykulu` §1 kręgosłup to „atlas + lekcja o języku". **Ten wynik wzmacnia
atlas:** odpowiedź na pytanie „kto to badał" ma teraz strukturę — kto zaczyna, kto przejmuje —
zamiast samej listy krajów czołowych. Proponuję go jako główny wynik części o krajach, z pięcioma
wyjątkami jako jej szczególnym przypadkiem, a nie osobnym akapitem.

W Tabeli 1 wystarczy jedna dodatkowa kolumna: **kraj najwcześniejszych prac** obok kraju
czołowego.

## 6. Kontrole

| | |
|---|---|
| nowe obliczenia | **brak** — odczyt `kraj_pochodzenia_54.csv` i `osie_54.csv` |
| materiał | **54**, zamrożony |
| manifest | **12/12** |
