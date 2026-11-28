---
title: "Types d'ordres : au marché, à cours limité et stop, expliqués étape par étape"
description: Ce que font les boutons Market, Limit et Stop dans l'appli d'une plateforme ou d'un courtier, avec un exemple chiffré et les 3 erreurs qui coûtent cher.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: types d'ordres de base — au marché (rapide, prix non fixé), à cours limité (prix fixé, exécution incertaine), stop (se déclenche à un prix)
---
**Quels sont les types d'ordres ?** Un **ordre au marché** (Market) achète ou vend tout de suite au meilleur prix disponible. Un **ordre à cours limité** (Limit) achète ou vend seulement à votre prix ou mieux : il peut donc ne jamais être exécuté. Un **ordre stop** (Stop) attend que le prix atteigne le niveau que vous avez choisi, puis envoie un ordre au marché — souvent pour limiter une perte.

> **À retenir**
> - Market = rapidité, mais vous ne maîtrisez pas le prix exact. Limit = maîtrise du prix, mais aucune garantie d'exécution.
> - Un ordre stop devient un ordre au marché quand il se déclenche. Lors d'une chute rapide, il peut être exécuté bien en dessous de votre prix stop.
> - Avant d'appuyer sur « Acheter », vérifiez toujours trois choses : le type d'ordre, la quantité et le prix.

## Les trois boutons, en mots simples

Quand vous ouvrez l'écran de passage d'ordre dans l'appli d'une plateforme crypto ou d'un courtier, vous voyez en général des onglets : **Market** (au marché), **Limit** (à cours limité) et **Stop** (parfois « Stop-limit », stop limite).

- **Ordre au marché (Market).** « Achète maintenant, peu importe le prix. » Il est exécuté presque instantanément à la meilleure offre (l'**ask**, le prix le plus bas auquel quelqu'un veut vendre). Pour les grosses cryptos et les grandes actions, le prix est en général très proche de celui affiché. Sur les petits marchés peu liquides, il peut être nettement moins bon.
- **Ordre à cours limité (Limit).** « Achète seulement à X $ ou moins cher » (ou « vends seulement à X $ ou plus cher »). Votre ordre attend dans le **carnet d'ordres** (order book, la liste de tous les ordres d'achat et de vente en attente) jusqu'à ce que quelqu'un accepte votre prix. Si le prix n'y arrive jamais, il ne se passe rien.
- **Ordre stop (Stop, stop loss).** « Si le prix tombe à X $, vends. » D'ici là, il est invisible et ne fait rien. Quand le prix touche X $, il devient un ordre au marché et vend au prix disponible suivant.
- **Ordre stop limite (Stop-limit).** Comme un stop, mais il devient un ordre *à cours limité*. Vous ne vendrez pas sous votre limite — mais lors d'une chute rapide, vous risquez de ne pas vendre du tout.

## Un exemple avec des chiffres simples

Disons qu'une action affiche **100,00 $**. Le meilleur acheteur propose 99,95 $ (le **bid**) et le meilleur vendeur demande 100,05 $ (l'ask). L'écart de 0,10 $ s'appelle le **spread**.

1. Vous appuyez sur **Market, acheter 10 actions** → vous payez environ 100,05 $ chacune = **1 000,50 $**, plus les frais éventuels.
2. Vous placez **Limit, acheter 10 actions à 98 $** → rien ne se passe tant qu'un vendeur n'accepte pas 98 $. Si le prix monte à 105 $, votre ordre attend simplement et vous n'achetez rien.
3. Vous détenez les actions et placez un **Stop à 90 $** → si le prix tombe à 90 $, une vente au marché est envoyée. Sur un marché calme, vous obtiendrez peut-être 89,95 $. Mais si une mauvaise nouvelle tombe avant l'ouverture et que l'action ouvre à 80 $, votre stop se déclenche et vous vendez vers **80 $**, pas 90 $.

Ce troisième cas est bien réel. Le 6 mai 2010 (le « flash crash »), les cours américains se sont effondrés en quelques minutes et certains ordres stop ont été exécutés bien en dessous de leur niveau stop ; quelques actions ont même été échangées à un cent, selon le rapport de la SEC et de la CFTC.

## Étape par étape : placez votre premier ordre à cours limité en toute sécurité

Entraînez-vous d'abord avec une toute petite somme.

1. **Étape 1 — Ouvrez l'écran de passage d'ordre** de la crypto ou de l'action et choisissez **Acheter** (Buy).
2. **Étape 2 — Appuyez sur l'onglet « Limit »**, pas « Market ».
3. **Étape 3 — Tapez votre prix.** Regardez d'abord le prix actuel (par exemple, le bitcoin est à {{price:btc}} en ce moment). Une limite très en dessous risque de ne jamais être exécutée.
4. **Étape 4 — Tapez la quantité.** Vérifiez si le champ correspond à des cryptos/actions ou à de l'argent (USD, EUR). C'est l'erreur de saisie la plus fréquente.
5. **Étape 5 — Vérifiez le récapitulatif** : type, prix, quantité, total, frais. Puis confirmez.
6. **Étape 6 — Retrouvez votre ordre** dans « Ordres ouverts » (Open orders). Vous pouvez l'annuler à tout moment tant qu'il n'est pas exécuté. Une fois exécuté, il passe dans l'« Historique des ordres » (Order history).

> **⚠️ Attention**
> - **Ordres au marché sur des marchés peu liquides.** Sur les petites cryptos ou en dehors des heures normales, un ordre au marché peut être exécuté bien moins bien que le prix affiché (c'est le **slippage**, ou glissement). Utilisez-y un ordre à cours limité.
> - **Croire qu'un stop loss garantit votre prix.** Ce n'est pas le cas : il garantit la vente, pas le prix. Les gaps et les krachs peuvent faire baisser l'exécution bien plus bas. Un stop limite protège le prix, mais peut ne pas vendre.
> - **Confondre les champs.** Mauvais sens (Vendre au lieu d'Acheter), un zéro de trop dans la quantité ou un prix tapé dans la mauvaise case. Lisez le récapitulatif avant de confirmer.

## Ce que cela signifie si vous achetez régulièrement

Si vous achetez simplement un peu chaque semaine ou chaque mois, vous n'avez pas besoin d'ordres compliqués. Un ordre au marché sur un actif important et liquide suffit en général, ou un ordre à cours limité un peu au-dessus du prix actuel si vous voulez un plafond. Le vrai résultat vient du temps passé sur le marché : 10 $ par jour en bitcoin pendant 3 ans vaudraient aujourd'hui {{dca:btc:3}} (pour {{dcainv:3}} investis) — des résultats passés, pas une prévision.

Ensuite sur WhatIfStack : voyez comment les carnets d'ordres et les gros traders font bouger le marché sur le [hub Trading]({lang}/trading/) et le [suivi des baleines Hyperliquid]({lang}/trading/hyperliquid/), comparez les frais des [plateformes d'échange]({lang}/exchanges/) et retrouvez toutes les leçons sur la [page Apprendre]({lang}/learn/).

## Sources

- [Investor.gov (SEC) : Types d'ordres](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC) : Bulletin aux investisseurs — ordres stop, stop limite et stop suiveur](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA : Types d'ordres](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC et SEC : Rapport sur les événements de marché du 6 mai 2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Ceci n'est pas un conseil en investissement.*
