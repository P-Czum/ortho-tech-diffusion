# Systematyczny test na obcą dziedzinę — wykonany, materiał czysty

Autor: sesja VS Code, 2026-09-03. Zamyka ograniczenie nazwane w §3
`brief_dla_vsc_d6_i_skroty_RESPONSE_2026-09-02.md`: *„nie mamy systematycznego testu na obcą
dziedzinę, tylko serię wykryć ad hoc"*.

Skrypt: `code/audyt_skazenia.py`. Wynik: `data/processed/audyt_skazenia.csv`.

---

## 1. Po co, skoro reguły już działają

D4, D5a, D5c i D6 wyłączają **rekordy**, i to tylko przypadki skrajne — D5a wymaga, żeby
**wszystkie** deskryptory pola rekordu były stomatologiczne. Technologia może więc być czysta
wobec reguł, a mimo to w większości opisywać inną dziedzinę.

Dokładnie tak było z CBCT: przeszło wszystkie filtry i miało **82,5%** prac stomatologicznych.
Wyszło to dopiero wtedy, gdy zgadliście, że warto sprawdzić akurat tę pozycję. Cztery wycieki
znaleziono czterema niezaplanowanymi drogami — to jest ta słabość, którą sami opisaliście.

Test liczy dla **każdej** pozycji materiału udział dokumentów niosących deskryptory obcych
dziedzin, po prefiksach drzew MeSH.

## 2. Błąd konstrukcji, który sam popełniłem i poprawiam

W pierwszym przebiegu wpisałem na listę dziedzin obcych **C10 (układ nerwowy)** i **C04
(nowotwory)**. To był błąd: dla ortopedii nie są obce.

Dał trzy fałszywe alarmy: `targeted muscle reinnervation` 46,6% „nerwowy" — a TMR **z definicji**
polega na przeszczepieniu nerwów do mięśni po amputacji; `anterior cervical discectomy fusion`
26,5% — ACDF leczy mielopatię i radikulopatię, więc deskryptory rdzenia są wskazaniem;
`vertebral augmentation` 15,7% „nowotwory" — złamania patologiczne w przerzutach to wskazanie
do wertebroplastyki.

Lista właściwa: **stomatologia (A14, C07, E06, E04.545), układ trawienny (C06), moczowo-płciowy
(C12), oko (C11)** — czyli dokładnie te dziedziny, wobec których reguły D5a i D5c były pisane.

## 3. Wynik

| | |
|---|---|
| powyżej 20% obcej dziedziny | **0 z 60** |
| powyżej 10% | **1 z 60** — `mimic software` 11,5% stomatologii, poniżej Waszego progu |
| mediana | **0,6%** |
| maksimum | 11,5% |

Czoło listy: `mimic software` 11,5%, `3d printing` 8,2%, `finite element analysis` 7,7%,
`mesenchymal stem cell` 7,4%, `augmented reality` 6,1% — wszystkie stomatologia, wszystkie
poniżej progu.

**Po usunięciu CBCT materiał nie ma pozycji zdominowanej przez obcą dziedzinę.**

## 4. Kontrola D6 przy okazji

Udział prac zwierzęcych (Animals bez Humans): **0,0% w każdej z 60 grup, bez wyjątku.**
Nie „niski" — dokładnie zero. Reguła D6 usunęła całość, a nie większość.

To jest też odpowiedź na pytanie, czy TPLO było przypadkiem odosobnionym: po D6 nie ma w materiale
ani jednej pozycji z resztkowym udziałem weterynaryjnym.

## 5. Co to zmienia w Ograniczeniach

Zdanie *„nie mamy systematycznego testu na obcą dziedzinę"* przestaje być prawdziwe i można je
zastąpić mocniejszym: **test wykonano na całym materiale, żadna pozycja nie przekracza progu,
mediana wynosi 0,6%.**

Zostaje uczciwe zastrzeżenie: test wykrywa dziedziny, o których pomyśleliśmy. Cztery wycieki
znaleziono ad hoc i dopiero wtedy powstała lista prefiksów. **Dziedzina, której nikt nie
podejrzewał, nadal by przeszła** — z tą różnicą, że teraz wystarczy dopisać jeden prefiks
i przeliczyć w trzy minuty, zamiast zgadywać pozycję po pozycji.

## 6. Stan

Materiał **60**, nietknięty — audyt niczego nie wyłącza, tylko mierzy. Manifest **12/12**.
