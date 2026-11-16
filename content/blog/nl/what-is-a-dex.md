---
title: Wat is een DEX en wat is het verschil met een crypto-exchange?
description: Wat is een DEX? Uitleg in gewone taal over gedecentraliseerde exchanges: AMM's, liquiditeitspools, wallets, gas fees en de voor- en nadelen tegenover een CEX.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**Wat is een DEX?** Een DEX (gedecentraliseerde exchange) is een set smart contracts op een blockchain waarmee je de ene token direct vanuit je eigen wallet voor een andere ruilt. Er is geen bedrijf dat je geld bewaart, geen account en meestal geen identiteitscontrole. Uniswap op Ethereum en Raydium, Orca en Meteora op Solana zijn bekende voorbeelden.

Een gewone crypto-exchange zoals Binance, Coinbase of Kraken is een **CEX** (gecentraliseerde exchange): een bedrijf dat je tegoed bewaart, kopers en verkopers in zijn eigen systeem aan elkaar koppelt en zich aan financiële regels moet houden.

## Hoe een DEX werkt

### Automated market makers (AMM's)

De meeste DEX'en hebben geen orderboek met kopers en verkopers. In plaats daarvan gebruiken ze een **automated market maker**: een formule die de prijs bepaalt.

De klassieke versie, gebruikt door Uniswap v2, is de "constant product"-regel: een pool bevat twee tokens, en de hoeveelheid token A vermenigvuldigd met de hoeveelheid token B moet na elke trade gelijk blijven. Koop je token A, dan voeg je token B toe aan de pool en haal je token A eruit; A wordt schaarser in de pool en de prijs stijgt.

Je hoeft de som niet zelf te maken. Het kernidee: **hoe groter de pool, hoe minder jouw trade de prijs beweegt.**

### Liquiditeitspools

De tokens in de pool komen van **liquiditeitsverschaffers**: mensen die paren van tokens storten en een deel van de handelskosten verdienen (vaak 0,05–1% per swap). Hun risico is dat de prijzen van de twee tokens uit elkaar lopen, waardoor ze slechter af kunnen zijn dan wanneer ze de tokens gewoon hadden vastgehouden ("impermanent loss").

Bij nieuw gelanceerde tokens zet de maker meestal de eerste pool op. Daarom zijn liquidity locks belangrijk: wie de pool beheert, kan hem opnemen.

### Je wallet is je account

Om een DEX te gebruiken koppel je een self-custody wallet zoals MetaMask (Ethereum en vergelijkbare chains) of Phantom (Solana). Elke trade is een transactie die je zelf ondertekent. Je **herstelzin (seed phrase)** is de hoofdsleutel: verlies je hem, dan is het geld weg; deel je hem, dan neemt iemand anders het geld.

### Gas en kosten

Elke DEX-trade betaalt een netwerkfee, op Ethereum **gas** genoemd. Op Ethereum stijgt die als het netwerk druk is; layer-2-netwerken en Solana zijn meestal veel goedkoper. De basisfee op Solana is 0,000005 SOL per handtekening. Bovenop gas betaal je de poolfee, en bij kleine of snel bewegende tokens krijg je mogelijk te maken met **slippage** en **price impact**.

## DEX vs CEX: de belangrijkste verschillen

- **Wie bewaart je tegoed:** bij een DEX jij zelf (je wallet); bij een CEX de exchange.
- **Account en ID-check:** een DEX vraagt meestal niets; een CEX vereist identiteitscontrole (KYC).
- **Keuze aan tokens:** een DEX biedt bijna elke token, ook gloednieuwe; een CEX noteert alleen geselecteerde tokens.
- **Kopen met kaart of bank:** meestal niet direct mogelijk op een DEX; standaard bij een CEX.
- **Kosten:** DEX: gas, poolfee en slippage; CEX: handelskosten, spread en opnamekosten.
- **Hulp als er iets misgaat:** een DEX heeft geen helpdesk; een CEX heeft klantenservice en soms beschermingsregelingen.
- **Grootste risico's:** DEX: scamtokens, verkeerde approvals en je eigen fouten; CEX: hacks, geblokkeerde accounts en faillissement.

## Voordelen van een DEX

- **Self-custody.** Niemand kan je account bevriezen of je geld kwijtraken in een faillissement.
- **Open toegang.** Iedereen met een wallet kan handelen, van bijna overal.
- **Nieuwe tokens eerst.** Tokens verschijnen op DEX'en lang voordat (of in plaats van dat) ze op een exchange worden genoteerd.
- **Transparantie.** Pools, trades en holders zijn zichtbaar op de blockchain.

## Nadelen van een DEX

- **Jij bent de bank.** Eén fout (een verkeerd adres, een nepsite, een kwaadaardige approval) en je geld is voorgoed weg.
- **Scamtokens.** Iedereen kan in een paar minuten een token en een pool aanmaken. De meeste nieuwe tokens verliezen bijna al hun waarde; zie onze [rug pull-checklist]({lang}/blog/how-to-spot-a-rug-pull/).
- **Verborgen kosten.** Slippage en price impact kunnen meer kosten dan de zichtbare fee.
- **Geen makkelijke instap.** Meestal moet je eerst crypto kopen op een CEX en die naar je wallet sturen.
- **Smart-contractrisico.** Bugs of hacks in DEX-code hebben tot grote verliezen geleid.

## Welke moet je als beginner gebruiken?

Veel mensen gebruiken allebei: een CEX met vergunning om euro's om te zetten in crypto, en een DEX voor tokens die alleen on-chain bestaan. Voor periodiek, langdurig kopen van grote assets zoals Bitcoin of Ethereum is een CEX met lage kosten meestal eenvoudiger; vergelijk de opties op onze [exchangepagina]({lang}/exchanges/).

Wil je memecoins en andere on-chain tokens verkennen, begin dan met heel kleine bedragen, een aparte wallet en de meest gevestigde munten op onze [memecoinpagina]({lang}/memes/). Onze stap-voor-stapgids [memecoin kopen op Solana]({lang}/blog/how-to-buy-memecoins-on-solana/) laat het hele proces zien, inclusief tools zoals [GMGN](/go/gmgn?from=blog&l=nl).

## Veelgebruikte DEX-termen

- **Swap**: de ene token ruilen voor een andere.
- **Pair**: de twee tokens in een pool, zoals SOL/USDC.
- **Slippage tolerance**: de maximale prijsverandering die je accepteert.
- **Approve**: toestemming voor een contract om een token uit je wallet te verplaatsen (vooral op Ethereum-achtige chains). Trek oude approvals in die je niet meer nodig hebt.
- **Aggregator**: een dienst die je trade over meerdere DEX'en verdeelt voor een betere prijs, zoals Jupiter op Solana of 1inch op Ethereum.

## Veelgestelde vragen

### Is een DEX veiliger dan een CEX?

Het haalt het risico weg dat de exchange je geld kwijtraakt of bevriest, maar voegt het risico toe van je eigen fouten en scamtokens. Geen van beide is zonder risico.

### Heb ik een ID nodig om een DEX te gebruiken?

Meestal niet, want je handelt vanuit je eigen wallet. De lokale wetten en belastingregels gelden wel gewoon voor jou.

### Waarom mislukte mijn DEX-trade?

Veelvoorkomende redenen: niet genoeg van de native munt voor gas, slippage te laag ingesteld voor een snel bewegende koers, of een token die verkopen blokkeert.

### Moet ik belasting betalen over DEX-trades?

In veel landen wel: een swap van de ene token naar de andere kan als verkoop tellen. Houd je trades bij.

## Bronnen

- [Hoe Uniswap werkt (Uniswap-documentatie)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas en kosten (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Solana-documentatie: kostenstructuur](https://solana.com/docs/core/fees/fee-structure)

*Geen beleggingsadvies. Deze gids legt uit hoe DEX'en werken en raadt geen enkel platform of token aan.*
