# S5 i podmiany sprawdzone; odpowiedzi na trzy pytania; S9 czeka na PC

Autor: sesja VS Code, 2026-11-10. Odpowiedź na `brief_dla_vsc_wylaczenia_RESPONSE_2026-10-30`
i `brief_dla_vsc_S9_nice_2026-10-30`.

Krótko:
- Podmiany z §4 są wierne, a Tabela 1 nie różni się od danych w żadnej komórce.
- S5 jest kompletny. Jedna kosmetyczna poprawka w kolejności S5.2 (§2).
- „×” to krotność współwystępowania ponad przypadek. Proponuję brzmienie po angielsku (§3).
- W S1.4 ma być `docs_total` (§4).
- S9 czeka na kodowanie PC. Jedna wskazówka do arkusza (§5).

Wszystkie Twoje pliki z dysku są zacommitowane razem z tym briefem.

## 1. Kontrola liczb

**`table1_48.md` wobec `osie_48.csv`:**
- 48 wierszy, kolejność według y₀ rosnąco;
- y₀, rok szczytu, czas podwojenia, efektywna liczba krajów i kraj prowadzący z udziałem: **0 różnic**.

**Tabela 2 w `results_v4`:** mediany przeliczone z `osie_48` według rodzaju z Tabeli 1 są zgodne
we wszystkich sześciu wierszach (narzędzia wspomagające: 2018 / 8,1 / 5,7).

**S5:**
- S5.1 jest identyczne z `table1_48.md`;
- S5.2: 48 grup, każda z 86 fraz `material_48.csv` występuje;
- S5.3: każda z 86 fraz `wylaczenia_48.csv` występuje.

## 2. S5.2 — kolejność grup

`build_S5.py` sortuje grupy po `y0` **pierwszej frazy** w `material_48.csv`. To rok wyłonienia
samej frazy ze starszego przebiegu, a nie rok wyłonienia grupy. U 17 grup te lata się różnią:
- *reverse shoulder arthroplasty*: 2021, a grupa 2007;
- *robotic assistance*: 2021, a grupa 2018;
- *unicompartmental knee arthroplasty*: 2013, a grupa 2018;
- i tak dalej.

Tabela S5.2 nie pokazuje lat, więc żadna liczba nie jest błędna. Kolejność nie odpowiada jednak
Tabeli 1. Proponuję sortować po `y0` z `osie_48.csv`, wtedy kolejność będzie jak w Tabeli 1:

```python
y0 = {r["grupa"]: int(r["y0"]) for r in rd("osie_48.csv")}
for g, rs in sorted(groups.items(), key=lambda kv: (y0[kv[0]], kv[0])):
```

## 3. „×” przy FEA i Mimics

To krotność współwystępowania ponad przypadek: liczba wspólnych prac obserwowana podzielona przez
oczekiwaną przy niezależności. W praktyce to lift. Pochodzi z `brief_dla_cowork_material_54_FEA_2026-09-25`
§1. Partnerzy FEA:
- femoral neck system: 25,4×;
- PFNA: 16,4×;
- PEEK: 12,2×;
- OLIF: 9,4×.

Stąd przedział „9–25×”. Mimics współwystępuje z FEA 13,1×.

Gołe „×” w S5 jest niejasne. Proponuję:
- FEA: *„instrument for testing implants, not used on patients: co-occurs with implants of the
  material 9–25 times more often than expected by chance”*;
- Mimics: *„segmentation software used to build FEA models: co-occurs with FEA 13 times more often
  than expected by chance”*.

## 4. S1.4 — 714 czy 637

**`docs_total`, czyli 714.** Tak liczone są wszystkie wiersze S1.4: `taa`/`tar` 853 → 1 498, PAO
404 → 700 itd. Musi tak być, bo grupy, które wypadają, nie mają y₀, więc nie mają też prac od y₀.
Tabela 3 i tekst zostają przy pracach od y₀. Warto dopisać w nagłówku S1.4 jedno słowo: „papers
(all years)”.

## 5. S9 — wskazówka do arkusza i co zrobię potem

W `S9_nice_screen.csv` nie ma jeszcze żadnej decyzji PC (0 z 247 wierszy).

Jedna wskazówka do `fraza_PC`, zanim PC zacznie: **wszystkie nazwy, pod którymi technologia
występuje w abstraktach, rozdzielone średnikami.** Dotyczy to pełnej nazwy, skrótu i wariantów, np.
`percutaneous vertebroplasty; vertebroplasty; pvp`. Policzę je razem, jako jedną grupę, tak jak
grupy materiału. Pojedyncza nazwa bez skrótu dałaby zaniżony udział, a o tym właśnie rozstrzyga
podział < θ / ≥ θ.

Po kodowaniu PC policzę dla każdej pozycji „tak”:
- udział w polu rok po roku (to samo pole, filtry i kanonizacja co `szeregi_48`);
- szczyt i rok szczytu;
- czy udział kiedykolwiek osiągnął ≥ 0,1%.

Z materiałem 48 nie porównuję niczego. Dopasowanie robisz Ty.

**Korekta, ten sam dzień.** Wskazówka powyżej była zła: PC nie ma skąd znać wszystkich wariantów
nazwy w abstraktach. Wraca Twoja pierwotna instrukcja: PC wpisuje **jedną nazwę** (skrót tylko,
jeśli go zna). Warianty wyszukuję ja w korpusie, mechanicznie: wszystkie frazy pola zawierające tę
nazwę lub skrót, z liczbą prac. PC potwierdza, które znaczą to samo, jak przy scaleniach.
Dopiero potem liczę udział grupy. Strona do kodowania: `code/s9_ui.html`.

Manifest **12/12**.
