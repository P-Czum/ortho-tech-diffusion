# D4 wykonane — reguła potwierdzona co do jednego PMID, rdzeń urósł do 827

Autor: sesja VS Code, 2026-09-01. Dotyczy: `brief_dla_vsc_pole_naczyniowe_2026-08-31.md`.

Skrypt: `code/apply_d4_filter.py`. Filtr `--exclude` dodany do `count_noun_phrases.py`.
Tabele `terms_np_d4_*` i `emerging_np_d4_*` w katalogu roboczym.

---

## Z1. Reguła zaimplementowana niezależnie i zgodna co do jednego rekordu

Nie wziąłem Twojej listy PMID — zaimplementowałem regułę z §2 od zera na `analytic_index.parquet`
(autorytatywnym, bo `analytic_msk` pokrywa tylko 243 523 z 268 383 rekordów pola) i dopiero potem
porównałem.

```
wyłączonych przez D4:  7 135 (2,66% pola)
Cowork 7 135, moje 7 135
wspólnych 7 135 | tylko u Coworku 0 | tylko u mnie 0
```

**Pole 2005–2025: 268 383 → 261 248.** Kontrola z Z1 mówiła 261 248. Zgadza się dokładnie,
bez korekty na brzegi lat.

Sprawdziłem też, że wszystkie cztery deskryptory bramy są w poddrzewie 56:
`D023821` Limb Salvage, `D000671` Amputation Surgical, `D004188` Disarticulation,
`D006428` Hemipelvectomy.

## Z2. Dziewięć terminów kontrolnych — **wszystkie zniknęły z list wyłonień**

Rozbijam na dwie sytuacje, bo to nie to samo:

**Zniknęły ze słownika całkowicie (docs → 0):**

| termin | docs przed | po D4 |
|---|---:|---:|
| chronic limb threatening ischemia | 656 | 0 |
| peripheral artery disease | 566 | 0 |
| endovascular therapy | 386 | 0 |
| endovascular revascularization | 200 | 0 |
| major amputation rate | 209 | 0 |
| drug coated balloon | 88 | 0 |

**Zostały w słowniku, ale poniżej progu wyłonienia** — czyli też zniknęły z listy wyłonień:

| termin | docs przed | po D4 | status |
|---|---:|---:|---|
| clti | 611 | 26 | w słowniku, nie wyłania się |
| amputation free survival | 571 | 47 | w słowniku, nie wyłania się |
| diabetic foot ulcer | 681 | 39 | nie wyłaniał się już przed D4 |

**Żaden nie został na liście wyłonień. Reguła nie jest za wąska.**

Osobny dowód, że D4 usunęło spójne piśmiennictwo, a nie przypadkowe rekordy: z rdzenia wypadło
45 fraz i są to niemal w całości słownik naczyniowy — `clti`, `cli patient`, `clti patient`,
`afs`, `amputation free survival`, `pad`, `dfu`, `dfus`, `dcb`, `evt`, `major adverse limb event`,
`major amputation rate`, `reintervention`, `hba1c`, `competing risk`, `kaplan meier estimate`.

## Z3. Rdzeń i klasa śmieci

**Rdzeń (primary ∩ S2 ∩ S3): 813 → 827, czyli +14.** Wypadło 45, doszło 59.

Wzrost przy kurczącym się polu nie jest błędem: **mianownik spadł o 2,66%, więc udziały wszystkich
terminów wzrosły** i część przekroczyła próg θ = 0,1%. Detektor mierzy udział, nie liczbę.

Gołe liczebniki — Twoje oczekiwania w nawiasach:

| | wynik | oczekiwane |
|---|---:|---:|
| (a) frazy wyłącznie liczbowe | **34** | 32 |
| (b) frazy z samodzielnym tokenem liczbowym | **62** | 60 |
| (c) z liczbą wśród 96 pozycji mapy klinicznej | **1** | 0 |

Różnice w (a) i (b) to +2 z przeliczenia na nowym polu, nie rozjazd metody.

**(c) = 1 to `covid 19`** — czyli **fałszywy alarm mojej kontroli, nie błąd Twojej klasyfikacji.**
Regex szuka samodzielnego tokenu liczbowego, a „19" jest tu częścią nazwy własnej choroby.
Twoje oczekiwanie zera jest praktycznie trafne; zgłaszam to jako własność testu.

**59 nowych fraz nie ma w `np_kategorie_propozycja.tsv`** — lista w
`data/processed/np_nowe_po_d4.csv`. Z tego 9 to liczebniki, 50 ma treść. Klasyfikacji nie ruszam,
ale zwracam uwagę, że wśród nowych są pozycje wyglądające na materiał mapy, nie na metodologię:
`vsp`, `ra total knee arthroplasty`, `mimic software`, `imn`, `vbq`, `hbl`, `fragility fracture`,
`rod fracture`, `mechanical lateral distal femoral angle`, `anterior cruciate ligament
reconstruction group`.

## Z4 (z briefu `osie_sily`). Relacja rdzeń 47 ⊂ mapa

- wszystkie **47 z 47** są obecne w `np_mapa_propozycja.csv`;
- na mapie klinicznej (`na_mapie == True`, pusty `wariant_do`): **27 z 47**;
- rozkład kategorii tych 47: metoda 12, rozpoznanie 11, technika 10, wynik 4, technologia 4,
  skala 2, lek 2, organizacja 2;
- **D4 przeżyło 45 z 47**; wypadły dwa: `chronic limb threatening ischemia`
  i `peripheral artery disease` — oba naczyniowe, czyli dokładnie zgodnie z celem reguły.

## Materiał 55 → **53**

Z `material_55.csv` wypadły dokładnie dwie pozycje, które przewidziałeś w §3 Z4:
**`endovascular therapy` i `endovascular revascularization`**. Reszta bez zmian.

Z 45 fraz, które wypadły z rdzenia, na mapie klinicznej były **cztery** — te dwie plus
`chronic limb threatening ischemia` i `peripheral artery disease`.

## Porządki z §6

Zrobione po mojej stronie: pliki Coworku zacommitowane (v1.3, mapa, `scoping_log` z D1–D4),
`_to_delete/` usunięty, `git gc` wykonany — **0 luźnych obiektów, pakiet 965 KiB**.

## Stan i co dalej

Manifest **12/12**, `coding_manual_v1.2.md` nietknięty, v1.3 to osobny plik.
`coding_sheet_koder_CODED_*.csv` w `.gitignore`, nietknięty.

Następne w kolejce: **osie siły na przeliczonym polu dla 53 pozycji**, plus kontrola
metal-on-metal (Z2 z briefu `osie_sily`). Ruszam, chyba że najpierw chcesz rozstrzygnąć
59 nowych fraz — bo jeśli któraś z nich wejdzie na mapę, materiał urośnie ponad 53 i osie
trzeba będzie policzyć raz jeszcze.
