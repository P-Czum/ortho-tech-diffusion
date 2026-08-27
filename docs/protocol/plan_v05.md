# Wschodzące trendy w ortopedii i ich siła — plan v0.5
2026-08-26 · Przemysław Czuma · zastępuje v0.4

---

## Pytanie

W piśmiennictwie ortopedii zabiegowej 2005–2025:

1. **Co wschodzi** — które pojęcia rosną szybciej niż samo pole?
2. **Jak silne jest wschodzenie** — jak szeroko, jak szybko, jak wysoko?
3. **Czy to nowość, czy nowa nazwa starej rzeczy?**

Pytanie trzecie jest sednem. Sześćdziesiąt dziewięć znalezionych prac pokazuje mapy „burstów"
i nazywa je emerging trends, nie sprawdzając ani razu, czy wykryty termin oznacza nową
technologię, czy zmianę słownictwa wokół starej. To jest luka, którą zajmujemy.

Mierzymy **uwagę naukową**, nie adopcję kliniczną.

## Dane i pole

PubMed Baseline 2026 + updatefiles, lustro lokalne, po deduplikacji (`analytic_index`).
Pole: `Orthopedic Procedures` + potomne deskryptory MeSH (56, rozwijane z `desc2026.xml`).
Lata 2005–2025; 2026 poza analizą jako niekompletny.

Mianownikiem jest pole. Każda miara to **udział w polu w danym roku**, nie liczba bezwzględna —
inaczej mierzymy wzrost ortopedii, nie wschodzenie pojęcia.

## Jednostka: termin

N-gramy 1–3 z tytułu i streszczenia, po normalizacji do małych liter i usunięciu stoplisty.
Próg wejścia: minimum 50 wystąpień w całym okresie — poniżej tego udziały są szumem.

Termin, nie klaster. Klastry osadzeń są mniej stabilne i trudniejsze do zweryfikowania ręcznie,
a cała wartość tej pracy leży w tym, że każde wykrycie da się obejrzeć i osądzić.

## Detekcja

Dla każdego terminu liczymy roczny szereg udziałów. Kandydat na wschodzący to termin, którego
udział w ostatnim pięcioleciu przewyższa udział w pierwszym o zadany próg, przy zachowanym
progu liczebności bezwzględnej.

**Świadomie nie używamy algorytmu Kleinberga.** Jest standardem w tej literaturze, ale ma
parametry, których nie da się zwalidować, a wyniki mocno się po nich przesuwają. Reguła
progowa jest gorsza teoretycznie i lepsza praktycznie: czytelnik może ją przeliczyć ręcznie
i sprawdzić nasze liczby. Detektor i progi są **preregistrowane przed analizą** — preregistrujemy
narzędzie, nie wynik, bo to jest badanie odkrywcze.

## Siła — trzy wymiary, raportowane osobno

**Szerokość adopcji.** Liczba różnych pierwszych autorów, ośrodków, czasopism i krajów
używających terminu, oraz **koncentracja**: jaki odsetek prac o danym terminie pochodzi
od jednego najpłodniejszego autora i z jednego kraju.

To jest wymiar rozstrzygający. Termin może rosnąć, bo jedna grupa opublikowała serię dwudziestu
prac — udział rośnie, krzywa wygląda jak dyfuzja, a to jest dorobek jednego laboratorium.
Szerokość oddziela trend od produktywności.

**Tempo wzrostu.** Nachylenie udziału w fazie wzrostu, czas podwojenia.

**Osiągnięty pułap.** Maksymalny roczny udział w polu.

Bez wskaźnika złożonego. Trzy liczby obok siebie są uczciwsze niż jedna, w której wagi
byłyby dobrane przez nas.

Dodatkowo, opisowo: **trwałość** — czy udział się utrzymuje, czy opada. Nie jest składnikiem
siły, ale odróżnia modę od zmiany i czytelnik o to zapyta.

## Osąd: nowość czy przemianowanie

Dla pięćdziesięciu najsilniejszych terminów szukamy **kandydata na poprzednika**: terminu,
którego udział opada w tym samym okresie i który **współwystępuje** z kandydatem w pracach
z lat przejściowych. Przemianowanie ma charakterystyczny kształt — stary termin wysoko i opada,
nowy rośnie, a przez kilka lat oba pojawiają się w tych samych pracach, bo autorzy piszą
„rapid prototyping (3D printing)".

Statystyka podaje kandydatów; **rozstrzygnięcie jest ręczne**, na podstawie przeczytanych prac
z lat przejściowych. Cztery kategorie: nowość · przemianowanie · artefakt indeksowania ·
termin niebędący technologią (metoda statystyczna, typ badania).

Kodowanie według spisanego kodeksu, podpróba kodowana niezależnie przez drugą osobę, zgodność κ.
**To jest walidacyjny rdzeń pracy, nie dodatek.**

## Produkt

1. Tabela pięćdziesięciu najsilniejszych terminów: rok początku, pułap, tempo, szerokość,
   koncentracja, trwałość, kategoria osądu.
2. Krzywe udziału dziesięciu najsilniejszych.
3. Rycina par przemianowań — stary termin opada, nowy rośnie, okno współwystępowania.
4. Diagram przepływu rekordów i terminów.

Pięć nazwanych rodzin technologii (druk 3D, robotyka, nawigacja, AI, biomateriały) wchodzi
jako **podświetlone wiersze** w tabeli — porównanie z planu v0.4 jest tu zawarte, nie utracone.

## Etap 1 — brama

Pole, lata, szereg udziałów, detektor, lista kandydatów. Bez osądu, bez kodowania, bez ryciny par.

**Jeśli lista kandydatów okaże się zdominowana przez terminy niebędące technologiami i artefakty
indeksowania, albo jeśli żaden kandydat nie przekracza progu liczebności — pracy nie ma.**
Zapisane przed danymi.

## Poza tą pracą

Klastrowanie osadzeń, lead–lag preprintów medRxiv, odtworzenie opublikowanych zapytań
z literatury, uogólnienie detektora na inne specjalności. Każde dokłada drugie pytanie.
