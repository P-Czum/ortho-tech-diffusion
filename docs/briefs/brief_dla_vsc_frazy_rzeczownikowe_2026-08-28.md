# Zmiana jednostki: frazy rzeczownikowe zamiast n-gramów

Autor: sesja Cowork, 2026-08-28. Decyzja Przemka po `brief_dla_cowork_count_zdarzen_RESPONSE_2026-08-28.md`.

**Zmienia się wyłącznie jednostka. Wszystko inne zostaje bit w bit.** To jest pomiar
porównawczy, nie nowy projekt — chodzi o jedną odpowiedź: czy lepsza jednostka naprawia to,
co zepsuł n-gram.

---

## 0. Dlaczego

N-gram to okno *n* kolejnych tokenów, obiekt pozycyjny, tnący przez granice składniowe. Stąd
`of robotic`, `question purpose`, `were included`, `slide can be`, `killed`, `particle of`.
Fraza rzeczownikowa jest jednostką, która **coś nazywa**.

Uderza to w obie zmierzone porażki naraz: szablon abstraktu w większości nie jest frazą
rzeczownikową, a fragmentacja znika na granicy frazy.

**Czego to nie naprawi, i nie udawajmy inaczej:** progu rozdzielającego przemianowanie od
sąsiedztwa tematycznego. Tamta porażka ma inną przyczynę — podobieństwo kontekstów z zasady
myli tożsamość z bliskością. Frazy poprawią listę i mapę, nie dadzą automatycznego werdyktu.

## 1. Ekstrakcja

Bazowe frazy rzeczownikowe (noun chunks) z tytułu i streszczenia rekordów pola def1.

- Parser: spaCy albo scispaCy, **wersja modelu i biblioteki przypięte i wypisane w nagłówku
  skryptu oraz w wyniku.** Parser jest zależnością zewnętrzną i musi być odtwarzalny co do wersji,
  tak jak przypięliśmy baseline.
- Bierzemy **chunki płaskie**, bez zagnieżdżonych fraz przyimkowych.
- Obcinamy wiodące określniki i zaimki dzierżawcze (`the`, `a`, `an`, `our`, `their`),
  interpunkcję z obu końców.
- Długość 1–5 tokenów po obcięciu.

## 2. Kanonikalizacja — **istniejąca, bez dodatków**

Stosujesz **zamrożone listy z `data/canon/`** w tej samej kolejności co dotąd: warianty zapisu
cyfrowo-słowne, liczba mnoga, warianty brytyjsko-amerykańskie, rozwinięcia skrótów.

**Nie dokładaj żadnej nowej reguły.** Jeśli uznasz, że przy frazach czegoś brakuje — zgłoś,
nie dopisuj. Chodzi o to, żeby różnica w wyniku pochodziła z jednostki, a nie z dziesięciu
drobnych zmian naraz.

Zwijanie zagnieżdżonych n-gramów (reguła §3.1 pkt 6) **zastosuj tak samo**, na frazach.

## 3. Wszystko poniżej bez zmian

Pole def1, lata 2005–2025, próg wejścia ≥ 50 wystąpień, detektor (θ = 0,1% i ≥ 5 prac,
`y₀` = pierwszy rok, w którym udział ≥ `max(θ, 5 × baza 2005–2007)` utrzymane 3 lata, `y₀ ≤ 2023`),
cztery warianty tekstowe primary/S1/S2/S3, rdzeń jako ich część wspólna.

## 4. Co odesłać — liczby porównywalne z tym, co mamy

| wielkość | n-gramy (mamy) | frazy (policz) |
|---|---:|---|
| jednostek powyżej progu 50 | 245 081 | ? |
| wschodzących (primary) | 7 662 | ? |
| rdzeń (część wspólna 4 wariantów) | 287 | ? |
| rodzin zawierania w rdzeniu / objętych terminów | 46 / 140 | ? |
| wierszy rodziny `robot*` w rdzeniu | 8 | ? |
| wierszy rodziny `3d`/`print*` w rdzeniu | 4 | ? |

Do tego:

1. **Pięćdziesiąt pierwszych rdzenia po `prevalence_2021_2025`**, dosłownie, bez oceny.
   Do porównania z listą, która była w 100% metodologiczna.
2. **Pozycje w rdzeniu** dla: `3d printing`, `3d printed`, `robotic`, `robotic assisted`,
   `machine learning`, `artificial intelligence`, `patient specific`, `augmented reality`,
   `virtual reality`, `deep learning`, `navigation`. Nazwy dopasuj do tego, jak wyjdą po frazowaniu
   — jeśli fraza brzmi inaczej, podaj obie postaci.
3. **Ile jednostek rdzenia to frazy jednotokenowe**, a ile dwu- i trzytokenowe.

## 5. Czego nie robić

- **Nie licz podobieństw kontekstowych ani par.** Gałąź odkrywcza jest zamknięta; jeśli jednostka
  okaże się wyraźnie lepsza, wtedy Przemek zdecyduje, co na niej uruchomić.
- Nie ruszaj zamrożonych plików ani manifestu. Wyjścia pod nowymi nazwami z przyrostkiem `_np`.
- Nie oceniaj list.

## 6. Kryterium — postawione przed wynikiem

Jednostka jest lepsza, jeśli **jednocześnie**: pięćdziesiątka rdzenia przestaje być zdominowana
przez szablon abstraktu, a rodzina `robot*` schodzi z ośmiu wierszy do najwyżej dwóch–trzech.

Jeśli poprawia się tylko jedno z dwojga — to jest wynik częściowy i wraca do decyzji.

## 7. Stan

Manifest 12/12. `coding_sheet_koder_CODED_*.csv` w `.gitignore`, nietknięty.
