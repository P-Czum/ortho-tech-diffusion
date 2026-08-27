# Prompty EN + ponowne zamrożenie — trzy hashe do rejestracji

Autor: sesja VS Code, 2026-08-27. Dotyczy: `brief_dla_vsc_angielski_i_refreeze_2026-08-27.md`.

---

## 1. Trzy hashe do wstawienia w miejsce `<pending re-freeze>`

```
d8adf778069ff5216e7928cddcd338dbe26c358e7063e7a09b678710f1867b83  coding_manual_v1.2.md
6b709843f63af82b045ea45ad348ce32c138d6585e2509c2f68d87d9debfbd47  prompt_system_v1.2_EN.txt
724398d6112026e8a8fde6d76c2d1dd37f464162b72617fac7741d50b582b294  prompt_user_v1.2_EN.txt
```

Hash promptu liczony przez skrypt (system + user, pierwsze 16 znaków, trafia do każdego
wiersza wyniku): **`522edf5153f20fc6`**.

## 2. Test integralności przeszedł

Twój punkt 2 był dobrym pomysłem — sprawdziłem, porównując z manifestem z poprzedniego commita:

**9 z 9 plików, które nie miały się zmienić, ma identyczne hashe.** Oba arkusze, cztery listy
kanonikalizacji, definicja pola, lista czasopism, `emerging_core.json`. Nic się nie rozjechało
przy okazji przekładu.

Wypisane z manifestu zgodnie z twoim punktem 4: `kodeks_kodowania_v1.1.md`,
`prompt_system_v1.1.txt`, `prompt_user_v1.1.txt`. Zostają w repo jako historia.

## 3. Jedna zmiana ponad twoje polecenie — klucze JSON

Przetłumaczyłem także **nazwy pól odpowiedzi modelu**:

| było | jest |
|---|---|
| `kategoria` | `category` |
| `poprzednik` | `predecessor` |
| `uzasadnienie` | `justification` |
| `krok` | `step` |
| `material_wystarczajacy` | `material_sufficient` |

Uzasadnienie: te pola nie są wewnętrzne — trafiają wprost do `llm_coding.csv`, a stamtąd do
tabeli wyników i do materiałów dodatkowych. Polskie klucze przy angielskim promptcie i angielskim
kodeksie byłyby **kolejnym miejscem, w którym dwa języki opisują to samo** — czyli tym samym
mechanizmem, przed którym sam ostrzegałeś w §1 briefu.

Uzasadnienie ma być teraz **po angielsku**, nie po polsku. To wynika z tej samej zasady:
uzasadnienia będą cytowane w pracy, a tłumaczenie ich po fakcie dałoby tekst, którego koder
nie napisał.

**Nazwy kolumn arkusza zostawiłem bez zmian**, zgodnie z twoim poleceniem — i test integralności
potwierdza, że hash arkusza się nie ruszył. Prompt odwołuje się do nich przez etykiety sekcji
po angielsku, więc koder-model widzi angielski interfejs nad polskimi nazwami kolumn, których
i tak nie widzi.

## 4. Stan

Wszystko po mojej stronie zrobione. Manifest: **12/12 plików**. Skrypt uruchamia się na
`coding_sheet_koder.csv` z promptami EN; `--dry-run` przechodzi.

Do uruchomienia brakuje wyłącznie klucza API i **złożonej rejestracji** — model nie zobaczy
pierwszego terminu wcześniej.
