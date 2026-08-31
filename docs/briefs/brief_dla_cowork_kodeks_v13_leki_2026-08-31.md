# Propozycja kodeksu v1.3 — leki wchodzą jako technologia, ale wtedy potrzebna jest reguła stopu

Autor: sesja VS Code, 2026-08-31. Decyzja kierunkowa Przemka; do rozstrzygnięcia i spisania
po Twojej stronie, bo `docs/protocol/` jest Twoje, a kodeks jest w manifeście.

---

## 1. Co się stało

κ drugiego kodera wyszła **0,442** przy progu 0,70. Sześć z siedemnastu niezgodności to jedna
i ta sama sprawa: człowiek kodował `tranexamic acid`, `local infiltration analgesia`,
`pericapsular`, `cephalomedullary` jako `non-technological term`, model jako `novel concept`.

**Oba odczyty są zgodne z literą kodeksu.** §2 definiuje technologię jako „device, material,
computational or operative technique" i tego przypadku nie rozstrzyga.

Przemek rozstrzygnął kierunkowo: **lek jest technologią** — to innowacja technologii chemicznej
i nie ma powodu, by praca o dyfuzji technologii w ortopedii o niej milczała. Zgadzam się.
Kwas traneksamowy zmienił gospodarkę krwią w endoprotezoplastyce bardziej niż niejedno
urządzenie z listy.

## 2. Dlaczego to nie jest doprecyzowanie, tylko zmiana definicji

Rozważałem najpierw wersję lżejszą: technika okołooperacyjna mieści się w „operative technique",
a lek nie mieści się nigdzie, więc kodeks już odpowiada i wystarczy jedno zdanie. Odrzucam ten
wariant po argumencie Przemka — prowadziłby do sytuacji, w której czteropozycyjna lista rządzi
treścią badania, a nie odwrotnie.

Skoro wchodzimy w definicję, trzeba zobaczyć, co ta lista naprawdę robi.

**Cztery pozycje pełnią funkcję reguły stopu, nie tylko definicji.** Dopóki technologią jest
„urządzenie, materiał, metoda obliczeniowa albo technika operacyjna", każda pozycja spoza tej
listy ma jasny los. Kiedy listę poszerzysz, pytanie wraca przy każdym kolejnym wierszu i **nie
ma go co zamknąć**.

To ryzyko jest konkretne, nie teoretyczne: kategoria `non-technological term` trzyma **229 z 287
(79,8%)** kodowania człowieka, a κ pokazała, że rozjeżdżamy się dokładnie na jej granicy.
**Poszerzenie strony technologicznej bez nowej reguły stopu pogorszy zgodność, nie poprawi.**

## 3. Propozycja brzmienia — pozytywna i negatywna naraz

> **Technologia** — artefakt albo wyspecyfikowana technika, która pośredniczy w rozpoznaniu lub
> leczeniu: urządzenie, materiał **wraz z substancją czynną**, metoda obliczeniowa, technika
> operacyjna lub okołooperacyjna.
>
> **Nie jest technologią**: metodologia badawcza, statystyka, konwencja raportowania,
> organizacja opieki, **jednostka chorobowa, powikłanie i miara wyniku**.

Człon negatywny jest tu ważniejszy od pozytywnego i o niego proszę najbardziej.

## 4. Ile pozycji to dotyka — na rdzeniu frazowym 47

**Bezpośrednio dwie**: `tranexamic acid` (pozycja 17) i `rivaroxaban` (46). Tyle zmienia sama
decyzja o lekach.

**Pośrednio znacznie więcej.** Wypisuję pozycje, których obecne brzmienie **nie rozstrzyga** —
nie przypisuję im kategorii, to robota kodera:

- jednostki chorobowe: `periprosthetic joint infection` (5), `chronic limb threatening ischemia`
  (13), `adult spinal deformity` (15), `femoroacetabular impingement syndrome` (20),
  `peripheral artery disease` (21), `covid 19` (22), `lumbar degenerative disease` (24),
  `early onset scoliosis` (44), `frailty` (31)
- powikłania: `proximal junctional kyphosis` (26), `surgical site infection` (10)
- miary wyniku: `patient reported outcome` (4), `patient reported outcome measure` (6),
  `postoperative outcome` (8), `clinical efficacy` (9), `mid term outcome` (38),
  `readmission` (7)

To jest **rząd siedemnastu pozycji z 47**, w tym pięć z pierwszej dziesiątki. Bez członu
negatywnego każda z nich jest sporna, a spór między dwoma koderami wyląduje w κ.

## 5. Co to znaczy dla rejestracji

`coding_manual_v1.2.md` jest w manifeście i cytowany w rejestracji, więc v1.3 jest
**zadeklarowanym odstępstwem**, nie poprawką. Uzasadnienie jest mocne i zmierzone, nie
uznaniowe — i to jest argument za tym, żeby je zapisać, a nie ukryć:

- κ = 0,442 przy progu 0,70, przy czym **6 z 17 niezgodności leży dokładnie na tej granicy**;
- κ Brennana–Predigera 0,646, więc wniosek nie zależy od wyboru statystyki;
- `measurement artifact` ma **zero obserwacji na 287** — osobna sprawa, ale też do odnotowania
  przy okazji rewizji;
- jednostka n-gramowa zawiodła niezależnie (79,8% w jednej kategorii), więc v1.3 i tak wchodzi
  razem ze zmianą jednostki na frazy.

Kodeks §5 przewiduje przy niespełnionym progu rewizję definicji i drugą rundę. **To jest
dokładnie ten tryb** — nie obchodzimy procedury, tylko ją wykonujemy.

Podtrzymuję jednak rekomendację z poprzedniego briefu: **drugiej rundy nie robić na zbiorze
n-gramowym.** Pięć z siedemnastu niezgodności to fragmenty (`study from`, `at minimum`,
`fracture a finite`), które przy chunkowaniu w ogóle nie powstają. Runda druga ma sens na
rdzeniu frazowym, gdzie da się zakodować komplet 47 zamiast podpróby — i wtedy κ przestaje być
statystyką z próby.

## 6. Czego potrzebuję

1. Rozstrzygnięcia i spisania **v1.3** — pozytywnie i negatywnie, wg §3 albo lepiej.
2. Zdania o **zakresie pracy**, bo włączenie leków zmienia to, co praca mierzy, i powinno stać
   w abstrakcie, a nie wynikać z definicji w załączniku.
3. Decyzji, czy **osie siły raportujemy osobno dla leków**. Koncentracja pierwszych autorów
   i krajów mierzy dla generyku coś innego niż dla implantu związanego z jednym producentem —
   porównywanie ich wprost w jednej tabeli jest porównywaniem rzeczy nieporównywalnych.

Po Twojej stronie jest też pytanie, czy `measurement artifact` z zerem obserwacji zostaje
w kodeksie bez zmian.

## 7. Stan

Manifest **12/12**, nic zamrożonego nietknięte. Kodeksu nie dotykam — to Twój plik.
