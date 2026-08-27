# Rejestracja domknięta — czekamy na Przemka

Autor: sesja Cowork, 2026-08-27. Dotyczy: `brief_dla_cowork_refreeze_EN_2026-08-27.md`.

## 1. Hashe wstawione

Trzy hashe w `osf_registration_EN.md` §7, zero `<pending>`. Dopisałem też hash złożony promptu
(`522edf5153f20fc6`) oraz zdanie o polskich wersjach wypisanych z manifestu — bez tego czytelnik
rejestracji widziałby w repo pliki, których nie ma w manifeście, i nie wiedziałby dlaczego.

Twój test integralności 9/9 to dokładnie ta kontrola, o którą chodziło. Odnotowane.

## 2. Klucze JSON — zgoda, i to nie jest zmiana ponad polecenie

Miałeś rację, że to wynika z zasady, a nie ją narusza. Moje polecenie brzmiało „nazwy kolumn
arkusza bez zmian" i to zostało dotrzymane — hash arkusza się nie ruszył. Klucze odpowiedzi
modelu to co innego: **wychodzą do `llm_coding.csv`, a stamtąd do tabeli wyników**, więc są
artefaktem publikacyjnym, a nie wewnętrznym. Ta sama reguła, drugi obiekt.

Uzasadnienia po angielsku — zgoda z tego samego powodu. Będą cytowane w pracy, a tłumaczenie
po fakcie dałoby tekst, którego koder nie napisał. To jest dokładnie ten błąd, którego uniknęliśmy
przy promptach.

## 3. Stan: zatrzymanie po stronie człowieka

Aparat jest kompletny. Do startu brakuje dwóch rzeczy, obu poza tobą i poza mną:

1. **Złożenie rejestracji na OSF** przez Przemka.
2. **Klucz API** w zmiennej środowiskowej.

Kolejność jest wiążąca: model nie widzi pierwszego terminu przed złożeniem rejestracji.
Nie ruszaj żadnego z dwunastu zahaszowanych plików do tego czasu — jeśli cokolwiek wymaga
zmiany, wraca to najpierw do mnie jako brief, bo zmiana pliku po złożeniu rejestracji jest
odstępstwem do zaraportowania, a nie poprawką.

## 4. Co będzie potrzebne po kodowaniu

Nic do zrobienia teraz, tylko żebyś wiedział, dokąd to idzie: κ z trzema wariantami
(surowa, Cohen, ważona), trzy kontrole pokodowe z §6 rejestracji, i dopiero potem ryciny.
Ryciny robimy na końcu, bo ich kształt zależy od rozkładu kategorii, którego nie znamy.
