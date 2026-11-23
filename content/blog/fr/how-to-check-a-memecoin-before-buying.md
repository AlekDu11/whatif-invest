---
title: Comment vérifier un memecoin avant d'acheter : 6 contrôles en 5 minutes
description: Avant d'acheter un memecoin, vérifiez le contrat, la liquidité, les détenteurs, la part du top 10, l'âge et l'audit de sécurité Binance. Checklist simple.
date: 2026-11-23T16:30:00Z
category: learn
track: memes
step: 6
assets: sol, bnb, doge
stat: 6
stat_label: contrôles avant d'acheter un memecoin
---
**Comment vérifier un memecoin avant d'acheter ?** Trouvez le token grâce à son adresse de contrat, puis vérifiez six choses : l'audit de sécurité, la liquidité, le nombre de détenteurs, la part détenue par les 10 plus gros wallets, son âge et si le créateur peut encore le modifier. Si un seul contrôle est rouge, passez votre chemin. Il existe des milliers d'autres coins.

> **À retenir**
> - Ces contrôles ne rendent pas un memecoin sûr. Ils vous aident seulement à éviter les pièges les plus évidents : les tokens impossibles à revendre, les fausses copies et les coins que quelques wallets peuvent faire s'effondrer.
> - L'onglet **Audit** de Binance Wallet vérifie les risques liés au contrat, au trading et aux arnaques (par exemple un « honeypot » : un token qu'on peut acheter mais jamais revendre). Binance précise elle-même que l'audit n'est pas infaillible.
> - Sur notre [page memecoins]({lang}/memes/), le filtre qualité est activé par défaut : « Qualité seulement : liquidité 100 K$+, 1 jour+ ».

Cette leçon fait suite à [Connecter Binance Wallet à un DEX]({lang}/blog/connect-binance-wallet-to-dex/). Les memecoins sont extrêmement risqués : n'utilisez que de l'argent que vous pouvez vous permettre de perdre.

## Étape 1 — Trouvez la bonne adresse de contrat

Chaque token a une **adresse de contrat** (son identifiant unique sur la blockchain, une longue suite de lettres et de chiffres). N'importe qui peut créer un token avec le même nom et le même logo : le nom ne prouve donc rien.

1. Copiez l'adresse depuis le compte officiel du projet ou un site de données fiable.
2. Collez-la dans la recherche de votre wallet. Comparez les 4 premiers et les 4 derniers caractères.
3. Si plusieurs tokens portent le même nom, les autres sont des copies.

## Étape 2 — Ouvrez l'audit de sécurité

Dans l'appli Binance, ouvrez le token dans **Wallet** puis touchez l'onglet **Audit** (sur le site : cliquez sur le token, puis sur **Audit**). Sur les pages de tokens de notre rubrique memecoins, vous retrouvez le même contrôle sous la forme **Contrôle de sécurité Binance : Risque faible / Risque moyen / Risque élevé**.

Regardez trois groupes :

- **Contract risk** (risque du contrat) : le créateur peut-il bloquer les ventes, mettre des wallets sur liste noire, modifier la taxe ou modifier les soldes ?
- **Trading risk** (risque de trading) : risque de honeypot, taxe inhabituelle à l'achat ou à la vente (des frais prélevés sur chaque transaction), faible liquidité, risque de rug pull.
- **Scam risk** (risque d'arnaque) : faux token, arnaque connue, spam.

Un seul point rouge = n'achetez pas. Même « Risque faible » ne veut pas dire sûr : le créateur peut encore agir après votre achat.

## Étape 3 — Vérifiez la liquidité

La liquidité, c'est l'argent du pool d'échange qui vous permet de revendre. Si elle est minuscule, même une petite vente fait chuter fortement le prix, et le créateur peut la retirer (un rug pull, « tirer le tapis »). Sur WhatIfStack, notre filtre par défaut masque les tokens qui ont moins de 100 K$ de liquidité. Vérifiez aussi si la liquidité du pool est verrouillée ou brûlée (supprimée pour de bon), quand le site de données l'indique.

## Étape 4 — Comptez les détenteurs et la part du top 10

Sur la page du token, regardez **Détenteurs** (combien de wallets le possèdent) et **Top 10 détient** (quelle part de tous les coins est entre les mains des 10 plus gros wallets). Quelques centaines de détenteurs et un top 10 très lourd, cela veut dire qu'une poignée de personnes peut vendre et faire s'effondrer le prix. Attention : les adresses du pool et de burn apparaissent aussi dans le top 10, et cette partie-là est normale.

## Étape 5 — Vérifiez l'âge

La plupart des tokens frauduleux vivent quelques heures ou quelques jours. Un token de moins d'un jour n'a aucun historique. Notre filtre sur /memes/ n'affiche que les tokens d'au moins 1 jour. Plus ancien ne veut pas dire sûr, simplement moins inconnu.

## Étape 6 — Sur Solana : le créateur peut-il encore modifier le token ?

Sur Solana, deux réglages comptent :

- **Mint authority** (droit d'émission) : le droit de créer de nouveaux tokens. S'il est encore actif, le créateur peut en imprimer davantage et votre part diminue.
- **Freeze authority** (droit de gel) : le droit de geler un wallet. S'il est encore actif, le créateur pourrait vous empêcher de déplacer ou de vendre vos tokens.

L'état le plus sûr est « revoked » ou « disabled » (personne ne détient ce droit). Vous voyez les deux sur la page du token dans un explorateur de blocs comme Solscan.

> **⚠️ Attention**
> - **Une fausse copie avec le même nom.** Achetez toujours via l'adresse de contrat, jamais d'après le nom ou le logo.
> - **Un honeypot.** Vous pouvez acheter, le graphique monte, mais personne ne peut vendre. Un historique avec des achats et aucune vente est un signal d'alarme.
> - **Se fier à un seul feu vert.** Un audit, beaucoup de détenteurs ou un nom célèbre ne vous protègent pas si le prix baisse tout simplement : la plupart des memecoins finissent près de zéro.

## Ce que cela signifie si vous achetez régulièrement

Les petits achats réguliers fonctionnent mieux avec des actifs qui existeront probablement encore dans cinq ans. Ce n'est pas le cas de la plupart des memecoins. Si vous voulez quand même en essayer un, limitez-vous à un tout petit montant fixe et suivez-le à côté du reste de votre argent dans [votre portefeuille]({lang}/me/).

Prochaine leçon : l'histoire de Dogecoin. Toutes les leçons sont sur la [page Apprendre]({lang}/learn/).

## Sources

- [Binance : How to Use the Token Audit Feature in Binance Wallet](https://www.binance.com/en/support/faq/detail/fd1b21bac5114feda49dd185461afdda)
- [Binance.US : What is a honeypot scam?](https://support.binance.us/en/articles/15388146-what-is-a-honeypot-scam)
- [Solana docs : Set authority (mint and freeze authority)](https://solana.com/docs/tokens/basics/set-authority)
- [Solana docs : Freeze account](https://solana.com/docs/tokens/basics/freeze-account)

*Ceci n'est pas un conseil en investissement. Ce guide explique comment vérifier un token et ne recommande d'acheter aucun coin.*
