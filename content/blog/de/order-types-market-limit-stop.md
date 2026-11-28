---
title: "Ordertypen: Market-, Limit- und Stop-Order Schritt für Schritt erklärt"
description: Was die Buttons Market, Limit und Stop in der App von Börse oder Broker tun – mit Rechenbeispiel und den 3 Fehlern, die Einsteiger Geld kosten.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: Grundtypen von Orders — Market (schnell, Preis nicht fix), Limit (Preis fix, Ausführung unsicher), Stop (löst bei einem Kurs aus)
---
**Welche Ordertypen gibt es?** Eine **Market-Order** (Bestens-Order) kauft oder verkauft sofort zum besten verfügbaren Preis. Eine **Limit-Order** kauft oder verkauft nur zu Ihrem Preis oder besser – sie wird also vielleicht nie ausgeführt. Eine **Stop-Order** wartet, bis der Kurs ein von Ihnen gewähltes Niveau erreicht, und schickt dann eine Market-Order – oft genutzt, um einen Verlust zu begrenzen.

> **Das Wichtigste**
> - Market = Tempo, aber Sie haben den genauen Preis nicht in der Hand. Limit = Kontrolle über den Preis, aber keine Garantie auf Ausführung.
> - Eine Stop-Order wird beim Auslösen zur Market-Order. Bei einem schnellen Absturz kann sie weit unter Ihrem Stop-Kurs ausgeführt werden.
> - Prüfen Sie vor dem Klick auf „Kaufen“ immer drei Dinge: Ordertyp, Menge und Preis.

## Die drei Buttons, einfach erklärt

Wenn Sie in der App einer Kryptobörse oder eines Brokers die Handelsmaske öffnen, sehen Sie meist Reiter: **Market** (Bestens), **Limit** und **Stop** (manchmal „Stop-Limit“).

- **Market-Order (Bestens).** „Jetzt kaufen, egal zu welchem Preis.“ Sie wird fast sofort zum besten Angebot ausgeführt (dem **Ask** oder Briefkurs, dem niedrigsten Preis, zu dem jemand verkaufen will). Bei großen Coins und großen Aktien liegt der Preis meist sehr nah an dem, was Sie sehen. In kleinen, illiquiden Märkten kann er deutlich schlechter sein.
- **Limit-Order.** „Nur zu X $ oder billiger kaufen“ (oder „nur zu X $ oder teurer verkaufen“). Ihre Order wartet im **Orderbuch** (Order Book, der Liste aller wartenden Kauf- und Verkaufsaufträge), bis jemand Ihren Preis annimmt. Erreicht der Kurs dieses Niveau nie, passiert nichts.
- **Stop-Order (Stop-Loss).** „Fällt der Kurs auf X $, verkaufen.“ Bis dahin ist sie unsichtbar und tut nichts. Berührt der Kurs X $, wird sie zur Market-Order und verkauft zum nächsten verfügbaren Preis.
- **Stop-Limit-Order.** Wie ein Stop, wird aber zur *Limit*-Order. Unter Ihrem Limit verkaufen Sie nicht – bei einem schnellen Absturz aber womöglich gar nicht.

## Ein Rechenbeispiel mit einfachen Zahlen

Angenommen, eine Aktie steht bei **100,00 $**. Der beste Käufer bietet 99,95 $ (der **Bid** oder Geldkurs), der beste Verkäufer verlangt 100,05 $ (der Ask). Die Lücke von 0,10 $ ist der **Spread**.

1. Sie klicken **Market, 10 Aktien kaufen** → Sie zahlen rund 100,05 $ pro Stück = **1.000,50 $** plus eventuelle Gebühr.
2. Sie setzen **Limit, 10 Aktien zu 98 $ kaufen** → nichts passiert, bis ein Verkäufer 98 $ akzeptiert. Steigt der Kurs stattdessen auf 105 $, wartet Ihre Order einfach, und Sie kaufen nichts.
3. Sie besitzen die Aktien und setzen einen **Stop bei 90 $** → fällt der Kurs auf 90 $, geht ein Market-Verkauf raus. In einem ruhigen Markt bekommen Sie vielleicht 89,95 $. Kommen aber vor Börsenöffnung schlechte Nachrichten und die Aktie eröffnet bei 80 $, löst Ihr Stop aus, und Sie verkaufen bei rund **80 $**, nicht 90 $.

Der dritte Fall ist real. Am 6. Mai 2010 (dem „Flash Crash“) brachen die US-Kurse innerhalb von Minuten ein, und manche Stop-Orders wurden weit unter ihrem Stop-Kurs ausgeführt; einige Aktien wurden sogar für einen Cent gehandelt, so der Bericht von SEC und CFTC.

## Schritt für Schritt: Ihre erste Limit-Order sicher platzieren

Üben Sie zuerst mit einem sehr kleinen Betrag.

1. **Schritt 1 — Öffnen Sie die Handelsmaske** des Coins oder der Aktie und wählen Sie **Kaufen** (Buy).
2. **Schritt 2 — Tippen Sie auf den Reiter „Limit“**, nicht auf „Market“.
3. **Schritt 3 — Geben Sie Ihren Preis ein.** Schauen Sie zuerst auf den aktuellen Kurs (Bitcoin steht zum Beispiel gerade bei {{price:btc}}). Ein Limit weit darunter wird womöglich nie ausgeführt.
4. **Schritt 4 — Geben Sie die Menge ein.** Prüfen Sie, ob das Feld Coins/Aktien oder Geld (USD, EUR) meint. Das ist der häufigste Tippfehler.
5. **Schritt 5 — Prüfen Sie die Zusammenfassung**: Typ, Preis, Menge, Gesamtbetrag, Gebühr. Dann bestätigen.
6. **Schritt 6 — Finden Sie Ihre Order** unter „Offene Orders“ (Open orders). Dort können Sie sie jederzeit stornieren, solange sie nicht ausgeführt ist. Danach wandert sie in die „Orderhistorie“ (Order history).

> **⚠️ Vorsicht**
> - **Market-Orders in illiquiden Märkten.** Bei kleinen Coins oder außerhalb der normalen Handelszeiten kann eine Market-Order deutlich schlechter ausgeführt werden als der Kurs auf dem Bildschirm (das nennt man **Slippage**). Nutzen Sie dort eine Limit-Order.
> - **Glauben, ein Stop-Loss garantiere Ihren Preis.** Tut er nicht: Er garantiert den Verkauf, nicht den Preis. Kurslücken und Crashs können die Ausführung weit nach unten drücken. Ein Stop-Limit schützt den Preis, verkauft aber womöglich nicht.
> - **Felder verwechseln.** Falsche Seite (Verkaufen statt Kaufen), eine Null zu viel bei der Menge oder der Preis im falschen Feld. Lesen Sie die Zusammenfassung, bevor Sie bestätigen.

## Was das bedeutet, wenn Sie regelmäßig kaufen

Wenn Sie einfach jede Woche oder jeden Monat ein wenig kaufen, brauchen Sie keine komplizierten Orders. Eine Market-Order auf einen großen, liquiden Wert reicht meist – oder eine Limit-Order knapp über dem aktuellen Kurs, wenn Sie eine Obergrenze wollen. Das echte Ergebnis kommt von der Zeit im Markt: 10 $ am Tag in Bitcoin über 3 Jahre wären heute {{dca:btc:3}} wert (eingezahlt: {{dcainv:3}}) — vergangene Ergebnisse, keine Prognose.

Weiter auf WhatIfStack: Sehen Sie im [Trading-Bereich]({lang}/trading/) und im [Hyperliquid-Wal-Tracker]({lang}/trading/hyperliquid/), wie Orderbücher und große Trader den Markt bewegen, vergleichen Sie Gebühren bei den [Börsen]({lang}/exchanges/) und finden Sie alle Lektionen auf der [Lernen-Seite]({lang}/learn/).

## Quellen

- [Investor.gov (SEC): Ordertypen](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Anlegerbulletin — Stop-, Stop-Limit- und Trailing-Stop-Orders](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Ordertypen](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC und SEC: Bericht zu den Marktereignissen vom 6. Mai 2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Keine Anlageberatung.*
