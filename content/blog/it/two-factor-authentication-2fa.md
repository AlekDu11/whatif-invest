---
title: "Autenticazione a due fattori (2FA): come attivarla, passo dopo passo"
description: La 2FA aggiunge una seconda serratura al tuo account. Come attivare un'app di autenticazione o una passkey passo passo, e perché l'SMS è il più debole.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: 68 mln $
stat_label: persi nel 2021 per frodi SIM swap, in 1.611 denunce all'FBI (IC3, febbraio 2022)
---
**Cos'è la 2FA e come si attiva?** L'autenticazione a due fattori (2FA) significa che per accedere o prelevare servono due cose: la tua password *e* una seconda prova, come un codice di 6 cifre generato da un'app sul telefono o una passkey (la tua impronta digitale o il tuo volto). Attivala nelle impostazioni **Security** (Sicurezza) del tuo exchange e usa un'app di autenticazione o una passkey invece dell'SMS.

> **In sintesi**
> - Con la 2FA, una password rubata da sola non basta per svuotarti l'account.
> - **I codici via SMS sono l'opzione più debole:** con un "SIM swap" (scambio di SIM) un criminale trasferisce il tuo numero di telefono sulla sua SIM e riceve i tuoi codici. L'FBI ha registrato 1.611 denunce di questo tipo e oltre **68 milioni di dollari** di perdite nel 2021, contro 320 denunce e circa 12 milioni di dollari nel 2018–2020.
> - L'FBI consiglia opzioni più forti: un'app di autenticazione, la biometria o una chiave di sicurezza fisica.

## Le opzioni, dalla più debole alla più forte

- **Codice via SMS** — un messaggio con un codice. Meglio di niente, ma il tuo numero di telefono può essere rubato.
- **Codice via e-mail** — sicuro quanto il tuo account e-mail (proteggi anche quello con la 2FA).
- **App di autenticazione** (Google Authenticator, Microsoft Authenticator e simili) — l'app crea un nuovo codice di 6 cifre ogni 30 secondi, anche offline. Nessuno può intercettarlo tramite il tuo operatore telefonico.
- **Passkey** (biometria) — confermi con l'impronta, il volto o il PIN del telefono. Funziona solo sul sito vero, quindi un sito falso non può rubarla.
- **Chiave di sicurezza fisica** (un piccolo dispositivo USB/NFC) — la più forte, ideale per somme importanti.

## Passo dopo passo: app di autenticazione (esempio con l'app Binance)

Gli altri exchange usano quasi gli stessi passaggi; cerca **Security** (Sicurezza) nel tuo profilo.

1. **Passo 1 — Installa l'app.** Scarica Google Authenticator (o un'altra app di autenticazione) dall'App Store o da Google Play ufficiali.
2. **Passo 2 — Apri le impostazioni di sicurezza.** Nell'app Binance tocca l'icona **Account**, tocca il tuo profilo in alto, poi **Security**.
3. **Passo 3 — Avvia la configurazione.** Tocca **Authenticator App**, poi **Enable**. Vedrai un codice QR e una **setup key** (chiave di configurazione, un codice lungo).
4. **Passo 4 — Scrivi la chiave di configurazione su carta.** È il tuo salvagente se perdi il telefono. Tienila offline, come una seed phrase. Non toccare ancora **Next**.
5. **Passo 5 — Aggiungi l'account nell'app di autenticazione.** In Google Authenticator tocca **+**, scegli **Enter a setup key** (Inserisci una chiave di configurazione) oppure scansiona il codice QR, incolla la chiave, scrivi un nome come "Binance" e tocca **Add**.
6. **Passo 6 — Conferma.** Torna in Binance, tocca **Next** e inserisci il codice di 6 cifre dell'app. Vedrai un messaggio di conferma.
7. **Passo 7 — Provala.** Esci e accedi di nuovo. Se ti viene chiesto il codice, funziona.

## Passo dopo passo: passkey (ancora più semplice)

Secondo la pagina di assistenza di Binance servono l'app versione 2.60 o successiva, iOS 16+ o Android 9+.

1. **Account → profilo → Security → Passkeys (Biometrics) → Add Passkey.**
2. Conferma con la tua 2FA attuale se richiesto, poi tocca **Continue**.
3. Scegli dove salvarla: Portachiavi iCloud (iPhone), Gestore delle password di Google (Android) o una chiave di sicurezza, e conferma con impronta, volto o PIN.

## Dopo aver attivato la 2FA

- Disattiva l'SMS come metodo di accesso se l'exchange lo permette, o almeno chiedi al tuo operatore un blocco della SIM / un PIN contro la portabilità del numero.
- Proteggi con la 2FA anche l'e-mail collegata all'exchange.
- Attiva una **whitelist dei prelievi** (solo gli indirizzi salvati possono ricevere) se il tuo exchange la offre.

> **⚠️ Attenzione**
> - **Nessuno di serio ti chiede il codice 2FA.** Un "supporto" su Telegram, una telefonata dall'"exchange" o dalla "banca" che chiede il codice di 6 cifre è sempre un truffatore.
> - **Perdere il telefono senza la chiave di backup.** Il recupero richiede giorni di verifiche dell'identità. Scrivi la chiave di configurazione su carta e conservala al sicuro.
> - **App di autenticazione false e pagine di accesso copiate.** Installa app solo dallo store ufficiale e digita tu l'indirizzo dell'exchange, oppure usa un segnalibro.

## Cosa significa se compri regolarmente

Se compri un po' ogni mese, il tuo account sull'exchange diventa piano piano una somma vera — per esempio il bitcoin vale {{price:btc}} in questo momento ({{chg1y:btc}} in 12 mesi), risultati passati, non una previsione. Dieci minuti per configurare la 2FA proteggono anni di acquisti. Segui ciò che possiedi nella tua [pagina portafoglio]({lang}/me/).

Lezione precedente: [seed phrase: 5 regole per tenerla al sicuro]({lang}/blog/seed-phrase-safety-rules/). Approfondisci: [come registrarsi su un exchange crypto]({lang}/blog/how-to-register-on-a-crypto-exchange/), [gli exchange che funzionano nel tuo Paese]({lang}/exchanges/). Tutte le lezioni sono nella [pagina Impara]({lang}/learn/).

## Fonti

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8 febbraio 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app (aggiornato il 10 dicembre 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account (aggiornato il 10 dicembre 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Non è un consiglio di investimento.*
