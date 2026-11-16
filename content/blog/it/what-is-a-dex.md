---
title: Cos'è un DEX e che differenza c'è con un exchange di criptovalute?
description: Cos'è un DEX? Guida semplice agli exchange decentralizzati: AMM, pool di liquidità, wallet, commissioni di gas e pro e contro rispetto a un CEX.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**Cos'è un DEX?** Un DEX (exchange decentralizzato) è un insieme di smart contract su una blockchain che ti permette di scambiare un token con un altro direttamente dal tuo wallet. Non c'è un'azienda che custodisce i tuoi soldi, non c'è un account e di solito non c'è verifica dell'identità. Uniswap su Ethereum, e Raydium, Orca e Meteora su Solana, sono esempi noti.

Un normale exchange di criptovalute come Binance, Coinbase o Kraken è un **CEX** (exchange centralizzato): un'azienda che custodisce i tuoi fondi, abbina acquirenti e venditori nel proprio sistema e deve rispettare le regole finanziarie.

## Come funziona un DEX

### Market maker automatici (AMM)

La maggior parte dei DEX non ha un order book con acquirenti e venditori. Usa invece un **market maker automatico** (AMM): una formula che stabilisce il prezzo.

La versione classica, usata da Uniswap v2, è la regola del "prodotto costante": un pool contiene due token, e la quantità del token A moltiplicata per la quantità del token B deve restare uguale dopo ogni scambio. Quando compri il token A, aggiungi token B al pool e togli token A, quindi A diventa più scarso nel pool e il suo prezzo sale.

Non devi fare i calcoli. L'idea chiave: **più grande è il pool, meno la tua operazione muove il prezzo.**

### Pool di liquidità

I token del pool arrivano dai **fornitori di liquidità**: persone che depositano coppie di token e guadagnano una parte delle commissioni di trading (spesso lo 0,05–1% per swap). Il loro rischio è che i prezzi dei due token si allontanino, cosa che può lasciarli in una situazione peggiore rispetto a tenere semplicemente i token ("impermanent loss").

Per i token appena lanciati, di solito è il creatore a creare il primo pool. Ecco perché il blocco della liquidità conta: chi controlla il pool può ritirarlo.

### Il tuo wallet è il tuo account

Per usare un DEX colleghi un wallet in autocustodia come MetaMask (Ethereum e reti simili) o Phantom (Solana). Ogni operazione è una transazione che firmi tu. La tua **seed phrase** è la chiave principale: se la perdi, i soldi spariscono; se la condividi, qualcun altro se li prende.

### Gas e commissioni

Ogni operazione su un DEX paga una commissione di rete, chiamata **gas** su Ethereum. Su Ethereum sale quando la rete è congestionata; le reti layer 2 e Solana di solito costano molto meno: la commissione base di Solana è di 0,000005 SOL per firma. Oltre al gas paghi la commissione del pool, e puoi subire **slippage** e **impatto sul prezzo** su token piccoli o che si muovono velocemente.

## DEX vs CEX: le differenze principali

- **Chi custodisce i fondi:** su un DEX tu (il tuo wallet); su un CEX l'exchange.
- **Account e verifica dell'identità:** un DEX di solito non chiede nulla; un CEX richiede la verifica dell'identità (KYC).
- **Scelta di token:** un DEX offre quasi qualsiasi token, anche quelli appena nati; un CEX quota solo token selezionati.
- **Comprare con carta o bonifico:** di solito non si può fare direttamente su un DEX; è la norma su un CEX.
- **Commissioni:** DEX, gas, commissione del pool e slippage; CEX, commissione di trading, spread e commissione di prelievo.
- **Aiuto se qualcosa va storto:** un DEX non ha un servizio clienti; un CEX ha l'assistenza e a volte sistemi di tutela.
- **Rischi principali:** DEX, token truffa, approvazioni pericolose e i tuoi stessi errori; CEX, attacchi hacker, blocchi dell'account e insolvenza.

## I vantaggi di un DEX

- **Autocustodia.** Nessuno può congelare il tuo account o perdere i tuoi soldi in un fallimento.
- **Accesso aperto.** Chiunque abbia un wallet può fare trading, da quasi ovunque.
- **Prima i nuovi token.** I token compaiono sui DEX molto prima di qualsiasi quotazione su un exchange (o al posto di essa).
- **Trasparenza.** Pool, operazioni e holder sono visibili sulla blockchain.

## Gli svantaggi di un DEX

- **La banca sei tu.** Un errore (un indirizzo sbagliato, un sito falso, un'approvazione malevola) e i fondi sono persi per sempre.
- **Token truffa.** Chiunque può creare un token e un pool in pochi minuti. La maggior parte dei nuovi token perde quasi tutto il suo valore; leggi la nostra [checklist anti rug pull]({lang}/blog/how-to-spot-a-rug-pull/).
- **Costi nascosti.** Slippage e impatto sul prezzo possono costare più della commissione visibile.
- **Nessun accesso facile.** Di solito devi prima comprare cripto su un CEX e poi inviarle al tuo wallet.
- **Rischio smart contract.** Bug o attacchi al codice dei DEX hanno causato grosse perdite.

## Quale dovrebbe usare un principiante?

Molti usano entrambi: un CEX autorizzato per passare dalla valuta locale alle cripto, e un DEX per i token disponibili solo on-chain. Per acquisti regolari e di lungo periodo di grandi asset come Bitcoin o Ethereum, un CEX con commissioni basse è di solito più semplice; confronta le opzioni sulla nostra [pagina degli exchange]({lang}/exchanges/).

Se vuoi esplorare le memecoin e altri token on-chain, inizia con importi minimi, un wallet separato e le monete più consolidate della nostra [pagina delle memecoin]({lang}/memes/). La nostra guida passo passo [come comprare una memecoin su Solana]({lang}/blog/how-to-buy-memecoins-on-solana/) mostra l'intero processo, compresi strumenti come [GMGN](/go/gmgn?from=blog&l=it).

## I termini più comuni dei DEX

- **Swap**: scambiare un token con un altro.
- **Coppia**: i due token di un pool, come SOL/USDC.
- **Tolleranza di slippage**: la variazione massima di prezzo che accetti.
- **Approve**: il permesso a un contratto di spostare un token dal tuo wallet (soprattutto sulle reti tipo Ethereum). Revoca le vecchie approvazioni che non ti servono più.
- **Aggregatore**: un servizio che divide la tua operazione tra più DEX per ottenere un prezzo migliore, come Jupiter su Solana o 1inch su Ethereum.

## Domande frequenti

### Un DEX è più sicuro di un CEX?

Elimina il rischio che l'exchange perda o congeli i tuoi fondi, ma aggiunge il rischio dei tuoi errori e dei token truffa. Nessuno dei due è privo di rischi.

### Serve un documento per usare un DEX?

Di solito no, perché operi dal tuo wallet. Le leggi e le tasse del tuo paese però valgono comunque per te.

### Perché la mia operazione sul DEX è fallita?

Motivi comuni: moneta nativa insufficiente per il gas, slippage troppo basso per un prezzo che si muove in fretta o un token che blocca le vendite.

### Le operazioni sui DEX si tassano?

In molti paesi sì: scambiare un token con un altro può valere come vendita. Tieni traccia delle tue operazioni.

## Fonti

- [Come funziona Uniswap (documentazione Uniswap)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas e commissioni (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Documentazione Solana: struttura delle commissioni](https://solana.com/docs/core/fees/fee-structure)

*Non è un consiglio di investimento. Questa guida spiega come funzionano i DEX e non raccomanda alcuna piattaforma né alcun token.*
