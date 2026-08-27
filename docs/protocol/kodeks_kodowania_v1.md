# Kodeks kodowania terminów wschodzących — v1.0 (projekt do rejestracji)
2026-08-27 · do prerejestracji PRZED kodowaniem · dotyczy planu v0.8 §8

---

## 1. Materiał i zaślepienie

Jednostką kodowania jest **termin** z zamrożonego arkusza (287 pozycji, hash w repo).
Koder widzi: termin, szereg udziałów, `y₀` (def1), kandydatów na poprzednika z liftem,
po trzy tytuły z okolic `y₀` i z lat 2023–2025. Koder może dodatkowo przeszukać tytuły
w korpusie — każde takie sprawdzenie odnotowuje w `uwagi`.

**Koder NIE widzi podczas kodowania:** czasu podwojenia, osi koncentracji, wyników def2.
Powód: czas podwojenia ma służyć jako **niezależna** kontrola zgodności po kodowaniu
(technologie 2–3 lata, metodologia 8–15). Jeśli koder go widzi, kontrola przestaje być
niezależna i mierzy zgodność kodera z liczbą, a nie z rzeczywistością. Arkusz roboczy kodera
to widok bez tych kolumn; pełny arkusz zostaje zamknięty do końca kodowania.

## 2. Pięć kategorii — definicje operacyjne

Kodujemy **desygnat** terminu (zdolność, urządzenie, praktykę), nie sam napis.

**`novel concept`** — desygnat nie istniał w polu przed oknem wyłonienia pod żadną nazwą.
Warunki: (a) tytuły z okolic `y₀` opisują zdolność bez wcześniejszego odpowiednika,
(b) brak kandydata na poprzednika o lifcie ≥ 5, którego desygnat odpowiada desygnatowi terminu.
Pusta lista kandydatów to **hipoteza domyślna, nie rozstrzygnięcie** — poprzednik mógł żyć
poniżej progu 50 wystąpień albo poza polem; koder potwierdza lekturą tytułów.

**`renaming`** — desygnat identyczny z desygnatem poprzednika. Test operacyjny —
**test podstawienia**: zamiana terminu na poprzednika w tytułach z okresu nakładania zachowuje
sens **w obu kierunkach**. Wspiera: okno współwystępowania (oba terminy w tych samych pracach),
zapis typu „X (Y)" w tytułach przejściowych. Wzorzec: `rapid prototyping → 3d printing`.

**`conceptual evolution`** — desygnat nowego terminu zawiera desygnat poprzednika **plus
element konstytutywny**, którego poprzednik nie miał (albo istotnie zmienia zakres). Test
podstawienia przechodzi w jedną stronę, a w drugą nie: każdy robot używa nawigacji, ale nie
każda nawigacja jest robotem. Wzorzec: `navigation → robotic`.

**`measurement artifact`** — wyłonienie napędzane pomiarem, nie zjawiskiem: zmianą indeksowania,
dostępności tekstu, miksu czasopism lub konwencji zapisu. Wskazania: `y₀ ≥ 2020` w oknie
opóźnienia indeksowania **i** brak potwierdzenia w def2; wyłonienie znikające w wariantach
S2/S3; termin będący konwencją zapisu (formuły dat, zwroty szablonu abstraktu).

**`non-technological term`** — desygnat prawdziwy i wschodzący, ale niebędący technologią:
metodologia badań, statystyka, konwencja raportowania, organizacja opieki, temat kliniczny.
Wzorce: `systematic review`, `machine learning` NIE (technologia), `length of stay` TAK
(organizacja opieki). Kategoria nie jest koszem: rozkład kategorii w przesiewie jest wynikiem
pierwszorzędnym pracy.

## 3. Procedura — drzewo decyzyjne, w tej kolejności

1. Czy wyłonienie jest artefaktem pomiaru? → TAK: `measurement artifact`, koniec.
2. Czy desygnat jest technologią (urządzenie, materiał, technika obliczeniowa lub operacyjna)?
   → NIE: `non-technological term`, koniec.
3. Czy istnieje poprzednik o odpowiadającym desygnacie (kandydat z liftem ≥ 5 albo znaleziony
   ręcznie)? → NIE: `novel concept`.
4. Test podstawienia z poprzednikiem: obustronny → `renaming`; jednostronny → `conceptual
   evolution`; nie przechodzi → wróć do 3 (kandydat błędny) lub `novel concept`.

Każdy werdykt z jednozdaniowym uzasadnieniem w `uwagi`; przy kategoriach 2–3 wpisany poprzednik.

## 4. Drugi koder i zgodność

Drugi koder koduje **60 terminów (21%)**, losowanych warstwowo: po epokach `y₀` (2005–2012 /
2013–2019 / 2020+) i po obecności kandydata na poprzednika. Ten sam widok zaślepiony, ta sama
procedura, bez wglądu w kody pierwszego kodera.

Zgodność: **κ Cohena, próg ≥ 0,70**. Poniżej progu: rewizja definicji operacyjnych, ponowne
kodowanie podpróby, raportowane obie rundy — pierwotna zgodność nie znika z pracy.
Rozbieżności rozstrzygane dyskusją; kody sprzed uzgodnienia zachowane w arkuszu.

## 5. Kontrole po kodowaniu (nie podczas)

1. **Czas podwojenia vs kategoria**: oczekiwanie — technologie krótkie, metodologia długa.
   Zgodność raportowana; niezgodne przypadki omówione pojedynczo.
2. **Def2 vs kategoria**: `renaming`/`evolution` powinny odtwarzać się w def2 częściej niż
   `measurement artifact` (który z definicji może być definicyjnie zależny).
3. **Rozkład kategorii po epokach `y₀`** — z flagą ostrożności dla `y₀ ≥ 2020`.

## 6. Raportowanie `y₀`

`y₀` podawany jako wartość def1 z wartością def2 obok; różnica > 2 lata = flaga w tabeli
(dotyczy 25% rdzenia). Nie uśredniamy i nie budujemy przedziału — def1 jest definicją
podstawową z decyzji projektowej, a rozbieżność międzydefinicyjna jest raportowana jako
oszacowanie niepewności, nie jako korekta.
