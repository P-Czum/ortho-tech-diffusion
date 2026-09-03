# Dwa przeliczenia wykonane: MTIX na materiale 60 i warstwa leków. Wniosek MTIX się wzmacnia

Autor: sesja VS Code, 2026-09-03. Wykonanie dwóch rzeczy, które sam zgłosiłem w briefie z 14:05 §2.

Nowe pliki: `results/mtix_impact_60.json`, `results/mtix_mechanizm_60.json`,
`code/kontrast_leki.py`. Nadpisane: `data/processed/kontrast_leki.csv` (stara wersja
zachowana w historii, commit `6d59a1a`).

---

## 1. MTIX — ta sama korelacja, dwukrotnie większa próba

| | stary przebieg | **materiał 60** |
|---|---:|---:|
| Spearman ρ | 0,1431 | **0,1426** |
| p | 0,360 | **0,185** |
| Pearson r | 0,1261 | 0,0393 |
| **n** | **43** | **88** |

Korelacja jest praktycznie identyczna (różnica na czwartym miejscu po przecinku) przy dwukrotnie
większej próbie. **Wniosek się nie zmienia — ekspozycja terminu na zyskujące albo tracące
deskryptory nie przewiduje jego odchylenia od trendu po 2022 — ale stoi teraz mocniej.**

Zdanie do Metod: *„a group's exposure to gaining or losing descriptors did not predict its
deviation from trend (Spearman ρ = 0.14, p = 0.18, n = 88)"*. Liczba `n` pasuje teraz do
materiału, więc znika zestawienie „n = 43" obok „60 grup", o którym pisałem.

Uwaga na marginesie, bo wyszła przy okazji i nie było jej w starym przebiegu: **T2 pokazuje, że
oś przekroczenia progu jest stabilniejsza od osi obecności.** Spearman między obiema osiami
rośnie z 0,721 (2017–2021) do 0,829 (2023–2025), a ranking po samej obecności ma między oknami
tylko 0,554. Zgodne z tym, co plan przewidywał jako zamiennik wrażliwy na mianownik.

## 2. Leki — dwa `y₀` poprawione, wszystkie siedem wchodzi do rdzenia

`data/processed/kontrast_leki.csv` odtworzony na `emerging_d6_primary`:

| lek | `y₀` | szczyt | prac | prevalence | szczyt % |
|---|---:|---:|---:|---:|---:|
| tranexamic acid | 2015 | 2021 | 1 185 | 0,587% | 0,804% |
| rivaroxaban | 2008 | 2012 | 344 | 0,068% | 0,350% |
| dexamethasone | 2016 | 2025 | 303 | 0,213% | 0,267% |
| vte prophylaxis | 2012 | 2012 | 277 | 0,131% | 0,184% |
| **multimodal analgesia** | **2018** ~~2021~~ | 2025 | 272 | 0,187% | 0,267% |
| **local infiltration analgesia** | **2014** ~~2017~~ | 2020 | 254 | 0,123% | 0,207% |
| liposomal bupivacaine | 2015 | 2017 | 205 | 0,100% | 0,229% |

**Zmiana, o której warto wiedzieć osobno:** stara kolumna `w_rdzeniu_4` była prawdziwa tylko dla
dwóch leków (`tranexamic acid`, `rivaroxaban`). Po D-2 rdzeń ma trzy warianty tekstu zamiast
czterech i **wszystkie siedem leków jest w rdzeniu**. To nie jest zmiana danych, tylko skutek
usunięcia S1 — wariantu tytułowego, który mechanicznie wycinał 94% rdzenia. Kolumna nazywa się
teraz `w_rdzeniu`; `pozycja` (ranga w liście n-gramowej) wypadła, bo nie ma odpowiednika.

Skrypt `code/kontrast_leki.py` powstał dlatego, że pliku nie dało się odtworzyć — nie miał
generatora. Teraz ma.

## 3. Co to zmienia w tekście

| dokument | było | ma być |
|---|---|---|
| `methods_v1.md` | „ρ = 0.14, p = 0.36, **n = 43**" | „ρ = 0.14, p = **0.18**, **n = 88**" |
| `methods_v1.md` | „Drugs (seven phrases) ... analysed separately" | **bez zmian** — siedem się potwierdza |
| gdziekolwiek | `multimodal analgesia` 2021, `local infiltration analgesia` 2017 | **2018**, **2014** |

## 4. Czego nie zrobiłem

Nie ruszałem `results/mtix_impact.json` ani `results/mtix_mechanizm.json` — stare przebiegi
zostają obok nowych z sufiksem `_60`, żeby dało się porównać. Jeśli wolisz, żeby stare zniknęły,
powiedz.

Nie przeliczałem `mtix_check.json` (skład deskryptorów pola), bo nie zależy od listy terminów.

## 5. Kontrole

| | |
|---|---|
| materiał | **60**, nietknięty |
| osie | nietknięte |
| manuskrypt | **nietknięty** |
| manifest | **12/12** |
