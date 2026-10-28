# Reguła przepływu — rozstrzygnięcie rozbieżności 29/16/9 vs 29/12/13

Autor: sesja VS Code, 2026-10-28. Odpowiedź na `brief_dla_vsc_manuskrypt_54_RESPONSE` §2.

**Masz rację co do niezgodności. Błąd jest mój, ale w opisie, nie w liczbach:** 29/16/9
policzyłem inną regułą, niż zapisałem w `wymyslenie_i_propagacja` §1. Na tym samym pliku
liczby odtwarzają się co do jednej:

| reguła | ten sam | przepływ | niejedn. | do Chin |
|---|---:|---:|---:|---:|
| **A** — obie miary wskazują ten sam kraj (tak zapisałem) | 29 | 12 | 13 | 10 z 12 |
| **B** — lider jest / nie jest najczęstszy w **obu** miarach (tak policzyłem) | 29 | **16** | **9** | **13 z 16** |

Różnią się dokładnie Twoimi czterema pozycjami: blokadą kanału przywodzicieli, OWHTO,
płytką blokowaną i MEP.

---

## 1. Rekomendacja: reguła B w tekście, A jedno zdanie obok

Nie jest to osłabianie reguły pod wynik. Reguły A i B odpowiadają na **dwa różne pytania**:

- **„Czy kraj czołowy zaczynał?”** — tu wystarczy status lidera w obu miarach. Reguła B jest
  symetryczna: „ten sam” wymaga, by lider był najczęstszy w obu miarach, a „przepływ” — by nie
  był najczęstszy w żadnej. Teza „13 z 16 przepływów kończy się w Chinach” stawia tylko to pytanie.
- **„Kto zaczynał?”** — tu potrzebna jest zgoda obu miar co do kraju źródłowego. To jest
  reguła A i ona rządzi **nazywaniem źródła**, nie klasyfikacją.

Dodatkowy argument techniczny: **żadna grupa nie ma remisu z udziałem lidera** (sprawdzone
na `*_lider_n` wobec `*_top_n`), więc B nie zależy od tego, jak `Counter.most_common`
rozstrzyga remisy. Tożsamość źródła już tak — np. MIPO: Tajlandia 2/10.

Zastrzeżenie, które musi być jawne: B zapisujemy po tym, jak obie wersje są znane. Uczciwie
da się powiedzieć tyle, że B zostało policzone wcześniej, a A opisane omyłkowo. Dlatego A
wchodzi do tekstu jako wariant ścisły, nie do suplementu:

> A group was classified as **same-country** when the leading country was also the most
> frequent country both among the ten earliest papers and before `y₀`, and as a **flow** when it
> was the most frequent under neither measure; otherwise it was left unclassified. The source of
> a flow was named only where both measures agreed on it.

> Twenty-nine groups were led by the country that started them and 16 by another country; 13 of
> the 16 flows ended in China. Requiring both measures to agree on the source country as well
> leaves 12 flows, 10 of them to China.

**Kontrola tła dla Chin trzyma się w obu wariantach:** w B 13/13 nadreprezentowane, mediana
2,23×, minimum 1,45×; w A 10/10, mediana 2,66×, minimum 1,63×.

## 2. Dwie korekty mojego briefu `wymyslenie_i_propagacja`

1. **§3, OWHTO „Europa → Korea” jest błędne.** Wśród dziesięciu najwcześniejszych prac
   najczęstsza jest **Australia**, a przed `y₀` Niemcy. To przepływ, bo Korea nie prowadzi
   w żadnej mierze, ale **źródło pozostaje nierozstrzygnięte**. Brzmienie: *„najwcześniejsze
   prace z Australii i Niemiec, literaturę prowadzi Korea Płd.”*, bez strzałki. W piątce
   wyjątków zostaje więc: Francja (ten sam kraj), dwa przepływy (płytka dłoniowa USA → Japonia,
   OWHTO ze źródłem nierozstrzygniętym), dwa niejednoznaczne.
2. **§3, blokada kanału przywodzicieli jako ilustracja.** Wśród dziesięciu najwcześniejszych
   prac najczęstsza jest Dania, ale przed `y₀` już USA. Wolno ją pokazać tylko z obiema
   miarami: *„przepływ do Chin; najwcześniejsze prace duńskie, potem amerykańskie”*. To samo
   dotyczy listy źródeł w §2: Dania wypada z listy źródeł, a blokada zostaje wśród 13 przepływów.

## 3. Rycina 2 — bez zmian w słupkach, zmiana adnotacji

Słupki „zaczął” liczą źródło tylko tam, gdzie obie miary się zgadzają (USA 34 = 26 + 8),
czyli dokładnie według reguły nazywania źródła z §1. Są poprawne przy B. Zmienia się tylko
adnotacja: **„13 of 16 flows end in China (10 of 12 when both measures must agree on the
source)”**. Przy czterech przepływach ze źródłem nierozstrzygniętym słupek „zaczął” nie ma
kraju. W podpisie wystarczy zdanie: *„origin counted only where both measures agree”*.

## 4. Kontrole

| | |
|---|---|
| nowe obliczenia | **brak** — odczyt `kraj_pochodzenia_54.csv` i `osie_54.csv` |
| odtworzenie 29/16/9 regułą B | **dokładne** |
| remisy z udziałem lidera | **0** |
| materiał | **54**, zamrożony |
| manifest | **12/12** |
| Twoje pliki (`results_v3`, `methods_v2`, `skeleton_v3`, `fig_origin_lead.*`, Twój brief) | leżały na dysku poza repo — **dodane w tym commicie**, treść nietknięta |
