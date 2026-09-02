# Reguła skrótów w kodeksie v1.4 — z jednym ryzykiem, którego nie zmierzyłeś

Autor: sesja Cowork, 2026-09-02. Odpowiedź na `brief_dla_cowork_d6_i_skroty_2026-09-02.md`.

Plik: **`docs/protocol/coding_manual_v1.4.md`** (nowy; v1.2 nietknięty, hash `d8adf778069ff521…`
zgadza się z manifestem; v1.3 zostaje jako osobna wersja). D6, D7, martwe pole detektora i MTIX
zapisane w `docs/protocol/scoping_log.md`, wpis 2026-09-02.

---

## 1. Reguła skrótów — przyjęta, jako §4a, z Twoim uzasadnieniem

> Termin dwu- lub trzyliterowy wchodzi do materiału dopiero po zmierzeniu jego rozwinięć na
> tytułach i streszczeniach dokumentów, które go zawierają. Wchodzi, jeżeli jedno rozwinięcie
> obejmuje wyraźną większość tych dokumentów; w przeciwnym razie wypada, a wyłączenie jest
> raportowane ze zmierzonym udziałem.

Twoje uzasadnienie przez „skrót wnosi wyłącznie prace używające samego skrótu" jest lepsze niż
moje pierwotne i weszło do kodeksu dosłownie, z Twoją tabelą 67–93%.

Umieściłem to jako **kryterium wejścia do materiału**, nie jako kategorię kodowania — reguła
działa przed drzewem decyzyjnym, więc §4a, a drzewo bez zmian.

## 2. Ryzyko, którego nie zmierzyłeś, i które trzeba domknąć przed zamrożeniem materiału

Odrzucenie skrótu jest zachowawcze dla **obecności** terminu. **Nie jest neutralne dla `y₀`.**

Jeżeli udział skrótu wśród dokumentów terminu **zmieniał się w czasie**, odrzucenie usuwa
dokumenty nierównomiernie po latach. Konkretnie: gdyby autorzy z biegiem lat coraz częściej
pisali samo „AI" zamiast „artificial intelligence" — co jest prawdopodobne, bo skrót
upowszechnia się razem z tematem — to odrzucenie `ai` usuwa **nieproporcjonalnie dużo dokumentów
późnych**. Skutek: spłaszczona krzywa wzrostu, **`y₀` przesunięte późno i czas podwojenia
zawyżony**. Czyli dokładnie te dwie wielkości, które są wynikiem pracy.

**Prośba: wypisz udział „tylko skrót" po latach** dla każdego terminu, którego reguła dotyczy
(21 w materiale). Jeżeli udział jest płaski — reguła jest bezpieczna i piszemy to jednym zdaniem.
Jeżeli rośnie — te terminy wymagają przywrócenia skrótu z zadeklarowaną wieloznacznością, albo
`y₀` liczonego na samej pełnej postaci z adnotacją.

To jest tania kontrola i jedyna rzecz, która dzieli §4a od reguły gotowej do tekstu.

## 3. D6 — przyjęte bez zastrzeżeń, i doceniam rozróżnienie

`Animals AND NOT Humans` na własnych znacznikach NLM. 11 749 rekordów, 3,95% pola — największa
z reguł.

Punkt, który sam podniosłeś i który jest ważny metodologicznie: **D6 nie wymagał testu progowego,
bo nie jest heurystyką.** D4 i D5b testowaliśmy progiem 5%, bo mogły chybiać; D6 mierzy dokładnie
to, co deklaruje. Ta różnica idzie do Metod — czytelnik musi wiedzieć, które filtry są
autorytatywne, a które są naszym oszacowaniem.

TPLO w materiale to najbrzydszy błąd, jaki mieliśmy, i znalazł się tylko dlatego, że ktoś zadał
pytanie z boku. Warto to odnotować w Ograniczeniach uczciwie: **nie mamy systematycznego testu
na obcą dziedzinę, tylko serię wykryć ad hoc.** Cztery wycieki (naczyniowy, stomatologiczny,
homonim, weterynaryjny) znalezione czterema różnymi drogami, żadna z nich nie była zaplanowana.

## 4. Martwe pole — zgoda, i to jest mocniejsze zdanie, niż wygląda

`platelet rich plasma` nigdy nie osiągnęło pięciokrotności własnej bazy; `bone morphogenetic
protein` ma pełną krzywą wycofania, ale rosło przed 2000.

**„Przesuwanie okna przesuwa martwe pole, nie usuwa go"** — biorę to zdanie do Metod dosłownie.
Razem z `hip resurfacing` daje to trzy zmierzone przypadki jednego mechanizmu i pozwala postawić
ograniczenie jako własność detektora, a nie jako przeprosiny za wybór okna.

Dodam do tego czwarty przypadek z drugiej strony: `virtual reality` wypadło z materiału **przez**
cofnięcie okna, bo dłuższa baza podniosła próg. Detektor ma więc martwe pole na obu końcach —
technologie, które weszły przed oknem, i technologie, których dłuższa baza podniosła próg ponad
ich wzrost. To jest jedno zdanie, nie dwa osobne ograniczenia.

## 5. Cichy błąd w `merge_and_axes.py` — dziękuję, że zgłosiłeś

Stała importowana między modułami, gdy okno przestało być stałe. Nie wywaliłby się, tylko podałby
złe liczby. **To jest ta klasa błędu, która przechodzi do publikacji.**

Zgłaszam analogiczne ryzyko po mojej stronie, bo dotyczy tego samego wzorca: mapowanie
`np_kategorie_propozycja.tsv` i `np_synonimy.tsv` powstało na oknie 2005–2025 i **przeżywa
zmianę okna tylko dlatego, że jest mapowaniem termin→kategoria bez odniesienia do lat**.
Gdyby ktoś kiedyś dopisał tam regułę zależną od `y₀`, złamie się dokładnie tak samo i tak samo
cicho. Dopisałem to jako uwagę w nagłówku obu plików.

## 6. MTIX — wniosek przyjmuję razem z Twoim zastrzeżeniem

Oś zostaje, całość do Ograniczeń. Test H3 z korelacją ekspozycji jest właściwym testem i wynik
jest czysty.

**Nie przeliczaj tego na rdzeniu 1 294.** Twój argument jest słuszny: 231 fraz metodologicznych
ma „ekspozycję na deskryptory" znaczącą co innego niż technologie, więc szerszy przedział
kupiłbyś kosztem jednorodności próby. Jeżeli recenzent naciśnie, zrobimy to wtedy i opiszemy
jako analizę na żądanie.

Zastrzeżenie o małej mocy wchodzi do Ograniczeń **Twoimi słowami** — „nie zmierzyliśmy
skrzywienia" nie znaczy „skrzywienia nie ma". To zdanie ma tam być, bo bez niego wynik czyta się
jako dowód nieobecności.

## 7. Liczebniki — 72, sprostowane po obu stronach

Przyjęte, zapisane w `scoping_log.md`. Te 14 różnicy to w większości prawdziwe terminy
(`srs 22`, `sf 12`, `l4 5`), więc dobrze, że sprawdziłeś definicję zamiast przyjąć moją.

## 8. Stan i co dalej

Manifest 12/12. Materiał: 75 grup.

Kolejność, jeśli się zgadzasz: **(1) kontrola udziału skrótu po latach z §2**, bo może zmienić
materiał; **(2) osie siły** na domkniętym zestawie; **(3)** ja składam `docs/protocol/deviations.md`
— mamy dziewięć zadeklarowanych odstępstw rozsypanych po dzienniku i briefach, a sekcji Metody
nie da się napisać bez jednej tabeli.
