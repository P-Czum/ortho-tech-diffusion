# 420 nowych fraz sklasyfikowanych. Materiał rośnie z 52 do ok. 87 — i cofnięcie okna się broni

Autor: sesja Cowork, 2026-09-01. Odpowiedź na `brief_dla_cowork_okno_2000_2026-09-01.md`.

Pliki: `data/processed/np_kategorie_propozycja.tsv` (643 wiersze, było 368),
`np_synonimy.tsv` (169 par, było 125), `nowe_kandydaci_materialu.json` (44).

---

## 1. Klasyfikacja — zrobiona, tym samym schematem

420 fraz (bez 72 liczebników — u mnie 72, u Ciebie 86, patrz §5). **275 dostało kategorię
jawnie, 159 wpada domyślnie do `metoda`** — tak jak w tabeli dla 813: brak wpisu znaczy
metodologia albo artefakt.

Rozkład całej tabeli po dołożeniu:

| kategoria | wierszy |
|---|---:|
| skala | 102 |
| technika | 101 |
| rozpoznanie | 97 |
| wynik | 96 |
| parametr | 66 |
| organizacja | 59 |
| technologia | 53 |
| czynnik | 24 |
| niejasne / artefakt | 30 |
| lek | 10 |

## 2. Materiał: 52 → 96 → **87 po odjęciu generyków**

68 nowych fraz wpada w `technika` lub `technologia`. Po sklejeniu wariantów i skrótów
(44 nowe pary w `np_synonimy.tsv` — `aci`, `tdr`, `pso`, `tplo`, `lcp`, `balloon kyphoplasty`,
`microcomputed tomography` i podobne) zostaje **44 nowych pozycji**.

**Dziewięć z nich uważam za generyki i rekomenduję odrzucenie**, ale nie odrzucam ich sam —
to sprawa ortopedy:

`corrective surgery` · `definitive fixation` · `surgical fixation` · `non surgical treatment` ·
`primary total knee arthroplasty` · `lumbar fusion surgery` · `conventional instrumentation` ·
`preoperative imaging` · `postoperative imaging`

To nie są nazwane technologie, tylko opisowe kategorie czynności. Gdyby weszły, każda zajęłaby
ponad procent materiału bez wnoszenia treści.

**Materiał: 52 + 44 = 96, po odjęciu generyków 87.** Osie siły licz na wersji po decyzji Przemka —
przejrzy listę tak jak poprzednio.

## 3. Nabytek merytoryczny jest większy, niż wynika z Twojego §5

Poza `locking plate`, `kyphoplasty`, `hip resurfacing` i `adjacent segment degeneration`, które
wymieniłeś, dochodzą pozycje nietrywialne:

**Nawigacja i wspomaganie komputerowe** — `computer navigation`, `computer assisted navigation`,
`intraoperative fluoroscopy`, `robotic` jako termin samodzielny. To jest **poprzednik rodziny
robotycznej**, którego w oknie 2005–2025 nie było. Praca o dyfuzji robotyki bez nawigacji
komputerowej jako punktu odniesienia byłaby niepełna — a teraz mamy oba końce łuku.

**Materiały** — `polyetheretherketone`, `highly cross linked polyethylene`. Dwie realne
innowacje materiałowe pierwszej dekady, dotąd niewidoczne.

**Techniki, które w krótszym oknie były już powszechne** — `unicompartmental knee arthroplasty`,
`transforaminal lumbar interbody fusion`, `medial patellofemoral ligament reconstruction`,
`autologous chondrocyte implantation`, `minimally invasive plate osteosynthesis`,
`single bundle` / `double bundle reconstruction`, `ponseti method`.

To razem, nie sam `hip resurfacing`, jest argumentem za oknem 2000–2025. **Pierwsza dekada XXI
wieku nie była pusta — była poza oknem.**

## 4. Cena z §4 przyjęta, ale jest tańsza, niż wygląda

`evidence` (18,8%), `level` (18,1%), `january`, `level iv`, `complete description`,
`therapeutic study` — formuła „Level of Evidence: IV". Wszystkie wpadają do `metoda` albo
`artefakt` i **żadna nie dociera do materiału.**

Czyli: szablon wraca do **rdzenia**, nie do **mapy**. To jest różnica warta zdania w tekście,
bo pokazuje, że klasyfikacja i detekcja robią dwie różne rzeczy i druga wyłapuje to, czego
pierwsza nie odsiała. Ale w Ograniczeniach ma paść wprost, że cofnięcie okna częściowo odwróciło
zysk z przejścia na frazy — z liczbą: rdzeń rośnie z 845 do 1 294, a materiał z 52 do 87, więc
**rdzeń rośnie o 53%, a materiał o 67%** — przyrost nie jest samym śmieciem, ale bez klasyfikacji
byłby.

## 5. Rozbieżność do wyjaśnienia: liczebniki 72 czy 86

Ty podajesz 86, u mnie z `nowe_do_klasyfikacji_w2000.csv` wychodzi **72** przy filtrze
`zawiera_liczbe == False` na 506 nowych. Różnica 14. Podejrzewam, że liczysz też frazy
**zawierające** liczbę obok słowa (`level iv`, `12 month`), a ja tylko frazy będące wyłącznie
liczbami. Zgłaszam, nie poprawiam — sprawdź, która definicja jest w Twoim skrypcie, bo ta
liczba pójdzie do tekstu.

## 6. Dwie rzeczy, które wypadły — moim zdaniem obie do odnotowania, nie do ratowania

`virtual reality` i `transfemoral amputation`. Pierwsza jest realną stratą: VR wyłania się
w krótszym oknie, a w dłuższym baza rośnie na tyle, że próg nie zostaje przekroczony.
**To jest własność progu, nie zjawiska** — i dokładnie ten sam mechanizm, którym S1 wycinał
`3d printing`. Warto to zestawić w Metodach jako jedną obserwację: *próg wyłonienia jest
wrażliwy na długość okna bazowego w obie strony*.

`transfemoral amputation` zostawiłem świadomie przy D4 jako protetykę; jego wypadnięcie
z materiału tę decyzję unieważnia bezboleśnie.

## 7. Twoje znalezisko z §2 jest pilniejsze niż całe okno

Udział pola w PubMedzie: **1,257% w 2011 → 0,825% w 2025, spadek o 34%.** Zgadzam się, że to
wygląda na nieciągłość indeksowania i że nikt tego nie sprawdził.

**To jest zagrożenie dla głównej osi rankingu.** `prevalence_2021_2025` to udział liczony na
mianowniku z lat, w których pole kurczy się najszybciej. Jeżeli niedoindeksowanie jest wybiórcze
— a przy przejściu na MTIX w 2022 nie ma powodu zakładać, że jest równomierne — to ranking
premiuje terminy z prac, które MTIX indeksuje chętniej.

Proponuję to jako **następny brief, przed osiami siły**: rozkład deskryptorów pola przed i po
2022, oraz udział pola liczony osobno dla rekordów `medline_indexed` i pozostałych. Jeżeli
rozjazd jest równomierny, zamykamy sprawę jednym zdaniem; jeżeli nie — trzeba zmienić oś
rankingu albo mianownik.

## 8. Stan

Manifest 12/12 po Twojej stronie. Klasyfikacji istniejących 788 nie ruszałem — dopisałem tylko
nowe wiersze i zdeduplikowałem tabelę. `coding_manual_v1.2.md` nietknięty.
