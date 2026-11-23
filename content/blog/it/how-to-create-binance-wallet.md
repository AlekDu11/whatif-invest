---
title: Come creare un Binance Wallet e comprare una memecoin: passo dopo passo
description: Crea il Binance Wallet nell'app Binance, fai il backup, sposta le monete dal tuo account, trova il token dal contratto e fai lo swap in sicurezza.
date: 2026-11-23T12:30:00Z
category: learn
track: memes
step: 5
assets: bnb, sol, doge
stat: 3
stat_label: parti della chiave proteggono un Binance Wallet: ne servono 2 per entrare
---
**Come si crea un Binance Wallet?** Apri l'app Binance, passa alla scheda **Wallet** in alto, tocca **Create Keyless Wallet** (crea wallet senza chiave) e fai il backup con una password di recupero. Ci vogliono pochi minuti, non serve nessuna seed phrase e ottieni un wallet in autocustodia (un wallet in cui sei tu, non l'exchange, a controllare le monete) per comprare token on-chain come le memecoin.

> **In sintesi**
> - Il Binance Wallet vive dentro l'app Binance. Ti serve un account Binance verificato, ma le monete nel wallet sono in autocustodia: il backup è una tua responsabilità.
> - È un wallet "keyless" (MPC): la chiave è divisa in 3 parti, sul tuo telefono, nel tuo backup in cloud e presso Binance. Ne bastano 2 qualsiasi per aprire il wallet.
> - Non saltare mai il backup. Se perdi il telefono **e** dimentichi la password di recupero, Binance non può ripristinare il wallet.

Prima di iniziare: la maggior parte delle nuove memecoin perde quasi tutto il suo valore. Usa solo soldi che puoi permetterti di perdere del tutto. Leggi [cosa sono le memecoin]({lang}/blog/what-are-memecoins/).

## Cosa ti serve

- Un telefono con l'app ufficiale Binance (scaricala solo da App Store, Google Play o binance.com: le app false sono comuni).
- Un account Binance con la verifica dell'identità (KYC, cioè mostrare un documento) completata. Se non ce l'hai ancora, puoi registrarti con il nostro link: [Binance Wallet](/go/binance-web3?from=learn&l=it).
- Un po' di BNB o SOL nel tuo account Binance, per comprare e per pagare le commissioni di rete.

## Passo 1 — Apri il wallet

1. Accedi all'app Binance.
2. In alto nello schermo, passa da **Exchange** a **Wallet**.
3. Tocca **Create Keyless Wallet**. (Se hai già un altro wallet, l'altra opzione è **Import Wallet** (importa wallet): a chi inizia non serve.)

La creazione richiede pochi secondi. L'app non ti mostra 12 o 24 parole della seed phrase: usa invece l'MPC (multi-party computation, calcolo a più parti: la chiave è divisa in pezzi che non stanno mai nello stesso posto).

## Passo 2 — Fai il backup (non saltarlo)

L'app offre tre modi per salvare la tua parte di backup. Scegline uno:

- **iCloud o Google Drive.** Imposti una **password di recupero** che conosci solo tu. La parte viene cifrata con questa password e salvata nel tuo cloud.
- **Codice QR.** Imposti una password di recupero e salvi un codice QR; la parte viene conservata in un cloud decentralizzato.
- **Quick Backup** (backup rapido). Confermi con Face ID o impronta digitale; nessuna password, ma la parte è custodita da un fornitore esterno.

Scrivi la password di recupero su carta e conservala in un posto sicuro. Poi controlla: tocca **Settings** (impostazioni, in alto a sinistra in Home o Assets) → **Wallet Management** (gestione wallet). Devi vedere l'etichetta **Backed Up** (backup fatto).

## Passo 3 — Sposta le monete da Binance al wallet

1. Nel wallet, tocca **Receive** (ricevi) → **Withdraw from Binance Exchange** (preleva dall'exchange Binance).
2. Scegli la moneta (per esempio BNB) **e la rete** (BNB Smart Chain per BNB, Solana per SOL). La rete deve corrispondere.
3. Inserisci l'importo. L'app mostra la commissione e l'importo finale prima della conferma.
4. Scegli se i soldi arrivano dal conto Spot o Funding, tocca **Withdraw** (preleva), controlla indirizzo e rete, poi **Confirm** (conferma).

Inizia con un piccolo importo di prova. Un trasferimento confermato non si può annullare. Lascia sempre un po' di BNB o SOL nel wallet: ogni azione sulla blockchain costa una commissione di rete (gas), anche se fallisce.

## Passo 4 — Trova il token giusto dal suo indirizzo del contratto

Molte memecoin hanno copie con lo stesso nome e lo stesso logo. L'unico identificativo affidabile è l'**indirizzo del contratto** (una lunga stringa di lettere e numeri, unica per ogni token).

1. Prendi l'indirizzo da una fonte affidabile: l'account verificato del progetto, un grande sito di dati o la pagina del token nella nostra [pagina delle memecoin]({lang}/memes/).
2. Nella schermata **Markets** (mercati) o **Trade** (fai trading) del wallet, incolla l'indirizzo nella ricerca invece di scrivere il nome.
3. Confronta i primi e gli ultimi 4–6 caratteri con la tua fonte.

## Passo 5 — Controlla il token prima di comprare

Nella nostra [pagina delle memecoin]({lang}/memes/), ogni pagina di token mostra il controllo di sicurezza di Binance e i numeri chiave. Guarda:

- **Liquidità**: quanti soldi ci sono nel pool di scambio. Poca liquidità = potresti non riuscire a vendere.
- **Holder e quota dei primi 10**: se pochi wallet hanno quasi tutta l'offerta, possono far crollare il prezzo.
- **Età**: un token creato un'ora fa è un biglietto della lotteria.
- **Avvisi**: se compare un qualsiasi avviso di rischio o di sicurezza, fermati.

Binance stessa dice di non controllare i token elencati su **Meme Rush** (il suo flusso di memecoin appena nate), quindi il controllo spetta a te. La nostra [lezione su truffe e rug pull]({lang}/blog/memecoin-scams-rug-pull/) elenca i segnali di allarme.

## Passo 6 — Fai lo swap

1. Apri **Trade** → **Swap** (scambia). Scegli con cosa paghi (BNB) e il token che vuoi, sulla stessa rete.
2. Inserisci un importo piccolo. Leggi il tasso, lo **slippage** (la variazione di prezzo massima che accetti prima che l'operazione fallisca) e la commissione di rete.
3. Alcuni token richiedono prima un passaggio **Approve** (approva); costa una piccola commissione.
4. Tocca **Swap** e conferma con la tua passkey o la 2FA.

Per vendere, fai lo stesso al contrario. Se vuoi vedere i token più nuovi in assoluto, la scheda Markets ha **Meme Rush**: lì i token appena nati si scambiano su una "bonding curve" e non si possono spostare fuori dal wallet finché non "migrano" su un DEX normale (exchange decentralizzato). È l'angolo più rischioso del mercato.

> **⚠️ Attenzione**
> - **Nessun backup, o password salvata negli screenshot.** Perdi telefono e password e le monete sono perse per sempre.
> - **Rete sbagliata o indirizzo sbagliato.** Le FAQ di Binance dicono che i token inviati a un indirizzo sbagliato non possono essere rimborsati. Invia sempre un importo di prova.
> - **Token falsi e messaggi del "supporto".** Cerca solo per indirizzo del contratto. Il personale Binance non ti chiederà mai la password di recupero né di "verificare" il wallet su un sito.

Prossima lezione: come collegare il Binance Wallet a un sito DEX e riportare le monete su Binance. Trovi tutte le lezioni nella [pagina Impara]({lang}/learn/).

## Fonti

- [Binance: Frequently Asked Questions on Binance Wallet](https://www.binance.com/en/support/faq/5a3fc86a702b43e1a4a398ebd8853b77)
- [Binance: What Is a Keyless Wallet and Why Do I Need to Back It Up?](https://www.binance.com/en/support/faq/4efebcb9a937417ca31baa2f7754c50f)
- [Binance: How to Back Up My Binance Wallet?](https://www.binance.com/en/support/faq/53521dedad474c908ec3761a935cb8d6)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance: What Is Binance Wallet Swap?](https://www.binance.com/en/support/faq/7ebe19e8ff884cc09a9dbb064aff131f)
- [Binance: Introducing Meme Rush — Fair Mode (9 Oct 2025)](https://www.binance.com/en/support/announcement/detail/c21eac66543c4a62b8b6868cb01ba4f3)

*Non è un consiglio di investimento. Le memecoin sono estremamente rischiose; questa guida spiega come funziona l'app e non raccomanda di comprare alcun token. Il Binance Wallet potrebbe non essere disponibile in tutti i paesi.*
