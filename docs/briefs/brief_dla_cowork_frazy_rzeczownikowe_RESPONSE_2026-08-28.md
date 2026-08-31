# Frazy rzeczownikowe — kryterium z §6 spełnione w obu punktach, ale rdzeń kurczy się do 47

Autor: sesja VS Code, 2026-08-28. Dotyczy: `brief_dla_vsc_frazy_rzeczownikowe_2026-08-28.md`.

Skrypty: `code/extract_noun_phrases.py`, `code/count_noun_phrases.py`, `code/np_report.py`.
Wyjścia: `data/processed/emerging_core_np.json`, `data/processed/core_np_ranking.csv`,
tabele `terms_np_*` i `emerging_np_*` w katalogu roboczym.

---

## 0. Parser — odstępstwo do zgłoszenia

**spaCy 3.8.16 + `en_core_web_sm` 3.8.0**, przypięte i wypisane w nagłówku skryptu oraz
w `noun_chunks.meta.json`.

**scispaCy sprawdzone i odrzucone**: przypina `spacy<3.8`, co pociąga `thinc<8.3`, a to nie ma kół
dla Pythona 3.13 i nie buduje się ze źródeł w tym środowisku. Zgłaszam jako odstępstwo, bo model
ogólnojęzykowy chunkuje tekst biomedyczny gorzej niż `en_core_sci_sm`. Gdyby to miało znaczenie
dla decyzji, dałoby się postawić osobne środowisko z Pythonem 3.11 — ale to osobna robota.

Kontrola na zdaniu testowym wypada dobrze: `3D rapid prototyping technology`,
`robotic-assisted total knee arthroplasty` wychodzą jako całe frazy, `was included` nie wychodzi
wcale.

## 1. Tabela porównawcza z §4

| wielkość | n-gramy | frazy | zmiana |
|---|---:|---:|---|
| jednostek powyżej progu 50 | 245 081 | **25 419** | ÷9,6 |
| wschodzących (primary) | 7 662 | **936** | ÷8,2 |
| rdzeń (część wspólna 4 wariantów) | 287 | **47** | ÷6,1 |
| rodzin zawierania w rdzeniu / objętych | 46 / 140 | **4 / 8** | ÷11,5 / ÷17,5 |
| wierszy rodziny `robot*` w rdzeniu | 8 | **1** | ÷8 |
| wierszy rodziny `3d`/`print*` w rdzeniu | 4 | **0** | — |

Per wariant:

| wariant | jednostek | wschodzących |
|---|---:|---:|
| primary | 25 419 | 936 |
| S1 (tytuł) | **1 882** | **85** |
| S2 (ze streszczeniem) | 25 277 | 929 |
| S3 (angielskie) | 23 855 | 957 |

Ekstrakcja: 17,7 mln chunków z 268 383 rekordów (4,2 z tytułu, 61,7 ze streszczenia), 24,4 min.

## 2. Kryterium z §6 — spełnione w obu punktach

**Szablon abstraktu zniknął całkowicie.** W pięćdziesiątce n-gramowej były `were included`,
`95 ci`, `question purpose`, `result a total`, `method this`, `arthroplasty a meta`. We frazowej
**nie ma ani jednego takiego wiersza**. Zostały nazwy typów badań (`systematic review`,
`meta analysis`, `retrospective cohort study`, `cross sectional study`, `network meta analysis`) —
ale to są byty, które coś nazywają, nie urwane fragmenty składniowe.

**Rodzina `robot*`: 8 wierszy → 1**, i to `robotic assisted total knee arthroplasty`, czyli fraza
nazywająca całą rzecz zamiast siedmiu fragmentów. Kryterium mówiło „najwyżej dwa–trzy".

Fragmentacja spadła w całym rdzeniu, nie tylko w tej rodzinie: **4 rodziny obejmujące 8 fraz**
wobec 46 rodzin obejmujących 140 terminów.

## 3. Koszt: rdzeń 287 → 47, i wiadomo dokładnie dlaczego

**Wąskim gardłem jest S1.** Część wspólna primary ∩ S2 ∩ S3 ma **813 fraz**. Dołożenie S1 zostawia
**47** — czyli **S1 usuwa 94,2%**.

Przyczyna jest mechaniczna: tytuł daje 4,2 chunku, streszczenie 61,7. Przy niezmienionym progu
≥ 50 wystąpień słownik S1 ma **1 882 frazy** wobec 25 419 w primary. Fraza jest jednostką znacznie
bardziej szczegółową niż n-gram, więc w samych tytułach rzadko dobija do progu.

To był ten sam mechanizm przy n-gramach (S1: 607 wyłonień wobec 7 662) — tyle że tam zostawało
287, a tu 47. **Zmiana jednostki nie stworzyła tego problemu, tylko go zaostrzyła.**

## 4. Czego nie ma w rdzeniu, i w których wariantach jest

Pozycje z §4 pkt 2. Nazwy po frazowaniu wychodzą tak samo, żadna nie zmieniła postaci.

| termin | primary | S1 | S2 | S3 | pozycja w rdzeniu |
|---|:--:|:--:|:--:|:--:|---:|
| artificial intelligence | wschodzi | wschodzi | wschodzi | wschodzi | **27** |
| machine learning | wschodzi | wschodzi | wschodzi | wschodzi | **30** |
| 3d printing | wschodzi | w słowniku | wschodzi | wschodzi | poza |
| augmented reality | wschodzi | w słowniku | wschodzi | wschodzi | poza |
| virtual reality | wschodzi | — | wschodzi | wschodzi | poza |
| robotic | wschodzi | — | wschodzi | — | poza |
| deep learning | w słowniku | — | w słowniku | w słowniku | poza |
| navigation | w słowniku | w słowniku | w słowniku | w słowniku | poza |
| 3d printed | — | — | — | — | poza |
| robotic assisted | — | — | — | — | poza |
| patient specific | — | — | — | — | poza |

`3d printed`, `robotic assisted` i `patient specific` nie istnieją jako frazy, bo to **fragmenty**
fraz — po frazowaniu wchodzą w `robotic assisted total knee arthroplasty` i podobne. To jest
dokładnie skutek, o który chodziło, tylko widziany od strony strat.

`3d printing` wschodzi w trzech wariantach z czterech i jest w słowniku S1 — wypada z rdzenia
na progu S1, nie z powodu jednostki.

## 5. Długości fraz w rdzeniu (§4 pkt 3)

| długość | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| fraz | 4 | 16 | 18 | 7 | 2 |

Dwutokenowe i trzytokenowe to 34 z 47 (72%). Jednotokenowych są cztery: `readmission`, `md`,
`frailty`, `rivaroxaban`.

## 6. Nowa klasa śmieci, której n-gramy nie miały

Frazowanie wprowadza **gołe liczebniki jako chunki**: `0 0`, `10 1`, `12 4`, `13 9`, `15 0`.
W części wspólnej bez S1 (813 fraz) jest ich **32, czyli 3,9%**; fraz zawierających samodzielną
liczbę — 60, czyli 7,4%.

Reguła tokena-rocznika z §3.1 tego nie łapie, bo dotyczy tylko czterocyfrowych z zakresu
1900–2100. **Nie dopisuję reguły** — zgłaszam, zgodnie z §2.

W rdzeniu 47 czysto liczbowych jest **zero**; jedyne dwie frazy z liczbą to `covid 19`
i `covid 19 pandemic`. S1 odsiewa je przy okazji, ale gdyby zrezygnować z S1 dla odzyskania
rdzenia, ta klasa wróci i będzie trzeba się nią zająć.

## 7. Pięćdziesiąt pierwszych rdzenia — dosłownie, bez oceny

Rdzeń ma 47 fraz, więc to cała lista.

| # | fraza | n | y₀ | prevalence 2021–25 |
|---:|---|---:|---:|---:|
| 1 | systematic review | 2 | 2014 | 6,525% |
| 2 | meta analysis | 2 | 2014 | 4,775% |
| 3 | retrospective cohort study | 3 | 2017 | 3,292% |
| 4 | patient reported outcome | 3 | 2010 | 2,447% |
| 5 | periprosthetic joint infection | 3 | 2011 | 2,344% |
| 6 | patient reported outcome measure | 4 | 2011 | 2,042% |
| 7 | readmission | 1 | 2016 | 1,630% |
| 8 | postoperative outcome | 2 | 2022 | 1,621% |
| 9 | clinical efficacy | 2 | 2020 | 1,400% |
| 10 | surgical site infection | 3 | 2017 | 1,179% |
| 11 | md | 1 | 2010 | 0,950% |
| 12 | reverse total shoulder arthroplasty | 4 | 2013 | 0,806% |
| 13 | chronic limb threatening ischemia | 4 | 2019 | 0,760% |
| 14 | reverse shoulder arthroplasty | 3 | 2011 | 0,617% |
| 15 | adult spinal deformity | 3 | 2017 | 0,594% |
| 16 | editorial commentary | 2 | 2015 | 0,564% |
| 17 | tranexamic acid | 2 | 2015 | 0,557% |
| 18 | cross sectional study | 3 | 2018 | 0,508% |
| 19 | direct anterior approach | 3 | 2015 | 0,498% |
| 20 | femoroacetabular impingement syndrome | 3 | 2018 | 0,442% |
| 21 | peripheral artery disease | 3 | 2014 | 0,411% |
| 22 | covid 19 | 2 | 2020 | 0,382% |
| 23 | enhanced recovery | 2 | 2018 | 0,381% |
| 24 | lumbar degenerative disease | 3 | 2019 | 0,368% |
| 25 | secondary analysis | 2 | 2020 | 0,359% |
| 26 | proximal junctional kyphosis | 3 | 2016 | 0,345% |
| 27 | artificial intelligence | 2 | 2021 | 0,343% |
| 28 | covid 19 pandemic | 3 | 2020 | 0,329% |
| 29 | percutaneous kyphoplasty | 2 | 2016 | 0,325% |
| 30 | machine learning | 2 | 2019 | 0,322% |
| 31 | frailty | 1 | 2020 | 0,310% |
| 32 | network meta analysis | 3 | 2017 | 0,298% |
| 33 | study protocol | 2 | 2019 | 0,296% |
| 34 | anatomic total shoulder arthroplasty | 4 | 2017 | 0,292% |
| 35 | robotic assisted total knee arthroplasty | 5 | 2021 | 0,292% |
| 36 | narrative review | 2 | 2019 | 0,283% |
| 37 | scoping review | 2 | 2021 | 0,269% |
| 38 | mid term outcome | 3 | 2016 | 0,223% |
| 39 | adult spinal deformity surgery | 4 | 2016 | 0,223% |
| 40 | adductor canal block | 3 | 2016 | 0,192% |
| 41 | oblique lumbar interbody fusion | 4 | 2019 | 0,190% |
| 42 | percutaneous endoscopic lumbar discectomy | 4 | 2016 | 0,188% |
| 43 | femoral neck system | 3 | 2022 | 0,167% |
| 44 | early onset scoliosis | 3 | 2013 | 0,159% |
| 45 | open wedge high tibial osteotomy | 5 | 2016 | 0,155% |
| 46 | rivaroxaban | 1 | 2008 | 0,071% |
| 47 | clinical article | 2 | 2012 | 0,001% |

Jedna obserwacja faktograficzna, nie ocena: **`chronic limb threatening ischemia` stoi na 13,
a `adductor canal block` na 40.** To są dokładnie te dwa zdarzenia, które test podobieństw
kontekstowych wyłowił z ośmiu milionów par jako najwyżej punktowane — tutaj pojawiają się same,
jako pojedyncze frazy, bez żadnego liczenia podobieństw.

## 8. Podsumowanie

Kryterium z §6 jest spełnione w obu punktach jednocześnie, więc według postawionej z góry reguły
**jednostka jest lepsza**. Szablon abstraktu znika, fragmentacja spada z 46 rodzin do 4.

Cena: rdzeń 47 zamiast 287, i to nie z winy jednostki, tylko przez interakcję jednostki z progiem
≥ 50 w wariancie tytułowym. Odzyskanie rdzenia wymagałoby ruszenia S1 albo progu — obie rzeczy są
poza tym briefem i obie zmieniałyby coś prerejestrowanego.

Nie liczyłem podobieństw ani par (§5). Nie oceniam list.

## 9. Stan

Manifest **12/12**. Zamrożone pliki nietknięte, wszystkie wyjścia z przyrostkiem `_np`.
`coding_sheet_koder_CODED_*.csv` w `.gitignore`, nietknięty.
