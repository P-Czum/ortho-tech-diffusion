# Słownictwo powikłań: wzorzec występuje wszędzie po równo — zostaje cechą cyklu życia

Autor: sesja VS Code, 2026-09-03. Dotyczy: `brief_dla_vsc_slownictwo_powiklan_2026-09-03.md`.

Skrypt: `code/powiklania_vs_szczyt.py`. Wynik: `data/processed/powiklania_vs_szczyt.csv`,
228 par powikłanie–technologia przy 61 grupach.

**Odpowiedź na pytanie rozstrzygające: wzorzec NIE występuje wyłącznie w paśmie „przeciw".
Występuje we wszystkich po równo. Zgodnie z Twoim własnym warunkiem — zostaje hipotezą
o cyklu życia, nie zapowiedzią upadku.**

---

## 1. Wynik surowy był obciążony i sam go prostuję

Pierwszy przebieg dał `bez zaniku` 92% wyprzedzeń przy medianie **−9 lat** i wyglądało to na
mocny efekt. **To artefakt.** Technologia, która wciąż rośnie, ma szczyt w 2025 — więc wyprzedza
ją prawie każde powikłanie, niezależnie od czegokolwiek.

Kontrola: tylko technologie ze szczytem **≤ 2022**, żeby „wyprzedzenie" nie było trywialne.

| pasmo | par | grup | wyprzedza | mediana lat |
|---|---:|---:|---:|---:|
| bez zaniku | 61 | 15 | 75% | −3 |
| **1. dowody PRZECIW** | 6 | 2 | **50%** | −2 |
| **3. BRAK dowodów** | 14 | 4 | **50%** | 0 |
| **5. dowody ZA + rutyna** | 6 | 2 | **50%** | −1 |
| 4. wchłonięcie | 1 | 1 | 0% | +13 |

**Dokładnie 50% w każdym paśmie zaniku.** Miara nie odróżnia upadku od rutyny.

Druga kontrola, na położeniu `y₀` powikłania we wzroście technologii (0 = jej wyłonienie,
1 = szczyt): mediana 0,50 przy „przeciw", 0,83 przy rutynie, 0,90 przy nierozstrzygniętych.
Kierunek jest zgodny z hipotezą — przy technologiach odrzuconych powikłania pojawiają się
wcześniej w cyklu — ale przy sześciu obserwacjach na pasmo to nie waży nic.

## 2. Test ma wadę, która osłabia tę liczbę, i muszę ją zgłosić

**Kategoria `rozpoznanie` miesza wskazanie z powikłaniem.** Maszyna po składzie ich nie odróżni,
bo oba są rozpoznaniami. Widać to wprost przy kifoplastyce — przypadku, który miał wzorzec złamać:

```
vcf                                          y0=2005   -6 lat  krotnosc 109  ← WSKAZANIE
osteoporotic vertebral compression fracture  y0=2016   +5 lat  krotnosc  57  ← WSKAZANIE
cement leakage                               y0=2009   -2 lat  krotnosc  55  ← powiklanie
ovcf                                         y0=2011    0 lat  krotnosc  37  ← WSKAZANIE
bone cement leakage                          y0=2019   +8 lat  krotnosc  31  ← powiklanie
```

Złamanie kompresyjne kręgu nie jest powikłaniem kifoplastyki, tylko powodem jej wykonania.
Trzy z pięciu „powikłań" to wskazania.

Przy metal-na-metalu takiego zanieczyszczenia nie ma — wszystkie trzy frazy są powikłaniami:

```
pseudotumor                    y0=2011   -7 lat  krotnosc 191
metal debris                   y0=2012   -6 lat  krotnosc 174
adverse local tissue reaction  y0=2014   -4 lat  krotnosc 146
```

**Liczba 50/50 jest więc policzona na mieszaninie.** Rozdzielenie wskazań od powikłań wymaga
ortopedy; podaję to jako ograniczenie testu, nie proszę o dodatkową pracę, skoro wynik i tak
nie idzie w stronę hipotezy.

## 3. Twój przypadek probny łamie wzorzec także po oczyszczeniu

To jest najważniejsze zdanie tego briefu. Kifoplastyka miała rozstrzygnąć, czy wzorzec odróżnia
upadek od rutyny. **Po odsianiu wskazań zostaje przy niej `cement leakage` — prawdziwe
powikłanie, wyprzedzające szczyt o 2 lata.** Czyli technologia z pasma „dowody za, rutyna" ma
ten sam układ czasowy co metal-na-metalu.

Twoja diagnoza z §Przypadek była trafna: **wyłonienie słownictwa powikłań jest cechą cyklu życia
technologii, nie zapowiedzią jej upadku.** Do Dyskusji w tej postaci.

## 4. Co z tego zostaje użytecznego

Nie jest to wynik pusty. Krotności współwystępowania są ogromne i bardzo selektywne — 146–191×
przy triadzie metal-na-metalu, 31–109× przy kifoplastyce. **Powiązanie technologia–powikłanie
jest w danych mocne i wykrywalne**, tylko jego chronologia nie niesie informacji o losie
technologii.

To sugeruje inne zastosowanie tej samej miary, którego **nie realizuję, bo nie o to prosiłeś**:
krotność mogłaby służyć do automatycznego wskazywania kandydatów na parę technologia–powikłanie
do przeglądu przez ortopedę. Przy 228 parach na 61 grupach jest to lista wykonalna.

## 5. Kontrole

| | |
|---|---|
| materiał | nietknięty (analiza na gotowych tabelach) |
| osie | nietknięte |
| próg krotności | 5×, jak w teście pęczków |
| próg wspólnych prac | 5 (poniżej krotność jest szumem) |
| manifest | **12/12** |
