# Mapowanie innowacji w ortopedii na podstawie MEDLINE — protokół v0.1

Status: projekt do dyskusji. Data: 2026-08-25.
Źródło danych: lustro MEDLINE 2026 (`medline_fetch.py` → `medline_extract.py`).

---

## 1. Pytania badawcze

**P1 (główne, opisowe).** Jak zmieniał się udział publikacji ortopedycznych dotyczących
poszczególnych rodzin technologii w latach 2005–2025?

**P2 (dynamika).** Kiedy każda technologia przekracza progi rozpowszechnienia i czy krzywe
mają punkty przegięcia? Ile trwa faza podwajania?

**P3 (eksploracyjne).** Jakie tematy rosną najszybciej niezależnie od zadeklarowanej listy —
czy istnieją innowacje, których nie przewidzieliśmy?

**P4 (opcjonalne, warstwa preprintowa).** O ile preprinty medRxiv wyprzedzają MEDLINE
w pierwszym wystąpieniu danej technologii?

---

## 2. Definicja pola: co to jest „publikacja ortopedyczna"

Trzy operacjonalizacje, liczone równolegle. **Podstawowa jest B**; A i C to analizy wrażliwości.

**A. Kryterium czasopisma.** Rekord opublikowany w czasopiśmie, któremu NLM przypisał
Broad Subject Term „Orthopedics". Wysoka swoistość, stabilne w czasie, łatwe do audytu.
Pomija ortopedię w czasopismach ogólnych, obrazowych i inżynierskich.

**B. Kryterium MeSH — ortopedia zabiegowa.** Rekord ma co najmniej jeden deskryptor
z rozwiniętych („explode") poddrzew: `Orthopedic Procedures`, `Arthroplasty`,
`Fracture Fixation`, `Fractures, Bone`, plus wybrane gałęzie `Musculoskeletal Diseases`
związane z leczeniem zabiegowym. **Poddrzewa rozwijamy programowo z `desc2026.xml`
(MeSH descriptor file), nie z ręcznie przepisanej listy** — numery drzewa zmieniają się między
rocznikami i ręczna lista cicho się rozjedzie.

Świadome wykluczenie: czysta reumatologia zachowawcza i metaboliczne choroby kości bez
komponentu zabiegowego. Innowacja, o którą pytamy — druk, robot, nawigacja — żyje w sali
operacyjnej, a `Musculoskeletal Diseases` w całości wciągnęłoby dwa razy więcej rekordów
o zupełnie innym profilu.

**C. Kryterium tekstowe.** Wyrażenie regularne na tytule, abstrakcie i słowach kluczowych
(`TEXT_MSK` w `medline_extract.py`). Jedyne, które działa na rekordach „in process" bez MeSH —
dlatego **musi** być użyte do zamknięcia prawej krawędzi każdej krzywej.

Raportujemy przecięcia i różnice A/B/C w tabeli, a przepływ rekordów w diagramie PRISMA-podobnym.

---

## 3. Zakres czasowy

**Podstawowy: 2005–2025.** Kompletne roczniki, dojrzałe indeksowanie, wysoka dostępność
abstraktów. Daje 5–8 lat okresu przedwzrostowego dla technologii, które startują ok. 2012–2015
(druk 3D, uczenie maszynowe) — bez tego nie da się pokazać, że wzrost to wzrost.

**Rozszerzony do 1990 r.** jako analiza wrażliwości: sprawdza, czy wnioski nie zależą od punktu
odcięcia, i pokazuje pełną historię technologii starszych (nawigacja komputerowa, robotyka).

**Rok 2026 wyłączony z analizy głównej.** Jest niekompletny i niedoindeksowany; pokazujemy go
osobno, oznaczonego jako niepełny, żeby nikt nie odczytał artefaktu jako końca trendu.

---

## 4. Definicja innowacji: warstwa konfirmacyjna

Rodziny technologii, każda z dwoma niezależnymi definicjami — **MeSH** (jeśli deskryptor istnieje)
i **tekstową**. Obie liczone osobno przez cały czas trwania analizy.

| rodzina | rdzeń definicji |
|---|---|
| wytwarzanie addytywne | druk 3D, produkcja addytywna, instrumentarium/implanty pacjento-specyficzne |
| robotyka | chirurgia wspomagana robotem, ramię robotyczne |
| nawigacja i obrazowanie śródoperacyjne | nawigacja chirurgiczna, CAS, O-arm, fluoro 3D |
| rzeczywistość rozszerzona i wirtualna | AR, VR, mixed reality, symulatory |
| sztuczna inteligencja | uczenie maszynowe, sieci neuronowe, radiomika, modele językowe |
| czujniki i wearables | akcelerometria, IMU, analiza chodu, implanty z czujnikami |
| zdrowie cyfrowe | telemedycyna, zdalne monitorowanie, aplikacje mobilne |
| biomateriały i powłoki | tytan porowaty, powłoki, biowchłanialne, magnez, tantal |
| terapie biologiczne | PRP, komórki macierzyste, scaffoldy, BMP, inżynieria tkankowa |
| dane i rejestry | rejestry endoprotezoplastyki, PROM, RWE |

Lista jest **preregistrowana przed analizą**. Rozszerzenia po zobaczeniu danych są dozwolone,
ale muszą być raportowane jako post hoc i pokazane osobno.

### Pułapka, która zniszczy wynik, jeśli się ją przeoczy

Deskryptory MeSH mają daty wprowadzenia. `Printing, Three-Dimensional` wszedł do słownika
w 2017 r. — prace wcześniejsze nie mają go, mimo że opisują to samo. Krzywa oparta na MeSH
pokaże wtedy skok, który jest zmianą słownika, nie zmianą praktyki.

Dlatego: **krzywa główna każdej technologii jest liczona po tekście**, krzywa MeSH służy jako
walidacja, a na każdym wykresie MeSH zaznaczamy pionową linią rok wprowadzenia deskryptora
(pobrany programowo z `desc2026.xml`, nie z pamięci).

---

## 5. Definicja innowacji: warstwa eksploracyjna

Na podzbiorze ortopedycznym, na tytułach i abstraktach:

1. **Wykrywanie terminów wschodzących** — n-gramy o największym przyspieszeniu udziału
   rok do roku (detekcja „burstów"), z filtrem na minimalną liczebność bezwzględną.
2. **Klastrowanie semantyczne** — osadzenia zdaniowe tytułu i abstraktu, redukcja wymiaru,
   klastrowanie; nazwy klastrów nadawane po fakcie, na podstawie terminów wyróżniających.
3. Klastry rosnące najszybciej konfrontujemy z listą z sekcji 4. **Co znalazło się poza listą,
   jest wynikiem** — i to jest właściwa odpowiedź na P3.

Raportowane jawnie jako eksploracja, bez testów istotności udających konfirmację.

---

## 6. Mianownik i miary

**Mianownikiem jest pole, nie PubMed.** Dla każdego roku: udział = rekordy ortopedyczne
z technologią X / wszystkie rekordy ortopedyczne. Liczby bezwzględne raportujemy obok,
ale wnioskujemy z udziałów — inaczej zmierzymy wzrost PubMedu, nie dyfuzję technologii.

Dodatkowo udział ortopedii w całym MEDLINE (z tabeli `index/`), żeby oddzielić wzrost pola
od wzrostu bazy.

Miary:

- roczny udział z przedziałem ufności Wilsona,
- **regresja segmentowa / joinpoint** — lokalizacja punktów przegięcia i tempo w każdym odcinku,
- **czas do adopcji** — pierwszy rok z ≥5 rekordami, rok osiągnięcia 0,5 % i 1 % udziału,
- **czas podwojenia** w fazie wzrostu wykładniczego,
- dla P4: różnica mediany dat pierwszego wystąpienia medRxiv vs MEDLINE.

---

## 7. Kryteria włączenia rekordu

Włączone typy publikacji: `Journal Article`, `Review`, `Systematic Review`, `Meta-Analysis`,
`Clinical Trial` i pochodne.
Wykluczone: `Comment`, `Editorial`, `Letter`, `News`, `Published Erratum`, `Retracted Publication`.
Analiza wrażliwości bez tego filtra — redakcyjne omówienia nowych technologii same w sobie są
sygnałem szumu wokół innowacji i warto pokazać, jak zmieniają obraz.

Bez ograniczenia językowego. Rekordy bez abstraktu zostają w mianowniku, ale nie mogą trafić
do licznika definicji tekstowej — ten fakt musi być w raporcie, bo zaniża wczesne lata.

---

## 8. Walidacja

| co | jak | próg |
|---|---|---|
| definicja pola | ręczny przegląd 200 losowych rekordów zaklasyfikowanych jako ortopedyczne | PPV ≥ 0,90 |
| czułość pola | 200 rekordów z czasopism ortopedycznych odrzuconych przez kryterium B | udział trafnych odrzuceń |
| słowniki technologii | 50 rekordów na rodzinę | PPV raportowany per rodzina |
| kontrola pozytywna | technologia o znanym przebiegu (np. artroskopia w latach 90.) | krzywa musi odtworzyć znany kształt |
| kontrola negatywna | termin bez powodu do wzrostu | brak trendu |

Kodowanie ręczne przez dwie osoby na podpróbie, zgodność Cohena κ.

---

## 9. Znane zagrożenia dla trafności

- **Opóźnienie indeksowania** — prawa krawędź krzywej MeSH sztucznie opada. Rozwiązanie:
  krzywa tekstowa + kolumna `indexed` + wyłączenie 2026.
- **Powstawanie nowych czasopism** — nowe tytuły w podspecjalności zawyżają liczby.
  Kontrola: analiza wrażliwości na stałym zbiorze czasopism istniejących w całym okresie.
- **Przesunięcie geograficzne** — gwałtowny wzrost produkcji z jednego kraju może zdominować
  krzywą technologii. Raportujemy rozkład krajów per technologia per okres.
- **Zmiany polityki indeksowania NLM** między rocznikami.
- **Wieloznaczność terminów** — „3D" łapie obrazowanie 3D, nie tylko druk; „robot" łapie
  roboty rehabilitacyjne. Stąd wymóg raportowania PPV per rodzina.

---

## 10. Produkty

1. Preregistracja protokołu (OSF) przed analizą.
2. Repozytorium kodu w konwencji `myslniki`: `code/`, `data/processed/`, `results/`, `logs/`,
   `docs/`, LICENSE, CITATION.cff.
3. Zestaw rycin: krzywe udziału per rodzina, mapa klastrów, tabela czasów adopcji,
   diagram przepływu rekordów.
4. Manuskrypt.

---

## 11. Decyzje do podjęcia przed startem

1. **Zakres pola** — ortopedia zabiegowa (rekomendacja) czy całe `Musculoskeletal Diseases`?
   Różnica to prawdopodobnie czynnik 2–3 w liczbie rekordów i inny profil tematyczny.
2. **Początek okresu** — 2005 (rekomendacja) czy 1990?
3. **Czy P4** — warstwa preprintowa medRxiv wchodzi do tej pracy, czy zostaje na osobną?
