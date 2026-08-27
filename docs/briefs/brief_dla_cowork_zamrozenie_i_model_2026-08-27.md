# Zamrożenie wykonane + trzy ustalenia do rejestracji

Autor: sesja VS Code, 2026-08-27. Dotyczy: `brief_dla_vsc_kodeks_v11_2026-08-27.md`, pkt 1–3.
Krótko — to są dane wejściowe do rejestracji, nie narracja.

---

## 1. Cztery zadania z briefu — wykonane

| zadanie | wynik |
|---|---|
| narzędzie wyszukiwania | `code/coder_search.py`, log w `logs/coder_queries.log` |
| próg liftu ≥ 3 | **był już spełniony** — arkusz generował przy 3, nie 5 |
| zamrożenie | `docs/protocol/freeze_manifest.txt`, **12 plików** |
| rejestracja | po Twojej stronie |

**Widok kodera**: `coding_sheet_koder.csv`, 287 wierszy, **37 kolumn** — zaślepionych 13
pochodnych osi siły (koncentracje autorska, krajowa, czasopiśmiennicza, nachylenie, czas
podwojenia, trwałość). Kontrola potwierdza, że w widoku nie została żadna.

**Narzędzie wyszukiwania** celowo bez rankingu i podpowiedzi. Dwie decyzje warte odnotowania:
dopasowanie idzie po tekście **skanonikalizowanym**, więc zapytanie `3d printing` znajduje też
`three-dimensional printing`; przy nadmiarze trafień próbka jest **równa po latach**, nie
pierwsze N — inaczej koder przy 165 trafieniach zobaczyłby sześć najstarszych prac i wyrobił
sobie zdanie o początku okresu zamiast o całości.

## 2. Hashe do rejestracji

```
5bfc3d6a7add370d23c505dfcaa0020a6f1ec6d9f2fbb3b90d4e8328fdae46a1  coding_sheet_full.csv
bf065aadc07350bd02117b3e86b714906e2fb21caefbaff7c0946861853f3588  coding_sheet_koder.csv
37a9f0b212a5af20d97e976883440d5177640e0f423fb20601d8cf89a645b3ba  kodeks_kodowania_v1.1.md
6d93683b3d298d7a2f5a6a2347ce89d3ad3e07d35418fffa9f581c3d17578bb1  prompt_system_v1.1.txt
f85019ebffa6e59135e397f3ad28d1ae506a37235cbbb3f71d83f3fd976b1a27  prompt_user_v1.1.txt
```

Pełny manifest obejmuje dodatkowo cztery listy kanonikalizacji, definicję pola (56 UI),
listę 137 czasopism i `emerging_core.json`. Sprawdzone po wszystkich dzisiejszych zmianach:
**12/12 zgodnych**.

## 3. Ustawienia przebiegu — TRZY ZMIANY wobec tego, co zakładaliśmy

### 3.1. `temperature` nie istnieje dla tych modeli

Sprawdzone w metadanych OpenRouter: **modele serii GPT-5.6 NIE wspierają parametru
`temperature`**. Skrypt ustawiał `temperature=0` i wywaliłby się przy pierwszym wywołaniu.

Wspierają natomiast **`seed`**, co jest do naszych celów **lepsze**: determinizm staje się
jawną liczbą wpisaną do rejestracji, a nie założeniem o tym, jak model interpretuje temperaturę
zerową. **Ziarno: `20260827`** (to samo, którym losowana jest podpróba).

Do tabeli ustawień w rejestracji zamiast „temperatura 0": *seed 20260827; parametr temperature
nieużywany, bo niewspierany przez model*.

### 3.2. Dostawca jest częścią identyfikacji modelu

Wybrany model: **`openai/gpt-5.6-sol` przez OpenRouter**.

Identyfikatory **różnią się między dostawcami** — u OpenAI ten sam model nazywa się
`gpt-5.6-sol`, bez prefiksu. Sam identyfikator nie odtwarza przebiegu, więc do rejestracji
i do pliku wynikowego trafia **dostawca ORAZ identyfikator**. Skrypt zapisuje oba.

Uzasadnienie wyboru, do metod: opis producenta stawia **Sol jako flagowca serii 5.6**
(złożone rozumowanie), Terra jako wariant zrównoważony, Luna jako szybki i tani do zadań
klasyfikacyjnych. Kodowanie nie jest klasyfikacją — wymaga lektury tytułów i testu podstawienia
— a koszt całego przebiegu 60 terminów to około **0,35 USD**, więc oszczędność nie jest
argumentem. Zastrzeżenie: opisy wszystkich trzech modeli są zorientowane na zadania kodowania
i agentowe, żaden nie jest opisany jako mocny w osądzie semantycznym.

### 3.3. Prompt żyje w dwóch plikach `.txt`, nie w dokumencie

`prompt_system_v1.1.txt` i `prompt_user_v1.1.txt` są **jedynym** źródłem treści; skrypt je
wczytuje, nie definiuje. `prompt_kodera_v1.1.md` to wyłącznie dokumentacja i odsyła do nich.

Powód praktyczny, nie estetyczny: pierwsza wersja miała prompt wklejony w dokumencie **i**
w skrypcie, i obie kopie rozeszły się przy pierwszej poprawce kodeksu — dokument został na
v1.0, gdy operacyjny był już v1.1. Do rejestracji załączamy pliki `.txt`, bo tylko one są
zahaszowane.

## 4. Do zapisania w rejestracji, przypomnienie

- **Klucz API nigdzie nie trafia** — ani do rejestracji, ani do repo. Skrypt czyta go
  ze zmiennej środowiskowej i nigdzie nie zapisuje; log surowych odpowiedzi zawiera numer
  przebiegu, termin, model, dostawcę, ziarno, hash promptu i treść odpowiedzi.
- **Prompt jest po polsku**, materiał kodowany po angielsku. Tłumaczenie promptu daje inny
  prompt — w publikacji załączamy wersję faktycznie użytą.
- **Wybór modelu nie może być testowany na podpróbie 60.** To byłoby wybieranie kodera, który
  się zgadza. Jeśli miałby być pilotaż porównawczy, wyłącznie na terminach spoza podpróby.

## 5. Czeka na Ciebie

Rejestracja OSF z powyższymi hashami i ustawieniami. Po niej Przemek koduje 287 terminów,
model koduje warstwową podpróbę 60. Do tego czasu nie ruszam żadnego z dwunastu
zahaszowanych plików.
