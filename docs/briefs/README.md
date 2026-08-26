# `docs/briefs/` — protokół wymiany między sesjami

Dwie sesje pracują nad tym repo: **Cowork** (Claude w aplikacji desktop, ma dostęp do dysku
przez mostek, **nie ma dostępu do sieci ani do AWS**) i **VS Code** (Claude Code na Windows,
ma sieć, AWS i pełne środowisko).

Wymiana idzie przez pliki w tym katalogu. Komenda **`R`** oznacza: *przeczytaj najnowszy
brief adresowany do ciebie i wykonaj*.

## Nazewnictwo

| kierunek | wzorzec |
|---|---|
| Cowork → VS Code | `brief_dla_vsc_<temat>_<RRRR-MM-DD>.md` |
| VS Code → Cowork | `brief_dla_cowork_<temat>_RESPONSE_<RRRR-MM-DD>.md` |

„Najnowszy" = najpóźniejsza data w nazwie, przy remisie — najpóźniejszy `mtime`.

## Co musi zawierać brief

1. **Stan wyjściowy** — ścieżki, liczby, co jest zrobione. Odbiorca nie zna kontekstu rozmowy.
2. **Kolejka zadań** w kolejności wykonania, każde z komendą do uruchomienia.
3. **Kontrole, które muszą przejść** — z oczekiwaną wartością, żeby dało się je zweryfikować.
4. **Czego NIE robić** — równie ważne jak lista zadań.
5. **Format raportu zwrotnego** — krótko, liczbami, pełne komunikaty błędów.

## Zasada edycji plików — obowiązuje od 2026-08-26

Po incydencie, w którym edycja z Coworku nadpisała zrównoleglenie zrobione w VS Code:

- **Pliki w `code/`, które już istnieją, edytuje wyłącznie VS Code.**
- **Cowork dostarcza pliki nowe albo specyfikacje zmian** — nigdy nadpisania istniejących.
- Jeśli Cowork uzna, że istniejący plik wymaga zmiany, opisuje ją w briefie zamiast wykonać.

## Podział ról

| | Cowork | VS Code |
|---|---|---|
| dostęp do sieci | nie | tak |
| AWS / poświadczenia | nie | tak |
| pobieranie danych | nie | tak |
| ciężkie przetwarzanie | nie | tak |
| projekt badania, protokół, przegląd literatury | tak | — |
| pisanie nowych narzędzi | tak (jako pliki nowe) | tak |
| edycja istniejących narzędzi | nie | tak |
