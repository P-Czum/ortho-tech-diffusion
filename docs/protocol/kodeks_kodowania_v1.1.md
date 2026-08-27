# Kodeks kodowania terminów wschodzących — v1.1 (do rejestracji)
2026-08-27 · zastępuje v1.0 po recenzji VSC (`brief_dla_cowork_recenzja_kodeksu_2026-08-27.md`)
Zmiany wobec v1.0 wypisane w §7.

---

## 1. Materiał i zaślepienie

Jednostką kodowania jest **termin** z zamrożonego arkusza (287 pozycji, 29 kolumn, hash w repo).
Koder widzi: termin, szereg udziałów, `y₀` (def1), kandydatów na poprzednika z liftem
(narzędzie wyszukiwania, patrz §3), tytuły z terminem z okolic `y₀` i z lat 2023–2025,
**tytuły z poprzednikiem** oraz **tytuły wspólne** z okna `y₀ ± 2` (kolumny `poprzednik_glowny`,
`tytuly_poprzednika`, `tytuly_WSPOLNE`; pokrycie 284/287).

Koder może przeszukać tytuły w korpusie **wyłącznie dostarczonym narzędziem** (skrypt
wyszukiwania po terminie kanonicznym, z logiem zapytań); każde przeszukanie odnotowane w `uwagi`.

**Koder NIE widzi podczas kodowania:** czasu podwojenia, osi koncentracji, wyników def2.
Powód: te trzy wielkości służą jako **niezależne kontrole po kodowaniu** (§5). Kontrola,
którą koder widzi, mierzy jego posłuszeństwo wobec liczby, nie zgodność dwóch niezależnych
dróg. Widok kodera = arkusz bez tych kolumn; pełny arkusz zamknięty do końca kodowania.

## 2. Pięć kategorii — definicje operacyjne

Kodujemy **desygnat** terminu (zdolność, urządzenie, praktykę), nie napis.

**`novel concept`** — desygnat nie istniał w polu przed oknem wyłonienia pod żadną nazwą.
Warunki: (a) tytuły z okolic `y₀` opisują zdolność bez wcześniejszego odpowiednika,
(b) żaden kandydat z listy nie ma desygnatu odpowiadającego desygnatowi terminu.
Pusta lista kandydatów to **hipoteza domyślna, nie rozstrzygnięcie** — poprzednik mógł żyć
poniżej progu 50 wystąpień albo poza polem; koder potwierdza lekturą tytułów.

**`renaming`** — desygnat identyczny z desygnatem poprzednika. Test operacyjny —
**test podstawienia** na materiale z kolumn `tytuly_*`: zamiana terminu na poprzednika
w tytułach z okresu nakładania zachowuje sens **w obu kierunkach**. Wspiera: tytuły wspólne
(zapis typu „3D rapid prototyping"), okno współwystępowania. Wzorzec:
`rapid prototyping → 3d printing`.

**`conceptual evolution`** — desygnat nowego terminu zawiera desygnat poprzednika **plus
element konstytutywny** (albo istotnie zmienia zakres). Test podstawienia przechodzi w jedną
stronę: każdy robot używa nawigacji, nie każda nawigacja jest robotem. Wzorzec:
`navigation → robotic` (por. tytuł wspólny „robotic navigation system").

**`measurement artifact`** — wyłonienie napędzane pomiarem, nie zjawiskiem. Wskazania:
`y₀ ≥ 2020` w zmierzonym oknie opóźnienia indeksowania **łącznie z** treścią terminu wskazującą
na konwencję zapisu lub indeksowania (formuły dat, zwroty szablonu abstraktu, terminy rejestrów
raportowania). Sama data nie wystarcza — 86 terminów rdzenia ma `y₀ ≥ 2020` i większość z nich
to realne zjawiska.

**`non-technological term`** — desygnat prawdziwy i wschodzący, ale niebędący technologią:
metodologia badań, statystyka, konwencja raportowania, organizacja opieki, temat kliniczny.
Wzorce: `systematic review` TAK; `length of stay` TAK (organizacja opieki);
`machine learning` NIE (technologia). Kategoria nie jest koszem — rozkład kategorii jest
wynikiem pierwszorzędnym.

## 3. Kandydaci na poprzednika — status liftu

Lift jest **narzędziem wyszukiwania kandydatów, nie regułą decyzyjną**. Zmierzono, że lift
nie odróżnia sygnału od szumu (`we tested the` ma lift 36,0 przy `machine learning`);
rozróżnia koder, semantycznie. Próg listy kandydatów: **lift ≥ 3, spójnie w arkuszu
i w kodeksie**. Próg jest celowo przepuszczalny: pominięty prawdziwy poprzednik jest
kosztowniejszy niż kandydat więcej do odrzucenia (lekcja `MIN_CO`: za ostry próg liczności
wyciął parę o najwyższym lifcie w zbiorze).

## 4. Procedura — drzewo decyzyjne

1. Czy wyłonienie jest artefaktem pomiaru (wg wskazań §2)? → TAK: `measurement artifact`, koniec.
2. Czy desygnat jest technologią (urządzenie, materiał, technika obliczeniowa lub operacyjna)?
   → NIE: `non-technological term`, koniec.
3. Czy na liście (lub znaleziony ręcznie przez narzędzie z §1) jest poprzednik o odpowiadającym
   desygnacie? → NIE: `novel concept`, koniec.
4. Test podstawienia z tym kandydatem: obustronny → `renaming`; jednostronny → `conceptual
   evolution`; nie przechodzi → **weź następnego kandydata z listy (w kolejności liftu)
   i powtórz krok 4; po wyczerpaniu listy → `novel concept`**.

Każdy werdykt z jednozdaniowym uzasadnieniem w `uwagi`; przy kategoriach `renaming`
i `conceptual evolution` wpisany poprzednik.

## 5. Drugi koder i zgodność

Drugi koder: **60 terminów (21%)**, losowanych warstwowo **po epokach `y₀`** (2005–2012 /
2013–2019 / 2020+ → alokacja proporcjonalna 6 / 36 / 18) **i po długości n-gramu**.
(Warstwa „obecność kandydata" odrzucona — przy 95% pokrycia jest zdegenerowana.)
Ten sam widok zaślepiony, ta sama procedura, bez wglądu w kody pierwszego kodera.

Zgodność: **κ Cohena, próg ≥ 0,70**; obok raportowane zgodność surowa i κ ważone
(pięć kategorii o nierównych częstościach czyni samo κ niestabilnym — dodatkowe miary
są uzupełnieniem, nie zamiennikiem progu). Poniżej progu: rewizja definicji, ponowne kodowanie
podpróby, raportowane obie rundy. Rozbieżności rozstrzygane dyskusją; kody sprzed uzgodnienia
zachowane.

## 6. Kontrole po kodowaniu i raportowanie

1. **Czas podwojenia vs kategoria** (technologie 2–3 lata, metodologia 8–15) — zgodność
   raportowana, niezgodne przypadki omówione pojedynczo.
2. **Def2 vs kategoria**: `renaming`/`evolution` powinny odtwarzać się w def2 częściej niż
   `measurement artifact`. Ta kontrola jest ważna dlatego, że def2 nie uczestniczy w kodowaniu.
3. **Rozkład kategorii po epokach `y₀`**, z flagą ostrożności dla `y₀ ≥ 2020`.

**Zastrzeżenie zakresu, obowiązkowe w wynikach:** rozkład kategorii jest zmierzony na rdzeniu
287 — zbiorze **wstępnie przefiltrowanym na czterokrotną odporność wariantową**. Udział
artefaktów będzie niski z konstrukcji. Zdanie „X% wyłonień to artefakty" opisuje wyłonienia
odporne, **nie** pełny zbiór 7 662 — czytelnik założy szersze uogólnienie, jeśli mu tego
nie zabronimy wprost.

**`y₀`:** wartość def1 + wartość def2 obok + flaga przy różnicy > 2 lata. Nie uśredniamy —
obie wartości są prawdziwe względem swoich definicji; rozbieżność jest oszacowaniem
niepewności, nie korektą.

## 7. Zmiany wobec v1.0 (po recenzji VSC)

1. Materiał testu podstawienia istnieje: kolumny `poprzednik_glowny`, `tytuly_poprzednika`,
   `tytuly_WSPOLNE` (okno `y₀ ± 2`); w v1.0 test był niewykonalny — koder nie miał tytułów
   poprzednika.
2. Lift: próg ujednolicony do **≥ 3** w arkuszu i kodeksie; status zdegradowany z reguły
   decyzyjnej do narzędzia wyszukiwania.
3. `measurement artifact`: **usunięty wskaźnik def2** (łamał zaślepienie z §1 i czynił
   kontrolę 2 tautologią) oraz **usunięty wskaźnik „znika w S2/S3"** (pusty z konstrukcji
   na rdzeniu — części wspólnej czterech wariantów). Kategoria opiera się na koniunkcji
   daty i treści.
4. Pętla kroku 4 domknięta: kolejni kandydaci w kolejności liftu, po wyczerpaniu listy
   `novel concept`.
5. Warstwowanie drugiego kodera: epoka `y₀` × długość n-gramu; warstwa obecności kandydata
   odrzucona jako zdegenerowana.
6. Dodane κ ważone i zgodność surowa obok κ Cohena.
7. Dodane zastrzeżenie zakresu rozkładu kategorii (rdzeń ≠ pełny zbiór wyłonień).
8. Przeszukiwanie korpusu przez kodera wyłącznie dostarczonym narzędziem z logiem.
