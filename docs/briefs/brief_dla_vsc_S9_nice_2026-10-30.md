# Brief dla VS Code — S9: wzorzec do testu recall wybrany i pobrany
### 2026-10-30

## 1. Decyzja (PC, dziś, zapisana w `deviations.md` §6 **przed** jakimkolwiek porównaniem)
Jeden wzorzec: program NICE *Interventional Procedures* (od 2003; od 2025 prowadzony jako HealthTech guidance z dawnym numerem IPG). Lista ekspercka z *Injury* 2022 rozważona i **odrzucona dla prostoty**. Reguły (trzy wyniki, podział „nigdy kandydat" na < θ / ≥ θ, lata 2024–25 poza oknem, żadnej zmiany parametrów po wyniku) — w rejestrze.

## 2. Co pobrałem
- Pełny katalog opublikowanych wytycznych NICE (2 446 pozycji, 30.10.2026) → 776 HTG → **610 z dawnym numerem IPG** (616 w filtrze NICE; sześć bez numeru to zapewne pozycje wycofane). Każdą stronę odczytałem po breadcrumbs (temat NICE) i numerze IPG.
- Filing tematyczny NICE jest niespójny (kifoplastyka balonowa pod *Cancer*, endoskopowa discektomia pod *Chronic pain*), więc „Musculoskeletal conditions" (69 pozycji) nie może definiować zbioru. Zbiór do przesiewu = 610 tytułów po szerokim sicie anatomicznym + 4 tematy → **247 tytułów**, `data/external/S9_nice_screen.csv`.
- Kolumny: `ipg, htg, published, year, nice_topic, nice_msk, title, propozycja_modelu, ortopedia_PC, fraza_PC, uwaga_PC`. `propozycja_modelu` = „other specialty?" dla 119 oczywiście nieortopedycznych (oko, serce, pęcherz…) — to propozycja; decyduje PC. 11 pozycji z lat 2024–25.

## 3. Podział pracy
- **PC:** w `ortopedia_PC` wpisuje tak/nie dla 247 wierszy (dla 119 z propozycją wystarczy potwierdzić), a dla „tak" w `fraza_PC` nazwę technologii tak, jak pisze się o niej w abstraktach (lub „brak odpowiednika") — **bez zaglądania do materiału 48**.
- **VSC (po PC):** dla każdej frazy PC policzyć udział w polu rok po roku (jak `szeregi_48`), szczyt i czy kiedykolwiek ≥ 0,1 % — to rozstrzyga „< θ" vs „prawdziwy brak". Dopasowanie do `material_48.csv` i `wylaczenia_48.csv` zrobię ja.
- Wynik: jedna tabela S9 (247 → N ortopedycznych → w materiale / wyłączone z powodem / nigdy kandydat < θ / nigdy kandydat ≥ θ / poza oknem) i jedno zdanie w limitacjach.

Nic nie porównywałem z materiałem. Manifest nietknięty.
