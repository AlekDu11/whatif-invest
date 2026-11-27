---
title: "Pourquoi la plupart des acheteurs de memecoins perdent de l'argent : lancements, slippage et frais"
description: Seuls 0,41 % des portefeuilles pump.fun ont encaissé plus de 10 000 $ de gains. Les calculs simples (lancements, slippage, frais) qui jouent contre vous.
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: 0,41 %
stat_label: des 13,55 millions de portefeuilles pump.fun avaient encaissé plus de 10 000 $ de gains (données Dune, janvier 2025)
---
**Pourquoi la plupart des gens qui achètent des memecoins perdent-ils de l'argent ?** Parce que les calculs sont contre eux avant même que le prix ne bouge : la plupart des nouveaux tokens meurent en moins d'une journée, chaque achat et chaque vente coûtent des frais et du slippage, et les tout premiers acheteurs (souvent des bots et des initiés) revendent à ceux qui arrivent après. Pour gagner, un token doit survivre *et* monter assez haut pour couvrir tout cela.

> **À retenir**
> - Des données Dune publiées en janvier 2025 montraient que seuls **0,41 %** environ des 13,55 millions de portefeuilles pump.fun avaient encaissé plus de **10 000 $** de gains.
> - CoinGecko a constaté que **68,67 %** des tokens pump.fun avaient fait leur dernière transaction le jour de leur lancement (données janvier 2024 – juin 2026).
> - Un aller-retour (achat + vente) sur un nouveau token peut coûter **2,5 % ou plus** rien qu'en frais de plateforme, sans compter les frais de réseau et le slippage.

## Partie 1 — Le calcul de la survie

La plupart des memecoins ne sont pas « pas chers » — ils ont surtout une vie très courte.

- **Mort le jour du lancement.** CoinGecko a compté 18,67 millions de tokens pump.fun ; 68,67 % ont fait leur dernière transaction le jour même de leur lancement (chiffres publiés le 25 juin 2026).
- **Très peu atteignent un vrai marché.** La « graduation », c'est le moment où un token quitte la courbe de départ de pump.fun et obtient un pool d'échange normal. Selon Dune, le taux hebdomadaire de graduation est resté sous **1 %** pendant quatre semaines à partir du 17 février 2025 ; sa meilleure semaine, en novembre 2024, était à **1,67 %**. En mars 2026, il a atteint **2,01 %**, son plus haut niveau depuis juillet 2025.

Si vous choisissez des nouveaux lancements au hasard, vous détiendrez donc surtout des coins qui cessent d'être échangés. Quelques gros gagnants ne peuvent pas compenser de nombreux coins qui tombent à zéro, à moins de très bien choisir — et le premier jour, personne ne sait lesquels survivront.

## Partie 2 — Les frais : vous payez à l'entrée et à la sortie

La page d'aide de pump.fun (septembre 2025) indique des frais de **1,25 %** sur chaque transaction avant la graduation (0,95 % pour la plateforme, 0,30 % pour le créateur). Après la graduation, les frais baissent à mesure que le token grossit : de 1,25 % pour les plus petits à 0,30 % pour les plus gros. S'y ajoutent les frais du réseau Solana et, en option, des frais de « priorité » et de protection MEV (0,003 à 0,03 SOL par transaction selon leur page).

**Exemple chiffré (illustration, pas des prix réels) :** vous achetez pour 50 $ d'un nouveau token et payez 0,02 SOL de frais de priorité à l'achat comme à la vente. Les 1,25 % à l'entrée et à la sortie font environ 1,25 $, et les deux frais de priorité peuvent ajouter plusieurs dollars. Rien que pour revenir à 50 $, le token doit peut-être monter de **5 à 10 %**. Avec des transactions de 10 $, c'est bien pire : les frais fixes en mangent une part beaucoup plus grande.

## Partie 3 — Le slippage : le prix bouge pendant que vous achetez

Le **slippage** (glissement de prix), c'est l'écart entre le prix que vous voyez et le prix que vous obtenez vraiment (voir le [glossaire des memecoins]({lang}/memes/glossary/)). Les nouveaux tokens ont des pools minuscules : votre propre achat fait monter le prix — et les achats de tous les autres dans la même seconde aussi. Si vous réglez le slippage à 10–20 % (beaucoup d'applis le suggèrent pour les nouveaux coins), vous acceptez de payer jusqu'à autant de plus. La vente pose le même problème à l'envers : dans un petit pool, votre vente fait baisser le prix.

## Partie 4 — Qui se trouve en face de vous

Les tout premiers acheteurs sont souvent des snipers, des bundlers et le portefeuille du développeur (voir [snipers, bundlers et portefeuilles des développeurs]({lang}/blog/snipers-bundlers-dev-wallets/)). Ils achètent au prix le plus bas et revendent dès la première vague de demande. Si vous achetez après la première bougie verte, vous êtes souvent la « liquidité de sortie » (exit liquidity) — l'argent auquel ils revendent.

## Pas à pas : vérifiez les calculs avant d'appuyer sur «Buy»

1. **Étape 1 — Comptez les frais.** Regardez la ligne des frais sur votre écran de swap et ajoutez les frais de réseau/priorité. Multipliez par deux (achat + vente).
2. **Étape 2 — Vérifiez le slippage.** Gardez-le aussi bas que la transaction le permet (par exemple 1–3 % sur un coin avec un gros pool). Si un coin exige 20 % de slippage, c'est un signal d'alerte.
3. **Étape 3 — Vérifiez la taille du pool.** Sur notre [page memes]({lang}/memes/), ouvrez le token et regardez la liquidité. Petit pool = gros slippage dans les deux sens.
4. **Étape 4 — Faites le contrôle de sécurité.** Suivez [comment vérifier un memecoin avant d'acheter]({lang}/blog/how-to-check-a-memecoin-before-buying/).
5. **Étape 5 — Fixez votre perte à l'avance.** N'utilisez que de l'argent que vous pouvez perdre entièrement, et décidez du montant avant de commencer.

> **⚠️ Attention**
> - **« Il ne vaut que 0,0001 $, il peut faire x1000. »** Un prix bas ne veut rien dire ; beaucoup de tokens existent en milliards d'unités. Ce qui compte, c'est que le token survive et de savoir qui vous le vend.
> - **Beaucoup de toutes petites transactions.** Les frais fixes de réseau et de priorité peuvent manger 10 % ou plus d'une transaction de 10 $ avant même que le prix ne bouge.
> - **Les captures d'écran de gagnants.** Vous voyez les 0,41 % qui ont gagné gros, pas les millions qui ont perdu ; les « gourous » revendent souvent les coins qu'ils recommandent.

## Ce que cela signifie si vous achetez régulièrement

Les petits achats réguliers fonctionnent sur des actifs qui existent encore des années plus tard — pas sur des tokens qui peuvent cesser d'être échangés ce soir. Si vous voulez de la crypto, la voie habituelle pour un débutant est un grand coin liquide, acheté petit à petit ; à titre de comparaison, le SOL, le coin de Solana, vaut {{price:sol}} en ce moment ({{chg1y:sol}} sur 12 mois) — ce sont des résultats passés, pas une prévision. Vous pouvez tester « 10 $ par jour » sur n'importe quel actif dans notre calculateur et le suivre sur votre [page portefeuille]({lang}/me/).

Leçon précédente : [snipers, bundlers et portefeuilles des développeurs]({lang}/blog/snipers-bundlers-dev-wallets/). Toutes les leçons sont sur la [page Apprendre]({lang}/learn/).

## Sources

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data (11 janvier 2025)](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive (14 mars 2025)](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, données Dune : pump.fun graduation rate hits 2.01% (17 mars 2026)](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / données CoinGecko : nearly 70% of pump.fun tokens disappear on launch day (25 juin 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [Centre d'aide pump.fun : Transaction fees on pump.fun (septembre 2025)](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*Ceci n'est pas un conseil en investissement.*
