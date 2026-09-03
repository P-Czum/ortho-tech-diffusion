# Osiem mechanizmów zastąpione jednym gradientem. Plus cztery korekty własne i dwa nowe ograniczenia

Autor: sesja VS Code, 2026-09-03. **Brief nadrabiający — wszystko poniżej powstało po
`brief_dla_cowork_mechanizmy_wycofan_2026-09-02.md` i nic z tego do Was nie poszło.**

Jeżeli piszecie cokolwiek na ośmiu mechanizmach z tamtego briefu, jest nieaktualne: zostały
zastąpione ramą prostszą i lepiej rozdzielającą.

---

## 1. Wynik główny: spadek uwagi ma przyczynę w **stanie pytania**, nie w losie technologii

Rama Przemka. Budowaliśmy taksonomię od strony technologii — co się z nią stało, czy miała
rywala, czy została wchłonięta. Stąd osiem klas, które zachodziły na siebie wszędzie, bo mieszały
wymiar epistemiczny (czy wiadomo) ze strukturalnym (czy była para).

Odwrócone pytanie: **skoro mierzymy uwagę, to jej spadek bierze się z tego, że pytanie się
zamknęło — a pytanie zamyka się na trzy sposoby.**

| | przyczyna spadku uwagi | n | zakres trwałości 2021–22 |
|---|---|---:|---|
| 1 | **dowody PRZECIW stosowaniu** | 2 | **0,10–0,17** |
| 2 | dowody ZA alternatywą (względnie przeciw tej) | 1 | 0,23 |
| 3 | **BRAK przekonujących dowodów** | 6 | **0,20–0,39** |
| 4 | dowody ZA + dalszy rozwój (wchłonięcie) | 1 | 0,39 |
| 5 | **dowody ZA + rutyna** | 3 | **0,43–0,61** |

**Trzy główne stany nie zachodzą na siebie.** 0,17 kończy pierwszy, 0,20 zaczyna trzeci;
0,39 kończy trzeci, 0,43 zaczyna piąty.

**Wykładnia sama się tłumaczy:** gdy dowody mówią „nie", piśmiennictwo umiera, bo nie ma czego
badać. Gdy pytanie zostaje otwarte, tli się sporadycznymi próbami. Gdy dowody mówią „tak",
technologia wchodzi do rutyny i generuje stały strumień prac — rejestry, serie, długie
obserwacje — więc uwaga opada najmniej.

**Wchłonięcie przestało być wyjątkiem.** Nawigacja też jest napędzana dowodami „za" — tylko po
przyjęciu przyszedł dalszy rozwój i technologia weszła w następcę. Siedzi między brakiem
rozstrzygnięcia a rutyną, bo część jej nazwy przeszła na robotykę. Schemat tłumaczy teraz
wszystkie trzynaście pozycji jedną zasadą, zamiast dwunastu i jednej osobno.

**Zastrzeżenie do napisania razem z wynikiem:** n = 2, 1, 6, 1, 3. Uporządkowanie jest czyste
i wykładnia spójna, ale to hipoteza na trzynastu przypadkach — postawiona tak, że da się ją
obalić na nowym materiale, i tak trzeba ją przedstawić.

## 2. Cztery korekty, które musiałem zrobić na sobie

**2.1. Kolumna koncentracji względnej — wycofana.** „Efektywna liczba krajów ważona
nadreprezentacją" miała wagę `udział × nadreprezentacja` = `p²/p_tła`, czyli kwadrat udziału
obserwowanego. Mierzyła koncentrację podwójnie ważoną, nie względną, i zbiegała do 1,0. Nazwa
obiecywała co innego niż liczba robiła. Usunięta, powód w komentarzu w kodzie.

**2.2. „Odpływ badań podstawowych z pola" przy chondrocytach — błędny.** Twierdziłem, że działa
ten sam mechanizm co przy komórkach mezenchymalnych. Test dojrzewania to obalił:

| | 2000–09 | 2021–25 |
|---|---:|---:|
| ACI, prace kliniczne | 53% | 55% |
| microfracture, prace kliniczne | 55% | 73% |
| **MSC, prace kliniczne** | **10%** | **41%** |

ACI i mikrozłamania były **kliniczne od początku okna**. Odpływ podstawowych pasuje wyłącznie
do MSC.

**2.3. „Szczyt współwystępowania jako sygnatura zastąpienia" — artefakt mianownika.** Pisałem,
że blokady mają szczyt 33% w 2016 i spadek do 3%. Liczyłem udział w pracach **następcy**,
a następca rósł. Przy mianowniku symetrycznym blokady mają 33/46/31/24% — wysoko i stabilnie.
**Współwystępowanie nie odróżnia zastąpienia od nierozstrzygniętej rywalizacji.**

**2.4. Nazwy klas twierdziły o praktyce.** „Spór dwóch, jedna wygrywa" — nic nie wygrało
klinicznie: blokada udowa jest nadal stosowana, **54 prace w 2022–2025 wobec 105 o blokadzie
kanału**. Przesunęła się proporcja uwagi. Wszystkie nazwy przepisane na opis uwagi; jedyny
wyjątek to „wycofanie z praktyki" (MoM, resurfacing), gdzie twierdzenie ma oparcie zewnętrzne
i jest oznaczone kolumną `poziom`.

**Cztery razy w jednej sesji przebrałem obserwację o piśmiennictwie za wniosek o medycynie,
i cztery razy korekta przyszła od ortopedy, nie z mojej kontroli.** To nie jest seria przeoczeń,
tylko systematyczna skłonność. Proponuję zdanie do Metod jako zasadę, a nie jako siedem
ostrożności przy siedmiu pozycjach: **pomiar pokazuje wzorzec uwagi, rozstrzyga rzecz.**

## 3. Współwystępowanie po korekcie na przypadek — jedna rzecz, którą ta miara robi dobrze

Pytanie Przemka: czy różnica nie bierze się z liczby prac. Sprawdzone przez porównanie
obserwacji z oczekiwaniem `nA × nB / pole` — i **odwrócone**: pęczki mają **mniej** prac niż
chrząstka (145/139 wobec 388/402), a wyższą krotność. Liczebność tę różnicę maskowała.

| para | oba | oczekiwane | krotność | w oknie 2014–21 |
|---|---:|---:|---:|---:|
| pęczki (warianty jednej metody) | 34 | 0,07 | **458×** | 473× |
| blokady (metody alternatywne) | 67 | 0,39 | 170× | 154× |
| chrząstka (metody alternatywne) | 53 | 0,57 | 92× | 82× |
| nawigacja/robotyka (wchłonięcie) | 9 | 0,76 | **12×** | 12× |

Stabilne w dwóch niezależnych oknach. **Miara odróżnia wyłącznie wchłonięcie od reszty** — bo
składnik wchłonięty przestaje być nazywany. Rywalizacji od zastąpienia nie odróżnia (§2.3).

Rozróżnienie merytoryczne postawił Przemek i ono jest pierwotne: **pęczki to warianty jednej
operacji** (dychotomia albo/albo), **mikrozłamania i chondrocyty to dwie odrębne metody**
wybierane wedle wskazania. Warianty muszą być porównywane head-to-head, bo randomizuje się
chorych do tej samej operacji wykonanej dwojako — stąd 458×. Liczba potwierdza rozstrzygnięcie,
nie zastępuje go.

## 4. Dwa nowe ograniczenia

**4.1. Uwaga miesza wartość kliniczną z dostępnością.** ACI jest kosztowne, regulowane jako
produkt leczniczy i wykonywane w nielicznych ośrodkach; mikrozłamania robi każdy artroskopista.
Przy równej skuteczności ACI i tak generowałoby mniej prac — i faktycznie ma trwałość 0,13 wobec
0,43, choć obie techniki są w użyciu. **Dotyczy każdej kosztownej albo skoncentrowanej
technologii, więc łączy się bezpośrednio z osią koncentracji.**

**4.2. Odpływ tematu z pola jest nieodróżnialny od zaniku tematu.** Przy definicji pola przez
poddrzewo MeSH widzimy tylko jego wnętrze. Krzywa wygląda tak samo, gdy technologia przestaje
być badana i gdy jest badana gdzie indziej. Dotyczy co najmniej MSC (31% prac usuwa D6 jako
zwierzęce, a udział klinicznych rośnie z 10% do 41%).

## 5. Pęczki ACL — rozstrzygnięte z korpusu, wbrew temu, co pisałem

Odłożyłem je jako wymagające wytycznych. Korpus jednak odpowiada: **spór nie wygasł.**
Współwystępowanie single/double utrzymuje się na 20–38% do 2025, a recentne tytuły to nadal
porównania i metaanalizy. Równocześnie rosną `lateral extra articular tenodesis` (6→146 prac)
i `anterolateral ligament` (8→77) — **obserwacja współbieżna; nie ustalono, czy pęczki zostały
przez nie wyparte**, i tak jest zapisane.

## 6. Stan

Manifest **12/12**. Materiał **76 grup** (FEA przywrócone decyzją Przemka). Trzynaście zaników
z przyczyną, klasą, poziomem i adnotacją: `data/processed/wycofania_mechanizmy.csv`.

Po stronie liczenia nie zostało nic otwartego.
