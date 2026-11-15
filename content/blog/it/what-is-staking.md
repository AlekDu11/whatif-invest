---
title: Cos'è lo staking di criptovalute ed è sicuro?
description: Lo staking crypto spiegato semplice: come funziona, i periodi di blocco, staking su exchange o on-chain e i rischi reali da valutare prima di fare staking.
date: 2026-11-16
category: guides
assets: eth, sol, ada, dot, atom
---
Lo **staking** consiste nel bloccare delle criptovalute per aiutare una blockchain a funzionare, ricevendo in cambio nuove monete come ricompensa. Spesso viene paragonato a un conto deposito, ma funziona in modo molto diverso e ha rischi tutti suoi.

Questa guida spiega come funziona lo staking, cosa significa "periodo di blocco", in cosa lo staking su un exchange è diverso da quello on-chain e cosa può andare storto.

## Come funziona lo staking

Molte blockchain moderne (Ethereum, Solana, Cardano, Polkadot, Cosmos e altre) usano un sistema chiamato **proof of stake** (prova di partecipazione). Invece di consumare elettricità per proteggere la rete (come fa il mining di Bitcoin), si affidano ai **validatori**: computer che verificano le transazioni e aggiungono nuovi blocchi.

Per diventare validatore devi mettere in gioco delle monete come garanzia di comportamento onesto. In pochi passaggi:

1. Blocchi (metti in staking) le monete sulla rete, gestendo tu stesso un validatore oppure delegandole a uno.
2. I validatori confermano le transazioni e producono i blocchi.
3. La rete paga ricompense in nuove monete, più una parte delle commissioni di transazione.
4. Se un validatore imbroglia o resta offline troppo a lungo, una parte dello stake può essere tagliata. Questo si chiama **slashing**.

Bitcoin non può essere messo in staking in questo modo, perché usa la proof of work. I prodotti che offrono "rendimento su Bitcoin" di solito sono prestiti o altri schemi, non staking.

## Da dove arrivano le ricompense dello staking

Le ricompense non sono soldi regalati. Arrivano soprattutto da:

- **Nuove monete** create dalla rete (inflazione dell'offerta),
- **Commissioni di transazione** pagate dagli utenti.

Questo conta: se una rete crea nuove monete al 5% l'anno, per esempio, e tu guadagni il 5%, in sostanza stai solo mantenendo la tua quota della rete, non ti stai arricchendo. Inoltre le ricompense sono pagate nella moneta stessa: se il suo prezzo scende, il valore totale può comunque calare in modo pesante.

I tassi di ricompensa cambiano di continuo in base al numero di partecipanti e alle regole della rete. Considera qualsiasi percentuale pubblicizzata come una fotografia del momento, non come una promessa.

## Blocco e unbonding: quando puoi riavere le monete

Fare staking di solito significa che le monete non sono disponibili subito. Ogni rete ha le sue regole:

- **Ethereum**: i prelievi sono possibili dall'aggiornamento "Shapella" del 2023, ma l'uscita passa da una coda che può durare da qualche giorno a diverse settimane quando molte persone escono insieme.
- **Solana**: l'unstaking diventa effettivo alla fine di una "epoch", di solito un paio di giorni.
- **Cosmos e Polkadot**: periodi di "unbonding" di diverse settimane, durante i quali le monete non rendono nulla e non si possono vendere.
- **Cardano**: le monete restano nel tuo wallet e non sono bloccate affatto.

Perché è importante: se il mercato crolla durante il periodo di unbonding, non puoi vendere. Controlla sempre le regole esatte e aggiornate della moneta prima di fare staking.

## Staking su exchange o staking on-chain

I risparmiatori comuni fanno staking in due modi principali.

### Staking su un exchange (custodial)

Premi "Stake" o "Earn" nell'app di un exchange e lui si occupa della parte tecnica.

- ✅ Facilissimo, vanno bene anche piccole cifre, nessun wallet da configurare.
- ❌ Le monete le tiene l'exchange. Se fallisce, subisce un attacco o blocca i prelievi, le tue monete sono a rischio.
- ❌ L'exchange trattiene una parte delle ricompense come commissione.
- ❌ Alcuni prodotti "earn" sono in realtà prestiti, non staking: un rischio molto diverso.

Le autorità di vigilanza hanno esaminato da vicino questi servizi. Nel 2023 la SEC statunitense ha contestato a Kraken il suo programma di staking; Kraken ha pagato 30 milioni di dollari e ha chiuso il servizio per i clienti USA. Nel 2025 lo staff della SEC ha dichiarato che alcune forme di "protocol staking" diretto non sono operazioni su strumenti finanziari (securities). Le regole cambiano da Paese a Paese e continuano a evolvere.

### Staking on-chain (non custodial)

Tieni le monete nel tuo wallet e le deleghi a un validatore, oppure gestisci tu stesso un validatore.

- ✅ Le chiavi sono tue: nessuno può bloccarti il conto.
- ✅ Commissioni di solito più basse.
- ❌ Più tecnico: indirizzi sbagliati, phishing e validatori inaffidabili sono un problema tuo.
- ❌ Gestire un proprio validatore Ethereum richiede 32 ETH e hardware affidabile.

### Liquid staking

Una via di mezzo: fai staking tramite un protocollo e ricevi un token che rappresenta le monete in staking (per esempio un token "staked ETH"). Puoi scambiarlo mentre le tue monete maturano ricompense. Il prezzo da pagare è un **rischio di smart contract** in più e la possibilità che il token venga scambiato sotto il valore delle monete sottostanti.

## I principali rischi dello staking

Lo staking è sicuro? È meno rischioso di molti prodotti cripto "ad alto rendimento", ma non è mai privo di rischi:

1. **Rischio di prezzo.** Il più grande. Una ricompensa di qualche punto percentuale conta poco se la moneta perde il 50%. Guarda quanto sono volatili le monete sulla [pagina di Ethereum]({lang}/eth/) o sulla [pagina di Solana]({lang}/sol/).
2. **Rischio di blocco.** Potresti non riuscire a vendere durante un crollo.
3. **Rischio piattaforma.** Exchange e piattaforme di prestito possono fallire. Quando Celsius è crollata nel 2022, gli utenti del suo programma "earn" hanno perso l'accesso alle proprie monete.
4. **Slashing.** Un validatore che si comporta male può perdere una parte dello stake, comprese le monete delegate su alcune reti.
5. **Rischio di smart contract** nel liquid staking e nella DeFi.
6. **Tasse.** In molti Paesi le ricompense dello staking sono reddito tassabile nel momento in cui le ricevi. Verifica le regole locali.
7. **Truffe.** Falsi siti di staking e offerte da "20% al mese garantito" sono diffusi. Leggi la nostra guida su [come evitare le truffe cripto]({lang}/blog/how-to-avoid-crypto-scams/).

## Una checklist prudente prima di fare staking

- Metti in staking solo monete che avevi già intenzione di tenere a lungo.
- Controlla il periodo di unbonding e se potresti aver bisogno del denaro prima.
- Capisci chi custodisce le monete: tu o una piattaforma.
- Confronta le commissioni: quale quota delle ricompense trattiene la piattaforma?
- Evita le offerte con rendimenti fissi molto alti: le vere ricompense dello staking variano.
- Inizia con poco e prova un prelievo.

Lo staking non cambia la domanda principale: la moneta in sé rientra nel tuo piano di lungo periodo? Un piano di accumulo (PAC/DCA) dipende dal prezzo dell'asset negli anni: provalo con il nostro [calcolatore DCA]({lang}/compare/). Ecco come sarebbero andati 10 $ al giorno in Ethereum in 5 anni, senza alcuna ricompensa da staking: {{dca:eth:5}} a fronte di {{dcainv:5}} investiti ({{dcaroi:eth:5}}).

{{card:eth}}
{{card:sol}}

## Domande frequenti

### Lo staking è come ricevere interessi?

No. Gli interessi arrivano da chi prende in prestito; le ricompense dello staking arrivano dalla rete stessa, in cambio dell'aiuto a renderla sicura. Sono pagate nella moneta, quindi il loro valore segue il prezzo.

### Si possono perdere soldi con lo staking?

Sì. Il prezzo della moneta può scendere, una piattaforma può fallire e, in rari casi, lo slashing può tagliare il tuo stake. Le ricompense non ti proteggono da un calo del prezzo.

### Posso fare staking di Bitcoin?

Non in modo nativo, perché Bitcoin usa la proof of work. Le offerte di "rendimento su Bitcoin" di solito sono prestiti o altri prodotti con rischi diversi.

### Meglio lo staking su exchange o dal wallet?

Lo staking su exchange è più semplice; quello dal wallet ti lascia il controllo delle chiavi. La scelta giusta dipende da quanto ti senti a tuo agio nel gestire un wallet: leggi la nostra guida ai [wallet hot e cold]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Fonti

- [ethereum.org — Staking su Ethereum](https://ethereum.org/en/staking/)
- [ethereum.org — Prelievi dallo staking](https://ethereum.org/en/staking/withdrawals/)
- [Solana — Staking](https://solana.com/staking)
- [SEC USA — Kraken chiude il programma di staking e paga 30 milioni di dollari (2023)](https://www.sec.gov/news/press-release/2023-25)
- [Skadden — SEC: alcune attività di protocol staking non sono operazioni su securities (2025)](https://www.skadden.com/insights/publications/2025/06/sec-certain-protocol-staking-activities-are-not-securities-transactions)

*Non è un consiglio di investimento. Questa guida spiega come funziona lo staking e non raccomanda alcuna moneta, piattaforma o validatore.*
