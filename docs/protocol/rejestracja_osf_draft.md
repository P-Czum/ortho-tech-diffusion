# Rejestracja OSF — projekt do zatwierdzenia
## Emerging concepts in orthopaedic literature: distinguishing novelty from renaming
2026-08-27 · szablon: OSF Secondary Data Analysis Preregistration · status: DRAFT do wklejenia

---

## 1. Pytania badawcze

1. Które pojęcia w piśmiennictwie ortopedii proceduralnej wyłoniły się między 2005 a 2025
   i w którym roku (`year of emergence`)?
2. Jak silne było każde wyłonienie: szerokość dyfuzji piśmienniczej (koncentracje), tempo
   (czas podwojenia), pułap (maksymalny udział w polu)?
3. Jaki odsetek wyłonień to nowe pojęcia, a jaki — nowe nazwy lub ewolucje pojęć istniejących
   (pięć kategorii: novel concept / renaming / conceptual evolution / measurement artifact /
   non-technological term)?

Badanie mierzy uwagę naukową w piśmiennictwie, nie adopcję kliniczną. Charakter: odkrywczy
z prerejestrowanym aparatem — rejestrujemy detektor, progi i kodeks osądu, nie przewidywane wyniki.

## 2. Dane — istniejące przed rejestracją

PubMed Baseline 2026 (`pubmed26n0001`–`n1334`, wydany 2026-01-30) + pliki aktualizacyjne,
lustro lokalne, deduplikacja (ostatni plik wygrywa; `DeleteCitation` usuwa rekord).
Pole podstawowe: MeSH `Orthopedic Procedures` + potomne (56 deskryptorów, rozwinięte
programowo z desc2026.xml) — 268 383 rekordy, 2005–2025. Pole drugie (analiza wtórna):
137 czasopism NLM Broad Subject Term „Orthopedics" — 281 261 rekordów.

## 3. Co zostało już wykonane (jawna deklaracja)

Wykonane przed rejestracją: budowa lustra i deduplikacja; obie definicje pola; kanonikalizacja
n-gramów (listy zamrożone); detekcja wyłonień z wariantami wrażliwości S1–S3 (rdzeń 287
terminów = część wspólna czterech wariantów); osie siły; kandydaci na poprzednika (lift ≥ 3
jako narzędzie wyszukiwania); zamrożenie arkusza i kodeksu (hashe niżej).

**Niewykonane: kodowanie kategorii.** Żaden termin nie został zaklasyfikowany do żadnej
z pięciu kategorii przez żadnego kodera. Rozkład kategorii — główny wynik pytania 3 —
jest nieznany w chwili rejestracji.

## 4. Detektor (zamrożony)

Udział terminu w polu `s(y)`; próg obecności θ = 0,1% rekordów pola i ≥ 5 prac; rok wyłonienia
`y₀` = pierwszy rok, w którym `s(y) ≥ max(θ, 5 × baza 2005–2007)` utrzymane ≥ 3 kolejne lata;
`y₀ ≤ 2023`. Rdzeń do kodowania: terminy wschodzące we wszystkich czterech wariantach
tekstowych (tytuł+abstrakt / tylko tytuł / tylko rekordy z abstraktem / tylko angielskie).

## 5. Kodowanie

Kodeks: `kodeks_kodowania_v1.1.md` (hash niżej) — definicje operacyjne pięciu kategorii,
test podstawienia (obustronny = renaming, jednostronny = conceptual evolution), drzewo
decyzyjne, zaślepienie kodera (bez czasu podwojenia, osi koncentracji i wyników def2).

**Koder 1 (całość, 287):** P. Czuma, wg kodeksu v1.1, z widokiem zaślepionym
i narzędziem przeszukiwania z logiem.

**Koder 2 (podpróba 60):** model językowy `openai/gpt-5.6-sol` przez OpenRouter,
seed 20260827, prompty zamrożone przed kodowaniem (`prompt_system_v1.1.txt`,
`prompt_user_v1.1.txt`, hashe niżej; parametr temperature niewspierany przez model —
determinizm przez seed). Model otrzymuje wyłącznie widok zaślepiony (te same kolumny,
co koder 1) i stosuje tę samą procedurę z kodeksu. Podpróba losowana warstwowo:
epoka `y₀` (2005–2012/2013–2019/2020+ → 6/36/18) × długość n-gramu.

Zgodność koder 1–koder 2: κ Cohena, próg ≥ 0,70; obok zgodność surowa i κ ważone.
Poniżej progu: rewizja definicji operacyjnych, ponowne kodowanie podpróby, raportowane
obie rundy. **Deklaracja wprost:** koder 2 jest modelem językowym, więc raportowane κ
jest zgodnością człowiek–model, nie klasyczną rzetelnością między dwiema osobami;
tak też będzie nazwane w metodach i omówione w ograniczeniach. W zamian koder 2 jest
w pełni odtwarzalny (model, dostawca, ziarno, hash promptu, log surowych odpowiedzi).
Model nie był i nie będzie dobierany na podpróbie; ewentualny pilotaż porównawczy modeli
mógłby użyć wyłącznie terminów spoza podpróby.

## 6. Analizy po kodowaniu (prespecyfikowane)

1. Rozkład pięciu kategorii w rdzeniu 287 — z obowiązkowym zastrzeżeniem zakresu: rdzeń jest
   przefiltrowany na odporność wariantową, więc udział artefaktów jest niski z konstrukcji;
   rozkład nie uogólnia się na pełny zbiór 7 662 wyłonień.
2. Kontrole zgodności: czas podwojenia vs kategoria; odtwarzalność w def2 vs kategoria;
   rozkład kategorii po epokach `y₀` (flaga ostrożności `y₀ ≥ 2020` — okno opóźnienia
   indeksowania).
3. `y₀` raportowany jako wartość def1 z wartością def2 obok; flaga przy różnicy > 2 lata.
4. Pary przemianowań: rycina stary-opada/nowy-rośnie/okno współwystępowania dla terminów
   zakodowanych jako renaming lub conceptual evolution.

## 7. Hashe zamrożonych plików (sha256)

```
5bfc3d6a7add370d23c505dfcaa0020a6f1ec6d9f2fbb3b90d4e8328fdae46a1  coding_sheet_full.csv
bf065aadc07350bd02117b3e86b714906e2fb21caefbaff7c0946861853f3588  coding_sheet_koder.csv
37a9f0b212a5af20d97e976883440d5177640e0f423fb20601d8cf89a645b3ba  kodeks_kodowania_v1.1.md
6d93683b3d298d7a2f5a6a2347ce89d3ad3e07d35418fffa9f581c3d17578bb1  prompt_system_v1.1.txt
f85019ebffa6e59135e397f3ad28d1ae506a37235cbbb3f71d83f3fd976b1a27  prompt_user_v1.1.txt
```
Pełny manifest (12 plików, w tym listy kanonikalizacji, definicja pola 56 UI, lista 137
czasopism, emerging_core.json): `docs/protocol/freeze_manifest.txt` w repozytorium projektu.

## 8. Odstępstwa

Każde odstępstwo od tej rejestracji będzie raportowane w publikacji z uzasadnieniem
i oznaczeniem jako post hoc.
