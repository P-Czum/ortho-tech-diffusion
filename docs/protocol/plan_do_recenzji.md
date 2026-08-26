# Dyfuzja badań nad technologiami w ortopedii — plan badania
## Wersja 0.3 · 2026-08-26 · Przemysław Czuma

Zastępuje `protokol_mapowanie_innowacji.md` (v0.1) i v0.2. Zmiany wobec v0.1 — sekcja 10,
wobec v0.2 — sekcja 10.1.

---

## 1. Cel i sformułowanie

Zmierzyć, jak w latach 2005–2025 zmieniał się udział piśmiennictwa ortopedycznego
dotyczącego poszczególnych rodzin technologii, i zidentyfikować punkty przyspieszenia.

**Twierdzenie o nowości: pierwsze porównanie wielu rodzin technologii w jednej specjalności
na wspólnym, znormalizowanym mianowniku.** Przeszukanie z 2026-08-26 (`scoping_log.md`)
znalazło w PubMedzie 69 prac bibliometrycznych o technologiach w ortopedii, w tym co najmniej
sześć poświęconych z osobna drukowi 3D i robotyce. **Wszystkie są jednotechnologiczne i
wszystkie raportują liczby bezwzględne.** Żadna nie zestawia rodzin ze sobą ani nie odnosi ich
do produkcji pola, więc żadna nie potrafi odpowiedzieć, która technologia rośnie *kosztem*
której. Tę lukę zajmujemy. Pytanie „jak rósł druk 3D w ortopedii" jest zajęte wielokrotnie
i nie jest naszym pytaniem.

**Co z tego ma czytelnik kliniczny.** Bez tego praca jest ćwiczeniem bibliometrycznym:

1. **Które rodziny rosną, a które weszły w plateau** — na tle całej produkcji pola, nie
   w liczbach bezwzględnych, które rosną zawsze, bo rośnie sama baza.
2. **Czy wzrosty są równoczesne, czy jedne rodziny wypierają inne** z uwagi badawczej.
   Wspólny mianownik jest jedynym sposobem, żeby to rozstrzygnąć — przy liczbach
   bezwzględnych wszystko rośnie i pytanie nie ma sensu.
3. **Gdzie rozjazd między szumem a dorobkiem jest największy.** Rodzina o stromym wzroście
   udziału przy niskiej liczebności bezwzględnej to kandydat na modę, nie na dyfuzję.

**Ramka interpretacyjna, konsekwentnie w całej pracy:** mierzymy *dyfuzję badań nad
technologią* i *uwagę naukową* (diffusion of technological research / scholarly attention).
**Nie** mierzymy adopcji klinicznej. Publikacja jest przybliżeniem zainteresowania i obiegu idei,
nie dowodem, że technologia weszła do praktyki. Wzrost liczby prac o robotyce może odzwierciedlać
aktywność marketingową producentów, a nie liczbę wykonanych zabiegów. Formułowanie wniosków musi
tego pilnować w tytule, abstrakcie i dyskusji.

### 1.1. Zakres tej pracy a praca metodologiczna

Materiał zebrany przy projektowaniu tego badania wystarcza na dwie prace i **ta jest pierwsza
z nich**. Tutaj metoda jest maszynerią opisaną w Metodach, nie tezą.

Do osobnej pracy metodologicznej (dalej **praca A**) odkładamy:

- analizę luk w wytycznej BIBLIO (`biblio_checklist.md`) — brak wymogu walidacji strategii
  wyszukiwania, brak wymogu normalizacji, brak odniesienia do zmiany terminologii w czasie;
- wywód o dwóch rozłącznych nurtach: dyfuzja technologii mierzona patentami wobec udziałów
  publikacyjnych liczonych dla dyscyplin i demografii (`scoping_log.md`);
- warstwy epokowe jako *twierdzenie* o niezmienniczości pomiaru — tutaj ich używamy
  i raportujemy PPV w epokach, ale nie budujemy z tego tezy;
- uogólnienie miary na inne specjalności kliniczne.

**Warunek, żeby praca A pozostała publikowalna po tej.** Nie może być „ta sama metoda, opisana
porządnie" — dostałaby zarzut uprzedniej publikacji. Musi wnieść co najmniej jedno z:
zastosowanie na kilku specjalnościach, formalną walidację niezmienniczości, albo komponent
pokazujący ilościowo, jak bardzo krzywa nienormalizowana myli. Metody tej pracy piszemy
kompletnie i odtwarzalnie, ale bez rozwijania ogólnego argumentu — inaczej praca A nie zostanie
z czym.

**Czego nie odkładamy.** Wynik przeszukania o jednotechnologiczności tych 69 prac jest
uzasadnieniem luki *tej* pracy i idzie wprost do wstępu, nie do pracy A.

## 2. Punkt wyjścia

**Pilotaż na medRxiv — wynik negatywny, przesądził o wyborze źródła.** Kategoria `Orthopedics`
to 316 prac przez siedem lat (potwierdzone niezależnie stroną kolekcji medRxiv: 381 na dziś).
Słownik technologii dał: AI 44, wearables 13, terapie biologiczne 6, **druk 3D 4**, robotyka 2,
nawigacja 1, AR/VR 1. Przyczyna strukturalna: medRxiv to ~88 tys. prac w całości, zdominowanych
przez epidemiologię i choroby zakaźne (29 % korpusu), specjalności zabiegowe marginalne.

**Dane docelowe:** PubMed Baseline 2026 (`pubmed26n0001`–`n1334`, wydany 2026-01-30) + pliki
aktualizacyjne. Skala odniesienia: PubMed przyjął 1 881 469 rekordów w samym 2025 r.

## 3. Dane — PubMed to nie MEDLINE

Baseline zawiera **cały PubMed**; MEDLINE jest jego podzbiorem. Mieszanie ich zafałszuje
mianownik, dlatego tabela zawiera trzy niezależne flagi:

| pole | znaczenie |
|---|---|
| `status` | `MedlineCitation/@Status`: MEDLINE, In-Process, In-Data-Review, Publisher, PubMed-not-MEDLINE, OLDMEDLINE |
| `medline_indexed` | `status == "MEDLINE"` — rekord w pełni zaindeksowany |
| `indexed` | rekord ma jakikolwiek deskryptor MeSH |
| `citation_subset` | podzbiory NLM |

Mianownik trendu liczymy na jawnie zadeklarowanym podzbiorze, nigdy „na PubMedzie" bez
doprecyzowania. Rekordy bez MeSH nie znikają — łapie je definicja tekstowa, dzięki czemu prawa
krawędź krzywej nie opada sztucznie.

## 4. Definicja pola

**Primary: `Orthopedic Procedures` + wszystkie potomne deskryptory MeSH.**

Obejmuje artroplastykę, osteotomie, artroskopię, zespolenia złamań, chirurgię kręgosłupa, ale
także procedury nieoperacyjne w rodzaju zamkniętej repozycji złamania. Traumatologia narządu
ruchu pozostaje w polu.

Roboczo pole nazywamy **procedural / interventional orthopaedics and musculoskeletal trauma** —
nie „surgical orthopaedics". Rezygnujemy z opozycji „zabiegowa vs zachowawcza", bo ta granica
jest sztuczna i nie da się jej czysto przeprowadzić.

**`Fractures, Bone` nie wchodzi do definicji podstawowej.** To gałąź chorobowa (C26), nie
proceduralna — wciągnęłaby epidemiologię złamań, diagnostykę, osteoporozę i profilaktykę
niezależnie od jakiejkolwiek interwencji ortopedycznej. Wchodzi natomiast do szerszej analizy
wrażliwości.

**Rozwijanie poddrzewa jest programowe** (`mesh_tree.py`, z pliku deskryptorów `descYYYY.xml`).
Numery drzewa zmieniają się między rocznikami; lista przepisana ręcznie rozjedzie się po cichu,
bez żadnego komunikatu o błędzie.

**Rozwinięcie wykonane 2026-08-26 na `desc2026.xml`: 56 deskryptorów.** Weryfikacja pokazała,
że v0.1 wymieniała cztery korzenie niepotrzebnie — `Arthroplasty` (D001178, poddrzewo 14)
i `Fracture Fixation` (D005592, poddrzewo 6) są **potomkami** `Orthopedic Procedures`
i wnoszą **zero** deskryptorów ponad nie. Po wyłączeniu `Fractures, Bone` definicja pola
sprowadza się więc do **jednego korzenia**. Unia czterech korzeni z v0.1 dałaby 107
deskryptorów; różnicę 51 wnosi wyłącznie `Fractures, Bone`, czyli dokładnie ta gałąź
chorobowa, którą wykluczamy — co potwierdza, że wykluczenie jest istotne, a nie kosmetyczne.

Kontrola negatywna do powtarzania przy każdej zmianie rocznika MeSH: w rozwiniętym poddrzewie
nie może być żadnego deskryptora z numerem drzewa `C*`. Na `desc2026.xml` jest ich zero.

Analizy wrażliwości nad definicją pola: (a) + `Fractures, Bone` i potomne, (b) czasopisma
z NLM Broad Subject Term „Orthopedics", (c) kryterium tekstowe.

## 5. Zakres czasowy

**2005–2025.** Daje 5–8 lat okresu przedwzrostowego dla technologii startujących ok. 2012–2015.
Rok 2026 wyłączony z analizy głównej — niekompletny i niedoindeksowany; pokazywany osobno,
oznaczony jako niepełny. Rozszerzenie do 1990 r. jako wrażliwość.

## 6. Technologie

**Trend podstawowy liczony z tytułu i abstraktu, nie z MeSH.** Deskryptory wchodziły do słownika
w różnych latach i nie zawsze były indeksowane retrospektywnie —
`Printing, Three-Dimensional` (D066330) wszedł w **2015 r.** Krzywa oparta na MeSH pokazałaby
wtedy skok będący zmianą słownika, nie zmianą praktyki badawczej. MeSH służy do walidacji;
na wykresach walidacyjnych zaznaczamy rok wprowadzenia deskryptora, pobrany programowo.

### 6.1. Niezmienniczość pomiaru w czasie — najpoważniejszy problem metodologiczny

Słownik tekstowy musi łapać to samo zjawisko w 2005 i w 2025 r. Terminologia technologii zmienia
się szybciej niż same technologie. Praca o drukowanym szablonie operacyjnym z 2008 r. nazywa to
`rapid prototyping` albo `stereolithography`; ta sama praca z 2022 r. mówi `3D printing`.
Słownik zbudowany na dzisiejszym języku zmierzy zmianę nazewnictwa i nazwie ją dyfuzją.

Konsekwencje operacyjne:

1. Każda rodzina ma **warstwy epokowe** synonimów — terminy historyczne obowiązują przez cały
   okres, nie tylko w epoce swojego rozkwitu.
2. **PPV liczony osobno w epokach** 2005–2011, 2012–2018, 2019–2025. Spadek precyzji w jednej
   epoce jest sygnałem, że słownik nie jest niezmienniczy.
3. Krzywe udziału poszczególnych synonimów wewnątrz rodziny raportujemy jako materiał
   diagnostyczny — pokazują moment przełączenia terminologii.

### 6.2. Pięć rodzin na Etap 1 (z warstwami historycznymi)

| rodzina | warstwa wczesna (2005–2012) | warstwa późna |
|---|---|---|
| **druk 3D / addytywna** | rapid prototyping, stereolithography, selective laser sintering/melting, fused deposition modeling, electron beam melting, CAD/CAM | 3D printing, three-dimensional printing, additive manufacturing, patient-specific instrumentation/guide/implant |
| **robotyka** | robotic surgery, robot-assisted, ROBODOC, computer-integrated surgery | robotic arm-assisted, semi-autonomous, handheld robotic |
| **nawigacja** | computer-assisted surgery/navigation, image-guided, fluoroscopic navigation | augmented reality navigation, mixed reality, intraoperative 3D imaging |
| **sztuczna inteligencja** | expert system, artificial neural network, pattern recognition | machine learning, deep learning, radiomics, large language model, foundation model |
| **biomateriały / powłoki** | hydroxyapatite coating, porous coating, bioabsorbable, PEEK | trabecular metal, porous tantalum, magnesium alloy, antibacterial coating |

**Hierarchia zostaje na później.** Docelowo `3D printing` jest rodziną nadrzędną, a pod nią
modele anatomiczne, szablony/PSI, implanty na miarę, rusztowania tkankowe. Rozbicia nie robimy
przed Etapem 1 — najpierw musimy wiedzieć, czy rodzina nadrzędna ma liczebność.

## 7. Mianownik, geografia, modelowanie

**Mianownik: pole.** Udział = rekordy pola z technologią X / wszystkie rekordy pola w danym roku.
Liczby bezwzględne raportowane obok. Udział pola w całym zadeklarowanym podzbiorze PubMed —
osobno, żeby oddzielić wzrost pola od wzrostu bazy.

**Geografia: kraj pierwszego autora.** Afiliacje wszystkich autorów nie są historycznie
porównywalne (MEDLINE zapisuje je systematycznie dopiero od połowy lat 2010.), więc jedyną
spójną w czasie jednostką jest afiliacja pierwszego autora. Kraj czasopisma
(`MedlineJournalInfo/Country`) trzymamy osobno — to inna zmienna, nie zamiennik.

Obok krzywych surowych liczymy **krzywą standaryzowaną przy stałych wagach krajów** (standaryzacja
bezpośrednia względem struktury z roku bazowego). To rozdziela rzeczywistą zmianę zainteresowania
technologią od zmiany struktury geograficznej piśmiennictwa — bez tego ekspansja produkcji
naukowej jednego kraju sama wygeneruje krzywą wyglądającą jak dyfuzja.

**Model trendu: primary — regresja segmentowa / joinpoint** na udziale publikacji
technologicznych w polu. Krzywa logistyczna i model Bassa **wyłącznie eksploracyjnie**, i tylko
jeśli w danych rzeczywiście pojawi się nasycenie. Dopasowywanie modelu dyfuzji do krzywej, która
wciąż rośnie, produkuje ekstrapolacje bez pokrycia.

**Cytowania nie są potrzebne do pytania podstawowego.** Pytamy o dyfuzję w piśmiennictwie, nie
o wpływ cytowaniowy. Scopus / WoS / OpenAlex mogą stanowić późniejszą warstwę dodatkową.

## 8. Kryteria włączenia rekordu

Włączone: Journal Article, Review, Systematic Review, Meta-Analysis, Clinical Trial i pochodne.
Wykluczone: Comment, Editorial, Letter, News, Published Erratum, Retracted Publication.
Wrażliwość bez tego filtra. Bez ograniczenia językowego. Rekordy bez abstraktu zostają
w mianowniku, ale nie mogą trafić do licznika definicji tekstowej — fakt raportowany, bo zaniża
wczesne roczniki.

## 9. Plan etapowy

**Etap 1 — czy krzywe w ogóle istnieją (≈1 dzień po pobraniu).**
2005–2025 × `Orthopedic Procedures` + potomne × 5 rodzin × licznik roczny + udział w polu.
Bez walidacji, bez alternatywnych definicji pola, bez modelowania.
*Kryterium przejścia:* co najmniej jedna rodzina osiąga rzędy setek rekordów rocznie i widoczną
zmianę udziału.

**Etap 2 — czy to jest publikowalne (≈1 tydzień).**
- **PPV: 90–120 trafień na rodzinę**, stratyfikowane po epokach 2005–2011 / 2012–2018 / 2019–2025.
  (50 na rodzinę, jak było w v0.1, wystarczy najwyżej na sanity check, nie na walidację końcową.)
- **Przynajmniej przybliżona ocena czułości / relative recall** — nie sam PPV. Ramy odniesienia
  do rozważenia: zbiór referencyjny z przeglądów systematycznych danej technologii, porównanie
  z niezależną strategią (MeSH vs tekst) metodą capture–recapture, ręczny przegląd próby z pola
  bez trafienia.
- Alternatywne definicje pola, przedziały ufności, rozkłady geograficzne i czasopiśmiennicze.
*Kryterium przejścia:* PPV pola ≥ 0,90, stabilność wniosków między definicjami, brak dryfu PPV
między epokami.

**Etap 3 — pełne badanie.** Preregistracja, hierarchia technologii, warstwa eksploracyjna
(terminy wschodzące, klastrowanie osadzeń), joinpoint, podwójne kodowanie z κ, manuskrypt.

## 10. Co zmieniła recenzja wobec v0.1

1. Pole: `Orthopedic Procedures` + potomne zamiast „ortopedii zabiegowej"; `Fractures, Bone`
   wypada z definicji podstawowej i schodzi do wrażliwości.
2. Nazwa pola: procedural/interventional orthopaedics and musculoskeletal trauma.
3. Rozdzielenie PubMed / MEDLINE na trzy osobne flagi statusu.
4. **Korekta faktograficzna:** `Printing, Three-Dimensional` wszedł do MeSH w 2015, nie 2017.
5. Niezmienniczość pomiaru w czasie podniesiona do rangi głównego problemu metodologicznego;
   warstwy epokowe synonimów, PPV w epokach.
6. Walidacja: 90–120 trafień na rodzinę zamiast 50, stratyfikacja epokowa, wymóg oceny czułości.
7. Model: joinpoint jako podstawowy; logistyczny i Bass tylko eksploracyjnie.
8. Geografia: kraj pierwszego autora + krzywa standaryzowana stałymi wagami krajów.
9. Cytowania: wyłączone z pytania podstawowego, ewentualna warstwa dodatkowa.
10. Ramka interpretacyjna: scholarly attention, nie clinical adoption.
11. Hierarchia technologii odłożona do Etapu 2/3.

### 10.1. Co zmienia v0.3 wobec v0.2

1. **Twierdzenie o nowości przeniesione z metody na przedmiot.** v0.2 opierała nowość na
   aparacie metodologicznym (normalizacja, niezmienniczość, walidacja). Przeszukanie
   z 2026-08-26 pokazało, że dla odbiorcy ortopedycznego nowe jest co innego: zestawienie
   wielu rodzin na wspólnym mianowniku, czego nie robi żadna z 69 istniejących prac.
2. **Dodane jawne „co z tego" dla czytelnika klinicznego** (§1, trzy pytania). v0.2 tego nie
   miała, a przy ramce „scholarly attention, nie clinical adoption" jest to konieczne —
   bez tego recenzent ortopedyczny nie zobaczy powodu, żeby czytać.
3. **Rozdzielenie na dwie prace** (§1.1). Argument metodologiczny — luki BIBLIO, patenty
   wobec publikacji, niezmienniczość jako teza — odłożony do pracy A, wraz z warunkiem,
   który utrzyma ją publikowalną.
4. Bez zmian merytorycznych w §§3–9. Definicja pola, warstwy epokowe, PPV stratyfikowany,
   standaryzacja geograficzna i joinpoint zostają — są potrzebne do trafności tej pracy,
   niezależnie od tego, gdzie leży twierdzenie o nowości.

## 11. Czego nadal nie wiem

- Liczebność pola w PubMed przy przyjętej definicji — rozstrzygnie Etap 1.
- Odsetek rekordów pola z abstraktem w kolejnych dekadach.
- Czy druk 3D ma liczebność wystarczającą do rozbicia hierarchicznego.
- Jaka rama odniesienia dla czułości jest realna przy nakładzie jednoosobowym.
- **Który z trzech wątków §1 uniesie pracę.** Rozstrzygnie Etap 1: jeśli rodziny rosną
  równolegle i żadna nie wypiera innych, wątek 2 odpada i zostają dwa. Jeśli udziały wszystkich
  rodzin łącznie są płaskie, odpada cała ramka „dyfuzji" i trzeba wrócić do sformułowania.
- Czy definicja pola oparta na MeSH nie jest obciążona własnym dryfem słownika: z 56
  deskryptorów poddrzewa `Orthopedic Procedures` 28 wprowadzono w 2006 r. lub później.
  Efekt jest w dużej mierze wygaszany rozwijaniem poddrzewa wraz z przodkami; ryzyko resztkowe
  dotyczy rekordów, których jedynym deskryptorem z pola jest deskryptor młodszy niż sam rekord.
  Policzalne na Etapie 1 i tam do zaraportowania.
