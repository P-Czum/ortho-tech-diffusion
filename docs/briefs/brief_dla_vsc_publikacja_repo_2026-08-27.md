# Publikacja repo — jeden błąd krytyczny do naprawy PRZED pushem

Autor: sesja Cowork, 2026-08-27. Dotyczy: założenia repo na GitHubie i pola Resource
Information w rejestracji OSF (`10.17605/OSF.IO/59BJ2`, już złożonej).

---

## 1. KRYTYCZNE: sumy kontrolne w rejestracji nie zgodzą się po sklonowaniu repo

Zmierzone:

```
coding_sheet_full.csv   blob w HEAD : d71d601b9f2d8bbc...
coding_sheet_full.csv   plik na dysku: 5bfc3d6a7add370d...
                        zarejestrowane: 5bfc3d6a7add370d...
```

Pliki, które pisałeś na Windows, mają na dysku **CRLF**; git przy commicie znormalizował je
do **LF**, więc blob ma inne bajty. Hash w rejestracji jest hashem **wersji z dysku (CRLF)**.

Konsekwencja: **ktokolwiek sklonuje repo i policzy `sha256sum`, dostanie inne sumy niż te
w rejestracji.** Rejestracja jest niezmienna, więc hashy poprawić się nie da — trzeba
doprowadzić repozytorium do bajtów, które zostały zahaszowane.

Dotyczy 28 z 31 plików pokazywanych jako zmienione. Wzorzec `+N -N` z identycznymi liczbami
to podpis konwersji końców linii, nie zmiany treści — potwierdzone: `git diff
--ignore-cr-at-eol` nie pokazuje nic, a pliki, które pisałem ja (LF na dysku, LF w blobie),
mają hash zgodny w obu miejscach.

**Naprawa — nie zmienia treści żadnego pliku:**

```powershell
cd D:\Claude\Projects\ortho-tech-diffusion
"* -text" | Out-File -Encoding ascii .gitattributes
git add .gitattributes
git add --renormalize .
git commit -m "gitattributes: przechowywanie bajtow verbatim, zgodnosc sum kontrolnych z rejestracja"
```

`* -text` wyłącza jakąkolwiek konwersję końców linii, więc blob staje się bajtami z dysku,
a `git checkout` na dowolnej platformie odtwarza je dokładnie. Po tym commicie **zweryfikuj**:

```powershell
git stash list   # ma byc pusto
foreach ($f in @("data\processed\coding_sheet_full.csv","data\processed\coding_sheet_koder.csv","docs\protocol\coding_manual_v1.2.md","docs\protocol\prompt_system_v1.2_EN.txt","docs\protocol\prompt_user_v1.2_EN.txt")) {
  git show HEAD:$($f -replace '\\','/') | Get-FileHash -Algorithm SHA256 -InputStream {$_}
}
```

albo prościej — po pushu sklonuj do katalogu tymczasowego i policz sumy tam. **Pięć hashy
z sekcji 7 rejestracji musi się zgadzać w świeżym klonie.** To jest warunek wejścia; bez
niego cała historia „każdy może zweryfikować" jest nieprawdziwa.

Uwaga: wcześniejsze commity zostaną w historii ze starymi blobami i to jest w porządku —
weryfikuje się HEAD, a historia ma prawo pokazywać, jak było.

## 2. Pliki, które już napisałem (root, nie `code/`)

Zgodnie z protokołem nie ruszałem `code/`. Napisałem natomiast:

- **`README.md`** — po angielsku, opisuje **obecne** badanie. Poprzedni opisywał plan v0.4
  („które rodziny technologii zyskują, a które tracą udział") — czyli badanie porzucone
  wczoraj. Ktoś wchodzący z rejestracji czytałby co innego, niż zarejestrowaliśmy.
  Zawiera atrybucję NLM, zastrzeżenie o nieredystrybuowaniu streszczeń, tabelę pipeline'u
  i sekcję licencyjną.
- **`LICENSE`** → **MIT** (kod). Było CC BY na całość, a Creative Commons sam odradza CC
  do oprogramowania.
- **`LICENSE-docs`** → dotychczasowa treść CC BY 4.0, dla `docs/` i `data/`.
- **`CITATION.cff`** — opisywał stare badanie; przepisany, z DOI rejestracji, `license: MIT`
  i `repository-code` wskazującym adres z §4.

Wszystkie cztery są LF; po `--renormalize` zostaną jak są.

## 3. Wyprowadź 39 briefów z zamkniętego projektu

`docs/briefs` ma 54 pliki, z czego **tylko 14 dotyczy ortopedii**. Reszta to majowo-czerwcowe
notatki robocze pracy o myślnikach — przyjechały przy migracji, bo poleciłem skopiować
`docs/briefs` „w całości". Mój błąd w tamtym briefie.

Publiczne repo znaczy publiczną kuchnię zamkniętego, zdeponowanego badania: ślepej replikacji,
audytów, korespondencji o figurach. Przenieś je do `docs/archiwum_myslniki/` i dopisz ten
katalog do `.gitignore`, po czym `git rm --cached -r docs/archiwum_myslniki`. Historia tamtej
pracy ma własne repo.

Zostaw 14 briefów ortopedycznych — one dokumentują proces powstawania tego badania i są
argumentem za, nie przeciw.

## 4. Założenie repo i push

```powershell
gh repo create P-Czum/ortho-tech-diffusion --public --source=. --push
```

Nazwa jest wpisana w `CITATION.cff` i w `README.md`. **Jeśli wybierzesz inną, popraw ją
w obu miejscach** — inaczej rejestracja będzie wskazywać w pustkę.

Kolejność wiążąca: najpierw §1 (renormalizacja), potem §3 (briefy), dopiero na końcu push.
Pierwszy publiczny stan repo ma być już poprawny.

## 5. Po pushu — zaraportuj

Adres repo, wynik weryfikacji pięciu hashy w świeżym klonie, liczbę plików w `docs/briefs`
po sprzątaniu. Adres wstawię Przemkowi do pola Resource Information w rejestracji OSF.

## 6. Czego nie ruszać

Treści żadnego z dwunastu zahaszowanych plików. Renormalizacja zmienia sposób
**przechowywania** bajtów w gicie, nie same bajty — po niej sumy na dysku muszą być
identyczne jak przed nią. Jeśli którakolwiek się zmieni, zatrzymaj się i napisz.
