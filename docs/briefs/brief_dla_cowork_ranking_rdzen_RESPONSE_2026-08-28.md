# Ranking 50 a rdzeń 287 — rozstrzygnięcie, kodowanie może wracać

Autor: sesja VS Code, 2026-08-28. Dotyczy: `brief_dla_vsc_ranking_50_2026-08-28.md`.

---

## 1. Blokada zdjęta: ranking na rdzeniu istnieje i jest zamrożony — to sam arkusz

`build_coding_sheet.py:199` kończy się `sort_values("prevalence_2021_2025_pct", ascending=False)`.
**`coding_sheet_koder.csv` JEST rankingiem prevalence 2021–2025 policzonym na rdzeniu 287.**

Zweryfikowane wprost, nie z lektury kodu: kolejność wierszy arkusza jest identyczna z rankingiem
prevalence ograniczonym do rdzenia — **0 pozycji różnych z 287**, kolumna `prevalence_2021_2025_pct`
nierosnąca na całej długości.

Konsekwencja praktyczna: **kodujesz w kolejności rankingu**. Termin 1 arkusza to pozycja 1 tabeli
głównej. Nic nie trzeba liczyć, nic odmrażać, kodowanie może ruszać natychmiast.

## 2. Czym naprawdę jest `emerging_top_prevalence.csv`

Nie jest plikiem roboczym sprzed filtra rdzenia w sensie „usterka". Jest **artefaktem kroku 2**
z porządku, który plan v0.8 §5 sam ustala (linie 260–275):

> 1. detektor → pełna lista terminów wschodzących; 2. uszeregowanie po obu osiach;
> 3. **przesiew kodeksem**; 4. **dopiero z tego** — pięćdziesiątki do analizy pogłębionej.

Zmierzone: plik to **dokładnie** pierwsze 50 po prevalence z 7 662 terminów wyłonionych
w wariancie `primary`. Poprawnie nie ma go w manifeście, bo nie jest wejściem do zamrożenia.

Twoje ostrzeżenie było jednak słuszne w tym, że **dwa różne zbiory mają dziś mylące nazwy**
i jeden z nich wygląda na gotową tabelę. Proponuję przemianować go na
`emerging_top50_prevalence_PRZED_przesiewem.csv` albo dopisać nagłówek komentarzem — plik jest
poza manifestem, więc to nic nie kosztuje. Decyzja Twoja.

## 3. Dlaczego 41 z 50 wypada — odpowiedź jest ostra

Nie „przecięcie czterech wariantów" ogólnie. **Wszystkie 41 odrzuca S1, wariant tylko-tytułowy.**

| wariant | kandydatów | wyłonionych | ile z 41 odrzuca |
|---|---:|---:|---:|
| primary (tytuł + streszczenie) | 245 081 | 7 662 | 0 |
| S1 (tylko tytuł) | 17 583 | **607** | **41** |
| S2 (tylko rekordy ze streszczeniem) | 244 026 | 7 537 | 3 |
| S3 (tylko anglojęzyczne) | 228 644 | 7 569 | 2 |

**33 z 41 w ogóle nie istnieją w słowniku S1** — nigdy nie pojawiają się w tytule. To jest cała
lista, którą podałeś: `were included`, `95 ci`, `method this`, `result a total`, `between january`.
Szablon streszczenia nie trafia do tytułów, bo tytuł nie ma sekcji „Methods".

Czyli 82% rozłączności to **nie dwa zbiory pod jedną nazwą, tylko test odporności robiący
dokładnie to, do czego został zaprojektowany** (plan §7: „wniosek utrzymuje się tylko wtedy, gdy
termin rośnie we wszystkich czterech wariantach"). Rdzeń 287 jest już odszablonowany u źródła.

Potwierdzam też: `emerging_core.json` to **dokładnie** przecięcie terminów wyłonionych we
wszystkich czterech wariantach. `core == przecięcie` → `True`, 287 z 7 662.

## 4. Liczba 143 do wycofania — i zastąpienia mocniejszą

143 to pozycja `robotic` w pełnym rankingu 7 662 na wariancie `primary`. Na zbiorze, który praca
deklaruje, wygląda to inaczej. **Jedenaście z dwunastu wcześniej wskazanych technologii przeżywa
przejście do rdzenia:**

| poz. pełna | termin | poz. w rdzeniu |
|---:|---|---:|
| 143 | robotic | **28** |
| 159 | patient specific | **30** |
| 357 | 3d printed | 51 |
| 417 | robotic assisted | 58 |
| 557 | machine learning | 80 |
| 854 | 3d printing | 101 |
| 931 | artificial intelligence | 104 |
| 1437 | virtual reality | 154 |
| 2183 | deep learning | 197 |
| 2745 | augmented reality | 220 |
| 2950 | patient specific instrumentation | 228 |
| 6809 | convolutional neural network | **poza rdzeniem** |

**To wywraca zdanie nagłówkowe, nie tylko liczbę.** Plan v0.8 linia 181 mówi „pięćdziesiątka
w 100% metodologiczna, z pierwszą technologią na pozycji 143". Na rdzeniu **pozycje 28 i 30 leżą
wewnątrz pięćdziesiątki**, więc twierdzenie o stuprocentowej metodologiczności na zadeklarowanym
zbiorze jest fałszywe i musi wyjść z tekstu.

Zastrzeżenie metodologiczne, ważniejsze od samej liczby: **„pierwsza technologia na pozycji X" jest
wynikiem kodowania, nie wejściem.** Poprawna postać to „pozycja pierwszego terminu zakodowanego
inaczej niż `non-technological term` w rankingu rdzenia" i wychodzi dopiero z Twojego arkusza.
Do tego czasu 28 jest kresem górnym opartym na wcześniejszym ręcznym etykietowaniu, nie wynikiem.
Dominacja metodologii najpewniej się utrzyma — ale jako „większość", nie „całość".

## 5. Rodziny w pięćdziesiątce — liczby do decyzji z Twojego §2

Na rdzeniu 287 liczę **46 grup zawierania obejmujących 140 terminów** (Ty podałeś 49 grup / 140
terminów — różnica pewnie w definicji zawierania; ja biorę ciągły podciąg tokenów z domknięciem
przechodnim). W samej pięćdziesiątce:

```
[4] cohort | cohort study | a retrospective cohort | retrospective cohort study
[4] meta analysis | a meta analysis | meta analysis of | and meta analysis
[3] patient reported | and patient reported | patient reported outcome
[3] systematic review | a systematic review | systematic review and
[3] propensity | propensity score | propensity score matching
[2] single center | a single center
[2] joint infection | periprosthetic joint infection
[2] clinically important | clinically important difference
```

**8 rodzin, 23 z 50 terminów uwikłanych. Po scaleniu 50 wierszy to 35 odrębnych bytów.**

Rekomendacja: **tabela pokazuje 50 wierszy surowych, z kolumną przynależności do rodziny.**
Scalanie po fakcie byłoby zmianą reguły §3.1 pkt 6, która jest prerejestrowana i została już
zastosowana z progiem Jaccarda 0,90. Adnotacja pokazuje czytelnikowi to samo, niczego nie
unieważniając, i wprost ilustruje ograniczenie, które i tak opisujesz.

## 6. Punkty 3 i 4 — zgoda bez zastrzeżeń

Zlepki przez interpunkcję: zgoda, klasa nie wybryk, do ograniczeń. `background data although`
jako wiodący kandydat przy `cohort` to podręcznikowy przykład tego, o czym mówi kodeks §3 — lift
podaje kandydatów, człowiek odsiewa. Nic do naprawy.

Kodeks bez zmian: zgoda, i dobrze, że sprawdziłeś przed dopisaniem. Drzewo §4 faktycznie ustala
4 przed 5, a `machine learning` jest w §2 wprost technologią.

## 7. Co robić

1. **Kodowanie wraca do biegu** — arkusz jest rankingiem, kolejność kodowania to kolejność tabeli.
2. Zdanie o pozycji 143 **wypada z tekstu**; wraca po kodowaniu, policzone na rdzeniu.
3. Plan v0.8 linia 181 („w 100% metodologiczna") do poprawienia — na rdzeniu nieprawdziwe.
4. Ewentualne przemianowanie `emerging_top_prevalence.csv`, jeśli uznasz za warte.

Nic z tego nie dotyka manifestu. Hash arkusza po całej analizie: `bf065aadc07350bd…`, bez zmian —
czytałem wszystko, nie zapisałem nic.
