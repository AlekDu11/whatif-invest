---
title: "Ordertypes: market-, limiet- en stoporders stap voor stap uitgelegd"
description: Wat de knoppen Market, Limit en Stop doen in een exchange- of broker-app, met een rekenvoorbeeld en de 3 fouten die beginners geld kosten.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: basisordertypes — market (snel, prijs niet vast), limiet (prijs vast, uitvoering niet zeker), stop (start bij een prijs)
---
**Welke ordertypes zijn er?** Een **marketorder** (Market) koopt of verkoopt meteen tegen de beste prijs die er nu is. Een **limietorder** (Limit) koopt of verkoopt alleen tegen jouw prijs of beter, dus hij wordt misschien nooit uitgevoerd. Een **stoporder** (Stop) wacht tot de prijs een niveau bereikt dat jij kiest, en stuurt dan een marketorder — vaak gebruikt om een verlies te beperken.

> **Belangrijkste punten**
> - Market = snelheid, maar je bepaalt de exacte prijs niet. Limit = controle over de prijs, maar geen garantie dat hij wordt uitgevoerd.
> - Een stoporder wordt een marketorder zodra hij afgaat. Bij een snelle daling kan hij ver onder je stopprijs worden uitgevoerd.
> - Check vóór je op "Kopen" drukt altijd drie dingen: ordertype, aantal en prijs.

## De drie knoppen, in gewone woorden

Open je het handelsscherm in een exchange- of broker-app, dan zie je meestal tabbladen: **Market**, **Limit** en **Stop** (soms "Stop-limit"). In Nederlandse apps heet dat vaak bestens, limiet en stop.

- **Marketorder (bestens).** "Koop nu, wat de prijs ook is." Hij wordt bijna direct uitgevoerd tegen het beste aanbod (de **ask**, de laagste prijs die een verkoper vraagt). Bij grote munten en grote aandelen ligt de prijs meestal heel dicht bij wat je ziet. Bij kleine, dunne markten kan het veel slechter uitvallen.
- **Limietorder.** "Koop alleen voor $X of goedkoper" (of "verkoop alleen voor $X of hoger"). Je order wacht in het **orderboek** (de lijst met alle wachtende koop- en verkooporders) tot iemand jouw prijs accepteert. Komt de prijs daar nooit, dan gebeurt er niets.
- **Stoporder (stop-loss).** "Als de prijs daalt tot $X, verkoop dan." Tot dat moment is hij onzichtbaar en doet hij niets. Raakt de prijs $X, dan wordt hij een marketorder en verkoopt hij tegen de eerstvolgende beschikbare prijs.
- **Stop-limitorder.** Zoals een stop, maar hij wordt een *limiet*order. Je verkoopt niet onder je limiet — maar bij een snelle daling verkoop je misschien helemaal niet.

## Een rekenvoorbeeld met simpele getallen

Stel: een aandeel staat op **$100,00**. De beste koper biedt $99,95 (de **bid**) en de beste verkoper vraagt $100,05 (de ask). Het verschil van $0,10 is de **spread**.

1. Je drukt op **Market kopen, 10 aandelen** → je betaalt ongeveer $100,05 per stuk = **$1.000,50** plus eventuele kosten.
2. Je plaatst **Limit kopen, 10 aandelen tegen $98** → er gebeurt niets tot een verkoper $98 accepteert. Gaat de prijs in plaats daarvan naar $105, dan wacht je order gewoon en koop je niets.
3. Je hebt de aandelen en zet een **Stop op $90** → daalt de prijs tot $90, dan gaat er een marketverkoop uit. In een rustige markt krijg je misschien $89,95. Komt er slecht nieuws vóór de beurs opent en opent het aandeel op $80, dan gaat je stop af en verkoop je rond **$80**, niet $90.

Dat derde geval is echt. Op 6 mei 2010 (de "flash crash") stortten Amerikaanse koersen binnen enkele minuten in. Sommige stoporders werden ver onder hun stopniveau uitgevoerd, en een paar aandelen wisselden zelfs voor een cent van eigenaar, volgens het rapport van de SEC en CFTC.

## Stap voor stap: plaats veilig je eerste limietorder

Oefen eerst met een heel klein bedrag.

1. **Stap 1 — Open het handelsscherm** van de munt of het aandeel en kies **Kopen** (Buy).
2. **Stap 2 — Druk op het tabblad "Limit"**, niet "Market".
3. **Stap 3 — Vul je prijs in.** Kijk eerst naar de huidige prijs (Bitcoin staat bijvoorbeeld nu op {{price:btc}}). Een limiet ver daaronder wordt misschien nooit uitgevoerd.
4. **Stap 4 — Vul het aantal in.** Check of het vakje munten/aandelen bedoelt of geld (USD, EUR). Dit is de meest gemaakte tikfout.
5. **Stap 5 — Check het overzicht**: type, prijs, aantal, totaal, kosten. Bevestig daarna.
6. **Stap 6 — Zoek je order** onder "Open orders". Daar kun je hem op elk moment annuleren tot hij is uitgevoerd. Daarna verschuift hij naar "Ordergeschiedenis".

> **⚠️ Let op**
> - **Marketorders in dunne markten.** Bij kleine munten of buiten de normale handelsuren kan een marketorder veel slechter uitvallen dan de prijs op je scherm (dat heet **slippage**). Gebruik daar een limietorder.
> - **Denken dat een stop-loss je prijs garandeert.** Dat doet hij niet: hij garandeert een verkoop, niet de prijs. Koerssprongen en crashes kunnen de uitvoering veel lager duwen. Een stop-limit beschermt de prijs, maar verkoopt misschien niet.
> - **Velden door elkaar halen.** De verkeerde kant (Verkopen in plaats van Kopen), een nul te veel in het aantal, of een prijs in het verkeerde vakje. Lees het overzicht voordat je bevestigt.

## Wat het betekent als je regelmatig koopt

Koop je gewoon elke week of maand een beetje, dan heb je geen ingewikkelde orders nodig. Een marketorder op een groot, liquide bezit is meestal prima, of een limietorder iets boven de huidige prijs als je een maximum wilt. Het echte resultaat komt van tijd in de markt: $10 per dag in Bitcoin gedurende 3 jaar zou nu {{dca:btc:3}} waard zijn (je legde {{dcainv:3}} in) — resultaten uit het verleden, geen voorspelling.

Verder op WhatIfStack: zie hoe orderboeken en grote traders de markt bewegen op de [tradinghub]({lang}/trading/) en in de [Hyperliquid-walvistracker]({lang}/trading/hyperliquid/), vergelijk kosten bij [exchanges]({lang}/exchanges/), en vind alle lessen op de [Leren-pagina]({lang}/learn/).

## Bronnen

- [Investor.gov (SEC): Soorten orders](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Beleggersbulletin — stop-, stop-limit- en trailing-stoporders](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Ordertypes](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC en SEC: Stafrapport over de marktgebeurtenissen van 6 mei 2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Geen beleggingsadvies.*
