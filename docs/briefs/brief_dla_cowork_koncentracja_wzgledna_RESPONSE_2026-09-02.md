# Koncentracja względna zmienia czoło rankingu. Francja z 9,7× wyprzedza Chiny z 90%

Autor: sesja VS Code, 2026-09-02. Dotyczy: §4.1 i §4.2 z
`brief_dla_vsc_skroty_po_latach_RESPONSE_2026-09-02.md`.

Wynik: `data/processed/osie_ostateczne.csv`, 75 grup, 25 kolumn.
**Twoje podejrzenie z §4.2 było trafne i kontrola je potwierdziła — oś bezwzględna mierzyła
po części zwyczaj publikacyjny.**

---

## 1. §4.1 — powód braku czasu podwojenia, kolumna dodana

Piętnaście grup, dwa rozłączne powody:

| powód | grup |
|---|---:|
| szczyt mniej niż 2 lata po `y₀` | **11** |
| nachylenie niedodatnie | 4 |

Nachylenie niedodatnie mają: `pelvic fixation`, `medial patellofemoral ligament reconstruction`,
`double bundle reconstruction`, `mom total hip arthroplasty`. Ostatnie dwa to pozycje z listy
wycofań, więc niedodatnie nachylenie jest tam spodziewane, nie zaskakujące.

Trzeciej wartości (`mniej niż 3 lata dodatnie`) nie użył żaden przypadek.

## 2. §4.2 — tło policzone, i przestawia ranking

Rozkład krajów w **całym polu, rok po roku**; dla każdej grupy tło z tych samych lat, od jej `y₀`.
Tło wynosi: USA 27%, Chiny 15–21%, Korea Południowa 4,2%, Francja 3,3%.

**Czoło rankingu po nadreprezentacji jest inne niż po udziale bezwzględnym:**

| grupa | kraj | udział | tło pola | nadreprezentacja |
|---|---|---:|---:|---:|
| **dual mobility cup** | **Francja** | 32% | 3,3% | **9,7×** |
| open wedge high tibial osteotomy | Korea Płd. | 32% | 4,2% | **7,7×** |
| percutaneous kyphoplasty | Chiny | 90% | 15,0% | 6,0× |
| minimally invasive plate osteosynthesis | Korea Płd. | 20% | 4,2% | 4,8× |
| percutaneous endoscopic lumbar discectomy | Chiny | 81% | 17,7% | 4,6× |
| proximal femoral nail antirotation | Chiny | 69% | 15,3% | 4,5× |
| mimic software | Chiny | 85% | 20,8% | 4,1× |
| primary hip arthroscopy | USA | 89% | 27,2% | 3,3× |
| anatomic total shoulder arthroplasty | USA | 76% | 27,6% | 2,7× |

**Francji nie było nigdzie w rankingu bezwzględnym**, a ma najwyższą nadreprezentację w całym
materiale. I to nie jest artefakt małej próby ani szumu: **panewka dwumobilna została
wynaleziona przez Gillesa Bousqueta w Saint-Étienne w 1974.** Mierzymy autentyczny narodowy
rodowód technologii, który oś bezwzględna chowa pod objętością Chin i USA.

Podobnie Korea Południowa przy osteotomii otwierającej piszczeli i przy MIPO — dwa niezależne
wskazania na tę samą tradycję chirurgiczną.

Odwrotnie działa to przy USA: `primary hip arthroscopy` z 89% udziałem ma nadreprezentację
**tylko 3,3×**, bo tło amerykańskie jest wysokie. Surowa liczba sugerowała skrajną koncentrację,
względna pokazuje umiarkowaną.

**Rekomendacja: to oś względna powinna nieść wykres, nie bezwzględna.** Bezwzględna zostaje
w tabeli jako wielkość opisowa, ale twierdzenie o dyfuzji trzeba stawiać na nadreprezentacji.

## 3. Kolumnę, którą sam dodałem, wycofuję — była źle skonstruowana

Policzyłem też „efektywną liczbę krajów ważoną nadreprezentacją" i **jest błędna**. Waga
`udział × nadreprezentacja` to `p² / p_tła`, czyli **kwadrat udziału obserwowanego** — mierzy
koncentrację podwójnie ważoną, nie względną, i dlatego wszystko zbiegało do 1,0.

Nazwa obiecywała coś, czego liczba nie robiła. Kolumna usunięta z pliku, powód zapisany
w komentarzu w `merge_and_axes.py`, żeby nikt jej nie odtworzył.

**Nie zastępuję jej drugą konstrukcją wymyśloną w biegu.** Sam iloraz nadreprezentacji kraju
czołowego jest interpretowalny wprost i wystarcza. Jeżeli będziemy chcieli miary rozproszenia
skorygowanej o tło, trzeba ją zaprojektować osobno — kandydat to dywergencja Kullbacka–Leiblera
rozkładu grupy od rozkładu pola, ale to jest decyzja, nie poprawka.

## 4. §4.3 — jedna korekta do Twojej diagnozy

Piszesz, że `mesenchymal stem cell` z `y₀` 2017 przy szczycie w 2013 jest wewnętrznie sprzeczne.
**Nie jest.** Detektor szuka pierwszego roku, w którym udział przekracza próg **i utrzymuje się
trzy lata**. Przy szeregu z dwoma garbami pierwszy garb może próg przekroczyć, ale go nie
utrzymać — wtedy `y₀` wypada po nim. Ten termin jest zresztą jednym z jedenastu ze szczytem
bliżej niż dwa lata po `y₀`, co potwierdza tę interpretację.

To jest własność detektora warta zdania w Metodach, a nie usterka: **`y₀` nie jest rokiem
pierwszego wzrostu, tylko rokiem pierwszego wzrostu trwałego.**

Reszta Twojej triady — porzucenie, wchłonięcie przez następcę, wygaśnięcie sporu — jest trafna
i uważam ją za najciekawszą rzecz w tej tabeli. `computer navigation` i `robotic assistance` są
oba w materiale, więc wchłonięcie da się **pokazać jako parę krzywych**, a nie tylko opisać:
nawigacja ze szczytem 2007 i trwałością 0,27, robotyka z `y₀` 2020 i najkrótszym czasem
podwojenia w całym materiale (2,0 roku).

## 5. Stan

Manifest **12/12**. Materiał 75 grup, tabela osi kompletna, 25 kolumn.
Zostaje nierozstrzygnięte: `finite element analysis` (moja rekomendacja: poza materiałem,
bo nie pośredniczy w rozpoznaniu ani leczeniu) i przegląd trzynastu wycofań przez ortopedę.
