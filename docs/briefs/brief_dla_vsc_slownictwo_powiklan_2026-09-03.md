# Czy słownictwo powikłań wyprzedza zanik technologii? Test, niski priorytet

Autor: sesja Cowork, 2026-09-03. **Nie blokuje pisania** — manuskrypt powstaje równolegle,
a to zdanie w Dyskusji jest na razie sformułowane jako „wzorzec widziany raz, do sprawdzenia".

## Obserwacja

Przy metal-on-metal frazy powikłań (`pseudotumor` y₀ 2013, `metal debris` 2012, `adverse local
tissue reaction` 2014) wyłoniły się **przed** szczytem `mom total hip arthroplasty` (2018).
Przemek potwierdził, że jako wzorzec kliniczny ma to sens: literatura widzi powikłanie, zanim
wytyczne wycofają technologię.

## Przypadek, który może to złamać

`cement leakage` y₀ 2009, `kyphoplasty` szczyt 2011. Ten sam układ czasowy — ale kyphoplastyka
jest w paśmie „dowody za, rutyna" (trwałość 0,39–0,43), nie „przeciw". Jeśli powikłania
wyprzedzają szczyt także u technologii przyjętych, wzorzec nie odróżnia upadku od rutyny.

## Zadanie

Dla każdej z 76 grup materiału:

1. Frazy z rdzenia (1 294) sklasyfikowane jako `rozpoznanie` w `np_kategorie_propozycja.tsv`,
   które **współwystępują** z technologią ponad oczekiwanie (krotność obs/oczek ≥ 5, jak w teście
   pęczków) — to są kandydaci na „jej powikłanie".
2. Dla każdej pary: y₀ powikłania minus rok szczytu technologii (ujemne = wyprzedza).
3. Zestawienie po pasmach zaniku (przeciw / nierozstrzygnięte / za+rutyna) i dla technologii bez
   zaniku.

**Pytanie rozstrzygające:** czy „powikłanie wyprzedza szczyt" występuje **wyłącznie** w paśmie
„przeciw", czy we wszystkich? Jeśli wyłącznie — do Dyskusji jako wynik z n. Jeśli wszędzie —
zostaje hipotezą i dopisujemy, że wyłonienie słownictwa powikłań jest cechą cyklu życia
technologii, nie zapowiedzią jej upadku.

Wyjście: `data/processed/powiklania_vs_szczyt.csv`, kilka zdań w RESPONSE. Bez interpretacji
klinicznej — to, czy pseudotumor „podważa technologię", a wyciek cementu „jest do opanowania",
rozstrzyga ortopeda.

## Czego nie robić

Nie ruszać materiału 76 ani osi. To jest analiza dodatkowa na gotowych tabelach.
