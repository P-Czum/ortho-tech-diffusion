# Kształt artykułu po odchudzeniu: atlas + lekcja o języku. I teza o kraju pochodzenia — sprawdzona, przepisana na ciekawszą

Autor: sesja VS Code, 2026-10-27. Decyzje ortopedy z dzisiejszej rozmowy.

Nowe pliki: `code/kraj_pochodzenia.py`, `data/processed/kraj_pochodzenia_54.csv`.
Zmienione: `docs/protocol/deviations.md` (D-11, D-12 i trzy aktualizacje),
`data/processed/material_54.csv` (klasa ALL).

**Ortopeda zapytał, czy nie przesadzamy z obliczeniami. Odpowiedź: liczenie jest skończone
i tanie — przesadzaliśmy z tym, ile z niego próbuje wejść do tekstu.** Poniżej nowy kształt.
Materiał 54 jest zamrożony; **żadnych nowych analiz** — dalej tylko pisanie.

---

## 1. Kręgosłup pracy

Artykuł próbował być trzema pracami naraz: atlasem technologii, pracą metodologiczną i pracą
o dowodach. Zostaje **atlas + lekcja o języku**:

> Co się wyłoniło w ortopedii XXI wieku i kto to badał — oraz dlaczego licznik publikacji myli
> nazwę z technologią, i przy wyłanianiu się (retronimy), i przy zanikaniu (10 z 22 pozornych
> zaników znika po scaleniu nazw).

Druga połowa łączy oba końce cyklu jedną myślą i jest tym, czego nie ma gatunek bibliometrii
pojedynczych technologii (`related_work.md` §1 — gatunek jest przepełniony i naiwny co do
nazw). Słowo „Decline" w tytule warto przemyśleć — patrz §4.

## 2. Co zostaje, co schodzi, co wypada

| element | gdzie |
|---|---|
| mapa 54 technologii (`y₀`, oś czasu) | **Wyniki, Tabela 1, Rycina 1** |
| dominacja USA/Chin | **Wyniki** |
| pięć wyjątków krajowych — **nowa wersja, §3** | **Wyniki, akapit** |
| retronimy (3 wiersze) + 10 z 22 zaników jako artefakt nazw | **Wyniki — awans na równy rdzeń** |
| klasy: implanty wolno i szeroko, techniki szybko i lokalnie | **Wyniki, akapit + mała tabela** (dotąd planowane do suplementu) |
| zaniki | **Wyniki, opisowo** — bez tezy o dowodach, §4 |
| czasy podwojenia | **kolumna w Tabeli 1**, bez osobnego akapitu |
| MTIX, audyt skażenia, wariant S1, dryf skrótów | **po jednym zdaniu w Metodach**, szczegóły w suplemencie |
| def2, runda druga | **D-11, D-12** w `deviations.md` — §5 |
| słownictwo powikłań | **wypada** (wynik zerowy) |
| warstwa leków | **wypada** — nigdzie nie raportowana; definicja upraszcza się do „urządzenia i techniki" |
| efektywna liczba autorów i czasopism | **wypada** (policzona, nieużywana) |

## 3. Kraj pochodzenia — sprawdzony na najwcześniejszych pracach

Zdanie z `results_v2.md` — *„Outside the two largest producers… a country leads the research
on a technology only when the technology originated there — five cases of five"* — **nie
przechodzi testu.** Ale to, co wychodzi zamiast niego, jest ciekawsze.

Test: dla każdej grupy kraj pierwszej pracy w korpusie i najczęstszy kraj wśród dziesięciu
najwcześniejszych prac ze znaną afiliacją; dodatkowo najczęstszy kraj przed `y₀`.

| technologia | prowadzi | pierwsza praca | 10 najwcześniejszych | przed `y₀` | ocena |
|---|---|---|---|---|---|
| dual mobility cup | **Francja** | Francja 2008 | **Francja 7/10** | Francja 26/47 | **pochodzenie = lider** |
| short stem | **Niemcy** | Niemcy 2000 | Niemcy 3/10 | USA 11, Niemcy 9 /42 | częściowo |
| volar locking plate | **Japonia** | **USA 2005** | **USA 4**, Japonia 2 /10 | USA 13, Japonia 10 /52 | **przejęcie** |
| MIPO | **Korea Płd.** | **Szwajcaria 2001** | Korea **0**/10 | Korea 14/69 | **przejęcie** |
| open wedge HTO | **Korea Płd.** | Brazylia 2004 | Korea 1/10 | **Niemcy 10**, Korea 8 /64 | **przejęcie** |

**Kraj pochodzenia potwierdza się wprost raz (Francja), częściowo raz (Niemcy). Trzy razy
literaturę przejął kraj, który techniki nie wymyślił:** płytkę dłoniową zaczęły prace
amerykańskie, MIPO szwajcarskie (AO), OWHTO europejskie — a prowadzą Japonia i dwukrotnie
Korea. Dane zgadzają się tu z historią techniki niezależnie od niej (Orbay w USA, Krettek
i AO, TomoFix).

**Częstość bazowa:** w pozostałych 49 grupach (prowadzonych przez USA albo Chiny) kraj
czołowy jest zarazem najczęstszym wśród najwcześniejszych prac w **31 z 49**. Wśród pięciu
wyjątków — w **2 z 5**. Wyjątki są więc *rzadziej* niż reszta prowadzone przez kraj, który
zaczynał.

### Proponowane brzmienie

> Poza parą USA–Chiny pięć technologii ma literaturę prowadzoną przez inny kraj. Tylko przy
> panewkach dwumobilnych kraj czołowy jest zarazem krajem najwcześniejszych prac (Francja).
> Trzy przypadki są odwrotne: najwcześniejsze prace o płytkach dłoniowych pochodzą z USA,
> o MIPO ze Szwajcarii, o osteotomii otwierającej z Europy — a literaturę prowadzą Japonia
> i dwukrotnie Korea Południowa. Przywództwo w piśmiennictwie wskazuje, gdzie technika
> znalazła swoje miejsce kliniczne, a nie gdzie ją wymyślono.

### Zastrzeżenia, które muszą stać obok

- **Okno zaczyna się w 2000.** Dla technik starszych (dual mobility 1974, MIPO 1997)
  najwcześniejsze prace w korpusie nie są pracami założycielskimi. Przy MIPO i tak wychodzi
  Szwajcaria, przy dual mobility i tak Francja — ale to jest „najwcześniejsze w oknie".
- **Dziesięć prac to mało.** Dlatego tabela podaje też okres przed `y₀` (42–69 prac); oba
  pomiary wskazują w tę samą stronę.
- **Przyczyna przejęcia nie jest mierzona.** „Miejsce kliniczne" to interpretacja —
  przy Korei i HTO zgodna z wiedzą kliniczną ortopedy, ale w tekście jako interpretacja.

## 4. Zaniki a stan dowodów — wycofane z wniosków

Teza „literatura widzi odrzucenie, nie widzi akceptacji" **schodzi z wniosków, streszczenia
i Clinical relevance.** Trzy powody łącznie: n = 2 po stronie odrzuconych; w oknie +1–3 odstęp
0,003; ortopeda klasyfikował stan dowodów, **znając już krzywe trwałości** (Metody piszą to
wprost). Każdy z osobna da się opisać zastrzeżeniem; razem nie unoszą konkluzji.

Co zostaje: jedenaście zaników opisowo, z trwałością względem własnego szczytu (Tabela 3),
oraz **zaniki jako druga połowa lekcji o języku** — 10 z 22 pozornych zaników znika po
scaleniu nazw. To jest twierdzenie mocne i przenosi rozdział o zanikach z dowodów na metodę.

Konsekwencja dla tytułu: *Emergence, Origin, and Decline…* obiecuje tezę o zanikach, której
już nie stawiamy. Do przemyślenia, nie narzucam brzmienia.

## 5. Rejestr odchyleń — D-11 i D-12 dopisane

| | rejestrowano | teraz |
|---|---|---|
| **D-11** | RQ3, kontrole §6.2, runda druga po κ < 0,70 | rozkład kodera 1 jako wynik zamknięty w S1; **runda druga niewykonana** — zaślepienie po stronie człowieka już złamane |
| **D-12** | `y₀` w obu definicjach pola | **tylko def1** — decyzja zakresowa, nie wymuszona pomiarem; tekst def2 za 2000–2025 (316 091 rekordów) wyciągnięty i zachowany |

D-12 opisany uczciwie jako **decyzja autora, nie wymuszenie** — tak samo jak D-8.

Przy okazji trzy aktualizacje rejestru: „Two of **twelve**" w §3; MTIX z wynikiem na
materiale końcowym (ρ = 0,14, p = 0,18, n = 88); i **zamknięty** punkt o braku
systematycznego testu skażenia — audyt z 2026-09-03 go zamyka.

**Do S1 — rozkład kodera 1, gotowy:**

| kategoria | n | % |
|---|---:|---:|
| non-technological term | 229 | 79,8 |
| renaming | 20 | 7,0 |
| novel concept | 20 | 7,0 |
| conceptual evolution | 18 | 6,3 |
| measurement artifact | 0 | 0,0 |

Z obowiązkowym zastrzeżeniem z rejestracji §6.1: rdzeń prefiltrowany przez cztery warianty
tekstu, więc niski udział artefaktów pomiaru jest **z konstrukcji** i nie uogólnia się na
7 662 wykryte wyłonienia.

## 6. Klasy — komplet

`anterolateral ligament reconstruction` → **III. technika operacyjna** (decyzja ortopedy
2026-10-27). Wpisane w `material_54.csv` jako dopisek po zamrożeniu; `klasy_60.csv` z commitu
`0dec1fc` nietknięty.

| klasa | n | `y₀` | podwojenie | kraje eff. | rośnie | zaniki |
|---|---:|---:|---:|---:|---:|---:|
| I. implant i materiał | 10 | 2014,5 | **18,4** | **7,7** | 3 | 2 |
| II. endoprotezoplastyka | 7 | **2007** | 11,7 | 5,5 | 2 | 2 |
| III. technika operacyjna | **24** | 2014 | **5,2** | **4,8** | 4 | 2 |
| IV. narzędzie wspomagające | 7 | **2019** | 8,1 | 5,7 | **5 z 7** | 1 |
| V. postępowanie okołozabiegowe | 3 | 2014 | 17,2 | 5,3 | 1 | 1 |
| VI. terapia biologiczna | 3 | 2012 | 5,0 | 7,0 | 0 | **3 z 3** |

Zdanie do Wyników: **implanty dyfundują wolno i szeroko** (18 lat, prawie 8 krajów),
**techniki szybko i lokalnie** (5 lat, niecałe 5 krajów). Narzędzia są **najmłodsze**
i pięć z siedmiu wciąż rośnie — o ich tempie nie piszemy (brief z 09-25 §4).

## 7. Kolejność pracy

1. Nanieść liczby materiału 54 (briefy z 09-07 i 09-25) na nowy kształt.
2. Przepisać akapit o pięciu wyjątkach wg §3.
3. Wyjąć tezę o dowodach z wniosków, streszczenia i Clinical relevance.
4. Metody: jedno zdanie o granicy klauzuli „research method" (FEA, Mimics wypadają; AI
   zostaje, bo jest stosowana u chorego).

## 8. Kontrole

| | |
|---|---|
| materiał | **54**, zamrożony — bez nowych analiz |
| klasy | komplet, 0 grup bez klasy; `klasy_60.csv` nietknięty |
| manuskrypt | **nietknięty** |
| manifest | **12/12** |
