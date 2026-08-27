# Recenzja kodeksu v1.0 — przed rejestracją

Autor: sesja VS Code, 2026-08-27. Dotyczy: `docs/protocol/kodeks_kodowania_v1.md`
oraz `brief_dla_vsc_kodeks_i_rozstrzygniecia_2026-08-27.md`.

Kodeks jest dobry i gotowy po naniesieniu poniższego. Zaślepienie kodera przed czasem
podwojenia jest rozstrzygnięciem trafnym i sam bym na to nie wpadł — kontrola, którą koder
widzi, mierzy jego posłuszeństwo wobec liczby, nie zgodność dwóch niezależnych dróg.

---

## 1. Twoje pytanie: czy test podstawienia był wykonalny

**Nie był.** Koder dostawał trzy tytuły zawierające **termin**, zero zawierających **poprzednika**
i zero, w których występują **oba**. Test wymaga materiału po obu stronach okresu nakładania,
więc koder mógł go co najwyżej wyobrazić sobie — a to jest dokładnie ta swoboda, którą kodeks
ma zamykać.

**Naprawione.** Arkusz ma teraz 29 kolumn, doszły trzy: `poprzednik_glowny`,
`tytuly_poprzednika`, `tytuly_WSPOLNE` — te ostatnie z okna `y₀ ± 2`, czyli stamtąd, gdzie
pojawia się zapis „X (Y)". Pokrycie: **284 z 287** terminów.

Przykłady materiału, którym koder teraz dysponuje:

| para | tytuł wspólny |
|---|---|
| `3d printing` / `rapid prototyping` | *„Application of **3D rapid prototyping** technology in posterior corrective surgery for Lenke 1 adolescent idiopathic scoliosis"* (2015) |
| `robotic` / `navigated total knee` | *„Comparison between **navigated** reported position and postoperative CT to evaluate accuracy in a **robotic navigation** system in TKA"* (2019) |

Drugi przykład jest wzorcowy dla testu jednostronnego z §2: robot **używa** nawigacji,
więc podstawienie działa w jedną stronę.

## 2. Twoje pytanie: czy lift ≥ 5 nie jest za niski

Pytanie jest lekko chybione i realny problem leży gdzie indziej.

**Empirycznie próg prawie nie gryzie.** Tylko **10 terminów (4%)** ma najlepszego kandydata
z liftem poniżej 5. Mediana najlepszego liftu wynosi **26,9**.

**Ale lift w ogóle nie odróżnia sygnału od szumu.** Zmierzone przykłady: `we tested the` ma
lift **36,0** przy `machine learning`, `a cadaver` **15,0** przy `virtual reality`. To są
najwyższe lifty przy tych terminach i oba są bezwartościowe. Rozróżnia **koder, semantycznie** —
lift jest narzędziem **wyszukiwania kandydatów, nie regułą decyzyjną**.

Wniosek jest odwrotny do sugerowanego przez Twoje pytanie: próg ma być **przepuszczalny**,
bo pominięty prawdziwy poprzednik jest kosztowniejszy niż jeden kandydat więcej do odrzucenia.
To jest ta sama lekcja co przy `MIN_CO`, tylko po drugiej stronie: tam za ostry próg **liczności**
wyciął `rapid prototyping` z liftem 52,1.

**Do naprawy: próg musi być ten sam w arkuszu i w kodeksie.** Arkusz generuje przy 3, kodeks §3
krok 3 wymaga 5 — koder widziałby więc kandydatów, których reguła każe ignorować. Proponuję **3
w obu miejscach**, z jawnym zapisem, że lift służy wyszukiwaniu, a rozstrzyga podstawienie.

## 3. Trzy sprzeczności wewnętrzne

### 3.1. Wskaźnik `measurement artifact` łamie zaślepienie z §1

§1: *„Koder NIE widzi podczas kodowania: […] wyników def2."*
§2 `measurement artifact`: *„Wskazania: `y₀ ≥ 2020` […] **i brak potwierdzenia w def2**."*

Koder nie może użyć wskaźnika, którego nie widzi.

Proponuję **usunąć def2 ze wskaźników artefaktu**, a nie odsłaniać go koderowi. Powód:
kontrola 2 z §5 sprawdza właśnie, czy `renaming`/`evolution` odtwarzają się w def2 częściej niż
`measurement artifact`. Jeśli koder widzi def2 i wie, że artefakty się nie odtwarzają, kontrola
staje się tautologią. Niezależność kontroli jest tu warta więcej niż jeden wskaźnik.

### 3.2. Wskaźnik „wyłonienie znikające w S2/S3" jest pusty z konstrukcji

Rdzeń 287 to **część wspólna czterech wariantów** — primary, S1, S2, S3. Żaden z tych terminów
nie znika w S2 ani w S3, bo inaczej nie byłoby go w rdzeniu.

Wskaźnik nie jest błędny, tylko **niemożliwy do spełnienia** na materiale, do którego się odnosi.
Do usunięcia albo do przeniesienia — miałby sens, gdybyśmy kodowali zbiór `abstract-only`
(odpadające wyłącznie na S1), który ustaliliśmy jako raportowany osobno.

### 3.3. Warstwa „obecność kandydata na poprzednika" jest zdegenerowana

Kandydata ma **274 z 287 terminów (95%)**. Przy 60 terminach dla drugiego kodera warstwa
mniejsza dostałaby **około trzech pozycji** — to nie jest warstwowanie, tylko szum.

Rozkład epok `y₀` jest użyteczniejszy: **27 / 174 / 86** dla 2005–2012 / 2013–2019 / 2020+,
co przy alokacji proporcjonalnej daje 6 / 36 / 18. Proponuję warstwować po epoce i po długości
n-gramu, a obecność kandydata odpuścić.

## 4. Konsekwencja dla wyniku nagłówkowego — do zapisania wprost

Po usunięciu wskaźników 3.1 i 3.2 kategoria `measurement artifact` opiera się na `y₀ ≥ 2020`
(dotyczy 86 terminów, 30% rdzenia) i na byciu konwencją zapisu. To znaczy, że **udział
artefaktów zmierzony na rdzeniu 287 będzie niski z konstrukcji** — rdzeń był wstępnie
przefiltrowany na czterokrotną odporność.

Zdanie „X% najsilniejszych wyłonień to artefakty pomiaru" **nie jest oszacowaniem częstości
artefaktów w pełnym zbiorze 7 662**, tylko w zbiorze już oczyszczonym. Trzeba to napisać
w wynikach, bo różnica jest duża i czytelnik założy szersze uogólnienie.

To samo dotyczy rozkładu pozostałych kategorii: jest to rozkład **wśród wyłonień odpornych na
wariant tekstowy**, nie wśród wyłonień w ogóle.

## 5. Drobniejsze

- §3 krok 4: *„nie przechodzi → wróć do 3 (kandydat błędny) lub `novel concept`"* — pętla
  z dwoma wyjściami bez reguły, które wybrać. Proponuję: wróć do 3 najwyżej raz, przechodząc
  do kolejnego kandydata z listy; po wyczerpaniu listy → `novel concept`.
- §1 pozwala koderowi przeszukać tytuły w korpusie i odnotować to w `uwagi`. Potrzebne jest
  do tego narzędzie — mogę dostarczyć prosty skrypt wyszukujący tytuły po terminie
  kanonicznym, żeby przeszukanie było odtwarzalne i logowane, a nie robione ad hoc.
- §4: κ Cohena przy pięciu kategoriach o bardzo nierównych częstościach bywa niestabilne.
  Warto rozważyć raportowanie obok niego zgodności surowej i κ z wagami, ale nie jako
  zamiennik — próg 0,70 zostaje.

## 6. Stan

Arkusz przebudowany: `data/processed/coding_sheet_full.csv`, 287 wierszy, **29 kolumn**.
Nie jest jeszcze zamrożony — czeka na Twoje decyzje z §2 i §3, bo próg liftu zmieni kolumnę
kandydatów.

Po nich: zamrożenie, hash, rejestracja, kodowanie.
