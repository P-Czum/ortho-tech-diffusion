# `mris` i VEGF — powody wyłączenia potwierdzone

Autor: sesja VS Code, 2026-10-30. Uzupełnienie `brief_dla_cowork_wylaczenia_48_2026-10-29` §3.3.

PC potwierdził powody dla dwóch pozycji, które w arkuszu miały tylko „?”:

| fraza | klasa | powód |
|---|---|---|
| `mris` | zbyt ogólna | MRI w liczbie mnogiej: ogólna metoda obrazowania, jak wyłączone *CT imaging* |
| *vascular endothelial growth factor*, `vegf` | nie technologia | czynnik wzrostu (cząsteczka), jak wyłączony *biomarker* |

`data/processed/wylaczenia_48.csv` jest poprawiona. Klasa „powód niezapisany” znika. Rozkład 55
pozycji:

| klasa | pozycji |
|---|---:|
| zbyt ogólna | **18** |
| brak wyłonienia | 10 |
| generyk | 6 |
| wieloznaczny skrót | 6 |
| nie technologia | **4** |
| obca dziedzina | 4 |
| retronim | 3 |
| metoda badawcza | 2 |
| powikłanie | 2 |

S5 możesz składać bez pozycji „do potwierdzenia”. W kolumnie `powod` obu wierszy zostaje ślad,
że w arkuszu był „?”, a powód potwierdzono 2026-10-30.
