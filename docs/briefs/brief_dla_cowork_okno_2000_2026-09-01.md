# Okno cofnięte do 2000. `hip resurfacing` wreszcie się wyłania — ale szablon wraca

Autor: sesja VS Code, 2026-09-01. Decyzja Przemka: „dorobić prace od 2000, wtedy mielibyśmy
XXI wiek w ortopedii".

Prośba do Ciebie jest w §6 i jest jedna: **klasyfikacja 506 nowych fraz** tym samym schematem,
którym zrobiłeś 813.

---

## 1. Dlaczego to zrobiliśmy — powód jest zmierzony, nie estetyczny

Kontrola metal-on-metal (`brief_dla_cowork_osie_sily_RESPONSE_2026-09-01.md`) pokazała dziurę:
**`hip resurfacing` nie wyłaniał się wcale**, bo szczyt miał w 2008, a baza 2005–2007 była już
wysoka. Detektor widział tylko słownictwo porażki (`metal debris`, `adverse local tissue
reaction`), nie samą technologię.

Po cofnięciu okna: **`hip resurfacing` ma `y₀ = 2005`** i pełny łuk.

```
        00    01    02    03    04    05    06    07    08    09    10    11    12   ...   25
      0.00  0.00  0.00  0.00  0.05  0.10  0.18  0.29  0.70  0.63  0.55  0.63  0.40  ...  0.07
      szczyt 0,696% w 2008, 2025/szczyt = 0,10
```

**To jest pierwsze pełne wejście-i-wycofanie prawdziwej technologii w tym materiale.** Twierdzenie
z poprzedniego briefu — że detektor widzi wycofanie tylko wtedy, gdy wytwarza ono własną
terminologię — **przestaje obowiązywać** i można je zastąpić mocniejszym: detektor widzi łuk
technologii, jeżeli okno zaczyna się przed jej wejściem.

## 2. Dryf indeksowania — sprawdzony przed decyzją, nie po

Główny argument przeciw brzmiał: 29 z 56 deskryptorów pola wprowadzono po 2000, a NLM nie
indeksuje wstecznie, więc lata 2000–2004 są niedoreprezentowane. Zmierzyłem proporcje:

| | udział pola w PubMedzie |
|---|---|
| 2000 → 2005 (dokładane) | 0,940% → 1,123% (**+23%**) |
| 2005 → 2025 (już akceptowane) | 1,123% → 0,825% (**−27%**) |

**Dryf dokładany jest mniejszy niż ten, który już mamy w oknie.** Odrzucenie 2000–2004 z tego
powodu byłoby niekonsekwentne.

**Osobne znalezisko, niezależne od tej decyzji i pilniejsze:** udział pola rośnie do **1,257%
w 2011**, a potem spada do **0,825% w 2025** — o 34%. To wygląda na nieciągłość indeksowania
MEDLINE, którą plan przewidywał do sprawdzenia (test MTIX-2022) i której nikt nie sprawdził.
Sam udział jest wewnętrznie spójny, bo licznik i mianownik kurczą się razem — ale jeśli
niedoindeksowanie jest wybiórcze, dotyka `prevalence_2021_2025`, czyli głównej osi rankingu.
**To jest do zbadania niezależnie.**

## 3. Bilans

| | 2005–2025 | 2000–2025 |
|---|---:|---:|
| rekordów pola przed filtrami | 268 383 | **297 667** |
| po D4+D5a+D5c | 254 508 | **282 908** |
| jednostek primary | 24 219 | 26 116 |
| wyłonień primary | 970 | **1 468** |
| rdzeń primary ∩ S2 ∩ S3 | 845 | **1 294** |
| materiał (49 terminów) | 49 | **47** |

Filtry pola przeliczone na całości: D4 7 784, D5a 6 402, D5c 573, razem 14 759 wyłączonych.
D5b nadal niewdrożone.

Rdzeń: 788 wspólnych, 57 wypadło, **506 nowych**.

**57, które wypadły, to niemal same liczebniki** (`1 0`, `12 4`, `13 9`, `2 3`) — czysty zysk.

**Z materiału wypadły dwie pozycje: `virtual reality` i `transfemoral amputation`** — dłuższa
historia podniosła im bazę i przestały przekraczać próg. Do odnotowania, bo `transfemoral
amputation` zostawiłeś świadomie przy D4.

## 4. Cena: szablon abstraktu wraca

Czoło 506 nowych, po prevalence 2021–2025:

| fraza | y₀ | prevalence | prac |
|---|---:|---:|---:|
| evidence | 2011 | **18,755%** | 36 946 |
| level | 2014 | **18,123%** | 37 053 |
| january | 2019 | 9,299% | 14 902 |
| impact | 2021 | 5,504% | 7 984 |
| risk factor | 2020 | 5,146% | 8 938 |
| sex | 2022 | 4,660% | 7 443 |
| stay | 2018 | 3,405% | 6 080 |
| level iv | 2003 | 1,673% | 4 399 |
| complete description | 2003 | 1,573% | 3 959 |
| therapeutic study | 2003 | — | 2 546 |

To jest formuła redakcyjna „Level of Evidence: IV; Therapeutic study" i pochodne. **Wracają,
bo z bazą 2000–2002 terminy powszechne już w 2005 mają wreszcie niską bazę.** Cofnięcie okna
częściowo odwraca to, co naprawiło przejście na frazy rzeczownikowe — i trzeba to powiedzieć
wprost w ograniczeniach, a nie przemilczeć.

## 5. Ale zysk jest realny i tego samego rzędu

Prawdziwe technologie i techniki pierwszej dekady, dotąd niewidoczne:

| termin | y₀ | prac |
|---|---:|---:|
| locking plate | 2006 | 1 119 |
| kyphoplasty | 2008 | 1 012 |
| adjacent segment degeneration | 2007 | 687 |
| cement leakage | 2009 | 650 |
| hip resurfacing | 2005 | 572 |

Plus rodzina skal wyników, która wcześniej nie miała szans: `oswestry disability index` (2007),
`oxford knee score` (2007), `neck disability index` (2009), `constant murley score` (2010),
`mayo elbow performance score` (2008). To nie jest materiał, ale jest to **osobna, spójna klasa
wyłonień, której w krótszym oknie po prostu nie było**.

## 6. Prośba: klasyfikacja 506 nowych

Przemek przejrzał już raz 82 nowe frazy i potwierdził, że żadna nie należy na mapę. Teraz jest
ich 506, z czego **86 to liczebniki**, więc realnie **420 do przejrzenia**.

**Nie chcę mu dawać 420 pustych pól.** Proszę o przepuszczenie ich przez ten sam schemat
11 kategorii, którym zrobiłeś 813 (`np_kategorie_propozycja.tsv`) — żeby rozstrzygał propozycje,
tak jak poprzednio.

Lista: `data/processed/rdzen_w2000.json` (1 294), nowe = różnica wobec
`np_rdzen_po_filtrach.json` (845). Mogę wypisać samą różnicę do osobnego pliku, jeśli wygodniej.

Klasyfikacji istniejących 788 nie ruszam — mapowanie termin→kategoria przeżywa zmianę okna,
tak jak ustaliliśmy przy zmianie pola.

## 7. Co zrobiłem, żeby oba okna dały się pokazać obok siebie

Zakres lat jest teraz **opcją wiersza poleceń** w `extract_field_text.py`,
`extract_noun_phrases.py`, `count_noun_phrases.py` i `detect_emergence.py`
(`--year-min/--year-max`, `--base-from/--base-to`), z dotychczasowymi wartościami jako
domyślnymi. **Stałych nie ruszałem**, więc wszystko policzone do tej pory odtwarza się tym samym
kodem bez żadnych flag. Przy zadeklarowanym odstępstwie od rejestracji musimy móc pokazać oba
okna, a nie tylko twierdzić, że stare dało się odtworzyć.

Tabele: `terms_w2000_*`, `emerging_w2000_*`, `noun_chunks_2000_2025.parquet`,
`field_text_auth_2000_2025.parquet` (autorzy dla 2000–2004, których wcześniej nie mieliśmy —
osie siły na dłuższym oknie nie będą miały dziury w pierwszych pięciu latach).

## 8. Stan

Manifest **12/12**. `coding_manual_v1.2.md` nietknięty, v1.3 osobny plik.
`coding_sheet_koder_CODED_*.csv` w `.gitignore`.

Osie siły dla materiału **przeliczę po klasyfikacji**, na ostatecznym zestawie — nie ma sensu
liczyć ich trzeci raz na materiale, który jeszcze się zmieni.
