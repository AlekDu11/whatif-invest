---
title: The Graph (GRT) spiegato semplice: protocollo di indicizzazione dei dati blockchain, attivo dal 2020 su Ethereum e Arbitrum
description: The Graph in parole semplici: come gli indexer trasformano i dati blockchain in query veloci, a cosa serve GRT, staking, delega, la storia e i rischi.
date: 2026-11-25
kind: analysis
---
**The Graph** viene spesso definito "il Google delle blockchain": organizza i dati grezzi delle blockchain in modo che le app trovino ciò che serve in pochi millisecondi. Wallet, exchange e app DeFi lo usano per mostrare saldi, scambi e prezzi senza gestire propri server di dati. Il suo token **GRT** paga questo lavoro e protegge la rete; oggi vale {{mcap:grt}} ({{rank:grt}} tra le criptovalute).

> **In sintesi**
> - La rete è partita a dicembre 2020 con 10 miliardi di GRT; ogni anno vengono emessi nuovi token come ricompense, quindi non c'è un tetto fisso.
> - Il massimo storico è {{ath:grt}} ({{athd:grt}}); oggi il prezzo è {{fromath:grt}} da lì.
> - GRT è un token di lavoro (work token): gli indexer devono metterlo in staking per servire i dati e le app ci pagano le commissioni sulle query.
> - È una scommessa sulla domanda di dati blockchain, non una moneta: utilizzo e prezzo sono andati spesso in direzioni diverse.

## Come funziona

Leggere i dati direttamente da una blockchain è lento e scomodo. Su The Graph gli sviluppatori descrivono i dati che servono loro in un "subgraph" aperto, per esempio ogni scambio su un exchange decentralizzato. Gli **indexer** — operatori indipendenti che gestiscono server — elaborano questi subgraph e rispondono alle query delle app, guadagnando commissioni e GRT di nuova emissione. I **curator** segnalano quali subgraph vale la pena indicizzare, mentre i **delegator** affidano i propri GRT a indexer di fiducia in cambio di una parte delle ricompense. Gli indexer che forniscono dati sbagliati possono perdere parte della quota in staking ("slashing"). Oggi The Graph supporta decine di blockchain e dal 2024 ricompense e pagamenti girano su Arbitrum, un layer 2 di Ethereum, per contenere i costi. Nel 2025 il progetto ha iniziato a introdurre **Horizon**, un aggiornamento che permette allo stesso sistema di staking di proteggere nuovi tipi di servizi di dati.

## A cosa serve il token

GRT ha tre funzioni. Gli indexer devono metterlo in staking prima di poter lavorare, il che blocca una grossa parte dell'offerta. Le app pagano le query in GRT (spesso convertito in automatico da stablecoin o pagamenti con carta). E i possessori possono delegarlo per ricevere una parte delle ricompense senza gestire un server. Una piccola quota delle commissioni sulle query e delle tasse di staking viene bruciata, mentre la nuova emissione, circa il 3% all'anno, va a indexer e delegator. Che GRT si apprezzi dipende dal fatto che la domanda pagante di dati cresca più in fretta della nuova offerta.

## I numeri di oggi

- Prezzo oggi: {{price:grt}}
- Massimo storico: {{ath:grt}} ({{athd:grt}}), {{fromath:grt}} da lì
- Valore di mercato: {{mcap:grt}} ({{rank:grt}} tra le criptovalute)
- Variazione del prezzo in 12 mesi: {{chg1y:grt}}
- 10 $ al giorno per 5 anni: {{dca:grt:5}} con {{dcainv:5}} investiti ({{dcaroi:grt:5}})

## La sua storia

The Graph è stato avviato nel 2018 da Yaniv Tal, Brandon Ramirez e Jannis Pohlmann, la cui società ha poi preso il nome di Edge & Node. Per anni ha gestito un "servizio ospitato" (hosted service) gratuito su cui si appoggiavano molte app di Ethereum. La rete decentralizzata e il token GRT sono partiti il 17 dicembre 2020 e, durante il boom delle cripto, GRT è salito a circa 2,84 $ a febbraio 2021. Poi ha perso oltre il 90% tra il 2021 e il 2022. Nel 2023 e nel 2024 il progetto ha spostato le ricompense su Arbitrum e a giugno 2024 ha chiuso il servizio ospitato, portando tutti gli utenti sulla rete a pagamento. Il rally dei token legati all'IA di inizio 2024 ha sostenuto GRT per un po', ma in seguito il prezzo è sceso a nuovi minimi.

## Alternative

The Graph compete con società e protocolli di indicizzazione come Goldsky, SubQuery e Covalent, e con le API di dati blockchain di Alchemy e QuickNode, che molti sviluppatori trovano più semplici. Alcune grandi app gestiscono semplicemente i propri indexer. Tra i token legati ai dati blockchain, [Chainlink]({lang}/link/) e [Pyth Network]({lang}/pyth/) vengono spesso paragonati a GRT, anche se forniscono feed di prezzo agli smart contract invece della ricerca sui dati passati.

## Rischi principali

- **Nuova offerta:** l'emissione annuale aggiunge nuovi GRT e gli indexer vendono spesso le ricompense per coprire i costi dei server.
- **Legame debole con l'utilizzo:** le commissioni sulle query sono da tempo piccole rispetto alle ricompense, quindi un uso intenso da solo non fa salire il prezzo.
- **Concorrenza:** i fornitori di dati centralizzati sono veloci ed economici, e le app possono passare a loro con facilità.
- **Dipendenza da una sola società:** Edge & Node e The Graph Foundation guidano ancora gran parte dello sviluppo.
- **Regolamentazione:** le regole sui token di staking e sulle relative ricompense cambiano da paese a paese e possono evolvere.

## Cosa significa se compri con regolarità

GRT ha passato gran parte della sua vita molto al di sotto del picco del 2021, quindi chi comprava con regolarità ha accumulato sempre più token a prezzi più bassi: questo ripaga solo se il prezzo si riprende. Comprare un importo fisso a intervalli regolari distribuisce il rischio di sbagliare il momento, ma non elimina il rischio di perdite. Molti tengono token di questo tipo solo come una piccola parte dei risparmi. I risultati passati non garantiscono quelli futuri.

*Non è una consulenza finanziaria.*

## Fonti

- [Che cos'è The Graph (documentazione The Graph)](https://thegraph.com/docs/en/about/)
- [Guida all'implementazione di Horizon: cosa cambia per i partecipanti alla rete (blog The Graph)](https://thegraph.com/blog/horizon-implementation-guide/)
- [The Graph: prezzo, capitalizzazione e massimo storico (CoinGecko)](https://www.coingecko.com/en/coins/the-graph)
