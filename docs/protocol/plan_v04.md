# Dyfuzja badań nad technologiami w ortopedii — plan v0.4
2026-08-26 · Przemysław Czuma · zastępuje v0.2/v0.3

---

## Pytanie

W polu ortopedii zabiegowej, 2005–2025: **jak zmieniał się udział publikacji dotyczących
pięciu rodzin technologii — i czy rosły razem, czy jedna wypierała drugą?**

Drugie pytanie da się zadać **wyłącznie na wspólnym mianowniku**. Na liczbach bezwzględnych
rośnie wszystko i pytanie nie istnieje. To jest uzasadnienie normalizacji i zarazem cała
nowość pracy: 69 znalezionych analiz bibliometrycznych technologii w ortopedii jest
jednotechnologicznych i raportuje liczby bezwzględne.

Mierzymy **dyfuzję badań i uwagę naukową**, nie adopcję kliniczną. Konsekwentnie, w tytule
i w dyskusji.

## Dane

PubMed Baseline 2026 + updatefiles, lustro lokalne. Dedup: przy powtórzonym PMID wygrywa
najpóźniejszy plik; PMID z `DeleteCitation` wypada. Mianownikiem jest `analytic_index`.
`PubmedBookArticle` wykluczone i policzone.

Typy publikacji: Journal Article, Review, Systematic Review, Meta-Analysis, Clinical Trial.
Bez ograniczenia językowego. Rok 2026 poza analizą — niekompletny.

## Pole — jedna definicja

`Orthopedic Procedures` + wszystkie potomne deskryptory MeSH (56, rozwijane programowo
z `desc2026.xml`). Obejmuje traumatologię narządu ruchu i procedury nieoperacyjne w rodzaju
zamkniętej repozycji. Nie obejmuje `Fractures, Bone` — to gałąź chorobowa, wciągnęłaby
epidemiologię i osteoporozę bez żadnej interwencji.

Jedna analiza wrażliwości: czasopisma z NLM Broad Subject Term „Orthopedics".

## Technologie — pięć, na stałe

Druk 3D i wytwarzanie addytywne · robotyka · nawigacja i obrazowanie śródoperacyjne ·
sztuczna inteligencja · biomateriały i powłoki.

Liczone **z tytułu i abstraktu**, nie z MeSH: deskryptory wchodziły do słownika w różnych
latach (`Printing, Three-Dimensional` w 2015) i krzywa MeSH pokazałaby zmianę słownika jako
zmianę praktyki. MeSH służy do walidacji.

**Każda rodzina ma warstwy epokowe synonimów.** Praca o drukowanym szablonie z 2008 r. mówi
`rapid prototyping` albo `stereolithography`; ta sama praca z 2022 r. mówi `3D printing`.
Słownik zbudowany na dzisiejszym języku zmierzyłby zmianę nazewnictwa. To jest jedyne miejsce,
w którym ta praca musi być trudna.

## Analiza

Udział = rekordy pola z technologią X / wszystkie rekordy pola, rocznie. Liczby bezwzględne obok.
Model: **regresja segmentowa (joinpoint)** na udziale. Nic więcej — bez krzywej logistycznej,
bez modelu Bassa.

Rozkład krajów (kraj pierwszego autora) raportowany zawsze. Krzywa standaryzowana stałymi
wagami krajów **tylko jeśli** struktura geograficzna faktycznie się zmienia — to kontrola,
nie produkt.

## Walidacja

PPV per rodzina, **stratyfikowany po epokach 2005–2011 / 2012–2018 / 2019–2025**, 90–120 trafień
na rodzinę. Dryf PPV między epokami jest sygnałem, że warstwy epokowe nie działają.
Jedna ocena relative recall względem zbioru referencyjnego z przeglądów systematycznych.
PPV definicji pola ≥ 0,90 na próbie 200 rekordów.

## Produkt

Trzy ryciny i jedna tabela:

1. krzywe udziału pięciu rodzin, 2005–2025
2. dopasowania joinpoint z latami przegięcia
3. diagram przepływu rekordów
4. tabela: słowniki epokowe + PPV per rodzina per epoka

Zgodność z BIBLIO deklarowana wprost, tabela zgodności w suplemencie.

## Poza tą pracą

Świadomie odłożone, każde na osobną publikację: warstwa eksploracyjna (terminy wschodzące,
klastrowanie osadzeń), lead–lag preprintów medRxiv, odtworzenie opublikowanych zapytań
z literatury i wywód metodologiczny o niezmienniczości pomiaru, hierarchia wewnątrz rodzin.

Powód jest jeden: każde z nich dokłada drugie pytanie do pracy, która ma odpowiadać na jedno.

## Etap 1 — brama

2005–2025 × pole × pięć rodzin × licznik roczny i udział. Bez walidacji, bez modelowania.
**Jeśli żadna rodzina nie osiąga rzędu setek rekordów rocznie ani widocznej zmiany udziału —
pracy nie ma i trzeba to powiedzieć wprost.** Zapisane przed danymi.
