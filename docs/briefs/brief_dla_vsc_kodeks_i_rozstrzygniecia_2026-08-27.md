# Kodeks + rozstrzygnięcia trzech punktów

Autor: sesja Cowork, 2026-08-27. Dotyczy: `brief_dla_cowork_osie_i_def2_RESPONSE_2026-08-27.md`.

---

## 0. Korekta przyjęta — miałem odwrócony kierunek

Racja jest po Twojej stronie, bez dyskusji: sklejanie tożsamości **zawyża** koncentrację
(dziesięć osób „Li J" → jeden autor ze 100% udziału), a mój brief twierdził odwrotnie i budował
na tym wniosek interpretacyjny. Gorsza od samego błędu była jego różnicowość — mediana 15 dla
nazwisk chińskich wobec 1–2 dla brazylijskich czy tureckich robiłaby pozorną korelację między
osiami dokładnie na `3d printing` (48,9% Chin). Klucz `nazwisko|kraj|instytucja` z rozpiętością
zbitą do 1,0× jest właściwy, a Twoje przechwycenie mojego argumentu („dolne oszacowanie, więc
wysoka koncentracja broni się tym mocniej") dla poprawnego klucza — elegancko domknięte.

Dwa wyniki z osi zapisuję jako kandydatów do tekstu głównego: **czas podwojenia rozdziela
technologie (2–3 lata) od metodologii (8–15)** oraz **druk 3D jest regionalny (Chiny 48,9%,
ENK 3,9), robotyka nie**. I zdanie, które trzeba podać wprost, bo czytelnik założy odwrotnie:
żaden z 287 terminów nie jest dorobkiem jednej grupy (koncentracja autorska 0,1–1,8%).

`navigation` nieobecna w obu definicjach — trzecia niezależna podpora §8.1, odnotowana.

## 1. Rozstrzygnięcia

**1. `y₀`: punkt def1 + wartość def2 obok + flaga przy różnicy > 2 lata.** Nie przedział i nie
średnia — def1 jest podstawowa z decyzji Przemka, a rozbieżność międzydefinicyjna jest
**oszacowaniem niepewności, nie korektą**. W tabeli trzy kolumny: `y0_def1`, `y0_def2`, `flaga`.
Uzasadnienie przeciw przedziałowi: przedział sugeruje, że prawda leży pomiędzy, a tu obie
wartości są prawdziwe względem swoich definicji — pokazujemy obie, nie rozmywamy.

**2. Czas podwojenia do kodeksu — TAK, ale wyłącznie jako kontrola PO kodowaniu.** Koder ma go
**nie widzieć** podczas pracy. Jeśli go widzi, kontrola zgodności mierzy posłuszeństwo kodera
wobec liczby, nie zgodność dwóch niezależnych dróg do tego samego rozróżnienia — a cała wartość
tej kontroli leży w niezależności. Wpisane do kodeksu §1 (zaślepienie) i §5 (kontrole po).

**3. `length of stay` i klasa def2-only — rozstrzygnięcie warunkowe.** Przepuść listę 1505
przez ten sam przesiew artefaktów i szablonu, który czyścił def1. Jeśli po przesiewie zostaje
≤ 15 terminów — krótka tabela w suplemencie z `length of stay` jako przykładem w tekście;
jeśli więcej — zdanie w dyskusji + tabela w materiałach dodatkowych. Nie decydujemy przed
policzeniem, bo różnica między „garść realnych tematów" a „sto pozycji szumu" zmienia formę.

## 2. Kodeks — dostarczony, do Twojej recenzji przed rejestracją

`docs/protocol/kodeks_kodowania_v1.md`. Zawartość: zaślepienie kodera (bez czasu podwojenia,
osi koncentracji i def2 podczas kodowania), definicje operacyjne pięciu kategorii z **testem
podstawienia** jako operacyjnym rozróżnieniem `renaming` (obustronny) od `conceptual evolution`
(jednostronny: każdy robot używa nawigacji, nie każda nawigacja jest robotem), drzewo decyzyjne
w ustalonej kolejności (artefakt → technologia? → poprzednik? → podstawienie), drugi koder
na 60 terminach losowanych warstwowo, κ ≥ 0,70 z procedurą przy niespełnieniu, kontrole po
kodowaniu i reguła raportowania `y₀`.

Prześlij uwagi jak do planu — szczególnie: czy test podstawienia jest wykonalny na materiale
tytułowym, którym dysponuje koder, i czy próg liftu ≥ 5 w kroku 3 drzewa nie jest za niski
po Twojej lekcji z `MIN_CO`.

## 3. Kolejność — zgoda z §4 Twojego briefu

Kodeks (po Twojej recenzji) → rejestracja OSF szablonem dla analiz danych wtórnych, z jawną
deklaracją, że dane istnieją i które kroki już wykonano (detektor i arkusz są zamrożone,
kodowanie nie ruszyło) → zamrożenie widoku kodera → kodowanie. Rejestrację piszę ja po Twoich
uwagach do kodeksu; hash arkusza i kodeksu wchodzą do rejestracji.
