---
title: "Rodzaje zleceń: rynkowe, z limitem i stop — krok po kroku"
description: Co robią przyciski Market, Limit i Stop w aplikacji giełdy lub brokera: przykład z liczbami i 3 błędy, przez które początkujący tracą pieniądze.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: podstawowe rodzaje zleceń — rynkowe (szybko, cena nieustalona), z limitem (cena ustalona, realizacja niepewna), stop (uruchamia się przy danej cenie)
---
**Jakie są rodzaje zleceń?** **Zlecenie rynkowe** (Market) kupuje lub sprzedaje od razu po najlepszej dostępnej cenie. **Zlecenie z limitem ceny** (Limit) kupuje lub sprzedaje tylko po twojej cenie albo lepszej, więc może się nigdy nie zrealizować. **Zlecenie stop** (Stop) czeka, aż cena dojdzie do wybranego przez ciebie poziomu, i wtedy wysyła zlecenie rynkowe — często używa się go, żeby ograniczyć stratę.

> **Najważniejsze**
> - Market = szybkość, ale nie kontrolujesz dokładnej ceny. Limit = kontrola ceny, ale bez gwarancji realizacji.
> - Zlecenie stop po uruchomieniu staje się zleceniem rynkowym. Przy gwałtownym spadku może się zrealizować dużo poniżej twojej ceny stop.
> - Zanim klikniesz „Kup”, zawsze sprawdź trzy rzeczy: rodzaj zlecenia, ilość i cenę.

## Trzy przyciski prostymi słowami

Gdy otwierasz ekran handlu w aplikacji giełdy kryptowalut albo brokera, zwykle widzisz zakładki: **Market** (rynkowe, PKC), **Limit** (z limitem) i **Stop** (czasem „Stop-limit”, stop z limitem).

- **Zlecenie rynkowe (Market).** „Kup teraz, za każdą cenę”. Realizuje się niemal natychmiast po najlepszej ofercie (to **ask**, najniższa cena, za jaką ktoś chce sprzedać). Przy dużych kryptowalutach i dużych spółkach cena jest zwykle bardzo blisko tej, którą widzisz. Na małych, płytkich rynkach może być dużo gorsza.
- **Zlecenie z limitem (Limit).** „Kup tylko po X USD albo taniej” (albo „sprzedaj tylko po X USD albo drożej”). Twoje zlecenie czeka w **arkuszu zleceń** (order book, liście wszystkich oczekujących zleceń kupna i sprzedaży), aż ktoś przyjmie twoją cenę. Jeśli cena nigdy tam nie dojdzie, nic się nie stanie.
- **Zlecenie stop (Stop, stop loss).** „Jeśli cena spadnie do X USD — sprzedaj”. Do tego momentu jest niewidoczne i nic nie robi. Gdy cena dotknie X USD, staje się zleceniem rynkowym i sprzedaje po następnej dostępnej cenie.
- **Zlecenie stop z limitem (Stop-limit).** Jak stop, ale zamienia się w zlecenie *z limitem*. Nie sprzedasz poniżej swojego limitu — ale przy gwałtownym spadku możesz nie sprzedać wcale.

## Przykład z prostymi liczbami

Załóżmy, że akcja kosztuje **100,00 USD**. Najlepszy kupujący oferuje 99,95 USD (to **bid**), a najlepszy sprzedający chce 100,05 USD (ask). Różnica 0,10 USD to **spread**.

1. Klikasz **Market, kup 10 akcji** → płacisz około 100,05 USD za sztukę = **1000,50 USD** plus ewentualna prowizja.
2. Składasz **Limit, kup 10 akcji po 98 USD** → nic się nie dzieje, dopóki sprzedający nie przyjmie 98 USD. Jeśli cena pójdzie za to do 105 USD, twoje zlecenie po prostu czeka i nic nie kupujesz.
3. Masz już akcje i ustawiasz **Stop na 90 USD** → jeśli cena spadnie do 90 USD, idzie rynkowe zlecenie sprzedaży. Na spokojnym rynku dostaniesz może 89,95 USD. Ale jeśli złe wiadomości pojawią się przed otwarciem sesji i akcja otworzy się po 80 USD, twój stop się uruchomi i sprzedasz w okolicach **80 USD**, a nie 90 USD.

Ten trzeci przypadek jest prawdziwy. 6 maja 2010 roku (tzw. „flash crash”) ceny w USA runęły w ciągu kilku minut, a część zleceń stop zrealizowała się dużo poniżej swoich poziomów stop; niektóre akcje handlowano nawet po jednym cencie — tak podaje raport SEC i CFTC.

## Krok po kroku: bezpiecznie złóż pierwsze zlecenie z limitem

Najpierw poćwicz na bardzo małej kwocie.

1. **Krok 1 — Otwórz ekran handlu** kryptowaluty lub akcji i wybierz **Kup** (Buy).
2. **Krok 2 — Kliknij zakładkę „Limit”**, a nie „Market”.
3. **Krok 3 — Wpisz swoją cenę.** Najpierw spójrz na aktualną cenę (na przykład bitcoin kosztuje teraz {{price:btc}}). Limit dużo poniżej niej może się nigdy nie zrealizować.
4. **Krok 4 — Wpisz ilość.** Sprawdź, czy pole oznacza monety/akcje czy pieniądze (USD, EUR). To najczęstsza pomyłka.
5. **Krok 5 — Sprawdź podsumowanie**: rodzaj, cena, ilość, suma, prowizja. Potem potwierdź.
6. **Krok 6 — Znajdź swoje zlecenie** w „Otwartych zleceniach” (Open orders). Tam możesz je w każdej chwili anulować, dopóki się nie zrealizuje. Po realizacji przechodzi do „Historii zleceń” (Order history).

> **⚠️ Uważaj**
> - **Zlecenia rynkowe na płytkich rynkach.** Na małych kryptowalutach albo poza zwykłymi godzinami handlu zlecenie rynkowe może się zrealizować dużo gorzej niż cena na ekranie (to tzw. **poślizg cenowy**, slippage). Tam używaj zlecenia z limitem.
> - **Myślenie, że stop loss gwarantuje twoją cenę.** Nie gwarantuje: gwarantuje sprzedaż, a nie cenę. Luki cenowe i krachy mogą zepchnąć realizację dużo niżej. Stop z limitem chroni cenę, ale może nie sprzedać.
> - **Pomylenie pól.** Zła strona (Sprzedaj zamiast Kup), dodatkowe zero w ilości albo cena wpisana w złe pole. Przeczytaj podsumowanie, zanim potwierdzisz.

## Co to oznacza, jeśli kupujesz regularnie

Jeśli po prostu kupujesz trochę co tydzień albo co miesiąc, nie potrzebujesz skomplikowanych zleceń. Zlecenie rynkowe na duże, płynne aktywo zwykle wystarczy, albo zlecenie z limitem trochę powyżej aktualnej ceny, jeśli chcesz ustawić górną granicę. Prawdziwy wynik daje czas na rynku: 10 USD dziennie w bitcoina przez 3 lata byłoby dziś warte {{dca:btc:3}} (przy wpłatach {{dcainv:3}}) — to wyniki z przeszłości, nie prognoza.

Dalej na WhatIfStack: zobacz, jak arkusz zleceń i duzi traderzy poruszają rynkiem, w [centrum Trading]({lang}/trading/) i w [trackerze wielorybów Hyperliquid]({lang}/trading/hyperliquid/), porównaj prowizje na [giełdach]({lang}/exchanges/), a wszystkie lekcje znajdziesz na [stronie Nauka]({lang}/learn/).

## Źródła

- [Investor.gov (SEC): Rodzaje zleceń](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Biuletyn dla inwestorów — zlecenia stop, stop z limitem i trailing stop](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Rodzaje zleceń](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC i SEC: Raport o wydarzeniach rynkowych z 6 maja 2010 roku](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*To nie jest porada inwestycyjna.*
