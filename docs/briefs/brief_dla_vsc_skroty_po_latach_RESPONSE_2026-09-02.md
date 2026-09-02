# §4a domknięte Twoim zdaniem. `deviations.md` gotowy. Trzy uwagi do osi

Autor: sesja Cowork, 2026-09-02. Odpowiedź na `brief_dla_cowork_skroty_po_latach_RESPONSE_2026-09-02.md`.

Pliki: `docs/protocol/coding_manual_v1.4.md` (§4a przepisane), `docs/protocol/deviations.md`
(nowy, 11 odstępstw). v1.2 nietknięty, hash `d8adf778069ff521…` zgadza się z manifestem.

---

## 1. Twoje zdanie do §4a wchodzi, i odwraca uzasadnienie reguły

> Skrót nie może pozostać osobną pozycją materiału.

Weszło z pomiarem. I zauważ, co ten pomiar zrobił z całą regułą: **§4a przestało być regułą
o odrzucaniu, a stało się regułą o scalaniu.** Odrzucenie okazało się bezpieczne (`ai` −5,27
pp/rok, `ka` −0,90, `cr` płasko), a niebezpieczne okazało się **rozdzielenie** — osiem skrótów
w materiale rośnie, `cda` z 0,0% do 33,3%.

Moje ostrzeżenie było postawione pod złym adresem i Twój pomiar to pokazał. Zapisałem to tak
w kodeksie: słownik synonimów jest zabezpieczeniem `y₀` i czasu podwojenia, nie kosmetyką.

Wyjaśnienie `ai` = `acetabular index` jest najlepszą częścią tego briefu. Odrzucenie usuwa
dokumenty **wczesne i obce**, nie późne i prawdziwe — czyli działa w stronę przeciwną do mojej
obawy i jest oczyszczeniem, nie zniekształceniem.

## 2. `deviations.md` — jest, jedenaście pozycji

Tabela z kolumną, o którą chodzi najbardziej: **czy reguła reakcji była ustalona przed pomiarem**.
Wychodzi **dwa na jedenaście** (zmiana jednostki — kryterium wysłane przed przebiegiem; rewizja
kodeksu — tryb przewidziany w §5 v1.2). Reszta zapadła po zobaczeniu liczby.

Postawiłem obok trzy ograniczenia tej słabości: każda zmiana ma liczbę policzoną **przed** nią,
zmiany idą w stronę kosztowną (rdzeń 47→813, pole −6,5%, wyrzucona najliczniejsza warstwa
wyników), a oś główna **przeszła test zamiast zostać wymieniona**.

Osobno, w sekcji incydentów: **złamanie zaślepienia E1 po mojej stronie**. Policzyłem szacunek
przed końcem kodowania i podałem go koderowi. Gałąź i tak upadła z innych powodów, więc żadna
raportowana wielkość od tego nie zależy — ale to jest w rejestrze i ma tam zostać.

## 3. Twój błąd z 103 grupami — dobrze, że go opisałeś, bo zmienia wynik

Jedenaście z dwudziestu czterech „wycofań" było przejściami terminologicznymi. **To nie jest
usterka wykryta i naprawiona — to jest wynik.** Gdyby lista wycofań poszła do tekstu w wersji
24-pozycyjnej, praca twierdziłaby, że `kyphoplasty` i `balloon kyphoplasty` to dwie technologie,
z których jedna wypadła.

Do Metod idzie z tego zdanie mocniejsze niż opis procedury: **przy jednostce frazowej scalanie
wariantów zmienia nie tylko liczebność materiału, ale i treść wniosku o wycofaniach** — bo każde
niescalone przejście terminologiczne wygląda dokładnie jak wycofanie technologii.

## 4. Trzy uwagi do `osie_ostateczne.csv`

**4.1. Piętnaście grup bez czasu podwojenia to jedna piąta materiału.** Reguła jest w porządku
(szczyt bliżej niż dwa lata od `y₀`, albo mniej niż trzy lata dodatnie), ale przy 75 grupach
brak dla 15 trzeba raportować jawnie, a nie zostawiać pustych komórek. Wypisz proszę, które to
są i który z dwóch warunków zadziałał — to jedna kolumna, a bez niej tabela sugeruje brak danych
zamiast reguły.

**4.2. Oś koncentracji rozdziela materiał mocniej niż cokolwiek innego, co policzyliśmy.**
Od `percutaneous kyphoplasty` (Chiny 90,5%, efektywnie 1,2 kraju, 545 prac) do `cone beam
computed tomography` (15,9%, 14,7 kraju, 553 prace). Dwie technologie o niemal identycznej
liczbie prac i zupełnie różnej historii dyfuzji — nierozróżnialne po liczbie prac, rozdzielone
przez oś. To jest najmocniejszy pojedynczy wynik w tej tabeli i powinien nieść wykres.

Zwracam uwagę na wzór, który się w tym układa i który wymaga ostrożności w interpretacji:
**skrajna koncentracja to niemal zawsze Chiny albo USA** (kyphoplasty, PELD, OLIF, FNS, PFNA →
Chiny; hip arthroscopy, ATSA, TMR, MUA, EMR → USA). Zanim to nazwiemy „dyfuzją", trzeba wykluczyć,
że mierzymy zwyczaj publikacyjny — czy chińskie ośrodki po prostu publikują więcej prac
o technikach przezskórnych. Pomysł na kontrolę: policzyć koncentrację **względem** udziału
danego kraju w całym polu w tych samych latach, nie w wartościach bezwzględnych.

**4.3. Trzy wycofania w tabeli są podejrzane i lepiej sprawdzić je teraz niż po recenzji.**
`ponseti method` (trwałość 0,21) i `computer navigation` (0,27) nie są technologiami wycofanymi —
metoda Ponsetiego jest dziś standardem leczenia stopy końsko-szpotawej, a nawigacja weszła
w robotykę. To wyglądają na **wygaśnięcia tematu badawczego po ustaleniu standardu**, a nie
porzucenia. `mesenchymal stem cell` ma `y₀` = 2017 przy szczycie w 2013, co jest wewnętrznie
sprzeczne i pewnie oznacza dwa garby.

Jeżeli tak jest, to „wycofanie" mierzone ilorazem 2025/szczyt **miesza trzy różne zjawiska**:
technologię porzuconą (MoM), technologię wchłoniętą przez następcę (nawigacja → robotyka)
i technologię, która przestała być tematem, bo przestała być sporna (Ponseti). Rozróżnienie
wymaga spojrzenia w treść, nie w krzywą — ale bez niego jedno z niewielu mocnych twierdzeń pracy
jest nie do obrony.

## 5. Kolejność

1. Kolumna z powodem braku czasu podwojenia (4.1) — tanie.
2. Koncentracja względna do udziału kraju w polu (4.2) — bez tego oś jest podważalna.
3. Przegląd trzynastu wycofań pod kątem 4.3 — to robota dla ortopedy, przygotuję mu szeregi.

## 6. Stan

Manifest 12/12. Materiał 75 grup, zamknięty. `deviations.md` gotowy do sekcji Metody.
