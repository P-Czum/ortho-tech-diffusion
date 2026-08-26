# Prace pokrewne i luka do zagospodarowania

Rozpoznanie: 2026-08-25. Materiał do sekcji „wprowadzenie" i „ograniczenia dotychczasowych badań".

## 1. Gatunek jest zajęty i przepełniony

Analizy bibliometryczne pojedynczych technologii w ortopedii to obecnie osobny, bardzo płodny
gatunek. Tylko w 2025–2026 r. ukazały się m.in.: robotyka ortopedyczna („hotspots and emerging
trends"), robotyka w chirurgii kręgosłupa, roboty w ortopedii urazowej, robot-assisted
arthroplasty (CiteSpace), top-100 najczęściej cytowanych przeglądów o robotyce, AI w ortopedii
(co najmniej trzy niezależne prace), druk 3D w chirurgii, druk 3D w chirurgii kręgosłupa,
druk 3D i PSI w resekcjach guzów narządu ruchu, oraz **druk 3D w ortopedii i traumatologii**.

**Wniosek praktyczny: prosta praca „bibliometria druku 3D w ortopedii" jest już zajęta.**
Powtórzenie jej nie ma sensu.

## 2. Jak te prace wyglądają — dwa zbadane przykłady

**AI w ortopedii (JMDH 2025, PubMed).** Zapytanie: `(artificial intelligence[topic]) AND
(orthopedics[topic])`, lata 2010–2024, **112 rekordów**, R + Bibliometrix. Analizy: liczba prac
na rok, cytowania, prawo Lotki, kraje i instytucje, współwystępowanie słów kluczowych, mapy
ko-cytowań, mapy tematyczne Callona. Brak normalizacji, brak walidacji zapytania, brak modelu
trendu. Ograniczenia własnymi słowami autorów: *„may not have captured all relevant articles due
to variations in terminology and indexing practices"*.

**Robotyka ortopedyczna (J Robot Surg 2025, Web of Science).** Lata 2005–2024, **820 rekordów**,
tylko artykuły i przeglądy, **tylko angielski**. VOSviewer + CiteSpace + Scimago Graphica.
Analizy: liczba prac na rok, sieci współpracy, klastry słów kluczowych, oś czasu, detekcja
„burstów". Brak normalizacji, brak walidacji, brak modelu trendu. Ograniczenia: wyłącznie WoSCC
i uwaga, że bibliometria mówi „co" i „kiedy", ale nie „dlaczego".

## 3. Mocne strony gatunku

- Dane cytowaniowe, których MEDLINE nie ma — pozwalają mówić o wpływie, nie tylko o objętości.
- Dojrzałe, powtarzalne narzędzia (VOSviewer, CiteSpace, Bibliometrix) i rozpoznawalny format.
- Szybkie i dobrze przyjmowane przez czasopisma kliniczne.
- Mapy współwystępowania faktycznie pokazują strukturę tematyczną pola.

## 4. Powtarzalne słabości

1. **Brak mianownika.** Liczby bezwzględne rosną, bo rośnie baza i rośnie pole. Bez udziału nie
   da się odróżnić dyfuzji technologii od wzrostu piśmiennictwa.
2. **Niewalidowane zapytania.** 112 rekordów na całą AI w ortopedii za 15 lat to nie jest
   oszacowanie, to awaria czułości rzędu wielkości. Żadna z obejrzanych prac nie raportuje
   precyzji ani czułości.
3. **Brak niezmienniczości pomiaru w czasie.** Dryf terminologii bywa wymieniony w ograniczeniach,
   nigdy nie jest zaadresowany w metodach.
4. **Opis zamiast wnioskowania.** „Hotspots and emerging trends" pochodzą z map współwystępowania,
   które nie mają testowalnej hipotezy. Brak modeli punktów zmiany.
5. **Jedna technologia na pracę.** Uniemożliwia jakiekolwiek porównanie — nie da się dziś
   powiedzieć, czy robotyka dyfundowała szybciej niż druk 3D, bo nikt nie liczył ich na wspólnym
   mianowniku.
6. **Filtry zawężające bez kontroli skutków** — tylko angielski, tylko artykuły i przeglądy,
   tylko WoSCC lub tylko Scopus.
7. **Brak kontroli struktury geograficznej.** Ekspansja produkcji jednego kraju sama generuje
   krzywą wyglądającą jak adopcja.
8. **Listy „top-N najczęściej cytowanych"** mylą wiek pracy z jej wpływem.

## 5. Luka, którą można zagospodarować

Wszystkie te słabości są tą samą słabością: **retrieval i normalizacja są traktowane jako
formalność, a nie jako źródło wyniku.**

Trzy warstwy przewagi, w kolejności siły:

**(a) Porównanie międzytechnologiczne na wspólnym mianowniku.** Pięć rodzin technologii, jedno
pole, jeden mianownik, jedna metoda. Pozwala postawić pytania, których dzisiejsza literatura nie
umie postawić: która technologia rośnie szybciej, czy krzywe mają wspólny punkt przegięcia, czy
któraś już nasyca.

**(b) Walidowany retrieval z niezmienniczością w czasie.** PPV i relative recall, stratyfikowane
po epokach, warstwy epokowe synonimów. To jest wkład metodologiczny, którego w tym gatunku nie ma.

**(c) Demonstracja empiryczna, ile kosztują te zaniedbania.** Odtworzenie zapytań z prac
opublikowanych — np. `(artificial intelligence[topic]) AND (orthopedics[topic])` — na naszym
pełnym lustrze i pokazanie, o ile zaniżają wynik i jak zmieniają kształt krzywej po
znormalizowaniu. **To jest najmocniejszy element**, bo zamienia krytykę metodologiczną w wynik
liczbowy, a komparatorem jest literatura, która już istnieje.

Warstwa dodatkowa, nigdzie niespotkana: **lead–lag preprintów** (medRxiv) wobec MEDLINE dla tych
samych technologii.

## 6. Konsekwencja dla pozycjonowania pracy

To przestaje być „kolejna bibliometria ortopedii", a staje się pracą o tym, **jak wybory dotyczące
wyszukiwania i normalizacji determinują wnioski o dyfuzji technologii**, zademonstrowaną na
technologiach ortopedycznych. Ortopedia jest poligonem, nie tematem.

Ryzyko do świadomego przyjęcia: taka praca jest trudniejsza do umieszczenia w czasopiśmie
klinicznym niż standardowa mapa „hotspotów". Naturalne kierunki to czasopisma scjentometryczne
i metodologiczne albo ortopedyczne o profilu metodycznym.

## 7. Weryfikacja luki — co znalazł scoping search (2026-08-25)

**Nie znalazłem pracy, która porównywałaby wiele technologii w jednej specjalności klinicznej
na znormalizowanym mianowniku.** Najbliższe trafienia i dlaczego nie zajmują tej luki:

**Adopcja AI w naukach (arXiv 2306.09145).** 137 mln publikacji z bazy The Lens, 333 dziedziny,
lata 1960–2021. Miarą jest **odsetek dziedzin**, w których AI się pojawia („In 1960 14% of 333
research fields were related to AI… but this increased to cover over half of all research fields
by 1972"), a nie udział publikacji wewnątrz jednej dziedziny. Inny projekt, ale dowód, że taka
skala analizy jest wykonalna — dobra praca do cytowania w metodach.

**Meta-badania nad jakością bibliometrii — przestrzeń częściowo zajęta.** Istnieją:
analiza praktyk raportowania w 100 najczęściej cytowanych pracach bibliometrycznych z lat
2019–2021 (Heliyon), korespondencja *The rapid growth of bibliometric studies: a call for
international guidelines* (Int J Surg 2024) i praktyczny przewodnik do recenzowania przeglądów
bibliometrycznych (Sage 2025).

**BIBLIO — wytyczna raportowania, którą trzeba znać i której trzeba przestrzegać.**
*Preliminary guideline for reporting bibliometric reviews of the biomedical literature*
(Syst Rev 2023). Powstała w czteroturowym Delphi z 11 ekspertami, próg zgodności 75–80 %,
zgodnie z zaleceniami EQUATOR. Ma **20 pozycji** (tytuł 2, abstrakt 1, wprowadzenie 2, metody 7,
wyniki 4, dyskusja 4).

**Kluczowa obserwacja: BIBLIO nie wymaga raportowania walidacji strategii wyszukiwania,
normalizacji ani sposobu radzenia sobie ze zmianą terminologii w czasie.** Nawet wytyczna
raportowania nie obejmuje tych trzech rzeczy. To wzmacnia lukę z innej strony: problem nie polega
na tym, że autorzy łamią standard — standard tego po prostu nie obejmuje.

### Wynikające z tego doprecyzowanie pozycjonowania

Przestrzeń krytyki *na poziomie raportowania* jest zajęta. Wolna pozostaje krytyka
**skwantyfikowana**: nikt nie odtworzył opublikowanych zapytań na kompletnym korpusie
i nie zmierzył, o ile zaniżają wynik i jak zmieniają kształt krzywej. Zdanie porządkujące pracę:
*BIBLIO mówi, co raportować; my mierzymy, ile kosztuje tego nieraportowanie.*

Dodatkowa, tania korzyść: protokół piszemy jako **zgodny z BIBLIO** i deklarujemy to wprost.
Recenzenci to lubią, a kosztuje jedną tabelę zgodności.

### Zastrzeżenie do tego rozpoznania

Przeszukanie było ograniczone technicznie — PMC, ScienceDirect i LWW zablokowały część zapytań
(captcha, 402, limit szybkości), więc kilku prac nie udało się przeczytać w całości.
**To nie jest scoping search o jakości publikacyjnej.** Przed pisaniem wstępu trzeba go powtórzyć
z nieblokowanej sieci, z zapisem zapytań i dat — sesja w VS Code ma do tego warunki.
Pytanie do rozstrzygnięcia pozostaje jedno i wąskie: czy istnieje praca porównująca wiele
technologii w jednej specjalności na wspólnym, znormalizowanym mianowniku.
