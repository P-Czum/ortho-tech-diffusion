# Prompt drugiego kodera (model językowy) — v1.1 · dokumentacja

**Materiał prerejestracyjny.** Ten prompt pełni wobec modelu tę samą rolę, co
`kodeks_kodowania_v1.md` wobec kodera-człowieka, i podlega tym samym rygorom: jest zamrożony
przed kodowaniem, załączony do rejestracji dosłownie i nie jest modyfikowany po zobaczeniu
wyników.

Zależność: odpowiada **kodeksowi v1.1**. Każda zmiana kodeksu wymaga przegenerowania promptu
i zmienia jego hash, a więc unieważnia manifest zamrożenia.

**Uwaga o języku, do zapisania w metodach.** Prompt jest w języku polskim, bo kodeks jest po
polsku i musi istnieć jedno źródło prawdy. Materiał kodowany (tytuły) jest angielski.
Tłumaczenie promptu na angielski **daje inny prompt** — w publikacji należy załączyć wersję
faktycznie użytą, a tłumaczenie oznaczyć jako pomocnicze.

---

## Treść promptu — NIE tutaj

Operacyjna treść żyje wyłącznie w dwóch plikach i to ich hashe są w `freeze_manifest.txt`:

| plik | rola |
|---|---|
| `prompt_system_v1.1.txt` | komunikat systemowy: kodeks przełożony na instrukcję |
| `prompt_user_v1.1.txt` | szablon zapytania z polami materiału |

**Ten dokument ich nie powtarza celowo.** Wklejona kopia byłaby drugim źródłem prawdy
i rozeszłaby się z operacyjnym przy pierwszej poprawce kodeksu — co zresztą się stało
między v1.0 a v1.1, zanim ten rozdział powstał. `llm_coder.py` czyta pliki `.txt`,
nie ten dokument.

## Ustawienia przebiegu — częścią rejestracji

| parametr | wartość |
|---|---|
| model | podawany jawnie przy uruchomieniu, zapisywany w wyniku |
| temperatura | **nieuzywana** — modele GPT-5.6 jej nie wspieraja (metadane OpenRouter) |
| seed | 20260827, jawny i zapisywany w wyniku |
| dostawca | zapisywany obok identyfikatora: `openai/gpt-5.6-sol` (OpenRouter) to nie to samo co `gpt-5.6-sol` (OpenAI) |
| liczba przebiegów na termin | 1 (przy 3 raportujemy zgodność wewnętrzną) |
| format odpowiedzi | wymuszony JSON |
| pola widoczne | wyłącznie te z szablonu powyżej |
| pola ukryte | czas podwojenia, osie koncentracji, wyniki definicji 2 |

## Kontrola kontaminacji — obowiązkowa

Głównym ryzykiem tej konstrukcji jest to, że model rozstrzyga z wiedzy uprzedniej, a nie
z kodeksu: może „wiedzieć", że `rapid prototyping` przeszło w `3d printing`, niezależnie od
podanych tytułów. Zgodność wynikałaby wtedy ze wspólnej wiedzy, a nie ze stosowania reguł,
i κ rosłoby, nie walidując niczego.

Dlatego kodeks wymaga wskazania w uzasadnieniu konkretnego elementu materiału. Po kodowaniu
raportujemy **odsetek uzasadnień powołujących się na dostarczony materiał** (tytuł, rok,
nazwany kandydat) wobec uzasadnień odwołujących się do wiedzy ogólnej. Ten odsetek jest
wynikiem, nie kontrolą techniczną — mówi, na ile kodeks jest samowystarczalny.

## Czego ta konstrukcja NIE mierzy

κ między człowiekiem a modelem mierzy, **czy kodeks daje się zastosować niezależnie na
podstawie samych zapisanych reguł**. Jest to mocniejszy test klarowności kodeksu niż drugi
koder-człowiek, który może dopytać autora.

Nie mierzy natomiast, czy pięć kategorii trafnie dzieli rzeczywistość. Tego nie wolno
napisać ani zasugerować.
