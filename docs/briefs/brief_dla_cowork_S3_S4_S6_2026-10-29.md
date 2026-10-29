# Suplementy S3, S4, S6 złożone — i trzy zdania w manuskrypcie, które nie zgadzały się z danymi

Autor: sesja VS Code, 2026-10-29. Druga część odpowiedzi na
`brief_dla_vsc_suplement_S1_S2_S7_2026-10-29` (pierwsza: `S1_S7_poprawki`).

Przy składaniu przeszukałem repo pod kątem źródła każdej liczby. Kilka liczb z tekstu i z mojego
rejestru **nie dało się odtworzyć z plików**. Poprawiłem je u źródła, a w manuskrypcie trzeba je
podmienić (§2).

## 1. Nowe pliki

| plik | treść |
|---|---|
| `supplement_S3.md` | pole (297 667 → 271 332); cztery reguły z dokładnymi warunkami MeSH; usunięte rekordy po deduplikacji (26 335 = 8,8%); **separacja reguła po regule**; D5b zmierzona i odrzucona; audyt materiału na obcą dziedzinę (**przeliczony na 48**) |
| `supplement_S4.md` | plik propozycji kategorii (643 frazy, rozkład); dwa arkusze ortopedy; co zmienił (0 kategorii, 115 + 43 scaleń); oceny 43/7/1 i 30/11/0 — **tylko w warstwie technologia/technika** (51 z 80, 41 z 68), więc to nie jest precyzja modelu na całej liście |
| `supplement_S6.md` | tabela 2000–2025 z plików: rekordy pola, % PubMed z MeSH, udział pola w PubMed, deskryptory/rekord, % ze streszczeniem, % angielskich |

Wszystkie liczby w S6.1 są generowane skryptem prosto z `mtix_check.json` i plików `denom`.

## 2. Do podmiany w manuskrypcie

**(a) `methods_v3`, akapit o filtrach:** *„94–100% of documents for foreign terms fell inside
the removed set, against 0–2% for orthopaedic terms”*. Żadna reguła nie spełnia tego
jednocześnie:

| reguła | obce | ortopedyczne |
|---|---|---|
| D4 | 92–99% | 0–2% |
| D5c | 72–100% | 0–4,3% |
| D6 | 94–97% | 0–10,8% (PEEK, spondylodeza — prawdziwe prace zwierzęce) |
| D5a | **nie mierzono na terminach kontrolnych** | mierzono koszt: VSP traci 44% |

Proponuję: *„For each rule we measured, on control terms, the share of documents it removes:
92–99% of foreign against 0–2% of orthopaedic documents for the vascular rule, 72–100% against
0–4.3% for the homonym, 94–97% against 0–10.8% for the veterinary rule, where the upper end is
genuine animal work on orthopaedic implants (Supplement S3).”*

W tym samym akapicie: ⟨n⟩ = **26,335**, ⟨N⟩ = **271,332**, „9%” → **8.8%**.

**(b) `intro_discussion_v2`:** *„the share of records with abstracts rose from 83% to 88% and of
English-language records from 90% to 97%”*. Tych liczb nie ma w żadnym pliku. Dane mówią:
- streszczenie **83% (2000) → 92% (2019)**, a 2024–2025 (96–100%) to artefakt niepełnych lat;
- angielski **82% → 96%** (2000 → 2025).

Dalsza część zdania, *„part of what the field-share denominator absorbs”*, jest nieścisła.
Więcej streszczeń znaczy więcej fraz na rekord, a mianownik tego nie pochłania. Pilnują tego
podzbiory S2 i S3. Proponuję: *„…rose from 83% to 92% (2000–2019) and of English-language
records from 82% to 96%; a phrase whose rise came only from these trends would fail the abstract
or English subset (Supplement S6).”*

**(c) `methods_v3`:** *„seven as generic descriptions”* → **six** (zob. `S1_S7_poprawki` §5).

## 3. Co poprawiłem u siebie

- **`deviations.md` D-3.** Było „+23% vs −27%”. Z obecnego `mtix_check.json` wychodzi **+23%
  vs −23%**; pomiar z 09-01 był na wcześniejszym stanie lustra. Wniosek słabnie z „mniejszy”
  do „**nie większy**”. Decyzja o oknie się nie zmienia.
- **`deviations.md` D-7.** Separacja jest teraz podana reguła po regule, jak w tabeli w §2(a).
- **Audyt skażenia.** Poprawka listy dziedzin obcych z 09-03 (bez C10, C04, C14) była tylko
  w ręcznie dopisanej kolumnie CSV, a nie w kodzie, więc liczb „0 z 60, mediana 0,6%” nie dało
  się odtworzyć. Przeniosłem poprawkę do `audyt_skazenia.py`; na materiale 60 odtwarza starą
  kolumnę co do komórki. **Na materiale 48:** 0 z 48 powyżej 20%, 0 powyżej 10%, mediana
  0,5%, maks. 8,6% (ACDF), zwierzęta 0,0% wszędzie. Plik: `audyt_skazenia_48.csv`.
- **S6 — nowa obserwacja.** Udział rekordów PubMedu z jakimkolwiek MeSH spada stale, z 90–94%
  przed 2010 do 56% w 2025. Udział pola w całym PubMedzie spada więc od 2013, a udział
  w rekordach z MeSH rośnie do 2019, ma dołek w latach MTIX i wraca. Pole jest zdefiniowane
  przez MeSH, więc wszystkie udziały liczymy w obrębie rekordów zindeksowanych. Założenie, że
  zindeksowane i niezindeksowane prace o danej technologii się nie różnią, jest w S6
  nazwane wprost jako nietestowalne.

## 4. Do Twojej decyzji

- **S4, wersja modelu:** nigdzie nie została zapisana. S4 mówi to wprost („Claude (Anthropic),
  desktop application; version not recorded”). Jeśli ją znasz, wpisz.
- **S1 D-7:** Twoje sformułowanie („separation… measured on terms known to belong to each side
  (S3)”) jest poprawne, bo szczegóły są teraz w S3. Nic nie trzeba zmieniać.

Manifest **12/12**. Materiał 48 nietknięty.
