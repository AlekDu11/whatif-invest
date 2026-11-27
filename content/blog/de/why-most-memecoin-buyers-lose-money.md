---
title: "Warum die meisten Memecoin-Käufer Geld verlieren: die Mathematik von Launches, Slippage und Gebühren"
description: Nur 0,41 % der pump.fun-Wallets erzielten über 10.000 $ Gewinn. Die einfache Mathematik von Launches, Slippage und Gebühren, die gegen Memecoin-Käufer arbeitet.
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: 0,41 %
stat_label: von 13,55 Millionen pump.fun-Wallets hatten über 10.000 $ Gewinn realisiert (Dune-Daten, Januar 2025)
---
**Warum verlieren die meisten Memecoin-Käufer Geld?** Weil die Mathematik gegen sie arbeitet, bevor sich der Kurs überhaupt bewegt: Die meisten neuen Token sterben innerhalb eines Tages, jeder Kauf und Verkauf kostet Gebühren und Slippage (Preisabweichung), und die allerersten Käufer (oft Bots und Insider) verkaufen an die, die später kommen. Um zu gewinnen, muss ein Token überleben *und* so weit steigen, dass all das gedeckt ist.

> **Das Wichtigste**
> - Laut Dune-Daten vom Januar 2025 hatten nur etwa **0,41 %** von 13,55 Millionen pump.fun-Wallets mehr als **10.000 $** Gewinn realisiert.
> - CoinGecko stellte fest, dass **68,67 %** der pump.fun-Token ihren letzten Trade am Launch-Tag hatten (Daten Januar 2024 – Juni 2026).
> - Jede Runde (Kauf + Verkauf) bei einem neuen Token kann allein an Plattformgebühren **2,5 % und mehr** kosten — plus Netzwerkgebühren und Slippage.

## Teil 1 — Die Mathematik des Überlebens

Die meisten Memecoins sind nicht „billig“ — sie sind kurzlebig.

- **Tod am Launch-Tag.** CoinGecko zählte 18,67 Millionen pump.fun-Token; bei 68,67 % fand der letzte Trade am Tag des Starts statt (Bericht vom 25. Juni 2026).
- **Nur wenige erreichen einen echten Markt.** „Graduation“ heißt, dass ein Token die Startkurve von pump.fun verlässt und einen normalen Handelspool bekommt. Laut Dune-Daten lag die wöchentliche Graduation-Rate ab dem 17. Februar 2025 vier Wochen lang unter **1 %**; die beste Woche, im November 2024, kam auf **1,67 %**. Im März 2026 erreichte sie **2,01 %**, den höchsten Wert seit Juli 2025.

Wer neue Launches also zufällig auswählt, hält meist Coins, die irgendwann gar nicht mehr gehandelt werden. Ein paar große Gewinner können viele Totalverluste nicht ausgleichen, außer Sie wählen sehr gut aus — und am ersten Tag weiß niemand, welche überleben.

## Teil 2 — Gebühren: Sie zahlen beim Einstieg und beim Ausstieg

Die Hilfeseite von pump.fun (September 2025) nennt eine Gebühr von **1,25 %** auf jeden Trade vor der Graduation (0,95 % an die Plattform, 0,30 % an den Ersteller). Nach der Graduation sinkt die Gebühr, je größer der Token wird: von 1,25 % bei den kleinsten bis 0,30 % bei den größten. Dazu kommen Solana-Netzwerkgebühren und optionale „Priority“- und MEV-Schutzgebühren (laut ihrer Seite 0,003–0,03 SOL pro Trade).

**Rechenbeispiel (Illustration, keine echten Kurse):** Sie kaufen für 50 $ einen neuen Token und zahlen in jede Richtung 0,02 SOL Priority-Gebühr. Die 1,25 % beim Ein- und Ausstieg machen etwa 1,25 $ aus, die zwei Priority-Gebühren können noch einige Dollar mehr kosten. Nur um wieder bei 50 $ zu landen, muss der Token vielleicht um **5–10 %** steigen. Bei Trades über 10 $ ist es noch viel schlimmer: Feste Gebühren fressen einen deutlich größeren Anteil.

## Teil 3 — Slippage: Der Kurs bewegt sich, während Sie kaufen

**Slippage** ist der Unterschied zwischen dem Kurs, den Sie sehen, und dem Kurs, den Sie tatsächlich bekommen (siehe [Memecoin-Glossar]({lang}/memes/glossary/)). Neue Token haben winzige Pools, deshalb treibt schon Ihr eigener Kauf den Kurs nach oben — und die Käufe aller anderen in derselben Sekunde ebenso. Wenn Sie die Slippage auf 10–20 % stellen (viele Apps empfehlen das für neue Coins), akzeptieren Sie, bis zu so viel mehr zu zahlen. Beim Verkauf gilt dasselbe umgekehrt: In einem dünnen Pool drückt Ihr Verkauf den Kurs nach unten.

## Teil 4 — Wer auf der anderen Seite steht

Die allerersten Käufer sind oft Sniper, Bundler und das Entwickler-Wallet (siehe [Sniper, Bundler und Entwickler-Wallets]({lang}/blog/snipers-bundlers-dev-wallets/)). Sie kaufen zum niedrigsten Kurs und verkaufen in die erste Nachfragewelle hinein. Wenn Sie nach der ersten grünen Kerze kaufen, sind Sie oft die „Exit-Liquidität“ (exit liquidity) — das Geld, an das sie verkaufen.

## Schritt für Schritt: Rechnen Sie nach, bevor Sie auf «Kaufen» tippen

1. **Schritt 1 — Gebühren zusammenzählen.** Sehen Sie sich die Gebührenzeile im Swap-Fenster an und addieren Sie die Netzwerk-/Priority-Gebühr. Mal zwei nehmen (Kauf + Verkauf).
2. **Schritt 2 — Slippage prüfen.** Halten Sie sie so niedrig, wie der Trade es zulässt (zum Beispiel 1–3 % bei einem Coin mit großem Pool). Braucht ein Coin 20 % Slippage, ist das ein Warnsignal.
3. **Schritt 3 — Poolgröße prüfen.** Öffnen Sie auf unserer [Memecoin-Seite]({lang}/memes/) den Token und schauen Sie auf die Liquidität. Kleiner Pool = hohe Slippage in beide Richtungen.
4. **Schritt 4 — Sicherheitscheck machen.** Nutzen Sie [Memecoin vor dem Kauf prüfen]({lang}/blog/how-to-check-a-memecoin-before-buying/).
5. **Schritt 5 — Verlust vorher festlegen.** Setzen Sie nur Geld ein, das Sie komplett verlieren können, und legen Sie den Betrag fest, bevor Sie anfangen.

> **⚠️ Vorsicht**
> - **„Kostet nur 0,0001 $, kann sich vertausendfachen.“** Ein niedriger Kurs sagt nichts; viele Token gibt es milliardenfach. Entscheidend ist, ob der Token überlebt und wer an Sie verkauft.
> - **Viele kleine Trades.** Feste Netzwerk- und Priority-Gebühren können über 10 % eines 10-$-Trades auffressen, bevor sich der Kurs überhaupt bewegt.
> - **Screenshots von Gewinnern.** Sie sehen die 0,41 %, die groß gewonnen haben, nicht die Millionen, die verloren haben; „Gurus“ verkaufen oft genau die Coins, die sie bewerben.

## Was das bedeutet, wenn Sie regelmäßig kaufen

Regelmäßige kleine Käufe funktionieren bei Anlagen, die es auch in Jahren noch gibt — nicht bei Token, die vielleicht schon heute Abend nicht mehr gehandelt werden. Wenn Sie Krypto möchten, ist der übliche Weg für Einsteiger ein großer, liquider Coin, den man nach und nach kauft; zum Vergleich: SOL, der eigene Coin von Solana, steht gerade bei {{price:sol}} ({{chg1y:sol}} in 12 Monaten) — vergangene Ergebnisse, keine Prognose. „10 $ am Tag“ können Sie mit jeder Anlage in unserem Rechner testen und auf Ihrer [Portfolio-Seite]({lang}/me/) verfolgen.

Vorherige Lektion: [Sniper, Bundler und Entwickler-Wallets]({lang}/blog/snipers-bundlers-dev-wallets/). Alle Lektionen finden Sie auf der [Lernen-Seite]({lang}/learn/).

## Quellen

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data (11. Januar 2025)](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive (14. März 2025)](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, Dune-Daten: pump.fun graduation rate hits 2.01% (17. März 2026)](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / CoinGecko-Daten: nearly 70% of pump.fun tokens disappear on launch day (25. Juni 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [pump.fun-Hilfecenter: Transaction fees on pump.fun (September 2025)](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*Keine Anlageberatung.*
