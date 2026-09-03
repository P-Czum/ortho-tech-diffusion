# Materiał 66 policzony. **Ale gradient z wczoraj upada — zostaje podział binarny**

Autor: sesja VS Code, 2026-09-03. Dotyczy: `brief_dla_vsc_material_66_2026-09-03.md`
oraz **korekty własnego wyniku** z `brief_dla_cowork_gradient_dowodow_2026-09-03.md`.

Wyniki: `data/processed/osie_66.csv` (66 grup), `wycofania_66.csv` (12),
`trwalosc_wzgledna.csv`.

**Najważniejsze najpierw: pięciostopniowy gradient stanu dowodów, który wczoraj podałem jako
wynik główny, nie przeżył właściwego pomiaru. Zostaje z niego podział binarny.**

---

## 1. Błąd, który wychwycił ortopeda: okno kalendarzowe zamiast cyklu życia

Trwałość liczyłem w oknie **kalendarzowym** (2021–22 i 2023–25). Ortopeda zapytał, czemu jedno
okno dla wszystkich — przecież każda technologia jest w innym punkcie swojego cyklu.

Ma rację i to unieważnia porównanie. Technologia ze szczytem w 2007 mierzona w latach 2021–22
jest **czternaście lat** po szczycie; ta ze szczytem w 2020 — **dwa**. Nazywałem to jedną miarą.
Stąd brało się to, co raportowałem jako zagadkę: separacja w oknie 2021–22 i jej brak w 2023–25.

Poprawnie: trwałość **względem szczytu każdej technologii z osobna**, w oknach +1..3, +3..5
i +5..7 lat po jej własnym szczycie. Wszystkie 12 zaników ma szczyt ≤ 2020, więc da się to
policzyć dla każdej.

## 2. Co przeżyło, a co nie

| okno wobec szczytu | **odrzucona** (n=2) | **nieodrzucona** (n=10) |
|---|---|---|
| +1..3 lata | **0,27–0,48** | 0,50–0,87 |
| +3..5 lat | **0,17–0,25** | 0,35–0,73 |
| +5..7 lat | **0,11–0,17** | 0,26–0,72 |

**Przeżyło jedno rozgraniczenie: odrzucona kontra nieodrzucona.** Rozdziela się czysto we
wszystkich trzech oknach — technologia z dowodami przeciw spada najgłębiej i najszybciej,
niezależnie od momentu pomiaru.

**Nie przeżyła reszta gradientu.** W oknie +3..5 „brak dowodów" rozciąga się na 0,35–0,73
i pokrywa całe pasmo rutyny (0,42–0,63). Uporządkowanie pięciu pasm było po części artefaktem
porównywania różnych punktów cyklu.

Do Wyników idzie więc twierdzenie słabsze i prawdziwe: **piśmiennictwo odróżnia technologię
odrzuconą od nieodrzuconej; dalszych stopni nie odróżnia.** Przy dwóch przypadkach po stronie
odrzuconych nawet to jest obserwacją, nie regułą.

Dwie rzeczy potwierdzają przy okazji rozstrzygnięcia merytoryczne: `mesenchymal stem cell` ma
w oknie +3..5 wartość **0,73**, najwyższą z dwunastki — praktycznie nie opada względem własnego
szczytu, co pasuje do „tematu wracającego". `computer navigation` **0,66**, zgodnie z wchłonięciem
zamiast porzucenia.

## 3. Konsekwencja D8, o której nie wspomniałeś

`single bundle` był **retronimem**, więc wypada z materiału słusznie. Ale był też jednym
z dwóch członów klasy „warianty jednej metody, bez zwycięzcy", a ta klasa opierała się na
znaczniku „oba człony pary opadają jednocześnie".

**Para nigdy nie była dwoma rywalami o symetrycznych losach** — była techniką i nazwą ukutą dla
starego sposobu, gdy pojawił się nowy. Klasa upada, a `double bundle reconstruction` przepisane
na: **technika, wobec której ukuto retronim**.

To jest zresztą ciekawsze niż poprzednia etykieta, bo pokazuje zjawisko, o którym jest cała
praca — powstanie nazwy z powodu pojawienia się rywala — **wewnątrz listy zaników**.

## 4. Zliczenia z §3 briefu

| | |
|---|---|
| `y₀` po dekadach | 2000–09: **11**, 2010–19: **42**, 2020–25: **13** |
| `kraj_eff_n ≤ 2,5` | **13 grup** — Chiny 7, USA 6; **nadal wyłącznie te dwa kraje** |
| `kraj_eff_n ≥ 9` | **12 grup** |
| bez czasu podwojenia | **11** — szczyt < 2 lata po `y₀`: 8, nachylenie niedodatnie: 3 |
| szczyt w 2025 | **19 grup**, blisko jedna trzecia wciąż rośnie |

Kontrola: trwałości pozostałych grup są **identyczne** co w przebiegu na 76 (maksymalna różnica
0,0000), więc usunięcie dziesiątki nie ruszyło reszty.

## 5. `arcr` — liczby do decyzji ortopedy

`y₀` 2017, **466 prac**, prevalence 0,422%, USA 44% przy tle 27,4% — nadreprezentacja **1,6×**,
najniższa spośród wyłączanych. Czas podwojenia 3,9 roku.

Z 466 pracami byłaby to pozycja z górnej połowy materiału. Wyłączenie jako generyku jest
obronne, ale warto, żeby ortopeda zobaczył tę liczebność. Twoja uwaga w `scoping_log`, że
artroskopowa naprawa stożka mogła w latach 2010. być realnym przesunięciem kosztem naprawy
otwartej, jest sprawdzalna — gdyby naprawa otwarta była w rdzeniu i opadała, byłaby to para
zastąpienia. **Nie sprawdzam, bo prosiłeś, żeby nie dokładać analiz.**

## 6. Kontrole

Materiał **66**. Zaniki **12**. Manifest **12/12**. Słownik synonimów i klasyfikacja nietknięte.
