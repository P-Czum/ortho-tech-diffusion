# Przejście na angielski + ponowne zamrożenie

Autor: sesja Cowork, 2026-08-27. Dotyczy: `brief_dla_cowork_zamrozenie_i_model_2026-08-27.md`
oraz decyzji Przemka o języku artefaktów.

---

## 1. Zasada

**Co idzie do publikacji albo do hasza — po angielsku. Robocze briefy zostają po polsku.**

Uzasadnienie operacyjne, nie estetyczne. Twoja uwaga z §4 („tłumaczenie promptu daje inny
prompt, w publikacji załączamy wersję faktycznie użytą") jest słuszna i **właśnie dlatego
moment jest teraz** — kodowanie nie ruszyło, więc możemy użyć angielskiego od pierwszego
wywołania, zamiast tłumaczyć po fakcie i publikować wersję, której nikt nie użył.

Drugi powód jest twój: jeśli prompt pójdzie po angielsku, a kodeks zostanie po polsku, mamy
dwa sformułowania tych samych reguł w dwóch językach — dokładnie ten mechanizm rozjazdu,
który raz już cię ugryzł, gdy prompt żył w dokumencie i w skrypcie naraz.

Koder 1 (Przemek) czyta angielski bez problemu, a cały materiał kodowany i tak jest angielski.

## 2. Co dostarczam

- `docs/protocol/coding_manual_v1.2.md` — **tłumaczenie v1.1, nie rewizja.** Żadna reguła
  operacyjna nie zmieniona; §7 zawiera historię wersji, więc widać to wprost. Od v1.2 tekst
  angielski jest jedynym źródłem prawdy, v1.1 zostaje dla historii.
- `docs/protocol/osf_registration_EN.md` — rejestracja po angielsku, z koderem 2 = GPT
  zgodnie z decyzją Przemka i jawną deklaracją, czym to κ jest.

Nazwy kolumn arkusza zostawiłem **bez zmian** (`poprzednik_glowny`, `tytuly_WSPOLNE`, `uwagi`) —
zmiana nazw kolumn zmieniłaby hash arkusza, a arkusz jest poprawny i nie ma powodu go ruszać.
Kodeks odwołuje się do nich dosłownie, więc nie ma niejasności.

## 3. Do zrobienia po twojej stronie

1. **Przetłumacz prompty na angielski** → `prompt_system_v1.2_EN.txt`,
   `prompt_user_v1.2_EN.txt`. Ty je pisałeś i znasz dokładną treść operacyjną, więc nie chcę
   ich pisać na ślepo. Warunek: mają odpowiadać kodeksowi v1.2 co do reguł, w szczególności
   nazwom pięciu kategorii **w angielskim brzmieniu** (`novel concept`, `renaming`,
   `conceptual evolution`, `measurement artifact`, `non-technological term`) — te nazwy trafiają
   potem wprost do tabeli wyników, więc muszą być identyczne wszędzie.
2. **Ponowne zamrożenie.** Nowe hashe dla: `coding_manual_v1.2.md`, obu promptów EN.
   Arkusze (`coding_sheet_full.csv`, `coding_sheet_koder.csv`) i pozostałe pliki manifestu
   **nie zmieniają się** — sprawdź, że ich hashe zostały te same, to jest test, że nic się
   nie rozjechało przy okazji.
3. **Zaktualizuj `freeze_manifest.txt`** i odeślij trzy nowe hashe — wstawię je do rejestracji
   w miejsce `<pending re-freeze>`.
4. Wersje polskie (`kodeks_kodowania_v1.0/v1.1.md`, prompty PL) **zostaw w repo** jako historię,
   ale wypisz je z manifestu — manifest ma haszować to, czego faktycznie użyto.

## 4. Czego nie ruszać

Detektora, arkuszy, list kanonikalizacji, definicji pola, listy czasopism, `emerging_core.json`.
Zmiana języka dotyczy wyłącznie instrukcji dla koderów i dokumentów publikacyjnych.
