# Liczby zmierzone, do wykorzystania w metodach i ograniczeniach

Zbierane na bieżąco, żeby nie trzeba było ich odtwarzać przy pisaniu. Każda z datą pomiaru
i sposobem policzenia.

## Rdzeń a pełna lista (2026-08-28)

Wyłonienia per wariant tekstowy, detektor z §4 bez zmian:

| wariant | kandydatów | wyłonionych |
|---|---:|---:|
| primary (tytuł + streszczenie) | 245 081 | 7 662 |
| S1 (tylko tytuł) | 17 583 | **607** |
| S2 (tylko rekordy ze streszczeniem) | 244 026 | 7 537 |
| S3 (tylko anglojęzyczne) | 228 644 | 7 569 |

`emerging_core.json` = dokładnie przecięcie czterech powyższych = **287**.

**S1 jest filtrem merytorycznym, nie analizą wrażliwości.** Z 41 terminów, które wypadają
z pierwszej pięćdziesiątki `primary` przy przejściu do rdzenia, **wszystkie 41 odrzuca S1**,
a **33 z 41 w ogóle nie istnieją w słowniku S1 — nigdy nie pojawiają się w tytule.**
Szablon streszczenia (`were included`, `95 ci`, `method this`, `result a total`) żyje
w streszczeniach, bo tytuł nie ma sekcji „Methods".

## Rodziny zawierania (2026-08-28)

Zawieranie = ciągły podciąg tokenów, domknięcie przechodnie.

- cały rdzeń 287: **46 grup, 140 terminów uwikłanych**
- pierwsza pięćdziesiątka rdzenia: **8 rodzin, 23 z 50 terminów; po scaleniu 35 odrębnych bytów**

Tabela główna pokazuje 50 wierszy surowych z kolumną przynależności do rodziny — scalanie
zmieniałoby prerejestrowaną regułę §3.1 pkt 6 (próg Jaccarda 0,90).

## Remisy w rankingu (2026-08-28)

`prevalence_2021_2025` = liczba prac 2021–2025 ÷ mianownik wspólny dla wszystkich terminów,
więc **równa liczba prac daje bitowo równą prevalence**. W rdzeniu:

**44 bloki remisowe obejmujące 95 z 287 pozycji; największy blok ma 3 wiersze.**

Kolejność wewnątrz bloku nie wynika z danych. Rozstrzyga ją zamrożona kolejność wierszy
`coding_sheet_koder.csv` — sortowanie stabilne po kolejności wierszy parquet. Każde zdanie
postaci „termin X na pozycji N" musi się do tej kolejności odwoływać, bo powtórny przebieg
z niestabilnym sortowaniem potrafi przestawić sąsiadów w remisie.

Przykład, na którym to wyszło: `virtual reality` leży w remisie pozycji **152–154**
(`secondary analysis`, `virtual reality`, `to sport after` — każdy 292 prace w 2021–2025).
Wiążąca jest pozycja **153** z zamrożonego arkusza.

## Pozycje wcześniej etykietowanych technologii (2026-08-28)

**Nie do cytowania jako wynik** — etykiety „technologia" nadano ręcznie w Etapie 1, bez kodeksu
i bez zaślepienia. Wielkość do tekstu jest wynikiem kodowania. Tabela poniżej służy wyłącznie
pokazaniu, że rdzeń przesuwa technologie w górę.

| poz. w pełnych 7 662 | termin | poz. w rdzeniu 287 |
|---:|---|---:|
| 143 | robotic | 28 |
| 159 | patient specific | 30 |
| 357 | 3d printed | 51 |
| 417 | robotic assisted | 58 |
| 557 | machine learning | 80 |
| 854 | 3d printing | 101 |
| 931 | artificial intelligence | 104 |
| 1437 | virtual reality | 153 |
| 2183 | deep learning | 197 |
| 2745 | augmented reality | 220 |
| 2950 | patient specific instrumentation | 228 |
| 6809 | convolutional neural network | poza rdzeniem |

Jedenaście z dwunastu przeżywa przejście do rdzenia.
