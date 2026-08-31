# Count zdarzeń — 767, ale liczba jest zaniżona, bo reguła grupowania perkoluje

Autor: sesja VS Code, 2026-08-28. Dotyczy: `brief_dla_vsc_count_zdarzen_2026-08-28.md`.

Skrypt: `code/group_renaming_events.py`. Wynik: `results/renaming_events.json`,
pary powyżej progu w `results/renaming_pairs_above.csv` (10 562, zgodne co do jednej
z liczbą z poprzedniego przebiegu).

---

## 0. Kontrola przed liczbami

Implementację grupowania zmieniłem — przy 10 562 parach porównywanie każdej z każdą to 56 mln
operacji, więc buduję łączenie na kluczach `(token A, token B)`, liniowo. **Reguła bez zmian.**
Skrypt uruchamia obie implementacje na pierwszych 50 parach i porównuje podziały:
**szybka 14 zdarzeń, wprost 14, podziały identyczne.**

## 1. Cztery liczby z §2

**Zdarzeń z 10 562 par: 767.**

Rozkład wielkości: mediana **1**, p90 **5**, największe **8 899**, jednoparowych **459**
(59,8% zdarzeń).

Progi ostrzejsze:

| próg | par | zdarzeń | największe | udział największego | A × B w największym |
|---:|---:|---:|---:|---:|---|
| 0,2719 | 10 562 | **767** | 8 899 | 84,3% | 669 × 1615 |
| 0,29 | 6 092 | 576 | 4 900 | 80,4% | 459 × 1059 |
| 0,31 | 3 299 | 423 | 2 309 | 70,0% | 288 × 581 |
| 0,33 | 1 827 | 306 | 1 015 | 55,6% | 142 × 299 |
| 0,35 | 1 040 | **200** | 451 | 43,4% | 71 × 131 |
| 0,37 | 602 | 118 | 207 | 34,4% | 34 × 36 |
| 0,40 | 292 | **65** | 122 | 41,8% | 18 × 21 |
| 0,43 | 136 | 36 | 72 | 52,9% | 10 × 16 |
| 0,45 | 78 | **20** | 45 | 57,7% | 9 × 13 |
| 0,48 | 28 | 8 | 19 | 67,9% | 5 × 8 |

**Spadek jest łagodny, naturalnego odcięcia nie ma.** 767 → 576 → 423 → 306 → 200 → 118 → 65 → 36
→ 20 → 8, monotonicznie, bez skoku.

## 2. Liczba 767 jest zaniżona i nie wolno jej czytać wprost

Największe „zdarzenie" przy progu 0,2719 ma **8 899 par obejmujących 669 różnych terminów *A*
i 1 615 różnych *B*, z `y₀` rozrzuconym od 2009 do 2022.** To nie jest zdarzenie. To gigantyczna
składowa spójna, zlepiona domknięciem przechodnim.

Losowe pary z jej wnętrza:

```
bundled payment             -> identifying patient           0.2845  y0=2022
to the cochrane             -> included randomized controlled 0.2774  y0=2022
from the nationwide         -> healthcare cost               0.2759  y0=2017
with cli                    -> independent predictor         0.3072  y0=2021
review author independently -> searched                      0.3835  y0=2016
drug eluting stent          -> free survival afs             0.3815  y0=2020
```

CLI/CLTI, metodyka przeglądów Cochrane, baza NIS, płatności pakietowe i stenty siedzą w jednym
„zdarzeniu", bo łańcuch połączeń biegnie przez wspólne tokeny, para po parze, i każde ogniwo
z osobna spełnia regułę.

**Dla porównania, przy progu 0,45 ta sama reguła zachowuje się poprawnie**: największa składowa
to 45 par, 9 terminów *A* i 13 *B*, wyłącznie warianty jednego zdarzenia:

```
A: cli, cli patient, critical limb ischemia, for cli, for critical, for critical limb,
   limb ischemia cli, patient with cli, with cli
B: and major amputation, chronic limb threatening, clti, clti and, clti patient,
   for chronic limb, for clti, limb event male, limb threatening, limb threatening ischemia,
   patient with clti, threatening ischemia clti, with clti
```

Wskaźnikiem perkolacji jest **rozpiętość** największej składowej (kolumna A × B), nie jej udział.
Udział spada do 34% przy 0,37 i potem rośnie, ale to dlatego, że przy wysokich progach prawie
wszystko, co zostaje, **jest** zdarzeniem CLI/CLTI. Rozpiętość spada monotonicznie: 669×1615 →
71×131 → 18×21 → 9×13. Przejście od sklejki do rozmiaru wiarygodnego dla jednego zdarzenia
wypada gdzieś między 0,40 a 0,43.

Wniosek: **766 zdarzeń poza gigantem plus nieznana liczba wewnątrz niego.** Prawdziwy count przy
0,2719 jest istotnie wyższy niż 767, a o ile — nie wiadomo bez reguły, która nie perkoluje.
Zgłaszam to zamiast zmieniać regułę, zgodnie z Twoim §1.

## 3. Trzydzieści największych zdarzeń przy progu 0,2719

Reprezentant = para o najwyższym podobieństwie w zdarzeniu. **Werdyktów nie wystawiam.**

| par | poprzednik *A* | termin *B* | y₀ | najlepsze |
|---:|---|---|---:|---:|
| 8899 | critical limb ischemia | limb threatening | 2021 | 0,5968 |
| 24 | killed | inc j biomed | 2016 | 0,2893 |
| 21 | and analysis two | pedro | 2017 | 0,3143 |
| 16 | supplementary | transforaminal lumbar interbody | 2022 | 0,2763 |
| 14 | critical limb ischemia | evt | 2022 | 0,4553 |
| 14 | restenosis | limb threatening ischemia | 2020 | 0,4305 |
| 14 | metal bearing | adverse local tissue | 2014 | 0,3381 |
| 14 | particle of | biomed mater res | 2016 | 0,2945 |
| 13 | day episode | race and | 2022 | 0,3199 |
| 13 | 9 code | to identify patient | 2022 | 0,3071 |
| 13 | propionibacterium | joint infection pjis | 2021 | 0,3070 |
| 12 | critical limb ischemia | hr | 2020 | 0,4355 |
| 12 | epidural analgesia | management after total | 2018 | 0,3235 |
| 11 | question purpose we | interquartile range | 2018 | 0,3316 |
| 11 | study see | joint infection | 2017 | 0,3011 |
| 10 | femoral nerve block | canal block acb | 2019 | 0,4685 |
| 10 | and histomorphometric | prf | 2021 | 0,3817 |
| 10 | bundled | metropolitan | 2021 | 0,3359 |
| 10 | and operation was | internal fixation failure | 2018 | 0,3088 |
| 10 | administrative data | ethnicity | 2022 | 0,3034 |
| 9 | bare metal | limb threatening ischemia | 2020 | 0,3815 |
| 9 | capsular plication | rate of achieving | 2021 | 0,3221 |
| 9 | electronic supplementary material | junctional kyphosis | 2021 | 0,3117 |
| 9 | old ranging from | internal fixation failure | 2018 | 0,3096 |
| 9 | electronic supplementary material | pi | 2020 | 0,3047 |
| 8 | bundled | deprivation | 2022 | 0,3775 |
| 8 | lateral transpsoas approach | lateral lumbar | 2016 | 0,3279 |
| 8 | periprocedural | limb threatening ischemia | 2020 | 0,3227 |
| 8 | hospital had | ethnicity | 2022 | 0,3092 |
| 8 | slide can be | study patient sample | 2022 | 0,2785 |

Zwracam uwagę, że `restenosis → limb threatening ischemia`, `bare metal → limb threatening ischemia`
i `periprocedural → limb threatening ischemia` są **osobnymi** zdarzeniami, nie częścią giganta —
reguła wymaga wspólnego tokenu po obu stronach, a te terminy *A* nie dzielą żadnego z CLI. Tam,
gdzie reguła nie ma jak połączyć, działa poprawnie; gigant powstaje z łańcucha, nie z jednego
tokenu.

## 4. Wobec kryterium z §4

Przy progu, o który pytałeś, wychodzi **kilkaset → generator**, i to jest odpowiedź przy dosłownym
odczycie liczby. Z zastrzeżeniem, które idzie w tę samą stronę: 767 to dolne oszacowanie, bo gigant
połyka nieznaną liczbę prawdziwych zdarzeń, więc prawdziwa liczba jest wyższa, nie niższa.

„Kilkadziesiąt" pojawia się dopiero przy progach 0,43–0,45, gdzie zostaje odpowiednio 136 i 78 par.
Ale to nie jest odcięcie znalezione w danych — spadek jest gładki na całej długości i próg trzeba
by wybrać arbitralnie, po zobaczeniu wyniku.

Zatrzymuję się na liczbach.

## 5. Wykonane poza countem

`liczby_do_metod.md` uzupełnione o Twoje §3 i §5:

- **Obserwacja post hoc o wspólnych pracach**, z nagłówkiem mówiącym wprost, że została zauważona
  po zobaczeniu danych i **nie została użyta** do żadnego wyboru ani progu. Z liczbami: mediana 8,
  zakres 0–331, CLI/CLTI 0–13, `question purpose` 268–331.
- **Zakres okien do diagramu przepływu**: `y₀` 2009–2022, odpada 1 053 z 7 662, zostaje 6 609;
  8 384 866 par, 13 odrzuconych przez wykluczenie zawierania, zostaje 8 384 853.

Dopisałem też perkolację reguły grupowania, bo to jest własność narzędzia, nie jednorazowa liczba.

## 6. Stan

Manifest **12/12**. Arkusz zamrożony bez zmian. `coding_sheet_koder_CODED_*.csv` w `.gitignore`,
nietknięty.
