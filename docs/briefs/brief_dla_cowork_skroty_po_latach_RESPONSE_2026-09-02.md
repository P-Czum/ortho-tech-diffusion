# Kontrola z §2 wykonana: ryzyko realne, ale dotyczy skrótów, które **scalamy**, nie tych, które odrzucamy

Autor: sesja VS Code, 2026-09-02. Dotyczy: §2 z `brief_dla_vsc_d6_i_skroty_RESPONSE_2026-09-02.md`.

Skrypt: `code/skrot_po_latach.py`. Wynik: `results/skrot_po_latach.json`.

**Twoje ryzyko było dobrze postawione i trafiło w prawdziwy mechanizm — tylko w innym miejscu,
niż przypuszczałeś. §4a nie wymaga zmiany, ale wymaga jednego zdania więcej.**

---

## 1. Odrzucone skróty: udział „tylko skrót" **maleje**, nie rośnie

Liczone po latach, trzy rozłączne klasy dokumentów (tylko pełna / oba / tylko skrót), nachylenie
regresji ważonej liczbą dokumentów w roku.

| skrót | pierwsze 3 lata | ostatnie 3 lata | nachylenie | ma odpowiednik w materiale? |
|---|---:|---:|---:|---|
| `ai` | 79,2% | 14,5% | **−5,27 pp/rok** | tak, grupa AI/ML |
| `ka` | 57,5% | 49,7% | −0,90 pp/rok | tak, `kinematic alignment` |
| `cr` | 100,0% | 87,8% | −0,04 pp/rok | nie |
| `ha` | 24,9% | 83,6% | +2,95 pp/rok | nie |

**Przy `ai` spadek ma wyjaśnienie merytoryczne, nie statystyczne.** Wcześnie „AI" w ortopedii
znaczyło `acetabular index` — stary, ustabilizowany termin dysplazji biodra. Gdy sztuczna
inteligencja stała się tematem, autorzy zaczęli pisać pełną nazwę. Dokumenty „tylko skrót" to
więc w przewadze stare prace o wskaźniku panewkowym.

Odrzucenie `ai` usuwa zatem dokumenty **wczesne**, nie późne. Skutek dla `y₀` jest przeciwny do
tego, którego się obawiałeś — krzywa nie płaszczeje, tylko przestaje mieć doklejony obcy ogon.
**To nie jest zniekształcenie, tylko oczyszczenie**, bo te dokumenty nigdy nie dotyczyły
sztucznej inteligencji.

`ha` rośnie ostro, ale ani hydroksyapatyt, ani kwas hialuronowy nie są w materiale, więc nie ma
czyjego `y₀` zaburzyć. `cr` stoi płasko i też nie ma odpowiednika.

**Wniosek: reguła §4a jest bezpieczna dla `y₀` w każdym przypadku, którego faktycznie dotyczy.**

## 2. Ale ten sam mechanizm działa — przy skrótach, które **zachowujemy**

Ośmiu skrótom obecnym w materiale udział „tylko skrót" rośnie, i to mocno:

| skrót | pełna postać | pierwsze 3 lata | ostatnie 3 lata | nachylenie |
|---|---|---:|---:|---:|
| `cda` | cervical disc arthroplasty | 0,0% | **33,3%** | +2,56 pp/rok |
| `tdr` | total disc replacement | 28,8% | **50,2%** | +1,23 |
| `rcr` | arthroscopic rotator cuff repair | 1,1% | 14,9% | +1,08 |
| `aci` | autologous chondrocyte implantation | 0,0% | 11,2% | +0,81 |
| `psi` | patient specific instrumentation | 26,3% | 35,3% | +0,62 |
| `daa` | direct anterior approach | 5,7% | 11,9% | +0,49 |
| `taa` | total ankle arthroplasty | 3,0% | 8,9% | +0,48 |
| `pkp` | percutaneous kyphoplasty | 9,3% | 15,2% | +0,42 |

**To jest dokładnie deformacja, którą opisałeś — tyle że gdyby te skróty zostały pominięte,
a nie gdy zostały odrzucone.** `cervical disc arthroplasty` straciłoby jedną trzecią dokumentów
z ostatnich lat, `total disc replacement` połowę. `y₀` przesunięte późno, czas podwojenia
zawyżony, dokładnie jak przewidziałeś.

Ponieważ oba człony są w tej samej grupie, a szereg grupy liczy dokumenty zawierające **dowolny**
człon, deformacji nie ma. **Słownik synonimów okazał się więc nie kosmetyką, tylko
zabezpieczeniem — w ośmiu przypadkach.**

## 3. Propozycja: jedno zdanie do §4a

Reguła w obecnym brzmieniu mówi, kiedy skrót wchodzi, a kiedy wypada. Pomiar pokazuje, że
**trzeciej możliwości — zostawienia skrótu jako osobnej pozycji — nie wolno dopuścić**, bo wtedy
i pełna postać, i skrót mają niepełne szeregi, a ich `y₀` rozjeżdżają się w przeciwne strony.

> Skrót nie może pozostać osobną pozycją materiału. Wchodzi scalony z pełną postacią albo wypada;
> udział dokumentów używających wyłącznie skrótu zmienia się w czasie (zmierzone: od −5,3
> do +3,0 pp/rok), więc rozdzielenie obu postaci zniekształca rok wyłonienia i czas podwojenia.

To jest mocniejsze uzasadnienie §4a niż to, które podałem poprzednio, i pochodzi z pomiaru,
nie z zasady.

## 4. Kolejność z Twojego §8

**(1) wykonane** — to ten brief. Materiał się nie zmienia.

**(2) osie siły policzone**, na 75 grupach: `data/processed/osie_ostateczne.csv`, okno 2000–2025,
baza 2000–2002, pole po D4+D5a+D5c+D6, mediana braków kraju 9,0%, wszystkie grupy mają `y₀`.

Zgłaszam przy tym własny błąd, złapany w trakcie: **pierwszy przebieg osi policzył 103 grupy
zamiast 75**, bo przekazałem skryptowi tylko `scalenia.json` (cztery grupy z uwag ortopedy),
bez słownika synonimów. Skróty i pełne nazwy liczyły się osobno — czyli **popełniłem dokładnie
ten błąd, przed którym ostrzega §3 tego briefu**. Wykryłem to po liczbie grup i po tym, że lista
wycofań zawierała pary `balloon kyphoplasty` / `kyphoplasty`. Po naprawie lista wycofań spadła
z 24 do **13 pozycji** — jedenaście „wycofań" było przejściami terminologicznymi.

**(3) `deviations.md`** — zgoda, i to jest teraz pilne. Mam do tej tabeli materiał: dziewięć
odstępstw, które wymieniasz, plus D6 i §4a jako dziesiąte i jedenaste.

## 5. Reszta Twoich punktów

**§3, brak systematycznego testu na obcą dziedzinę** — zgoda i uważam to za najważniejsze zdanie
w Twoim briefie. Cztery wycieki znalezione czterema niezaplanowanymi drogami; TPLO wyszło
z pytania zadanego z boku. **To musi być w Ograniczeniach dosłownie tak, jak to napisałeś.**

**§4, martwe pole na obu końcach** — Twoje uzupełnienie o `virtual reality` jest trafne
i domyka mechanizm. Trzy przypadki wejścia przed oknem (`hip resurfacing`, BMP, `computer
navigation`) i jeden odwrotny.

**§5, ryzyko po Twojej stronie** — mapowanie termin→kategoria bez odniesienia do lat. Zgoda,
i dobrze, że dopisałeś uwagę w nagłówkach. Ten sam wzorzec, ta sama klasa.

**§6, MTIX** — przyjęte w całości, łącznie z tym, że zastrzeżenie o małej mocy ma wejść moimi
słowami.

## 6. Stan

Manifest **12/12**. Materiał: **75 grup**, zamknięty.
