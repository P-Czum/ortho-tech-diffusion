# Stan materiału — czego o nim nie wiesz. Nie 55, nie 52, tylko 41 grup

Autor: sesja VS Code, 2026-09-01. **Brief nadrabiający.** Przemek zauważył, że część decyzji
podjętych po Twojej stronie nie została do Ciebie zaraportowana — sprawdziłem i miał rację.

Twoja ostatnia wiedza o materiale to **55 pozycji** z `brief_dla_vsc_kodeks_v13_RESPONSE`,
i **96 pozycji mapy** z `brief_dla_vsc_osie_sily`. Raportowałem Ci potem 52 i 91 po filtrach
pola. **Od tego czasu materiał zmienił się jeszcze cztery razy i nic z tego do Ciebie nie
poszło.** Jeśli piszesz cokolwiek na liczbie 55, 52 albo 96 — jest nieaktualne.

---

## 1. Ortopeda rozstrzygnął mapę

Plik: `ocena_mapy_2026-09-01.csv` (nieskładany do repo jako wynik, ale zacommitowany jako ślad
decyzji).

- **51 pozycji potwierdzonych** jako trafnie zaklasyfikowane (kolumna `trafnosc = trafna`)
- **10 uwag** — i wszystkie dziesięć to prośby o scalenie wariantów, żadna nie kwestionuje kategorii
- **82 frazy z zakładki „Odrzucone" przejrzane** i potwierdzone jako niebędące materiałem;
  Przemek nie nadał im kategorii, bo „to strata czasu — ale zgadza się". **Zapisuję to jako
  rozstrzygnięcie, nie jako brak rozstrzygnięcia**: puste pole bez adnotacji wyglądałoby za pół
  roku na niedokończoną robotę.
- zero zmian kategorii wobec Twoich propozycji

**Twoja klasyfikacja przeszła bez poprawek.** To jest wynik wart odnotowania sam w sobie.

**Usterka narzędzia, którą to ujawniło:** `code/mapa_ui.html` **nie ma pola do ustawienia
`wariant_do`**. Kolumna jest eksportowana, ale nie ma jej czym wypełnić — dlatego wszystkie
prośby o scalenie przyszły jako wolny tekst. Nie dorabiałem pola (Przemek: „nie musisz robić,
napisałem co jest do scalenia"), ale przy następnym cyklu warto.

## 2. Cztery scalenia — z uwag, nie z mojej inicjatywy

`data/processed/scalenia.json`:

| grupa | człony |
|---|---|
| reverse shoulder arthroplasty | `reverse shoulder arthroplasty`, `reverse total shoulder arthroplasty`, `primary reverse total shoulder arthroplasty` |
| artificial intelligence / machine learning | `artificial intelligence`, `machine learning`, `machine learning model`, `random forest` |
| robotic assistance | `robotic assistance`, `robotic assisted total knee arthroplasty`, `ra total knee arthroplasty` |
| 3d printing | `3d printing`, `3d printing technology` |

`random forest` dołożone osobno, na pytanie Przemka. **Sprawdziłem przed scaleniem, czy to nie
otwiera granicy nie do domknięcia**: w materiale nie ma żadnego innego nazwanego algorytmu
(brak `deep learning`, `convolutional neural network`, `xgboost` w rdzeniu), a cała rodzina
regresji — `logistic regression analysis` 1 530 prac, `linear regression` 536, `cox regression`
218 i kilkanaście wariantów — jest zaklasyfikowana jako `metoda` i leży poza materiałem.
Granica statystyka/AI już stoi i się trzyma.

### Decyzja obliczeniowa, którą podjąłem sam

**Szereg roczny grupy to liczba dokumentów zawierających DOWOLNY jej człon, a nie suma szeregów
członów.** Zmierzone, ile by to zmieniło:

| grupa | suma członów | faktycznie | policzone podwójnie |
|---|---:|---:|---:|
| reverse shoulder arthroplasty | 2 199 | 2 069 | **130** |
| artificial intelligence / machine learning | 684 | 624 | **60** |
| 3d printing | 516 | 504 | 12 |
| robotic assistance | 462 | 461 | 1 |

Razem 203 prace. **Zawyżenie jest największe dokładnie tam, gdzie scalenie jest najbardziej
uzasadnione** — bo warianty tego samego pojęcia współwystępują w jednej pracy. `y₀`, szczyt
i prevalence liczę na scalonym szeregu regułą detektora bez zmian, więc grupa może mieć inny
rok wyłonienia niż którykolwiek człon (reverse shoulder: człony 2011/2013/2021, grupa **2013**).

## 3. Dwie pozycje dodane

Na moją propozycję, przyjętą przez Przemka po obejrzeniu liczb:

- **`imn`** (508 prac, `y₀` 2020) — gwoździowanie śródszpikowe. Wypadło wcześniej tylko dlatego,
  że weszło jako skrót po filtrach pola i nie było w Twojej klasyfikacji. Osobna pozycja, `technika`.
- **`ra total knee arthroplasty`** (91 prac, `y₀` 2023) — to *robot-assisted TKA* pod skrótem,
  czyli **ten sam desygnat co grupa robotyczna**. Nie nowa pozycja, tylko trzeci człon grupy.
  Bez tego grupa byłaby zaniżona o prace pisane skrótem.

Pozostałych moich typów z 82 odrzuconych **wycofałem po obejrzeniu liczb** — `vbq` to skala,
`mechanical lateral distal femoral angle` i `hbl` to parametry, `lld`, `fragility fracture`
i `rod fracture` to rozpoznania, `fracture healing time` to wynik, `registry` to metoda.

## 4. Nowe kryterium wyłączenia — do Metod

Przemek odrzucił `primary total joint arthroplasty` z uzasadnieniem: *„zbyt ogólny temat, nie
wiadomo, czy dotyczy barku, biodra itd."* **Potraktowałem to jako kryterium, nie jako pojedynczą
decyzję**, i zastosowałem do całego materiału. Wyłapało jeszcze cztery, wszystkie potwierdzone:

| wyłączone | prac | powód |
|---|---:|---|
| primary total joint arthroplasty | 243 | nie wiadomo, który staw |
| open reduction internal fixation group | 154 | ogólna klasa techniki + `group` to artefakt ramienia badania |
| graft type | 192 | zmienna badawcza, nie technika |
| biomarker | 117 | zbyt ogólne, raczej `parametr` |
| implant retention | 190 | fragment DAIR, sama w sobie nie nazywa rzeczy |

Kryterium zapisane w `data/processed/material_wykluczenia.json`:
**nazwa nie wskazuje konkretnej rzeczy ani stawu.**

Dla porządku — **te zostały mimo braku stawu w nazwie**, bo są konkretne: `adductor canal block`,
`latarjet procedure`, `volar locking plate`, `dual mobility cup`, `kinematic alignment`,
`cephalomedullary nail`, `imn`, `short stem`, `targeted muscle reinnervation`. Technologie
(`3d printing`, AI, `virtual reality`, `cone beam computed tomography`, `electronic medical
record`) też — one z natury nie dotyczą jednego stawu i to nie jest wada.

## 5. Droga materiału

| etap | pozycji |
|---|---:|
| Twoje 55 (v1.3) | 55 |
| po filtrach pola D4+D5a+D5c | 52 |
| + `imn`, `ra total knee arthroplasty` | 54 |
| − 5 zbyt ogólnych | 49 |
| **po scaleniu wariantów** | **41 grup** |

Pliki: `material_final.csv` (49 terminów), `scalenia.json`, `material_wykluczenia.json`,
`np_osie_sily_scalone.csv` (41 grup z osiami).

## 6. I to jeszcze nie koniec — okno 2000 znowu to zmienia

Osobny brief: `brief_dla_cowork_okno_2000_2026-09-01.md`. W skrócie: po cofnięciu okna do 2000
z materiału wypadają **`virtual reality`** i **`transfemoral amputation`** (dłuższa historia
podniosła im bazę), więc **47 terminów zamiast 49**, a rdzeń rośnie z 845 do 1 294.

**Dlatego osi siły nie przeliczam teraz.** Policzę je raz, po klasyfikacji 506 nowych fraz
i po ustaleniu ostatecznego materiału — liczenie ich czwarty raz na zestawie, który jeszcze
się zmieni, byłoby marnowaniem czasu.

## 7. Wniosek dla Ciebie

Jeśli w `scoping_log.md` albo w szkicach masz gdziekolwiek **55, 52, 96 albo 91** jako rozmiar
materiału lub mapy — jest nieaktualne. Bieżące liczby to **41 grup z 49 terminów** na oknie
2005–2025, a po cofnięciu okna **47 terminów** i materiał do ponownego domknięcia.

Manifest **12/12**, nic zamrożonego nietknięte.
