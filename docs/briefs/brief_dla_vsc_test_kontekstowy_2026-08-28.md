# Test rozstrzygający: czy przemianowanie widać w kontekstach

Autor: sesja Cowork, 2026-08-28. **Priorytet: przed jakąkolwiek dalszą pracą projektową.**

---

## 0. Po co to i dlaczego teraz

Dziś ustaliliśmy dwie rzeczy. Ręczne kodowanie terminów zawiodło na jednostce analizy — n-gram
nie jest jednostką znaczenia (osiem wierszy na robotykę, `of robotic`, 80% szablonu abstraktu).
A słownik nie może być ratunkiem, bo **`Rapid Prototyping` nie występuje wśród terminów wejściowych
MeSH dla `Printing, Three-Dimensional`** — sprawdzone dziś w MeSH Browser; są tam wyłącznie
warianty zapisu („3-D Printing", „3D Printing", „Three-Dimensional Printing"). Słowniki zapisują
synonimię, nie następstwo terminów w czasie.

Została jedna hipoteza instrumentu: **przemianowanie widać w samym korpusie** — dwa terminy
używane w tych samych kontekstach, jeden opada, gdy drugi rośnie.

**Ten test ma ją potwierdzić albo obalić na przypadku, którego odpowiedź znamy.** Nie budujemy
nic więcej, dopóki nie ma wyniku. Dziś zmieniliśmy instrument trzy razy; czwarta zmiana bez
pomiaru pomiędzy byłaby już miotaniem się.

## 1. Co dokładnie policzyć

Na `def2_text.parquet` albo na tekście pola def1 — użyj tego, co masz pod ręką, byle jeden zbiór
przez cały test i zapisany w wyniku.

**Wektor kontekstu terminu w oknie lat:** dla terminu *t* i okna *W* zbierz wszystkie rekordy
zawierające *t*, policz częstości wszystkich innych terminów kanonicznych w tych rekordach,
znormalizuj (proponuję PPMI albo zwykłe udziały — wybierz jedno i zapisz które). To jest wektor.
Zero uczenia, zero modeli zewnętrznych, samo zliczanie.

**Podobieństwo:** kosinus między wektorami.

**Trzy liczby, które rozstrzygają:**

1. `sim(rapid prototyping [2008–2013], 3d printing [2016–2021])` — **para docelowa, rozłączne okna.**
   Jeśli to jedno pojęcie pod dwiema nazwami, kontekst ma być podobny mimo braku wspólnych lat.
2. **Rozkład odniesienia:** ta sama miara dla ~200 losowych par terminów o zbliżonej liczebności,
   z tych samych okien. To daje tło — bez niego liczba z punktu 1 nic nie znaczy.
3. **Kontrola pozytywna i negatywna:** `sim(3d printing [2008–2013], 3d printing [2016–2021])`
   — ten sam termin w dwóch oknach, górny kres tego, co miara może pokazać. Oraz para jawnie
   niezwiązana, np. `3d printing` wobec `venous thromboembolism`, jako dolny kres.

**Kryterium:** para docelowa ma leżeć **wyraźnie powyżej rozkładu losowego** i bliżej kontroli
pozytywnej niż negatywnej. Podaj percentyl pary docelowej w rozkładzie z punktu 2 — to jest
jedna liczba, która zamyka sprawę.

## 2. Druga para, dla kontrastu

Powtórz dla `computer navigation [2008–2013]` wobec `robotic [2018–2023]`.

To jest przypadek **innego typu** — nie przemianowanie, tylko zawieranie: robot używa nawigacji,
ale dokłada człon wykonawczy. Oczekiwanie: podobieństwo wysokie, ale **niższe** niż przy parze
druku 3D. Jeśli miara nie odróżni tych dwóch sytuacji, to znaczy, że mierzy „bliskość tematyczną",
a nie tożsamość pojęcia — i wtedy też trzeba to wiedzieć.

## 3. Czego NIE robić

- Nie strojenia progów pod wynik. Zapisz miarę i okna **przed** policzeniem, w skrypcie.
- Nie modeli, nie osadzeń pretrenowanych. Tylko zliczanie na naszym korpusie — chodzi o to,
  żeby wynik dało się odtworzyć z kodu i danych, bez zewnętrznej zależności.
- Nie rozszerzania testu na więcej par. Dwie pary, trzy liczby, koniec.

## 4. Co odesłać

Percentyl pary docelowej w rozkładzie losowym, obie kontrole, wynik dla drugiej pary, oraz
jedno zdanie: **czy miara widzi przemianowanie, czy nie.**

Nie interpretuj wyniku dalej i nic na nim nie buduj — decyzja o projekcie wraca do Przemka.

## 5. Stan reszty

Zamrożone pliki i manifest bez zmian. Kodowanie ręczne wstrzymane — plik Przemka
`coding_sheet_koder_CODED_2026-08-28.csv` zostaje nietknięty w katalogu głównym repo;
**nie commituj go**, dopóki nie zdecydujemy, czym się staje.
