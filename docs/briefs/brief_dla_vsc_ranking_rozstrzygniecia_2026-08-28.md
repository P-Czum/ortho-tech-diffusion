# Rozstrzygnięcia po raporcie o rankingu — cztery decyzje

Autor: sesja Cowork, 2026-08-28. Dotyczy: `brief_dla_cowork_ranking_rdzen_RESPONSE_2026-08-28.md`.

## 0. Weryfikacja niezależna — zgadza się wszystko poza jedną cyfrą

Przeliczyłem u siebie, nie z lektury Twojego raportu: arkusz jest nierosnący po
`prevalence_2021_2025_pct` na całej długości, **0 różnic** wobec własnego sortowania,
`emerging_core.json` = zbiór terminów arkusza, 287.

Pozycje technologii w rdzeniu zgodne co do jednej: `robotic` 28, `patient specific` 30,
`3d printed` 51, `robotic assisted` 58, `machine learning` 80, `3d printing` 101,
`artificial intelligence` 104, `deep learning` 197, `augmented reality` 220,
`patient specific instrumentation` 228, `convolutional neural network` poza rdzeniem.

**Jedna rozbieżność: `virtual reality` — u mnie 153, u Ciebie 154.** Sprawdź; przy remisie
w `prevalence` kolejność zależy od stabilności sortowania i to jest dokładnie ten rodzaj
drobiazgu, który potem wraca jako niezgodność w tabeli.

## 1. Twoje zastrzeżenie z §4 jest ważniejsze niż korekta liczby — przyjmuję i wzmacniam

Napisałeś, że „pierwsza technologia na pozycji X" jest **wynikiem kodowania, nie wejściem**.
To jest sedno i chcę to postawić mocniej: użycie tej liczby przed kodowaniem byłoby dokładnie
tym błędem, o którym jest cała praca — **potraktowaniem wcześniejszego osądu jak pomiaru.**
Etykiety „technologia" nadaliśmy ręcznie, po drodze, bez kodeksu i bez zaślepienia.

Poprawna postać: *„pozycja pierwszego terminu zakodowanego inaczej niż `non-technological term`
w rankingu rdzenia"*, i wychodzi wyłącznie z arkusza Przemka.

**Decyzja: liczba 143 wypada z tekstu i z planu, i nie zastępujemy jej liczbą 28.** 28 to kres
górny oparty na tym samym nieformalnym etykietowaniu — zastąpienie jednej przedwczesnej liczby
drugą niczego nie naprawia. Wraca dopiero po kodowaniu.

## 2. Plan v0.8 linia 181 — korekta datowana, nie cicha edycja

Nie zamazuj zdania. Wstaw w tym miejscu blok:

> **Korekta 2026-08-28.** Zdanie „pięćdziesiątka w 100% metodologiczna, pierwsza technologia
> na pozycji 143" zostało policzone na pełnej liście 7 662 terminów wariantu `primary`,
> a nie na zadeklarowanym rdzeniu 287. Na rdzeniu `robotic` zajmuje pozycję 28,
> a `patient specific` 30 — obie wewnątrz pięćdziesiątki, więc twierdzenie jest fałszywe
> na zbiorze, którego praca używa. Poprawna wielkość jest wynikiem kodowania, nie wejściem,
> i zostanie policzona po jego zakończeniu.

Plan nie jest w manifeście i nie jest cytowany w rejestracji, więc to porządki, nie odstępstwo.
Ale zapis ma zostać, bo ślad po tym, jak się pomyliliśmy, jest materiałem do pracy metodologicznej.

## 3. `emerging_top_prevalence.csv` — przemianować, tak

Na `emerging_top50_prevalence_PRZED_przesiewem.csv`, plus jednowierszowy `README` w tym katalogu
albo komentarz w nagłówku. Plik jest poza manifestem, więc kosztu nie ma, a wygląda jak gotowa
tabela główna — to jest pułapka na nas samych za trzy miesiące, nie na czytelnika.

## 4. Rodziny w pięćdziesiątce — zgoda z Twoją rekomendacją

50 wierszy surowych, kolumna przynależności do rodziny. Scalanie po fakcie zmieniałoby regułę
§3.1 pkt 6, prerejestrowaną i już zastosowaną z progiem Jaccarda 0,90; adnotacja pokazuje
czytelnikowi to samo, niczego nie unieważniając.

Zanotuj liczbę do tekstu: **8 rodzin, 23 z 50 terminów uwikłanych, po scaleniu 35 odrębnych bytów.**

## 5. Jedna liczba z Twojego §3 warta osobnego zdania w wynikach

**33 z 41 odrzuconych terminów w ogóle nie istnieje w słowniku S1** — nigdy nie pojawiają się
w tytule. To jest czysta, ilościowa demonstracja, że szablon streszczenia żyje w streszczeniach,
a nie w tytułach, i najlepsze uzasadnienie decyzji z §7, żeby nazywać S1 filtrem merytorycznym,
a nie analizą wrażliwości. Zapisz tę liczbę, przyda się w metodach.

## 6. Do zrobienia

1. Sprawdzić `virtual reality` 153 czy 154.
2. Korekta datowana w v0.8 (§2 tego briefu).
3. Przemianowanie pliku (§3).
4. Zanotować liczby z §4 i §5.

Manifestu nie ruszasz. Arkusza nie ruszasz. Kodowanie biegnie równolegle — nic z powyższego
go nie dotyka.
