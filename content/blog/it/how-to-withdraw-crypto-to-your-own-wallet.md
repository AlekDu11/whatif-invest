---
title: Come prelevare crypto da un exchange al tuo wallet personale: passo per passo
description: Sposta le tue monete dall'exchange al tuo wallet in sicurezza: copia l'indirizzo giusto, scegli la stessa rete, aggiungi il memo se serve e fai un test.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 rete
stat_label: exchange e wallet devono usare la stessa, altrimenti le monete possono andare perse
---
**Come si prelevano crypto sul proprio wallet?** Nel tuo wallet copi il tuo **indirizzo di ricezione** per quella moneta. Poi, sull'exchange, apri **Withdraw** (Preleva), incolli l'indirizzo, scegli **la stessa rete** che usa il tuo wallet, inserisci un piccolo importo di prova e confermi con la 2FA. Quando la prova arriva, invii il resto.

> **In sintesi**
> - Tre cose devono coincidere: la **moneta**, l'**indirizzo** e la **rete** (la blockchain su cui viaggiano le monete, per esempio Ethereum, BNB Smart Chain, TRON o Solana). Binance avverte che le monete inviate sulla rete sbagliata possono andare perse per sempre.
> - Alcune monete (come XRP, XLM o ATOM) richiedono anche un **memo** o **tag** (un breve numero che dice a chi riceve di chi sono le monete). Senza, il trasferimento può bloccarsi o finire alla persona sbagliata.
> - **Fai sempre prima un piccolo test.** Un prelievo non si può annullare una volta che le monete hanno lasciato l'exchange.

Questa lezione segue [Come impostare un acquisto ricorrente]({lang}/blog/how-to-set-up-a-recurring-buy/). Perché potresti volere un wallet tuo è spiegato in [wallet caldi e freddi]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Prima di iniziare

Ti servono due cose. Un account su un exchange con delle monete, protetto con la 2FA: vedi [Come registrarsi su un exchange di criptovalute]({lang}/blog/how-to-register-on-a-crypto-exchange/). E la tua app di wallet già configurata, con la **seed phrase** (le 12 o 24 parole segrete che ripristinano il wallet) scritta su carta e conservata offline. Non digitare mai la seed phrase da nessun'altra parte: nessun exchange, sito o «assistenza» ne avrà mai bisogno.

## Passo 1 — Copia l'indirizzo di ricezione del tuo wallet

1. Apri l'app del wallet e tocca **Receive** (Ricevi; a volte **Deposit**).
2. Scegli la moneta, per esempio Bitcoin o USDT.
3. Se il wallet lo chiede, scegli la rete. Annota quale: per esempio «USDT su TRON (TRC20)» o «USDT su Ethereum (ERC20)».
4. Tocca **Copy** (Copia) accanto all'indirizzo. Non scriverlo a mano.

Un indirizzo è una lunga riga di lettere e numeri. Gli indirizzi Bitcoin spesso iniziano con **bc1**, quelli di Ethereum e BNB Smart Chain con **0x**, quelli di TRON con **T**.

## Passo 2 — Apri Withdraw sull'exchange

Nell'app di Binance il percorso è **Assets → Spot → Send → Withdraw Crypto**; sul sito è **Wallet → Overview → Withdraw**. Gli altri exchange hanno un pulsante **Withdraw** accanto a ogni moneta nella schermata del wallet o del portafoglio. Scegli la stessa moneta del passo 1.

## Passo 3 — Incolla l'indirizzo e scegli la rete

1. Incolla l'indirizzo nel campo **Address** (Indirizzo).
2. Confronta i **primi 4 e gli ultimi 4 caratteri** con il tuo wallet. Alcuni malware sostituiscono l'indirizzo copiato con quello del ladro.
3. Scegli la **rete**. Deve essere quella che il wallet ti ha mostrato al passo 1. Binance può proporti una rete in automatico: controllala comunque. Non scegliere una rete solo perché ha la commissione più bassa.
4. Se compare un campo **Memo** o **Tag** e il tuo wallet te ne ha dato uno, compilalo. Se il tuo wallet non mostra nessun memo, di solito non serve, ma verifica nelle pagine di aiuto del wallet.

Consiglio: se non sei sicuro, salva l'indirizzo in **Address Management** (la rubrica degli indirizzi) dell'exchange. Binance ha anche una **whitelist** (lista bianca): quando la attivi, i prelievi possono andare solo verso indirizzi salvati, e questo ti protegge se qualcuno ti ruba la password.

## Passo 4 — Invia un piccolo test

1. Inserisci un piccolo importo, appena sopra il prelievo minimo indicato sullo schermo.
2. Guarda le righe **commissione di rete** e **riceverai**. La commissione è fissa per ogni prelievo, quindi su un importo minuscolo può pesare molto.
3. Premi **Withdraw** e conferma con il codice 2FA o la passkey. Alcuni exchange inviano anche un'e-mail di conferma: aprila e premi **Confirm**.

## Passo 5 — Controlla che sia arrivato, poi invia il resto

1. Aspetta. Un trasferimento può richiedere da pochi secondi a circa un'ora, a seconda della rete e del traffico.
2. Sull'exchange apri lo storico dei prelievi per vedere lo stato e il **TxID** (l'ID della transazione, che puoi cercare su un block explorer).
3. Quando le monete compaiono nel wallet, ripeti i passi da 2 a 4 con il resto. L'indirizzo è già nello storico o in rubrica, quindi la seconda volta è più veloce.

Aggiungi le monete al [tuo portafoglio]({lang}/me/) per seguirne il valore in un solo posto, ovunque siano custodite.

> **⚠️ Attenzione**
> - **Rete sbagliata.** USDT esiste su molte reti. Inviare USDT «TRC20» a un indirizzo che si aspetta solo «ERC20» può far perdere le monete. Controlla la rete due volte.
> - **Memo o tag mancante.** Gli exchange e i wallet che richiedono il memo non sanno di chi sono le monete arrivate senza. Recuperarle, se possibile, è lento e costa una commissione.
> - **Falsa assistenza e siti di «verifica indirizzo».** Nessuno di serio ti chiede la seed phrase o di «verificare» un wallet inviando monete. Preleva solo dall'app o dal sito ufficiale.

## Cosa significa se compri regolarmente

Se compri un po' ogni settimana o ogni mese, non serve prelevare dopo ogni acquisto: ogni prelievo ha una commissione. Molte persone lasciano accumulare le monete sull'exchange e ogni tanto le spostano sul proprio wallet, per esempio una volta a trimestre, con un unico trasferimento più grande. Un esempio dal nostro calcolatore: 10 $ al giorno in Bitcoin per 3 anni ({{dcainv:3}} in totale) sono diventati {{dca:btc:3}} ({{dcaroi:btc:3}}). Sono risultati passati, non una previsione. In questo momento Bitcoin vale {{price:btc}}; guarda la [pagina di Bitcoin]({lang}/btc/).

Lezione precedente: [Come impostare un acquisto ricorrente]({lang}/blog/how-to-set-up-a-recurring-buy/). Prossima lezione: come vendere crypto e ricevere i soldi sul conto in banca. Confronta gli exchange nella nostra [pagina degli exchange]({lang}/exchanges/); tutte le lezioni sono nella [pagina Impara]({lang}/learn/).

## Fonti

- [Binance Support: come depositare e prelevare criptovalute su Binance (aggiornato a marzo 2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: come recuperare un deposito con tag o memo errato o mancante](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: come prelevare crypto dal tuo account Binance.US (giugno 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*Non è un consiglio di investimento.*
