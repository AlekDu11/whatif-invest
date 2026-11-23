---
title: Come collegare Binance Wallet a un DEX e riportare le monete: passo dopo passo
description: Collega Binance Wallet a un DEX in sicurezza, rimanda le monete al tuo conto Binance sulla rete giusta e rimuovi le vecchie autorizzazioni, passo dopo passo.
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: piccolo trasferimento di prova prima di ogni nuovo indirizzo o rete
---
**Come si collega Binance Wallet a un DEX?** Apri il sito ufficiale del DEX, premi **Connect Wallet** (collega wallet), scegli Binance Wallet (oppure WalletConnect e scansiona il QR code con l'app Binance) e conferma nell'app. Per riportare le monete, copia il tuo **indirizzo di deposito** Binance per la stessa moneta e la stessa rete, poi invia dal wallet — prima un piccolo importo di prova.

> **In sintesi**
> - Un DEX (exchange decentralizzato — un sito dove scambi token direttamente dal tuo wallet) non ha mai bisogno della tua password di recupero né della seed phrase. Il collegamento permette al sito solo di *chiederti* una firma; non si muove nulla finché non confermi.
> - La rete deve coincidere da entrambe le parti (BNB Smart Chain con BNB Smart Chain, Solana con Solana). Una rete o un indirizzo sbagliati possono far perdere le monete.
> - Ogni «Approve» permette a un sito di spendere un token al posto tuo. Dai autorizzazioni piccole e rimuovi quelle che non usi più.

Questa lezione continua [Come creare un Binance Wallet]({lang}/blog/how-to-create-binance-wallet/). Le memecoin sono estremamente rischiose: usa solo soldi che puoi permetterti di perdere.

## Passo 1 — Apri il sito vero

I siti DEX falsi con lo stesso logo sono una delle trappole più comuni.

1. Scrivi l'indirizzo a mano o usa un preferito. Non cliccare sugli annunci nei risultati di ricerca né sui link nelle chat.
2. Controlla la barra degli indirizzi lettera per lettera.
3. Verifica che il DEX funzioni sulla rete in cui si trovano le tue monete.

## Passo 2 — Collega il wallet

Ci sono tre modi, a seconda del dispositivo:

- **Su computer con l'estensione Binance Wallet per il browser** (Chrome o Brave). Accedi all'estensione scansionando il suo QR code con l'app Binance. Poi sul DEX premi **Connect** o **Connect Wallet**, scegli Binance Wallet e conferma la finestra che compare.
- **Su computer senza estensione.** Sul DEX premi **Connect Wallet → WalletConnect**. Compare un QR code. Scansionalo con lo scanner dell'app Binance e tocca **Connect**.
- **Sul telefono.** Apri il DEX nel browser del telefono, premi **Connect Wallet**, scegli Binance Wallet dalla lista e conferma nell'app.

Prima di confermare, leggi la finestra: il nome del sito, l'indirizzo e la rete. Se qualcosa non torna, premi Cancel (annulla).

## Passo 3 — Fai lo swap e leggi ogni firma

1. Scegli la moneta con cui paghi e il token che vuoi (cerca il token per **indirizzo del contratto**, non per nome).
2. Inserisci un piccolo importo e controlla il tasso, lo slippage (la massima variazione di prezzo che accetti) e la commissione di rete.
3. La prima volta che vendi un token, il sito chiede **Approve** (il permesso di spendere quel token). Se l'app lo consente, imposta un importo invece di «illimitato».
4. Conferma lo swap nell'app. Se una richiesta di firma è una pagina di codice illeggibile o non ha senso — **non firmarla**.

## Passo 4 — Rimanda le monete al tuo conto Binance

1. Nell'app Binance passa a **Exchange** → **Assets** (asset) → **Deposit** (deposita). Scegli la moneta (per esempio BNB).
2. Scegli la **rete** (per esempio BNB Smart Chain). Copia l'indirizzo di deposito. Alcune monete richiedono anche un **memo/tag** — copia anche quello.
3. Passa a **Wallet** → **Send** (invia). Scegli la stessa moneta e la stessa rete. Incolla l'indirizzo (e il memo, se c'è).
4. Invia prima un piccolo importo di prova. Quando arriva sul tuo conto Binance, invia il resto.

Tieni un po' di BNB o SOL nel wallet: ogni azione on-chain, anche fallita, costa una commissione di rete. Alcune memecoin non si possono proprio depositare sull'exchange (perché non le quota) — per incassare, scambiale prima in BNB, SOL o USDT nel wallet.

## Passo 5 — Scollega e fai pulizia

1. Quando hai finito, scollega il sito (nelle impostazioni dei siti collegati o di WalletConnect del wallet, oppure con il pulsante **Disconnect** del DEX).
2. Ogni tanto controlla le autorizzazioni dei token e revoca (annulla) quelle che non ti servono. Una revoca costa una piccola commissione.
3. Su un computer condiviso, esci dall'estensione.

Puoi seguire i token comprati nel [tuo portafoglio]({lang}/me/) e vedere i dati delle memecoin in tempo reale sulla nostra [pagina memecoin]({lang}/memes/).

> **⚠️ Attenzione**
> - **Un sito o un «supporto» ti chiede la password di recupero, la seed phrase o una «sincronizzazione del wallet».** Nessun vero DEX o dipendente Binance lo fa mai. Chiudi la pagina.
> - **Autorizzazioni illimitate e firme alla cieca.** Un'autorizzazione o una firma malevola può permettere a un truffatore di svuotare quel token più tardi, senza un'altra tua conferma.
> - **Rete sbagliata, memo dimenticato o indirizzo incollato che è cambiato.** Un malware può sostituire un indirizzo copiato. Confronta ogni volta i primi e gli ultimi caratteri e fai una prova con un piccolo importo.

Prossima lezione: come controllare una memecoin prima di comprarla. Tutte le lezioni sono nella [pagina Impara]({lang}/learn/).

## Fonti

- [Binance: What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy: How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US: How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*Non è un consiglio di investimento. Questa guida spiega come funzionano gli strumenti e non raccomanda di comprare alcun token. Il Binance Wallet potrebbe non essere disponibile in tutti i paesi.*
