---
title: Come controllare una memecoin prima di comprarla: 6 controlli in 5 minuti
description: Prima di comprare una memecoin controlla contratto, liquidità, holder, quota della top 10, età e l'audit di sicurezza Binance. Una checklist semplice.
date: 2026-11-23T16:30:00Z
category: learn
track: memes
step: 6
assets: sol, bnb, doge
stat: 6
stat_label: controlli prima di comprare qualsiasi memecoin
---
**Come si controlla una memecoin prima di comprarla?** Trova il token tramite il suo indirizzo di contratto, poi controlla sei cose: l'audit di sicurezza, la liquidità, il numero di holder, quanto possiedono i 10 wallet più grandi, da quanto tempo esiste e se il creatore può ancora modificarlo. Se anche un solo controllo è rosso, lascia perdere quella moneta. Ce ne sono migliaia di altre.

> **In sintesi**
> - Questi controlli non rendono sicura una memecoin. Ti aiutano solo a evitare le trappole più evidenti: token che non puoi vendere, copie false e monete che pochi wallet possono far crollare.
> - La scheda **Audit** di Binance Wallet controlla i rischi del contratto, del trading e di truffa (per esempio un «honeypot»: un token che puoi comprare ma non vendere mai). Binance stessa dice che l'audit non è infallibile.
> - Sulla nostra [pagina memecoin]({lang}/memes/) il filtro qualità è attivo di default: «Solo qualità: liquidità da 100K $, da 1 giorno».

Questa lezione continua [Come collegare Binance Wallet a un DEX]({lang}/blog/connect-binance-wallet-to-dex/). Le memecoin sono estremamente rischiose: usa solo soldi che puoi permetterti di perdere.

## Passo 1 — Trova l'indirizzo di contratto giusto

Ogni token ha un **indirizzo di contratto** (il suo codice unico sulla blockchain, una lunga stringa di lettere e numeri). Chiunque può creare un token con lo stesso nome e lo stesso logo, quindi il nome non significa nulla.

1. Copia l'indirizzo dall'account ufficiale del progetto o da un sito di dati affidabile.
2. Incollalo nella ricerca del tuo wallet. Confronta i primi e gli ultimi 4 caratteri.
3. Se vedi più token con lo stesso nome, gli altri sono copie.

## Passo 2 — Apri l'audit di sicurezza

Nell'app Binance apri il token in **Wallet** e tocca la scheda **Audit** (sul sito: clicca sul token, poi su **Audit**). Nelle pagine dei token della nostra sezione memecoin vedi lo stesso controllo come **Controllo di sicurezza Binance: Rischio basso / Rischio medio / Rischio alto**.

Guarda tre gruppi:

- **Contract risk** (rischio del contratto): il creatore può bloccare le vendite, mettere wallet in una lista nera, cambiare la tassa o cambiare i saldi?
- **Trading risk** (rischio di trading): rischio honeypot, tassa strana su acquisto o vendita (una commissione trattenuta a ogni operazione), poca liquidità, rischio di rug pull.
- **Scam risk** (rischio di truffa): token falso, truffa nota, spam.

Qualsiasi voce rossa = non comprare. Anche «Rischio basso» non significa sicuro: il creatore può ancora fare qualcosa dopo il tuo acquisto.

## Passo 3 — Controlla la liquidità

La liquidità sono i soldi nel pool di scambio che ti permettono di vendere. Se è minuscola, anche una piccola vendita fa crollare il prezzo, e il creatore può ritirarla (un rug pull, «tirare via il tappeto»). Su WhatIfStack il nostro filtro predefinito nasconde i token con meno di 100K $ di liquidità. Controlla anche se la liquidità del pool è bloccata o bruciata (eliminata per sempre), se il sito di dati lo mostra.

## Passo 4 — Conta gli holder e la quota della top 10

Nella pagina del token guarda **Holder** (quanti wallet lo possiedono) e **Top 10 detengono** (che quota di tutte le monete hanno i 10 wallet più grandi). Poche centinaia di holder e una top 10 molto pesante significano che un pugno di persone può vendere e far crollare il prezzo. Attenzione: anche gli indirizzi del pool e di burn compaiono nella top 10, ed è normale.

## Passo 5 — Controlla l'età

La maggior parte dei token truffa vive ore o giorni. Un token con meno di un giorno di vita non ha alcuna storia. Il nostro filtro su /memes/ mostra solo token con almeno 1 giorno. Più vecchio non vuol dire sicuro, solo meno sconosciuto.

## Passo 6 — Su Solana: il creatore può ancora modificare il token?

Su Solana contano due impostazioni:

- **Mint authority** (diritto di emissione): il diritto di creare nuovi token. Se è ancora attivo, il creatore può stamparne altri e la tua quota si riduce.
- **Freeze authority** (diritto di congelamento): il diritto di congelare un wallet. Se è ancora attivo, il creatore potrebbe impedirti di spostare o vendere.

Lo stato più sicuro è «revoked» o «disabled» (nessuno ha quel diritto). Li vedi entrambi nella pagina del token su un block explorer come Solscan.

> **⚠️ Attenzione**
> - **Una copia falsa con lo stesso nome.** Compra sempre tramite l'indirizzo di contratto, mai in base a nome o logo.
> - **Un honeypot.** Puoi comprare, il grafico sale, ma nessuno riesce a vendere. Uno storico con acquisti e nessuna vendita è un campanello d'allarme.
> - **Fidarsi di un solo semaforo verde.** Un audit, tanti holder o un nome famoso non ti proteggono se il prezzo semplicemente scende: la maggior parte delle memecoin finisce vicino a zero.

## Cosa significa se compri regolarmente

I piccoli acquisti regolari funzionano meglio con asset che probabilmente esisteranno ancora tra cinque anni. La maggior parte delle memecoin non è così. Se vuoi comunque provarne una, limitati a una cifra minuscola e fissa e seguila accanto al resto dei tuoi soldi nel [tuo portafoglio]({lang}/me/).

Prossima lezione: la storia di Dogecoin. Tutte le lezioni sono nella [pagina Impara]({lang}/learn/).

## Fonti

- [Binance: How to Use the Token Audit Feature in Binance Wallet](https://www.binance.com/en/support/faq/detail/fd1b21bac5114feda49dd185461afdda)
- [Binance.US: What is a honeypot scam?](https://support.binance.us/en/articles/15388146-what-is-a-honeypot-scam)
- [Solana docs: Set authority (mint and freeze authority)](https://solana.com/docs/tokens/basics/set-authority)
- [Solana docs: Freeze account](https://solana.com/docs/tokens/basics/freeze-account)

*Non è un consiglio di investimento. Questa guida spiega come controllare un token e non raccomanda di comprare alcuna moneta.*
