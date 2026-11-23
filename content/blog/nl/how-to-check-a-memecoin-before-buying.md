---
title: Een memecoin checken vóór je koopt: 6 checks in 5 minuten
description: Check vóór je een memecoin koopt het contract, de liquiditeit, de houders, het aandeel van de top 10, de leeftijd en de Binance-audit. Simpele checklist.
date: 2026-11-23T16:30:00Z
category: learn
track: memes
step: 6
assets: sol, bnb, doge
stat: 6
stat_label: checks om te doen vóór je een memecoin koopt
---
**Hoe check je een memecoin voordat je koopt?** Zoek de token op via zijn contractadres en check dan zes dingen: de veiligheidsaudit, de liquiditeit, het aantal houders, hoeveel de top 10 wallets bezitten, hoe oud de token is en of de maker hem nog kan aanpassen. Is één check rood? Sla de coin over — er zijn er duizenden andere.

> **Belangrijkste punten**
> - Deze checks maken een memecoin niet veilig. Ze helpen je alleen de duidelijkste valkuilen te vermijden: tokens die je niet kunt verkopen, nepkopieën en coins die een paar wallets kunnen laten crashen.
> - Het tabblad **Audit** in Binance Wallet checkt risico's in het contract, bij het handelen en op oplichting (bijvoorbeeld een "honeypot" — een token die je wel kunt kopen maar nooit kunt verkopen). Binance zegt zelf dat de audit niet waterdicht is.
> - Op onze [memecoinpagina]({lang}/memes/) staat het kwaliteitsfilter standaard aan (**Alleen kwaliteit: liquiditeit $100K+, 1 dag+**): alleen tokens met $100K+ liquiditeit die minstens 1 dag oud zijn.

Deze les gaat verder op [Binance Wallet koppelen aan een DEX]({lang}/blog/connect-binance-wallet-to-dex/). Memecoins zijn extreem riskant — gebruik alleen geld dat je kunt missen.

## Stap 1 — Zoek het juiste contractadres

Elke token heeft een **contractadres** (zijn unieke ID op de blockchain, een lange reeks letters en cijfers). Iedereen kan een token maken met dezelfde naam en hetzelfde logo, dus de naam zegt niets.

1. Kopieer het adres van het officiële account van het project of van een betrouwbare datasite.
2. Plak het in de zoekbalk van je wallet. Vergelijk de eerste en laatste 4 tekens.
3. Zie je meerdere tokens met dezelfde naam? Dan zijn de andere kopieën.

## Stap 2 — Open de veiligheidsaudit

Open in de Binance-app de token in **Wallet** en tik op het tabblad **Audit** (op de website: klik op de token en dan op **Audit**). Op onze tokenpagina's voor memecoins zie je dezelfde check als **Binance-veiligheidscheck: Laag risico / Gemiddeld risico / Hoog risico**.

Kijk naar drie groepen:

- **Contractrisico** — kan de maker verkopen blokkeren, wallets op een zwarte lijst zetten, de belasting aanpassen of saldo's veranderen?
- **Handelsrisico** — honeypotrisico, vreemde koop- of verkoopbelasting (een vergoeding die bij elke trade wordt ingehouden), lage liquiditeit, risico op een rug pull.
- **Oplichtingsrisico** — nep-token, bekende scam, spam.

Eén rood punt = niet kopen. "Laag risico" betekent nog steeds niet veilig: de maker kan na je aankoop nog dingen doen.

## Stap 3 — Check de liquiditeit

Liquiditeit is het geld in de handelspool waardoor je kunt verkopen. Is die heel klein, dan drukt zelfs een kleine verkoop de prijs flink omlaag, en de maker kan het geld eruit halen (een rug pull). Op WhatIfStack verbergt ons standaardfilter tokens met minder dan $100K liquiditeit. Check ook of de liquiditeit van de pool vastgezet (locked) of verbrand (burned, voorgoed weg) is, als de datasite dat laat zien.

## Stap 4 — Tel de houders en het aandeel van de top 10

Kijk op de tokenpagina naar **Houders** (hoeveel wallets hem bezitten) en **Top 10 bezit** (welk deel van alle coins de 10 grootste wallets hebben). Een paar honderd houders en een groot aandeel voor de top 10 betekenen dat een handjevol mensen kan verkopen en de prijs kan laten crashen. Let op: ook de pool en burn-adressen staan in de top 10 — dat deel is normaal.

## Stap 5 — Check de leeftijd

De meeste scamtokens leven een paar uur of dagen. Een token die jonger is dan een dag heeft helemaal geen geschiedenis. Ons filter op /memes/ toont alleen tokens van minstens 1 dag oud. Ouder is niet veilig — alleen minder onbekend.

## Stap 6 — Op Solana: kan de maker de token nog aanpassen?

Op Solana zijn twee instellingen belangrijk:

- **Mint authority** (het recht om nieuwe tokens te maken). Staat dit nog aan, dan kan de maker er meer bijmaken en wordt jouw deel kleiner.
- **Freeze authority** (het recht om een wallet te bevriezen). Staat dit nog aan, dan kan de maker je tegenhouden om te verplaatsen of te verkopen.

Veiliger is "revoked" of "disabled" (niemand heeft dat recht). Je ziet beide op de tokenpagina van een blockexplorer zoals Solscan.

> **⚠️ Let op**
> - **Een nepkopie met dezelfde naam.** Koop altijd op contractadres, nooit op naam of logo.
> - **Een honeypot.** Je kunt kopen, de grafiek stijgt, maar niemand kan verkopen. Een geschiedenis met wel aankopen maar geen verkopen is een rode vlag.
> - **Vertrouwen op één groen lampje.** Een audit, veel houders of een bekende naam beschermen je niet als de prijs gewoon daalt — de meeste memecoins eindigen rond nul.

## Wat het betekent als je regelmatig koopt

Regelmatig kleine bedragen kopen werkt het best met beleggingen die over vijf jaar waarschijnlijk nog bestaan. De meeste memecoins horen daar niet bij. Wil je er toch een proberen? Houd het bij een heel klein, vast bedrag en volg het naast de rest van je geld in [je portfolio]({lang}/me/).

Volgende les: het verhaal van Dogecoin. Alle lessen staan op de [Leer-pagina]({lang}/learn/).

## Bronnen

- [Binance: How to Use the Token Audit Feature in Binance Wallet](https://www.binance.com/en/support/faq/detail/fd1b21bac5114feda49dd185461afdda)
- [Binance.US: What is a honeypot scam?](https://support.binance.us/en/articles/15388146-what-is-a-honeypot-scam)
- [Solana docs: Set authority (mint and freeze authority)](https://solana.com/docs/tokens/basics/set-authority)
- [Solana docs: Freeze account](https://solana.com/docs/tokens/basics/freeze-account)

*Geen beleggingsadvies. Deze gids legt uit hoe je een token checkt en raadt niet aan om welke coin dan ook te kopen.*
