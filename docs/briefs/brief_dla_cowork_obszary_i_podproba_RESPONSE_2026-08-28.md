# Rozkład 47 po obszarach, podpróba drugiego kodera, i rozbieżność kodeks–kod

Autor: sesja VS Code, 2026-08-28. Decyzja Przemka: 47 fraz to wystarczająca lista, S1 zostaje.

---

## 1. Rozkład 47 fraz po obszarach ortopedii

Liczony z **MeSH prac zawierających frazę**, nie z mojego osądu o terminie. Obszar przypisany,
gdy ≥ 50% prac danej frazy ma w MeSH słowo kluczowe obszaru; inaczej „przekrojowy".
Wynik: `results/np_core_obszary.csv`.

| obszar | fraz |
|---|---:|
| kręgosłup | **9** |
| kolano | 5 |
| bark | 3 |
| biodro | 3 |
| naczynia | 2 |
| **przekrojowy** | **25** |
| stopa i staw skokowy | **0** |
| ręka i nadgarstek | **0** |
| łokieć | **0** |

**22 z 47 lokalizują się anatomicznie, 25 jest przekrojowych.** Wśród zlokalizowanych kręgosłup
ma 9 pozycji, czyli więcej niż bark, biodro i naczynia razem.

**Zero pozycji dla stopy, ręki i łokcia.** To jest realne ograniczenie dla zdania „co wyłoniło się
w ortopedii" i lepiej je nazwać samemu. Nie wiem jeszcze, czy to własność piśmiennictwa (chirurgia
ręki i stopy publikuje w osobnych czasopismach, które definicja pola przez poddrzewo MeSH może
łapać słabiej), czy artefakt progu ≥ 50 — to jest sprawdzalne i warte sprawdzenia przed pisaniem.

Jedno chybienie mojego mapowania, które zgłaszam zamiast poprawiać: **`femoral neck system`
wylądował jako „przekrojowy" przy 15%**, bo lista słów kluczowych dla biodra ma `femur head`,
a złamania szyjki kości udowej mają w MeSH `Femoral Neck Fractures`. Fraza jest oczywiście
biodrowa. Mapowanie jest pomocnicze i nie wchodzi do żadnej liczby poza tą tabelą.

Osobna ciekawostka: `clinical article` przypisało się do kręgosłupa w 72% prac — to nie jest
termin kliniczny, tylko formuła redakcyjna czasopisma neurochirurgii kręgosłupa.

## 2. Podpróba drugiego kodera — wylosowana i zamrożona

`data/processed/second_coder_sample.csv`, sha256 `65aaa78119c8c9f4…`,
skrypt `code/draw_second_coder_sample.py`, ziarno **20260827** (to samo, które jest w rejestracji).

Wylosowana **na widoku zaślepionym, przed jakimkolwiek przebiegiem modelu i bez wglądu w kodowanie
Przemka** — skrypt sprawdza to jawnie i odmawia działania, gdyby arkusz zawierał kategorie.

| epoka | n=1 | n=2 | n=3 | razem | kodeks §5 |
|---|---:|---:|---:|---:|---:|
| 2005–2012 | 1 | 2 | 3 | **6** | 6 |
| 2013–2019 | 5 | 13 | 18 | **36** | 36 |
| 2020+ | 2 | 6 | 10 | **18** | 18 |

Alokacja epokowa zgadza się z zarejestrowaną co do jednego terminu.

## 3. Rozbieżność do zgłoszenia: kodeks §5 kontra `llm_coder.py`

Kodeks v1.2 §5 — **zamrożony i w manifeście** — mówi:

> stratified random sample by `y₀` epoch (…) **and n-gram length**

Funkcja `stratified()` w `llm_coder.py:69` warstwuje **wyłącznie po epoce**. Długości n-gramu nie
uwzględnia wcale. Rozbieżność jest w kodzie, nie w rejestracji, więc rozstrzygnięcie jest
jednoznaczne: **wiążący jest kodeks.**

Rozwiązałem to bez dotykania `llm_coder.py`: podpróbę losuje osobny skrypt zgodnie z regułą
zarejestrowaną, a modelowi poda się gotowy plik przez `--sheet` z `--n 0`. Dzięki temu nie ma
dwóch implementacji tej samej reguły, które mogłyby się rozjechać.

Kwoty komórek wychodzą ułamkowe (0,6 / 1,9 / 3,1 …), więc zaokrąglam metodą **największych
reszt** — deterministyczną i sumującą się dokładnie do 60. To jest doprecyzowanie, którego kodeks
nie zawiera, bo nie przewidział warstwowania krzyżowego; zapisuję je jawnie w nagłówku skryptu.

`stratified()` zostaje w `llm_coder.py` nieużywana. Nie usuwam jej — to nie jest mój bałagan —
ale zgłaszam, bo przy `--n 60` nadal by się odpaliła i dałaby inną podpróbę niż zarejestrowana.

## 4. Blokada: brak klucza

`OPENROUTER_API_KEY` nie jest ustawiony w środowisku, więc przebiegu modelu-kodera nie da się
uruchomić. Wszystko, co go poprzedza, jest gotowe: podpróba zamrożona, prompty w manifeście,
`llm_coder.py` gotowy do przyjęcia gotowej listy.

Przypominam, że klucz **nie wchodzi do żadnego pliku ani do rejestracji** — do rejestracji idzie
wyłącznie nazwa modelu, dostawca i ziarno. Klucz zostaje w zmiennej środowiskowej.

## 5. Stan

Manifest **12/12**. Zamrożone pliki nietknięte. `coding_sheet_koder_CODED_*.csv` w `.gitignore`,
nietknięty i nieprzeczytany co do treści kategorii.
