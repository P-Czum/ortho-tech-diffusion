# Test kontekstowy — miara widzi przemianowanie

Autor: sesja VS Code, 2026-08-28. Dotyczy: `brief_dla_vsc_test_kontekstowy_2026-08-28.md`.

Skrypt: `code/context_shift_test.py`, wynik `results/context_shift.json` (poza gitem, odtwarzalny
przy `SEED = 20260828`). Miara, okna i progi zapisane w nagłówku skryptu **przed** policzeniem.

---

## 1. Odpowiedź na §4, jednym zdaniem

**Tak — miara widzi przemianowanie, i odróżnia je od zawierania w przewidzianym kierunku.**

## 2. Trzy liczby

| | podobieństwo | n | percentyl w rozkładzie losowym |
|---|---:|---|---:|
| **para 1: `rapid prototyping` [2008–13] vs `3d printing` [2016–21]** | **0,3816** | 108/470 | **100,0** |
| **para 2: `computer navigation` [2008–13] vs `robotic` [2018–23]** | **0,3272** | 275/1018 | **99,5** |

Para 1 leży **powyżej wszystkich 200** dobranych liczebnościowo par losowych; para 2 powyżej 199
z 200. W jednostkach rozkładu: **z = 8,3** i **z = 3,6**.

Rozkłady odniesienia liczone osobno dla każdej pary, na parach dobranych tak, by liczebności
w obu oknach mieściły się w ±30% wobec pary docelowej:

```
para 1:  srednia 0,1392  sd 0,0293  p95 0,1882  max 0,2719   (n=200)
para 2:  srednia 0,1879  sd 0,0388  p95 0,2501  max 0,3549   (n=200)
```

## 3. Kontrole — i jedna, która wyszła tak, jak ostrzegałem przed uruchomieniem

| kontrola | wynik | n |
|---|---:|---|
| **+ zamówiona**: `3d printing` [2008–13] vs [2016–21] | **0,2226** | 6/470 |
| **+ liczebna**: `venous thromboembolism` [2008–13] vs [2016–21] | **0,5390** | 521/626 |
| **−**: `3d printing` vs `venous thromboembolism`, oba [2016–21] | **0,1025** | 470/626 |

**Kontrola pozytywna z briefu jest nieużyteczna i wypadła poniżej obu par docelowych.** Powód
sprawdziłem przed liczeniem: `3d printing` ma w oknie 2008–2013 **sześć rekordów**. Wektor z sześciu
prac mierzy rzadkość, nie górny kres miary — gdyby zostawić ją samą, wynik czytałoby się jako
„para docelowa podobniejsza niż ten sam termin do siebie", co jest artefaktem, nie odkryciem.

Dlatego dołożyłem drugą kontrolę pozytywną na terminie o przyzwoitej liczebności po obu stronach.
**To ona jest kresem górnym: 0,5390.** Zgłaszam jako odstępstwo od §1 briefu — jedyne.

Położenie par docelowych między kontrolami:

- para 1: **64% drogi** od negatywnej do pozytywnej, bliżej pozytywnej (0,157 vs 0,279)
- para 2: **51% drogi**, bliżej pozytywnej (0,212 vs 0,225)

Kryterium z §1 („wyraźnie powyżej rozkładu losowego i bliżej kontroli pozytywnej") **spełnione
przez obie pary**.

## 4. Druga para zachowała się zgodnie z §2

Oczekiwałeś: podobieństwo wysokie, ale **niższe** niż przy druku 3D. Tak wyszło, i to na obu
sposobach liczenia — surowo (0,3272 wobec 0,3816) i po standaryzacji własnym rozkładem
(z = 3,6 wobec 8,3). Różnica po standaryzacji jest wyraźniejsza, bo `robotic` ma 1018 rekordów
i jego rozkład odniesienia siedzi wyżej: **większe próby dają mniej zaszumione wektory, więc
podnoszą tło**. Surowych podobieństw z dwóch par nie wolno porównywać wprost.

## 5. Czego ten wynik NIE dowodzi

Trzy zastrzeżenia, bo bez nich liczba 100. percentyla łatwo przeczytać za mocno.

**Dwa przypadki to nie walidacja.** Kierunek zgadza się na obu parach, ale „miara odróżnia
przemianowanie od zawierania" wymagałoby rozkładu na wielu parach każdego typu. Na razie mamy
dwie strzałki wskazujące w tę samą stronę.

**Miara łapie bliskość tematyczną, nie tożsamość pojęcia.** Widać to w ogonie rozkładu losowego:
najwyższe pary to `implant surface / experimental study` (0,2719) i `bone allograft / tissue and`
(0,3549) — czyli terminy z tego samego obszaru, bez żadnego następstwa. Para docelowa je bije,
ale przewaga jest ilościowa, nie jakościowa.

**Wysokie tło pary 2 nie jest szumem do odjęcia.** `bone allograft / tissue and` na 0,3549 to
para tematycznie sąsiednia i to jest uczciwa konkurencja dla `computer navigation / robotic`.
Rozkład losowy jest czysty — sprawdziłem pięć najwyższych par w obu rozkładach, żadna nie jest
zamaskowanym wariantem tego samego terminu.

## 6. Decyzje techniczne, które musiałem podjąć sam

Brief nie przesądzał normalizacji („PPMI albo zwykłe udziały — wybierz jedno i zapisz które").

- **PPMI**, na częstości **dokumentowej**, nie tokenowej — odporniejsze na jedną pracę powtarzającą
  termin dwadzieścia razy.
- **Tło liczone per okno**, nie globalnie. Inaczej mierzylibyśmy dryf częstości słów w czasie:
  słowo częstsze w 2016–2021 niż w 2008–2013 dostawałoby wyższe PPMI w późnym oknie z samego
  upływu czasu.
- **Z obu wektorów usuwane są tokeny obu porównywanych terminów**, tak samo w parach losowych.
  Bez tego `3d`/`printing` podbijałyby podobieństwo same z siebie.
- Słownik kontekstu: unigramy o częstości dokumentowej ≥ 50 w korpusie (14 247 tokenów).
- Korpus: `field_canon.parquet`, 268 383 rekordy pola def1, tekst po kanonizacji z §3.1.

Żadnego stroje­nia pod wynik: parametry stoją jako stałe w nagłówku skryptu, jeden przebieg,
jedno ziarno. Drugi przebieg dołożył wyłącznie wypisanie pięciu najwyższych par losowych —
diagnostykę, nie zmianę miary; liczby są identyczne.

## 7. Nie interpretuję dalej

Zgodnie z §4 zatrzymuję się na wyniku. Decyzja o projekcie należy do Przemka.

## 8. Stan

Manifest **12/12**. Arkusz zamrożony bez zmian.

`coding_sheet_koder_CODED_2026-08-28.csv` leży nietknięty w katalogu głównym, **nieśledzony**.
Dołożyłem go do `.gitignore` wzorcem `coding_sheet_koder_CODED_*.csv` — nie po to, żeby
przesądzać, czym się stanie, tylko żeby `git add -A` nie wciągnął go przypadkiem. Zdjęcie wzorca
to jedna linia, kiedy zapadnie decyzja.

Jedna obserwacja przy okazji, bo może się przydać do tej decyzji: **plik ma 287 z 287 wierszy
z niepustą kategorią**, czyli kodowanie ręczne jest kompletne, a nie przerwane. Samych kategorii
nie oglądałem — policzyłem wypełnienia, nie wartości.
