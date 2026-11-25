---
title: Crypto van een exchange naar je eigen wallet opnemen: stap voor stap
description: Zet je coins veilig van de exchange naar je eigen wallet: kopieer het juiste adres, kies hetzelfde netwerk, vul zo nodig een memo in en test eerst.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 netwerk
stat_label: de exchange en de wallet moeten hetzelfde gebruiken, anders kunnen de coins verloren gaan
---
**Hoe neem je crypto op naar je eigen wallet?** In je wallet kopieer je je **ontvangstadres** voor de coin. Daarna open je op de exchange **Withdraw** (Opnemen), plak je dat adres, kies je **hetzelfde netwerk** dat je wallet gebruikt, vul je een klein testbedrag in en bevestig je met 2FA. Komt de test aan, dan stuur je de rest.

> **Belangrijkste punten**
> - Drie dingen moeten kloppen: de **coin**, het **adres** en het **netwerk** (de blockchain waarover de coins reizen, bijvoorbeeld Ethereum, BNB Smart Chain, TRON of Solana). Binance waarschuwt dat coins die via het verkeerde netwerk zijn verstuurd voorgoed verloren kunnen gaan.
> - Sommige coins (zoals XRP, XLM of ATOM) hebben ook een **memo** of **tag** nodig (een kort nummer dat de ontvanger vertelt van wie de coins zijn). Zonder memo kan de overboeking vastlopen of bij de verkeerde persoon terechtkomen.
> - **Stuur altijd eerst een kleine test.** Een opname kun je niet meer annuleren zodra de coins de exchange hebben verlaten.

Deze les gaat verder op [Een periodieke aankoop instellen]({lang}/blog/how-to-set-up-a-recurring-buy/). Waarom je überhaupt een eigen wallet zou willen, lees je in [hot en cold wallets]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Voordat je begint

Je hebt twee dingen nodig. Een account bij een exchange met coins erop, beveiligd met 2FA — zie [Registreren bij een crypto-exchange]({lang}/blog/how-to-register-on-a-crypto-exchange/). En je eigen wallet-app die al is ingesteld, met de **herstelzin** (seed phrase: de 12 of 24 geheime woorden die de wallet herstellen) op papier geschreven en offline bewaard. Typ de herstelzin nooit ergens anders in — geen exchange, website of "support"-medewerker heeft hem ooit nodig.

## Stap 1 — Kopieer het ontvangstadres van je wallet

1. Open je wallet-app en tik op **Receive** (Ontvangen; soms **Deposit**).
2. Kies de coin, bijvoorbeeld Bitcoin of USDT.
3. Als de wallet erom vraagt, kies je het netwerk. Schrijf op welk het is — bijvoorbeeld "USDT op TRON (TRC20)" of "USDT op Ethereum (ERC20)".
4. Tik op **Copy** (Kopiëren) naast het adres. Typ het niet over.

Een adres is een lange reeks letters en cijfers. Bitcoin-adressen beginnen vaak met **bc1**, adressen van Ethereum en BNB Smart Chain met **0x**, TRON-adressen met **T**.

## Stap 2 — Open Withdraw op de exchange

In de Binance-app is dat **Assets → Spot → Send → Withdraw Crypto**; op de website **Wallet → Overview → Withdraw**. Andere exchanges hebben een knop **Withdraw** naast elke coin in het wallet- of portfolioscherm. Kies dezelfde coin als in stap 1.

## Stap 3 — Plak het adres en kies het netwerk

1. Plak het adres in het veld **Address** (Adres).
2. Vergelijk de **eerste 4 en laatste 4 tekens** met je wallet. Sommige malware verwisselt een gekopieerd adres met dat van de dief.
3. Kies het **netwerk**. Het moet het netwerk zijn dat je wallet in stap 1 liet zien. Binance stelt soms automatisch een netwerk voor — controleer het toch. Kies een netwerk niet alleen omdat de kosten het laagst zijn.
4. Verschijnt er een veld **Memo** of **Tag** en gaf je wallet je er een, vul het dan in. Toont je eigen wallet geen memo, dan is er meestal geen nodig — maar controleer het in de helppagina's van de wallet.

Tip: twijfel je, sla het adres dan op in **Address Management** (het adresboek) van de exchange. Binance heeft ook een **whitelist**: als je die aanzet, kunnen opnames alleen naar opgeslagen adressen gaan. Dat helpt als iemand je wachtwoord steelt.

## Stap 4 — Stuur een kleine test

1. Vul een klein bedrag in — net boven de minimale opname die het scherm toont.
2. Kijk naar de regels **netwerkkosten** en **je ontvangt**. De kosten zijn vast per opname, dus bij een heel klein bedrag kunnen ze een groot deel zijn.
3. Druk op **Withdraw** en bevestig met je 2FA-code of passkey. Sommige exchanges sturen ook een bevestigingsmail — open die en klik op **Confirm**.

## Stap 5 — Controleer of het is aangekomen en stuur de rest

1. Wacht. Een overboeking kan van een paar seconden tot ongeveer een uur duren, afhankelijk van het netwerk en de drukte.
2. Open op de exchange de opnamegeschiedenis om de status en de **TxID** te zien (het ID van de transactie, dat je kunt opzoeken op een blockexplorer).
3. Staan de coins in je wallet, herhaal dan stap 2 tot en met 4 met de rest. Het adres staat al in de geschiedenis of het adresboek, dus de tweede keer gaat sneller.

Voeg de coins toe aan [je portfolio]({lang}/me/), zodat je hun waarde op één plek volgt, waar ze ook bewaard worden.

> **⚠️ Let op**
> - **Verkeerd netwerk.** USDT bestaat op veel netwerken. USDT via "TRC20" sturen naar een adres dat alleen "ERC20" verwacht, kan betekenen dat de coins weg zijn. Controleer het netwerk twee keer.
> - **Memo of tag vergeten.** Exchanges en wallets die een memo nodig hebben, weten zonder memo niet van wie de binnengekomen coins zijn. Terughalen, als het al kan, is traag en kost geld.
> - **Nep-support en sites voor "adresverificatie".** Niemand die te vertrouwen is, vraagt om je herstelzin of vraagt je een wallet te "verifiëren" door coins te sturen. Neem alleen op via de officiële app of website.

## Wat het betekent als je regelmatig koopt

Koop je elke week of maand een beetje, dan hoef je niet na elke aankoop op te nemen — elke opname kost geld. Veel mensen laten de coins op de exchange oplopen en zetten ze af en toe naar hun eigen wallet, bijvoorbeeld eens per kwartaal, in één grotere overboeking. Een voorbeeld uit onze calculator: $10 per dag in bitcoin gedurende 3 jaar ({{dcainv:3}} in totaal) werd {{dca:btc:3}} ({{dcaroi:btc:3}}). Resultaten uit het verleden, geen voorspelling. Bitcoin staat nu op {{price:btc}}; zie de [Bitcoin-pagina]({lang}/btc/).

Vorige les: [Een periodieke aankoop instellen]({lang}/blog/how-to-set-up-a-recurring-buy/). Volgende les: hoe je crypto verkoopt en het geld op je bankrekening krijgt. Vergelijk exchanges op onze [exchangepagina]({lang}/exchanges/); alle lessen staan op de [Leren-pagina]({lang}/learn/).

## Bronnen

- [Binance Support: crypto storten en opnemen op Binance (bijgewerkt in maart 2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: een storting met een verkeerde of ontbrekende tag/memo terughalen](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: crypto opnemen van je Binance.US-account (juni 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*Geen beleggingsadvies.*
