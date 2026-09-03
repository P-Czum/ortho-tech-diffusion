# „11 z 24" nie odtwarza się — bo pochodzi z przebiegu z błędem. Poprawnie: **10 z 22**, i to dwa różne zjawiska

Autor: sesja VS Code, 2026-09-03. Dotyczy: `brief_dla_vsc_piec_liczb_2026-09-03.md`.

Nowy plik: `data/processed/zaniki_przed_scaleniem.csv` (22 wiersze, kolumna `los_po_scaleniu`).

**Twoja hipoteza jest trafna co do mechanizmu, ale liczba jest nie do uratowania w tej postaci.
Nie pisz „11 z 24". Poniżej liczba policzona na materiale 60 — i powód, dla którego jedno zdanie
jej nie udźwignie.**

---

## 1. §1 BLOKUJĄCE — skąd wzięło się 24, i czemu nie wolno tego cytować

Liczba pochodzi z przebiegu osi, w którym **pomyliłem argumenty i policzyłem 103 grupy zamiast
75** — podałem tylko `scalenia.json`, bez słownika synonimów. Wykryłem to po duplikatach w liście
wycofań i naprawiłem tego samego dnia. Raportowałem wtedy „lista spadła z 24 do 13".

Czyli: **24 to artefakt usterki, a nie stan „przed scaleniem".** Przypadkiem był bliski prawdy,
bo usterka polegała właśnie na niescaleniu — ale to zbieg okoliczności, nie pomiar. Do tego
13 z tamtego przebiegu było liczone **sumą szeregów członów**, a dla grup obowiązuje **zliczanie
unijne** (dokument z dwoma członami liczony raz). Suma zawyża i daje 13 zamiast 12.

### Liczba policzona porządnie, na materiale 60

Ten sam detektor trwałości (`udział 2025 / udział w szczycie < 0,5`), raz termin po terminie,
raz na grupach ze zliczaniem unijnym:

| | |
|---|---:|
| pozorne zaniki **przed scaleniem**, termin po terminie | **22** |
| zaniki **po scaleniu**, grupami | **12** |
| **usuwa je scalenie** | **10** |

## 2. Ale „10 przemianowań" też byłoby nieprawdą — to dwa różne zjawiska po pięć

Dziesiątka nie jest jednorodna i **łączenie jej w jedną liczbę zaciera właśnie to, o czym jest
praca**. Rozkład:

**(a) Pięć to podwójne liczenie — technologia zanika naprawdę, tylko pod dwiema nazwami:**

| druga nazwa | trw. | → grupa | trw. grupy |
|---|---:|---|---:|
| `aci` | 0,12 | autologous chondrocyte implantation | 0,13 |
| `hip resurfacing arthroplasty` | 0,20 | hip resurfacing | 0,15 |
| `tdr` | 0,24 | total disc replacement | 0,23 |
| `computer assisted navigation` | 0,27 | computer navigation | 0,27 |
| `balloon kyphoplasty` | 0,30 | kyphoplasty | 0,39 |

Tu scalenie **nie zmienia wniosku o żadnej technologii** — usuwa duplikat wiersza. Gdyby ktoś
liczył zaniki bez scalenia, policzyłby te pięć technologii dwa razy.

**(b) Pięć to zaniki, które scalenie unieważnia — grupa nie zanika:**

| termin | trw. | → grupa | trw. grupy | co się dzieje |
|---|---:|---|---:|---|
| `locked plating` | 0,14 | locking plate | **0,51** | dwa warianty opadają, `locking plate` nie |
| `owhto` | 0,39 | open wedge high tibial osteotomy | **0,79** | uwagę przejmuje `mowhto` |
| `pedicle subtraction osteotomy` | 0,40 | pedicle subtraction osteotomy | **0,58** | przejście na skrót `pso` |
| `lcp` | 0,42 | locking plate | **0,51** | jw. |
| `open wedge high tibial osteotomy` | 0,43 | open wedge high tibial osteotomy | **0,79** | jw. |

**Tylko ta piątka to „pozorny zanik, który był zmianą nazwy" w sensie, w jakim brzmi zdanie
w tekście.** Kryją się w niej trzy różne mechanizmy:

```
                          2010   2016   2019   2022   2025
open wedge high tib. ost. 0.092  0.118  0.225  0.203  0.096   szczyt 2019
owhto                     0.010  0.079  0.267  0.248  0.104   szczyt 2019
mowhto                    0.010  0.031  0.112  0.135  0.222   szczyt 2024  <- rosnie
```

`mowhto` (zmodyfikowana OWHTO) rośnie, gdy obie starsze formy opadają. To **nie jest** zmiana
nazwy — to trzeci, nowszy wariant przejmujący piśmiennictwo. Przy `pedicle subtraction osteotomy`
jest odwrotnie i prościej: pełna nazwa spada 0,181 → 0,111, skrót `pso` rośnie 0,165 → 0,185.
Czysty dryf ku skrótowi. Przy `locking plate` dwa warianty opadają, a nazwa główna trzyma się
na granicy progu.

### Propozycja zdania do Wyników

> Przed scaleniem wariantów dwadzieścia dwa terminy spełniały kryterium zaniku; po scaleniu
> zostaje dwanaście. Z dziesięciu usuniętych pięć było drugą nazwą tej samej zanikającej
> technologii, a pięć — formami, których spadek jest przesunięciem nazewnictwa wewnątrz grupy,
> która jako całość nie zanika.

## 3. Ostrzeżenie: liczba 12 wisi na 0,01

`locking plate` ma trwałość **0,51** przy progu 0,50. Przesunięcie progu o jedną setną zmienia
12 na 13. Nie proponuję zmiany progu — proponuję, żeby w tekście **nie stało nagie „dwanaście"**
bez wzmianki, że jedna pozycja leży na granicy. Inaczej pierwszy recenzent, który przeliczy
wrażliwość, znajdzie to sam.

## 4. §2 — pliki wyłączeń uzgadniają się co do rekordu. Definitywny jest ten drugi

| plik | zawartość | liczba |
|---|---|---:|
| `pmid_filtry_pola_d6.csv` | **log diagnostyczny**: jeden wiersz na parę (pmid, reguła), zawiera też **D5b, która NIE jest stosowana** | 32 794 wiersze |
| `pmid_pole_wylaczone_d6.csv` | **suma czterech stosowanych reguł**, po deduplikacji | **26 335 PMID** |

Sprawdzone: zbiór PMID-ów z wierszy D4+D5a+D5c+D6 pierwszego pliku jest **identyczny** ze zbiorem
drugiego pliku. Rozbieżność 32 794 → 26 335 rozkłada się dokładnie: 6 286 wierszy D5b
(niestosowana) + 173 PMID-y złapane przez więcej niż jedną regułę.

**Do Metod idzie 26 335 = 8,8%.** Liczba **11,0% jest błędna dwukrotnie**: liczy niewdrożoną
D5b i liczy podwójnie rekordy trafione dwiema regułami.

### Rozkład po deduplikacji

| reguła | trafień | wyłącznie ta reguła | przypisane wg priorytetu |
|---|---:|---:|---:|
| D4 naczyniowa | 7 784 | 7 768 | 7 784 |
| D5a stomatologiczna | 6 402 | 6 258 | 6 402 |
| D5c homonim `Traction` | 573 | 560 | 573 |
| D6 weterynaryjna | 11 749 | 11 576 | 11 576 |
| **razem** | 26 508 | | **26 335** |

Kolumna „wyłącznie ta reguła" jest odporna na kolejność i to ją proponuję do Metod, jeśli chcesz
jedną liczbę na regułę bez arbitralnego priorytetu; ostatnia kolumna zależy od kolejności
D4 → D5a → D5c → D6. **D5b zostaje w `deviations.md` §5 jako proponowana i niewdrożona** — nie
wolno jej policzyć do 8,8%.

## 5. §3 — 297 667 potwierdzone, deduplikacja udokumentowana

| | |
|---|---:|
| `noun_chunks_2000_2025.parquet` | **297 667** wierszy, **297 667** unikalnych PMID, duplikatów **0** |
| po odjęciu wyłączeń pola | **271 332** |

Deduplikacja jest wcześniej, na `analytic_index.parquet`, i ma własny raport
(`D:/medline_2026/parsed/dedup_report.json`): 45 101 678 wierszy surowych → **4 075 055
duplikatów PMID** i **5 157 `DeleteCitation`** usuniętych → 41 021 466 rekordów, 1 602 pliki
baseline. Indeks ma 0 duplikatów PMID, więc pole odziedziczyło stan po dedupie.

Zdanie do Metod: **297 667 rekordów pola def1 w latach 2000–2025 po deduplikacji, 271 332 po
czterech wyłączeniach dziedzinowych.**

## 6. §4 — to nie jest odchylenie. Ale jest niewykonane zobowiązanie, i to poważniejsze

Sprzeczności między wierszami planu nie ma. Wiersz 70 pochodzi z pierwotnej redakcji, a **ten sam
dokument** koryguje go niżej datowanym akapitem („**Podstawowa jest def1** (decyzja 2026-08-27);
def2 pozostaje analizą wrażliwości"). **Rejestracja OSF jest już zredagowana po tej korekcie** —
§33–38 mówią wprost „Secondary field definition (sensitivity analysis)". Status def2 jest więc
zgodny z rejestracją i **nie idzie do `deviations.md`.**

**Problem leży gdzie indziej i nie pytałeś o niego.** Rejestracja §111 i §114 zobowiązują do
rzeczy, która nadal obowiązuje:

> „**`y₀` reporting.** The primary-definition value with the secondary-definition value beside
> it, and a flag where the two differ by more than two years"

Tego **nie da się dziś zrobić.** Cały dorobek def2 pochodzi z 2026-08-27 i jest sprzed trzech
odchyleń naraz:

| plik def2 | jednostka | okno | filtry pola |
|---|---|---|---|
| `emerging_def2.parquet` (253 746 wierszy) | **n-gramy** (D-1) | **2005–2025** (D-3) | **brak** (D-7) |
| `def2_text.parquet` (281 261 rekordów) | tekst surowy | **2005–2025** | — |

Żadnej z tych liczb nie wolno położyć obok `y₀` materiału 60. **Są dwa wyjścia i to decyzja
ortopedy, nie moja:**

1. **Odtworzyć def2** na obecnych zasadach — dociągnięcie tekstu za 2000–2004, ekstrakcja fraz
   (~340 tys. rekordów, rząd wielkości jak def1), zliczanie, detektor, odczyt `y₀` dla 60 grup.
   Wszystkie skrypty istnieją i są sparametryzowane; to przebieg mechaniczny, zero nowych decyzji
   metodologicznych. **Rekomenduję to.**
2. **Zapisać D-11 w `deviations.md`**: zobowiązanie z §114 niewykonane, `y₀` raportowane tylko
   w def1. Uczciwe, ale oddaje recenzentowi kontrolę, którą rejestracja obiecywała.

Zwracam uwagę, że wyjście 1. jest tanie **dziś** i drogie po napisaniu Wyników, bo rozbieżność
`y₀` powyżej dwóch lat dotyczyła w rdzeniu **25% terminów** — jeśli podobnie wypadnie na
materiale 60, to jest materiał na akapit Dyskusji, a nie na przypis.

## 7. §5 — κ i 79,8% aktualne i niezmienne. Liczby przeglądu nie mam

**κ = 0,442 i 79,8% są aktualne i nie mogą się zmienić**, bo opisują **zamkniętą analizę
rejestracyjną** na rdzeniu 287 n-gramów, który jest w manifeście zamrożenia
(`emerging_core.json`). Nie dotyczą materiału 60 i nie wolno ich do niego odnosić.

Metryki do Metod, żeby nie trzeba było ich szukać:

| | |
|---|---|
| model | `openai/gpt-5.6-sol` przez OpenRouter, ziarno 20260827 |
| hash promptu | `522edf5153f20fc6` |
| podpróba | **60 terminów**, zamrożona **przed** przebiegiem (`second_coder_sample.csv`, sha256 `65aaa781…`) |
| zaślepienie | kodowanie człowieka odczytane **po** przebiegu modelu |
| zgodność surowa | **71,7%** (17 niezgodności z 60) |
| κ Cohena | **0,442**; zgodność przypadkowa 0,492 |
| κ Brennana–Predigera | 0,646 |
| 79,8% | **229 z 287** — cały rdzeń, nie podpróba |

**Uwaga redakcyjna: 71,7% i 79,8% to różne rzeczy i łatwo je pomylić** — pierwsze to zgodność
koderów na 60, drugie to udział jednej kategorii w 287. W `skeleton_v2.md` §45 stoją obok siebie
w jednym nawiasie; warto rozdzielić.

### Liczby 69 nie ma w repozytorium i nie umiem jej potwierdzić

Przeszukałem `related_work.md`, `biblio_checklist.md` i `docs/manuscript/`. **Nigdzie nie ma
policzonego N przeglądu.** `related_work.md` (2026-08-25) jest notatką narracyjną: wylicza gatunek
z nazwy, omawia dwa przykłady szczegółowo, ale nie ma zapytania, daty pobrania ani liczby trafień.

Co gorsza, dokument **sam się dyskwalifikuje** — wiersz 135:

> „To nie jest scoping search o jakości publikacyjnej. **Przed pisaniem wstępu trzeba go
> powtórzyć.**"

Więc jeśli 69 jest Twoją liczbą z osobnego przebiegu — podaj zapytanie i datę, wpiszę je do
protokołu. Jeśli pochodzi z `related_work.md`, **to jej tam nie ma** i nie wolno jej podać.
Wstęp albo dostaje policzony przegląd z jawnym zapytaniem, albo opisuje piśmiennictwo
narracyjnie, bez N. Trzeciej drogi nie ma, a BIBLIO poz. 5–6 pyta wprost o strategię
wyszukiwania.

## 8. Kontrole

| | |
|---|---|
| materiał | **60**, nietknięty (analiza na gotowych tabelach) |
| zaniki | **12**, z ostrzeżeniem o granicy 0,51 |
| osie | nietknięte |
| manifest | **12/12** |
