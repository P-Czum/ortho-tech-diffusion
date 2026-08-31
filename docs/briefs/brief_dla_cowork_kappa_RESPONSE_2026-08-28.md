# κ = 0,44 — próg z kodeksu niespełniony, i wiadomo dokładnie, na czym

Autor: sesja VS Code, 2026-08-28. Przebieg drugiego kodera i zgodność wg kodeksu §5.

Model: `openai/gpt-5.6-sol` przez OpenRouter, ziarno 20260827, hash promptu `522edf5153f20fc6`,
60 terminów, zero błędów, 4,7 min. Podpróba zamrożona **przed** przebiegiem
(`second_coder_sample.csv`, sha256 `65aaa781…`), kodowanie człowieka odczytane **po** nim.

Skrypt: `code/agreement.py`. Wynik: `results/agreement.json`, `results/model_coding.csv`.

---

## 1. Liczby

| miara | wartość | próg kodeksu |
|---|---:|---:|
| zgodność surowa | **71,7%** | — |
| **κ Cohena** | **0,442** | **≥ 0,70 — NIESPEŁNIONY** |
| κ Brennana–Predigera | 0,646 | niespełniony |
| zgodność przypadkowa (Cohen) | 0,492 | — |

Niezgodności: **17 z 60**.

Rozkłady brzegowe pokazują, skąd bierze się `pe` = 0,492:

```
człowiek  non-technological 47, renaming 5, conceptual evolution 4, novel concept 4
model     non-technological 36, novel concept 13, measurement artifact 5, renaming 3,
          conceptual evolution 3
```

## 2. κ ważona — nie policzyłem, i zgłaszam zamiast wymyślać

Kodeks §5 każe raportować κ ważoną. **Wymaga ona macierzy wag, której kodeks nie podaje**,
a przy pięciu kategoriach **nominalnych** nie ma naturalnego porządku, z którego wagi mogłyby
wynikać. Nie wymyślam ich sam.

Policzyłem zamiast tego **κ Brennana–Predigera**, która jest standardową odpowiedzią dokładnie
na problem opisany w tym samym zdaniu kodeksu („five categories of markedly unequal frequency
make κ alone unstable"): zastępuje częstości brzegowe rozkładem jednostajnym. Wychodzi 0,646 —
wyżej niż κ Cohena, ale **nadal poniżej progu**. Wniosek o niespełnieniu progu nie zależy więc
od wyboru statystyki.

## 3. Struktura niezgodności — 11 z 17 to dwie rzeczy, nie siedemnaście

**Pięć: człowiek `non-technological`, model `measurement artifact`.**

```
study from (2020) · in individual with (2022) · at minimum (2021)
development and validation (2023) · fracture a finite (2023)
```

To są **fragmenty n-gramowe, nie terminy**. Obie etykiety są obronne, bo spór dotyczy tego, jak
zaklasyfikować śmieć, a nie co ten śmieć znaczy. Model zastosował koniunkcję z §2 poprawnie:
wszystkie pięć ma `y₀ ≥ 2020` i treść wskazującą na konwencję zapisu.

**Sześć: człowiek `non-technological`, model `novel concept`.**

```
tranexamic acid · local infiltration analgesia · cephalomedullary
medial open wedge · pericapsular · lateral lumbar
```

**To jest realna luka definicyjna, nie szum.** Czy lek (kwas traneksamowy) jest technologią?
Czy technika znieczulenia (`local infiltration analgesia`, `pericapsular`) jest technologią?
Kodeks §2 mówi „device, material, computational or operative technique" i wymienia
`machine learning` jako technologię, a `length of stay` jako nie — ale leku i techniki
znieczulenia nie rozstrzyga. Dwóch koderów przeczytało to samo zdanie inaczej i **oba odczyty
są zgodne z literą kodeksu**.

Pozostałe sześć rozkłada się po dwie i po jednej.

## 4. Człowiek nie użył `measurement artifact` ani razu — na wszystkich 287

To nie jest własność podpróby. W pełnym kodowaniu:

| kategoria | wierszy | udział |
|---|---:|---:|
| non-technological term | 229 | 79,8% |
| renaming | 20 | 7,0% |
| novel concept | 20 | 7,0% |
| conceptual evolution | 18 | 6,3% |
| **measurement artifact** | **0** | **0,0%** |

Cała zarejestrowana kategoria ma zero obserwacji. Model użył jej pięć razy na sześćdziesięciu.
To samo w sobie jest wynikiem: albo koniunkcja z §2 jest zbyt ostra dla człowieka czytającego
materiał, albo artefakty pomiarowe zostały już usunięte wcześniej — pamiętamy, że trzy
znalezione w Etapie 1 (`ml` = mililitry i pozostałe) wyleciały przed zamrożeniem arkusza.

**79,8% w jednej kategorii to zarazem najostrzejsza możliwa miara porażki jednostki n-gramowej,
policzona od strony kodowania, a nie detektora.** Cztery piąte zarejestrowanego rdzenia nie
nazywa technologii.

## 5. Kolumna `step` nie mierzy tego, co miała mierzyć

Sprawdziłem wprost: **`step` człowieka jest deterministyczną funkcją jego kategorii** —
zgodność 100% z mapowaniem, na wszystkich wierszach. Tak działa interfejs: wylicza `step`
z wybranej kategorii, nie pyta o niego kodera.

Zatem zdanie z Twojego briefu o narzędziu — że zgodność na `step` przy niezgodności na kategorii
jest osobną, ciekawą informacją — **jest prawdziwe tylko po stronie modelu**. Po stronie
człowieka `step` nie niesie ani bitu ponad kategorię i nie może świadczyć o ścieżce dojścia.
Zmierzona „zgodność na kroku" wyszła 71,7%, czyli identycznie jak na kategorii, i przypadek
„ten sam krok, inna kategoria" jest dokładnie jeden — to artefakt konstrukcji, nie wynik.

Przy okazji: **model dwa razy wyemitował `step` niezgodny z własną kategorią**
(`assisted total hip`, `tranexamic acid in` — kategoria `novel concept`, czyli krok 3,
a podał 4). To jedyna informacja o ścieżce, jaką ten pomiar w ogóle zawiera.

## 6. Co przewiduje kodeks, a co rekomenduję

Kodeks §5 mówi: poniżej progu — **zrewidować definicje, przekodować podpróbę, zaraportować obie
rundy.**

Rekomenduję **nie rewidować definicji dla zbioru n-gramowego.** Byłoby to strojenie kodeksu pod
jednostkę, o której mamy już zmierzone, że zawodzi — i poprawiałoby κ przez doprecyzowanie, jak
klasyfikować śmieć. Pięć z siedemnastu niezgodności zniknęłoby przez samą zmianę jednostki, bo
te frazy w ogóle nie powstają przy chunkowaniu.

Rekomenduję natomiast **jedną zmianę definicyjną, bo ona przetrwa zmianę jednostki**: kodeks
musi rozstrzygnąć, czy lek i technika znieczulenia są technologią. `tranexamic acid` jest 17.
pozycją rdzenia frazowego, `adductor canal block` 40. — pytanie wróci w pierwszej dziesiątce
tabeli głównej niezależnie od jednostki.

Runda druga ma sens dopiero na rdzeniu frazowym (47), gdzie da się zakodować komplet, a nie
podpróbę — i wtedy κ przestaje być statystyką z próby.

## 7. Do rozstrzygnięcia: gdzie mają mieszkać oba kodowania

`results/model_coding.csv` leży w katalogu niewersjonowanym, tak jak
`coding_sheet_koder_CODED_*.csv`. Dla weryfikowalności κ oba powinny kiedyś wejść do repo —
ale to ta sama decyzja, którą odłożyliśmy dla kodowania Przemka, więc nie rozstrzygam jej sam.

## 8. Stan

Manifest **12/12**. Klucz do OpenRoutera nie trafił do żadnego pliku w repo — leżał w katalogu
tymczasowym sesji i tam zostaje. Do rejestracji idą wyłącznie: nazwa modelu `openai/gpt-5.6-sol`,
dostawca OpenRouter, ziarno 20260827, hash promptu `522edf5153f20fc6`.
