# Jeden plik do dwóch rycin: szeregi roczne grup

Autor: sesja Cowork, 2026-10-28. Bez nowych analiz — to eksport tego, co już policzone.

## Co potrzebne

`data/processed/szeregi_54.csv` — dla każdej z 54 grup udział w polu po roku 2000–2025
(**suma dokumentów zawierających dowolny człon grupy** ÷ rekordy pola w roku; te same szeregi,
z których liczono `trwalosc_wzgledna_54`). Kolumny: `grupa, y2000 … y2025` w procentach.

Plus `szeregi_czlonow.csv` dla członów trzech grup, osobno: `kyphoplasty` (4 człony),
`single bundle` + `double bundle reconstruction`, `mechanical alignment` + `kinematic alignment`
— do ryciny „nazwa to nie technologia" (scalenie i retronim na jednym obrazku).

## Po co

Rycina 5 (11 zaników względem własnego szczytu, jedna linia na technologię, x = lata od szczytu)
i Rycina 6 (retronim i scalenie). Plan rycin i definicje punktów krzywej:
`docs/manuscript/box1_definitions_and_figures.md` — proszę o jedno spojrzenie, czy definicje
w Box 1 zgadzają się co do joty z tym, co liczy `detect_emergence.py` i `merge_and_axes.py`
(parametry b, k, θ, m, d). Jeśli coś się różni, popraw Box 1, nie kod.

## Kontrole

Materiał 54, nietknięty. `szeregi_54.csv` ma 54 wiersze, 26 kolumn roku; wartości dla
`mom total hip arthroplasty` zgodne z `szeregi_jednoterminowe.json` (grupa jednoterminowa).
