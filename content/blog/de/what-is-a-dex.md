---
title: Was ist eine DEX und was unterscheidet sie von einer Krypto-Börse?
description: Was ist eine DEX? Dezentrale Börsen einfach erklärt: AMMs, Liquiditätspools, Wallets, Gas-Gebühren sowie Vor- und Nachteile im Vergleich zu einer CEX.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**Was ist eine DEX?** Eine DEX (dezentrale Börse) ist eine Sammlung von Smart Contracts auf einer Blockchain, mit der Sie einen Token direkt aus Ihrer eigenen Wallet gegen einen anderen tauschen. Es gibt kein Unternehmen, das Ihr Geld verwahrt, kein Konto und meist keine Identitätsprüfung. Bekannte Beispiele sind Uniswap auf Ethereum sowie Raydium, Orca und Meteora auf Solana.

Eine klassische Krypto-Börse wie Binance, Coinbase oder Kraken ist eine **CEX** (zentrale Börse): ein Unternehmen, das Ihre Gelder verwahrt, Käufer und Verkäufer im eigenen System zusammenbringt und Finanzvorschriften einhalten muss.

## So funktioniert eine DEX

### Automated Market Maker (AMMs)

Die meisten DEXs haben kein Orderbuch mit Käufern und Verkäufern. Stattdessen nutzen sie einen **Automated Market Maker** – eine Formel, die den Preis festlegt.

Die klassische Variante, die Uniswap v2 nutzt, ist die „Constant Product“-Regel: Ein Pool enthält zwei Token, und die Menge von Token A multipliziert mit der Menge von Token B muss nach jedem Trade gleich bleiben. Wenn Sie Token A kaufen, geben Sie Token B in den Pool und entnehmen Token A – A wird im Pool knapper, und sein Preis steigt.

Rechnen müssen Sie nicht. Der Kerngedanke: **Je größer der Pool, desto weniger bewegt Ihr Trade den Preis.**

### Liquiditätspools

Die Token im Pool stammen von **Liquiditätsanbietern** – Menschen, die Token-Paare einzahlen und einen Anteil an den Handelsgebühren erhalten (oft 0,05–1 % pro Swap). Ihr Risiko: Die Preise der beiden Token laufen auseinander, sodass sie schlechter dastehen können als beim bloßen Halten („Impermanent Loss“).

Bei neu gestarteten Token richtet meist der Ersteller den ersten Pool ein. Deshalb sind Liquidity Locks wichtig: Wer den Pool kontrolliert, kann ihn abziehen.

### Ihre Wallet ist Ihr Konto

Um eine DEX zu nutzen, verbinden Sie eine Self-Custody-Wallet wie MetaMask (Ethereum und ähnliche Chains) oder Phantom (Solana). Jeder Trade ist eine Transaktion, die Sie selbst signieren. Ihre **Seed-Phrase** ist der Generalschlüssel – verlieren Sie sie, ist das Geld weg; geben Sie sie weiter, nimmt sich jemand anderes das Geld.

### Gas und Gebühren

Jeder DEX-Trade zahlt eine Netzwerkgebühr, auf Ethereum **Gas** genannt. Auf Ethereum steigt sie, wenn das Netzwerk ausgelastet ist; Layer-2-Netzwerke und Solana sind meist deutlich günstiger – die Basisgebühr von Solana beträgt 0,000005 SOL pro Signatur. Zusätzlich zum Gas zahlen Sie die Poolgebühr, und bei kleinen oder schnell bewegten Token kommen **Slippage** und **Price Impact** hinzu.

## DEX vs. CEX: die wichtigsten Unterschiede

- **Wer Ihr Geld verwahrt:** bei einer DEX Sie selbst (Ihre Wallet); bei einer CEX die Börse.
- **Konto und Identitätsprüfung:** Eine DEX braucht meist keine; eine CEX verlangt eine Identitätsprüfung (KYC).
- **Token-Auswahl:** Eine DEX bietet fast jeden Token, auch brandneue; eine CEX listet nur ausgewählte Token.
- **Kauf per Karte oder Bank:** auf einer DEX direkt meist nicht möglich; bei einer CEX Standard.
- **Gebühren:** DEX – Gas, Poolgebühr und Slippage; CEX – Handelsgebühr, Spread und Auszahlungsgebühr.
- **Hilfe, wenn etwas schiefgeht:** Eine DEX hat keine Hotline; eine CEX hat Kundensupport und manchmal Schutzprogramme.
- **Hauptrisiken:** DEX – Betrugs-Token, gefährliche Freigaben und eigene Fehler; CEX – Hacks, Kontosperrungen und Insolvenz.

## Vorteile einer DEX

- **Self-Custody.** Niemand kann Ihr Konto sperren oder Ihr Geld in einer Insolvenz verlieren.
- **Offener Zugang.** Jeder mit einer Wallet kann handeln, von fast überall.
- **Neue Token zuerst.** Token erscheinen auf DEXs lange vor (oder statt) einem Börsenlisting.
- **Transparenz.** Pools, Trades und Holder sind auf der Blockchain sichtbar.

## Nachteile einer DEX

- **Sie sind die Bank.** Ein Fehler – eine falsche Adresse, eine gefälschte Seite, eine bösartige Freigabe – und das Geld ist für immer weg.
- **Betrugs-Token.** Jeder kann in Minuten einen Token und einen Pool erstellen. Die meisten neuen Token verlieren fast ihren gesamten Wert; siehe unsere [Rug-Pull-Checkliste]({lang}/blog/how-to-spot-a-rug-pull/).
- **Versteckte Kosten.** Slippage und Price Impact können mehr kosten als die sichtbare Gebühr.
- **Kein einfacher Einstieg.** Meist müssen Sie Krypto zuerst an einer CEX kaufen und an Ihre Wallet senden.
- **Smart-Contract-Risiko.** Fehler oder Hacks im DEX-Code haben schon große Verluste verursacht.

## Was sollten Einsteiger nutzen?

Viele nutzen beides: eine lizenzierte CEX, um Landeswährung in Krypto zu tauschen, und eine DEX für Token, die es nur On-Chain gibt. Für regelmäßige, langfristige Käufe großer Werte wie Bitcoin oder Ethereum ist eine CEX mit niedrigen Gebühren meist einfacher – vergleichen Sie die Optionen auf unserer [Börsen-Seite]({lang}/exchanges/).

Wenn Sie Memecoins und andere On-Chain-Token ausprobieren möchten, beginnen Sie mit winzigen Beträgen, einer separaten Wallet und den etabliertesten Coins auf unserer [Memecoin-Seite]({lang}/memes/). Unsere Schritt-für-Schritt-Anleitung [Memecoin auf Solana kaufen]({lang}/blog/how-to-buy-memecoins-on-solana/) zeigt den ganzen Ablauf, einschließlich Tools wie [GMGN](/go/gmgn?from=blog&l=de).

## Wichtige DEX-Begriffe

- **Swap** – Tausch eines Tokens gegen einen anderen.
- **Paar** – die zwei Token in einem Pool, etwa SOL/USDC.
- **Slippage-Toleranz** – die maximale Preisänderung, die Sie akzeptieren.
- **Approve (Freigabe)** – Erlaubnis für einen Kontrakt, einen Token aus Ihrer Wallet zu bewegen (vor allem auf Ethereum-ähnlichen Chains). Widerrufen Sie alte Freigaben, die Sie nicht mehr brauchen.
- **Aggregator** – ein Dienst, der Ihren Trade für einen besseren Preis auf mehrere DEXs aufteilt, etwa Jupiter auf Solana oder 1inch auf Ethereum.

## FAQ

### Ist eine DEX sicherer als eine CEX?

Sie beseitigt das Risiko, dass die Börse Ihr Geld verliert oder einfriert, fügt aber das Risiko eigener Fehler und von Betrugs-Token hinzu. Keine der beiden ist risikofrei.

### Brauche ich einen Ausweis, um eine DEX zu nutzen?

Meist nicht, da Sie aus Ihrer eigenen Wallet handeln. Örtliche Gesetze und Steuern gelten trotzdem für Sie.

### Warum ist mein DEX-Trade fehlgeschlagen?

Häufige Gründe: nicht genug native Coin für Gas, zu niedrige Slippage bei schnell steigendem oder fallendem Preis oder ein Token, der Verkäufe blockiert.

### Sind DEX-Trades steuerpflichtig?

In vielen Ländern ja – ein Tausch von einem Token in einen anderen kann als Verkauf gelten. Dokumentieren Sie Ihre Trades.

## Quellen

- [So funktioniert Uniswap (Uniswap-Dokumentation)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas und Gebühren (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Solana-Dokumentation: Gebührenstruktur](https://solana.com/docs/core/fees/fee-structure)

*Keine Anlageberatung. Diese Anleitung erklärt, wie DEXs funktionieren, und empfiehlt keine Plattform und keinen Token.*
