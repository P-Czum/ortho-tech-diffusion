# MTIX-2022: nieciągłość jest realna i duża — ale oś rankingu ją przeżywa

Autor: sesja VS Code, 2026-09-01. Dotyczy: §7 z `brief_dla_vsc_okno_2000_RESPONSE_2026-09-01.md`.

Skrypty: `code/mtix_check.py`, `code/mtix_impact.py`, `code/mtix_mechanizm.py`.
Wyniki: `results/mtix_check.json`, `mtix_impact.json`, `mtix_mechanizm.json`.

**Wniosek jednym zdaniem: nie zmieniamy osi ani mianownika. Idzie to do Ograniczeń, z liczbami.**

---

## 1. Test rozbity na trzy rozłączne hipotezy

Bo „udział pola spadł o 34%" nie mówi, czy to groźne. Rozłączne sygnały:

| | hipoteza | sygnał | groźna dla osi? |
|---|---|---|---|
| H1 | mniej prac indeksowanych w ogóle | spada odsetek rekordów z jakimkolwiek MeSH | nie, jeśli równomiernie |
| H2 | płytsze indeksowanie tych, które są | spada liczba deskryptorów na rekord | nie, jeśli równomiernie |
| H3 | przesunięcie **składu** deskryptorów | zmienia się ich rozkład | **tak** |

H1 i H2 są nieszkodliwe przy równomiernym działaniu, bo pole jest definiowane przez MeSH —
licznik i mianownik kurczą się razem. **H3 jest groźne, bo zmienia zawartość pola, a nie rozmiar,
i mianownik tego nie koryguje.**

## 2. Wszystkie trzy potwierdzone

**H1.** Odsetek rekordów PubMedu z jakimkolwiek MeSH: **93,4% (2003) → 73,7% (2019) →
66,4% (2022) → 56,4% (2025)**.

**H2. Podręcznikowe V z dnem dokładnie w 2022:**

| | 2018 | 2019 | 2020 | 2021 | **2022** | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| deskryptorów na rekord pola | 13,14 | 12,61 | 11,06 | 9,63 | **8,70** | 9,02 | 11,73 | 12,48 |

Osiemnaście lat stabilnie ~13, załamanie do 8,70, powrót do 12,48. **Nieciągłość jest tam,
gdzie plan kazał jej szukać, i ma kształt przejścia technologicznego, nie trendu.**

**H3. Przesunięcie nie jest losowe — jest systematyczne w jedną stronę:**

| deskryptor | 2015–21 | 2023–25 | zmiana |
|---|---:|---:|---:|
| Orthopedic Procedures *(rodzic)* | 6,59% | 3,64% | **−2,94 pp** |
| Fracture Fixation *(rodzic)* | 2,10% | 1,03% | −1,07 pp |
| Arthroplasty *(rodzic)* | 1,82% | 1,10% | −0,73 pp |
| Arthroplasty, Replacement, **Knee** | 11,19% | 12,38% | **+1,19 pp** |
| Fracture Fixation, **Internal** | 9,46% | 10,55% | +1,09 pp |
| Arthroplasty, Replacement, **Shoulder** | 1,43% | 2,28% | +0,84 pp |

**Wszystkie spadki to deskryptory ogólne, wszystkie wzrosty to szczegółowe.** MTIX indeksuje
konkretniej kosztem terminów rodzicielskich — znana własność automatycznego indeksowania.

## 3. Ale przesunięcie deskryptorów **nie przekłada się** na ranking

To jest test rozstrzygający i dlatego opisuję go dokładnie.

**T1.** Dla każdego terminu materiału dopasowałem trend log-udziału na 2015–2021 i porównałem
przewidywanie na 2023–2025 z obserwacją. Mediana `z = −0,87`, 9 terminów poniżej −2, 2 powyżej +2,
rozrzut od **−6,24** (`open wedge high tibial osteotomy`) do **+3,52** (`reverse shoulder
arthroplasty`).

**Sam ten rozrzut niczego nie dowodzi.** Trend wykładniczy dopasowany na siedmiu latach
i ekstrapolowany na trzy prawie zawsze przestrzeliwuje w górę, bo wzrost się nasyca — ujemna
mediana jest spodziewana niezależnie od MTIX.

**Rozstrzyga kierunek.** Jeżeli H3 działa, terminy, których prace noszą deskryptory **zyskujące**,
powinny mieć `z` wyższe niż terminy z deskryptorami **tracącymi**. Policzyłem ekspozycję każdego
terminu jako średnią zmianę pp deskryptorów jego prac z lat 2023–2025 i skorelowałem z `z`:

```
n = 43
Spearman  rho = +0,143   p = 0,36
Pearson   r   = +0,126   p = 0,42
```

**Związku nie ma.** Kierunek jest nominalnie zgodny z H3, ale nieodróżnialny od szumu.
Najmocniejsze odchylenie w dół, `open wedge high tibial osteotomy` (z = −6,24), ma ekspozycję
+0,01 pp, czyli praktycznie zerową; `cone beam computed tomography` z ekspozycją ujemną
(−0,075 pp) odchyla się w **górę** (z = +1,53).

**T2.** Korelacja osi obecności z osią przekroczenia progu: **0,862 przed MTIX, 0,916 po**.
Osie zgadzają się po przejściu **bardziej**, nie mniej — więc zamiana osi na przekroczenie
niczego by nie naprawiła, bo nie ma czego naprawiać.

## 4. Co z tego wynika

**Oś zostaje.** Nieciągłość MTIX jest realna i duża w głębokości indeksowania oraz w składzie
deskryptorów, ale **nie daje mierzalnego skrzywienia obecności terminów materiału**. Zmiana osi
albo mianownika byłaby leczeniem objawu, którego nie ma.

Do Ograniczeń, z liczbami: *odsetek rekordów PubMedu z przypisanym MeSH spadł z 93% (2003)
do 56% (2025), a liczba deskryptorów na rekord pola załamała się z 13,1 (2018) do 8,7 (2022)
i wróciła do 12,5 (2025); skład deskryptorów pola przesunął się z terminów ogólnych na
szczegółowe. Sprawdziliśmy, czy przesunięcie przekłada się na obecność terminów — nie przekłada
się (Spearman 0,14, p = 0,36 na 43 terminach).*

## 5. Uczciwe zastrzeżenie do tego wniosku

**43 terminy to mała moc.** Przy `r = 0,126` przedział ufności obejmuje umiarkowany efekt
dodatni, więc „nie zmierzyliśmy skrzywienia" **nie znaczy** „skrzywienia nie ma". Nie da się
tego poprawić na materiale tej wielkości; dałoby się, licząc to samo na całym rdzeniu (1 294),
gdyby recenzent naciskał. **Nie robię tego teraz**, bo wniosek praktyczny — oś zostaje — nie
zmieniłby się od węższego przedziału, a rdzeń zawiera 231 fraz metodologicznych, dla których
„ekspozycja na deskryptory" znaczy co innego niż dla technologii.

Jeśli uważasz inaczej, powiedz — przeliczenie na rdzeniu to kilkanaście minut.

## 6. Przy okazji: liczebniki 72, nie 86 — masz rację

Twoje §5. Sprawdziłem własną definicję: liczyłem frazy **zawierające** samodzielny token
liczbowy, Ty frazy **będące wyłącznie** liczbami. 86 = 72 + 14, a te 14 to w większości
prawdziwe terminy: `95 confidence interval`, `minimum 2 year follow up`, `srs 22` (kwestionariusz
SRS-22), `sf 12` (skala SF-12), `l4 5` (poziom L4-5). **Do tekstu idzie 72.** Moja liczba
zawyżała.

## 7. Stan

Manifest **12/12**. Osie siły policzę po domknięciu materiału — teraz wiadomo, że nie trzeba
ich będzie przeliczać z powodu osi rankingu.
