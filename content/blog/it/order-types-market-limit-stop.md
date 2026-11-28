---
title: "Tipi di ordine: al mercato, limite e stop spiegati passo dopo passo"
description: Cosa fanno i pulsanti Market, Limit e Stop nell'app di un exchange o di un broker, con un esempio in numeri e i 3 errori che costano soldi.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: tipi base di ordine — al mercato (veloce, prezzo non fisso), limite (prezzo fisso, esecuzione incerta), stop (scatta a un prezzo)
---
**Quali tipi di ordine esistono?** Un **ordine al mercato** (Market) compra o vende subito al miglior prezzo disponibile. Un **ordine limite** (Limit) compra o vende solo al tuo prezzo o meglio, quindi potrebbe non essere mai eseguito. Un **ordine stop** (Stop) aspetta che il prezzo arrivi al livello che scegli e poi invia un ordine al mercato: si usa spesso per limitare una perdita.

> **In sintesi**
> - Market = velocità, ma non controlli il prezzo esatto. Limit = controllo del prezzo, ma nessuna garanzia di esecuzione.
> - Un ordine stop diventa un ordine al mercato quando scatta. In un crollo veloce può essere eseguito molto sotto il tuo prezzo stop.
> - Prima di premere «Compra», controlla sempre tre cose: tipo di ordine, quantità e prezzo.

## I tre pulsanti, in parole semplici

Quando apri la schermata di trading nell'app di un exchange o di un broker, di solito vedi delle schede: **Market** (al mercato), **Limit** (limite) e **Stop** (a volte «Stop-limit», stop limite).

- **Ordine al mercato (Market).** «Compra adesso, a qualsiasi prezzo.» Viene eseguito quasi all'istante alla migliore offerta (l'**ask**, il prezzo più basso a cui qualcuno vuole vendere). Per le cripto grandi e le grandi azioni il prezzo di solito è molto vicino a quello che vedi. Nei mercati piccoli e poco liquidi può essere molto peggiore.
- **Ordine limite (Limit).** «Compra solo a X $ o meno» (oppure «vendi solo a X $ o più»). Il tuo ordine aspetta nel **book di negoziazione** (order book, l'elenco di tutti gli ordini di acquisto e vendita in attesa) finché qualcuno non accetta il tuo prezzo. Se il prezzo non arriva mai lì, non succede nulla.
- **Ordine stop (Stop, stop loss).** «Se il prezzo scende a X $, vendi.» Fino ad allora è invisibile e non fa niente. Quando il prezzo tocca X $, diventa un ordine al mercato e vende al prezzo successivo disponibile.
- **Ordine stop limite (Stop-limit).** Come uno stop, ma diventa un ordine *limite*. Non venderai sotto il tuo limite, ma in un crollo veloce potresti non vendere affatto.

## Un esempio con numeri semplici

Supponiamo che un'azione segni **100,00 $**. Il miglior compratore offre 99,95 $ (il **bid**) e il miglior venditore chiede 100,05 $ (l'ask). La differenza di 0,10 $ è lo **spread**.

1. Premi **Market, compra 10 azioni** → paghi circa 100,05 $ l'una = **1.000,50 $** più l'eventuale commissione.
2. Inserisci **Limit, compra 10 azioni a 98 $** → non succede nulla finché un venditore non accetta 98 $. Se invece il prezzo sale a 105 $, il tuo ordine resta lì in attesa e non compri niente.
3. Hai già le azioni e imposti uno **Stop a 90 $** → se il prezzo scende a 90 $, parte una vendita al mercato. In un mercato tranquillo potresti ottenere 89,95 $. Ma se arrivano brutte notizie prima dell'apertura e l'azione apre a 80 $, il tuo stop scatta e vendi intorno a **80 $**, non a 90 $.

Il terzo caso è reale. Il 6 maggio 2010 (il «flash crash») i prezzi negli Stati Uniti sono crollati in pochi minuti e alcuni ordini stop sono stati eseguiti molto sotto il loro livello stop; alcune azioni sono state persino scambiate a un centesimo, secondo il rapporto di SEC e CFTC.

## Passo dopo passo: inserisci il tuo primo ordine limite in sicurezza

Esercitati prima con una cifra molto piccola.

1. **Passo 1 — Apri la schermata di trading** della cripto o dell'azione e scegli **Compra** (Buy).
2. **Passo 2 — Premi la scheda «Limit»**, non «Market».
3. **Passo 3 — Scrivi il tuo prezzo.** Guarda prima il prezzo attuale (per esempio il bitcoin ora vale {{price:btc}}). Un limite molto più basso potrebbe non essere mai eseguito.
4. **Passo 4 — Scrivi la quantità.** Controlla se il campo indica monete/azioni o soldi (USD, EUR). È l'errore di battitura più comune.
5. **Passo 5 — Controlla il riepilogo**: tipo, prezzo, quantità, totale, commissione. Poi conferma.
6. **Passo 6 — Trova il tuo ordine** in «Ordini aperti» (Open orders). Lì puoi annullarlo in qualsiasi momento finché non viene eseguito. Quando viene eseguito, passa nello «Storico ordini» (Order history).

> **⚠️ Attenzione**
> - **Ordini al mercato in mercati poco liquidi.** Sulle cripto piccole o fuori dall'orario normale, un ordine al mercato può essere eseguito molto peggio del prezzo sullo schermo (si chiama **slippage**). Lì usa un ordine limite.
> - **Pensare che uno stop loss garantisca il tuo prezzo.** Non è così: garantisce la vendita, non il prezzo. Gap e crolli possono spingere l'esecuzione molto più in basso. Uno stop limite protegge il prezzo, ma potrebbe non vendere.
> - **Confondere i campi.** Lato sbagliato (Vendi invece di Compra), uno zero in più nella quantità o un prezzo scritto nel campo sbagliato. Leggi il riepilogo prima di confermare.

## Cosa significa se compri regolarmente

Se compri semplicemente un po' ogni settimana o ogni mese, non ti servono ordini complicati. Di solito basta un ordine al mercato su un asset grande e liquido, oppure un ordine limite poco sopra il prezzo attuale se vuoi un tetto. Il risultato vero viene dal tempo passato sul mercato: 10 $ al giorno in bitcoin per 3 anni oggi varrebbero {{dca:btc:3}} (avendo investito {{dcainv:3}}) — risultati passati, non una previsione.

Prossimi passi su WhatIfStack: guarda come i book e i grandi trader muovono il mercato nell'[hub Trading]({lang}/trading/) e nel [tracker delle balene di Hyperliquid]({lang}/trading/hyperliquid/), confronta le commissioni sugli [exchange]({lang}/exchanges/) e trova tutte le lezioni nella [pagina Impara]({lang}/learn/).

## Fonti

- [Investor.gov (SEC): Tipi di ordine](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Bollettino per gli investitori — ordini stop, stop limite e trailing stop](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Tipi di ordine](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC e SEC: Rapporto sugli eventi di mercato del 6 maggio 2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Non è una consulenza finanziaria.*
