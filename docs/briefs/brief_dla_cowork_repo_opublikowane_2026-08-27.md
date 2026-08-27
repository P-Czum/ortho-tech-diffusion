# Repo opublikowane — raport z §5

Autor: sesja VS Code, 2026-08-27. Dotyczy: `brief_dla_vsc_publikacja_repo_2026-08-27.md`.

---

## Adres do pola Resource Information

**https://github.com/P-Czum/ortho-tech-diffusion**

Publiczne. Nazwa zgodna z tym, co wpisane w `CITATION.cff` i `README.md`, więc rejestracja
nie wskazuje w pustkę.

## Weryfikacja sum w świeżym klonie — 12/12

Sklonowałem repo do katalogu tymczasowego i przeliczyłem **wszystkie dwanaście**, nie tylko
pięć z §7 rejestracji:

```
OK  5bfc3d6a7add370d  data/processed/coding_sheet_full.csv
OK  bf065aadc07350bd  data/processed/coding_sheet_koder.csv
OK  d8adf778069ff521  docs/protocol/coding_manual_v1.2.md
OK  6b709843f63af82b  docs/protocol/prompt_system_v1.2_EN.txt
OK  724398d6112026e8  docs/protocol/prompt_user_v1.2_EN.txt
OK  d3e156100f7f4dff  data/canon/spelling_uk_us.csv
OK  989de7498d0c2fd3  data/canon/irregular_plurals.csv
OK  ee7e427af757d27d  data/canon/phrase_map.csv
OK  e4262b55c66d494d  data/canon/countries.csv
OK  23bee2273706d92b  data/processed/field_orthopedic_procedures.csv
OK  1e37db8cfc698bd5  data/processed/journals_orthopedics.csv
OK  1a7659724b709008  data/processed/emerging_core.json

zgodnych: 12/12, rozbieżnych: 0
```

Twoja diagnoza z §1 była trafna i potwierdziłem ją niezależnie przed naprawą: **7 z 12 plików
miało blob w HEAD różny od bajtów na dysku.** Zgodne były dokładnie te pięć, które pisałem
narzędziem zapisującym LF; rozbieżne te, które przeszły przez `write_text` albo `to_csv`
na Windows.

Po `* -text` i renormalizacji: **zero plików zmieniło zawartość na dysku** — sprawdzone
porównaniem hashy dyskowych przed i po, zgodnie z twoim §6.

## Briefy — 17 w repo, ale trzeba było iść dalej

`docs/briefs` ma teraz **17 plików**: 16 ortopedycznych i `README.md` z protokołem wymiany
sesji (jest ogólny, nie projektowy). Przeniesione **39**, do `docs/archiwum_myslniki/`,
katalog w `.gitignore`.

**Ale `git rm` nie wystarczał.** Pliki znikały z bieżącego stanu, natomiast **`git log`
pokazywałby je każdemu** — 78 wystąpień w historii. Cel §3, czyli nieujawnianie kuchni
zamkniętego, zdeponowanego badania, nie zostałby osiągnięty.

Przepisałem więc historię (`filter-branch --index-filter`, za wyraźną zgodą Przemka, bo
operacja jest nieodwracalna). Wynik w świeżym klonie: **0 wystąpień w plikach, 0 w historii.**
19 commitów z pracy nad ortopedią zachowanych — te zostają, bo dokumentują proces i są
argumentem za.

Gałąź zapasowa i `refs/original` usunięte po weryfikacji, `gc` wykonane. Ich jedyną zawartością
ponad `main` było dokładnie to, co usuwaliśmy, a przy istniejącym zdalnym byłyby stałym
ryzykiem przy `push --all`.

## Audyt czystości przed pushem

Poza twoją listą sprawdziłem też:

| kontrola | wynik |
|---|---|
| sekrety (`sk-…`, klucze prywatne, `api_key=`) | brak |
| adresy e-mail | tylko `przemek.czuma@gmail.com` w `CITATION.cff`, celowo |
| `logs/` | śledzony wyłącznie `.gitkeep`; log zapytań kodera poza gitem |
| rozmiar | 596 KiB, największy plik 0,6 MB |
| gałęzie na zdalnym | wyłącznie `main` |

## Stan

85 plików, 19 commitów, `main` śledzi `origin/main`, drzewo czyste.

Kodowanie może ruszać — rejestracja złożona, materiał zamrożony i publicznie weryfikowalny.
