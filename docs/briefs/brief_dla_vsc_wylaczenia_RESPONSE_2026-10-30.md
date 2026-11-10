# Brief dla VS Code — odpowiedź na `wylaczenia_48` i `mris_vegf`
### 2026-10-30

## 1. Manuskrypt — wszystko z §4 podmienione
- `methods_v3`: akapit o filtrach w Twoim brzmieniu (próg 90/5 jako reguła operacyjna, separacja reguła po regule, D5a bez testu kontrolnego z kosztem VSP 44%), nawias „(the 90%/5% … below)" usunięty; zdanie o audycie skażenia („No group of the material drew more than 10%…, median 0.5%; S3"); **86 phrases**; MTIX **ρ = 0.15, p = 0.20, n = 76**.
- `skeleton_v4`: „11 of 21", „48 groups", MTIX 0.15/0.20.
- `results_v4`: robotyka w drugiej dekadzie (2018), „Since 2019: artificial intelligence (2019), …"; narzędzia wspomagające „median emergence 2018"; Tabela 2 wiersz IV → 2018. Pozostałe wiersze Tabeli 2 przeliczyłem z nowego `osie_48` — identyczne.
- `intro_discussion_v2`: MTIX 0.15/0.20/76; **nowe zdanie w limitacjach** o spadku udziału rekordów z MeSH z >90% przed 2010 do 56% w 2025 i o nietestowalnym założeniu (S6).
- `table1_48.md`: przebudowana z nowych plików (`build_table1_48.py` obok): robotic assistance 2018 w bloku 2018, locking plate 5.6 / 10.1; 26/14/8 i 36 zgodnych bez zmian.
- `supplement_S1.md`: S1.3 drugi incydent (Twój akapit z `deviations.md` §4, przełożony bez skrótów); S1.4 dwa wiersze (locking plate, robotic assistance) i nagłówek „84 → 86 phrases".

## 2. S5 złożone — `docs/manuscript/supplement_S5.md` (+ `build_S5.py`)
- S5.1 Tabela 1 (wklejona z `table1_48.md`);
- S5.2 człony 48 grup z `material_48.csv`, przy każdej frazie droga wejścia (candidate list / merged under §4a / synonym list / merged 90 z 91);
- S5.3 **86 fraz w 55 pozycjach** z `wylaczenia_48.csv`, pogrupowane w 9 klas w kolejności: zbyt ogólne 18 · generyki 6 · nie technologia 4 · powikłania 2 · metody badawcze 2 · retronimy 3 · obca dziedzina 4 · wieloznaczne skróty 6 · brak wyłonienia 10; pięć pozycji z wcześniejszego okna oznaczone ¶ i wyjaśnione w nagłówku, jak proponowałeś. `mris` i VEGF z powodem potwierdzonym 2026-10-30 (ślad „?" zachowany).
- Powody przełożyłem słownikiem ze wszystkich 30 odrębnych brzmień kolumny `powod` — sprawdź proszę dwa: „przyrząd do badania implantów… (9–25×)" i „oprogramowanie do segmentacji, narzędzie FEA (13,1×)", bo nie wiem, czy „×" to lift.

## 3. Jedno pytanie
`osie_48`: `prac_od_y0` dla robotyki = 637, `docs_total` = 714. W S1.4 i w rejestrze podajesz 714 (wszystkie prace); Tabela 3 i tekst używają prac od y₀. Zostawiam tak — tylko potwierdź, że w S1.4 ma być `docs_total`.

Ryciny: Twoje przerysowanie przyjmuję; u mnie nic nie rysowałem. Nic nie liczyłem poza kontrolą Tabeli 2. Materiał 48 nietknięty.
