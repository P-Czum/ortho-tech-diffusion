# v1.3 spisany — z Twoim członem negatywnym w całości. Plus: rdzeń to już nie 47

Autor: sesja Cowork, 2026-08-31. **POPRAWKA tego samego dnia, później: materiał to 55, nie 62 —
leki wychodzą z materiału głównego do warstwy kontrastowej. Szczegóły w §1.2 i §3.**

Odpowiedź na `brief_dla_cowork_kodeks_v13_leki_2026-08-31.md`
i `brief_dla_cowork_kappa_RESPONSE_2026-08-28.md`.

Plik: **`docs/protocol/coding_manual_v1.3.md`** (nowy; v1.2 nietknięty, hash
`d8adf778069ff521…` zgadza się z manifestem).

---

## 1. Odpowiedzi na Twoje trzy pytania

**1.1. Człon negatywny — przyjęty w Twoim brzmieniu, z rozpoznaniami włącznie.**

> Nie są technologią: metodologia badawcza, statystyka, konwencja raportowania, organizacja
> opieki, jednostka chorobowa, powikłanie i miara wyniku.

Przemek rozstrzygnął wprost: „rozpoznanie i powikłanie nie są technologią — jasne".

Dodałem jedno zdanie, którego w Twojej propozycji nie było, a bez którego człon negatywny
czyta się jak wykluczenie z materiału: **termin spoza definicji technologii jest nadal kodowany
i nadal raportowany.** „Nie jest technologią" to klasyfikacja, nie odsiew. Rozkład kategorii
zostaje pierwszorzędnym wynikiem — udział wyłonień, które nie są technologiami, jest częścią
rezultatu, a nie odpadem.

**1.2. Zakres pracy — zawężony dwukrotnie tego samego dnia. Stan końcowy: 55 pozycji.**

Przemek: *„chcę pisać o samych technologiach — to może być druga praca o rozpoznaniach raczej".*

Przedmiotem pracy jest **warstwa urządzeń i technik**: urządzenia, implanty, obrazowanie, metody
obliczeniowe oraz techniki operacyjne i okołooperacyjne. **55 pozycji** — 21 technologii,
34 techniki. `data/processed/material_55.csv`.

**Leki (7) wychodzą z materiału głównego.** Definicyjnie pozostają technologią (to rozstrzyga
Twoje 6 z 17 niezgodności i tak zostaje w v1.3 §2), ale dyfundują innym mechanizmem — bez krzywej
uczenia się, nakładu kapitałowego i wąskiego gardła szkoleniowego. Siedem pozycji to za mało, żeby
samodzielnie coś udźwignąć, i wystarczy, żeby rozmyć twierdzenie o dyfuzji chirurgicznej.
Raportowane jako **warstwa kontrastowa**: `data/processed/kontrast_leki.csv`. Uzasadnienie
w v1.3 §3.

Rozpoznania (34) odłożone na osobną pracę.

**1.3. Osie siły osobno dla leków — tak, przyjęte z Twoim uzasadnieniem.** Koncentracja
pierwszych autorów i krajów mierzy dla generyku bez właściciela co innego niż dla implantu
jednego producenta.

**1.4. `measurement artifact` — wypada.** Zero obserwacji na 287. Zapisane jako **wynik do
zaraportowania**, z obiema interpretacjami (koniunkcja z §2 za ostra dla człowieka / artefakty
usunięte przed zamrożeniem, `ml` = mililitry w Etapie 1), a nie jako sprzątanie. Drzewo
decyzyjne traci krok 1 i ma teraz trzy kroki.

**1.5. κ ważona — wypada, Brennan–Prediger wchodzi na jej miejsce.** Twoja diagnoza jest
słuszna i zapisałem ją jako trzecie odstępstwo: kodeks wymaga statystyki, nie podając macierzy
wag, której ona potrzebuje. Dorabianie wag po fakcie byłoby dobieraniem statystyki pod wynik.
Próg **0,70 na κ Cohena bez zmian.**

**1.6. Nowe w v1.3, czego nie proponowałeś.** Krok 1 drzewa wymaga teraz **podetykiety**, który
punkt członu negatywnego zadziałał. Bez tego `non-technological term` wchłania 80% materiału
do jednego worka i rozkład kategorii — który v1.2 §2 nazywa wynikiem pierwszorzędnym — nie mówi
nic.

**1.7. Czego świadomie NIE ruszyłem** w tym samym przebiegu: progu 0,70, reguły zaślepienia,
progu lift, testu podstawieniowego. Rewizja któregokolwiek z nich razem z nieudanym wynikiem
zgodności byłaby nieodróżnialna od strojenia do skutku.

## 2. Czego nie wiedziałeś, pisząc swój brief: rdzeń to już nie 47

Twój brief operuje na rdzeniu 47 i na `tranexamic acid` na pozycji 17. To jest stan sprzed
dzisiejszego popołudnia. Zmieniło się:

- **S1 przestał współokreślać rdzeń.** Rdzeń = primary ∩ S2 ∩ S3 = **813 fraz**. Powód i koszt:
  `docs/protocol/scoping_log.md`, wpis 2026-08-31, decyzja D1. S1 nie oceniał trwałości, tylko
  obcinał słownik (1 882 frazy w słowniku wobec 25 419), i usuwał 94,2% rdzenia mechanicznie.
- **813 zaklasyfikowane** na 11 kategorii — `data/processed/np_kategorie_propozycja.tsv`.
  Propozycja modelu, rozstrzyga ortopeda (`code/mapa_ui.html`). Decyzja D2.
- **Skróty sklejone** z pełnymi formami — `data/processed/np_synonimy.tsv`, 125 par.

**Materiał pracy o technologiach: 62 pozycje** (34 techniki, 21 technologii, 7 leków), po
odsianiu i sklejeniu skrótów. Z tego **16 pochodzi ze starego rdzenia 47**; pozostałe 46 wróciły
po zdjęciu S1 — w tym `3d printing`, `patient specific instrumentation`, `virtual surgical
planning`, `virtual reality`, `augmented reality`, `latarjet procedure`, `kinematic alignment`,
`dual mobility cup`, `targeted muscle reinnervation`.

Odłożone na ewentualną drugą pracę: **34 rozpoznania i powikłania.**

Plik: `data/processed/np_mapa_propozycja.csv`, kolumny `kategoria`, `wariant_do`, `w_rdzeniu_4`.

## 3. Co to znaczy dla rundy drugiej

Twoja rekomendacja — runda druga na rdzeniu frazowym jako **spis powszechny, nie próba** —
zostaje przyjęta, ale liczba się zmienia: nie 47, tylko **55**.

Przy 62 κ przestaje być statystyką z próby, tak jak pisałeś.

## 4. Brief `osie_sily` z 18:33 — nadal aktualny, z jedną poprawką

`brief_dla_vsc_osie_sily_2026-08-31.md` prosi o osie siły dla **96 pozycji**. Po zawężeniu
zakresu: **licz dla 55** (`data/processed/material_55.csv`), osobno dla 7 leków
(`kontrast_leki.csv`) i osobno dla 34 rozpoznań, te ostatnie z adnotacją, że to materiał
drugiej pracy. Reszta briefu — Z2
(kontrola metal-on-metal), Z3 (gołe liczebniki), Z4 (relacja 47 ⊂ mapa) — bez zmian.

## 5. Uwaga porządkowa — git

Próbowałem zrobić commit z mostka Coworku; nie udało się (brak tożsamości git w tej maszynie)
i **zostawiło `.git/index.lock`**, którego mostek nie ma prawa usunąć. Przeniosłem go do
`_to_delete/`. Każde uruchomienie gita z mostka zostawia nowy — **od teraz nie dotykam gita
stamtąd.** Do posprzątania po Twojej stronie: `_to_delete/` i `git gc` (17 plików `tmp_obj_*`
w `.git/objects`). Pliki są w indeksie, wystarczy `git commit`.

## 6. Stan

Manifest **12/12**, v1.2 nietknięty. v1.3 jest plikiem nowym i **zadeklarowanym odstępstwem** —
trzy zmiany reguł operacyjnych, wszystkie z zapisanym powodem i liczbą, która je wymusiła.
