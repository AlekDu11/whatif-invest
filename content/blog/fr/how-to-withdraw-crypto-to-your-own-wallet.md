---
title: Comment retirer ses cryptos d'une plateforme vers son propre portefeuille : étape par étape
description: Transférez vos cryptos vers votre portefeuille en sécurité : bonne adresse, même réseau, mémo si besoin et un petit envoi test d'abord.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 réseau
stat_label: la plateforme et le portefeuille doivent utiliser le même, sinon les cryptos peuvent être perdues
---
**Comment retirer ses cryptos vers son propre portefeuille ?** Dans votre portefeuille, copiez votre **adresse de réception** pour la crypto. Puis, sur la plateforme, ouvrez **Withdraw** (Retirer), collez cette adresse, choisissez **le même réseau** que celui de votre portefeuille, saisissez un petit montant test et confirmez avec la 2FA. Quand le test est arrivé, envoyez le reste.

> **À retenir**
> - Trois choses doivent correspondre : la **crypto**, l'**adresse** et le **réseau** (la blockchain sur laquelle voyagent les jetons, par exemple Ethereum, BNB Smart Chain, TRON ou Solana). Binance prévient que des cryptos envoyées sur le mauvais réseau peuvent être perdues pour de bon.
> - Certaines cryptos (comme XRP, XLM ou ATOM) demandent aussi un **mémo** ou un **tag** (un court numéro qui indique au destinataire à qui appartiennent les jetons). Sans lui, le transfert peut rester bloqué ou arriver chez quelqu'un d'autre.
> - **Faites toujours d'abord un petit envoi test.** Un retrait ne peut plus être annulé une fois que les cryptos ont quitté la plateforme.

Cette leçon fait suite à [Comment programmer un achat récurrent]({lang}/blog/how-to-set-up-a-recurring-buy/). Pourquoi avoir son propre portefeuille : c'est expliqué dans [portefeuilles chauds et froids]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Avant de commencer

Il vous faut deux choses. Un compte sur une plateforme avec des cryptos dessus, protégé par la 2FA (voir [Comment s'inscrire sur une plateforme crypto]({lang}/blog/how-to-register-on-a-crypto-exchange/)). Et votre propre appli de portefeuille, déjà configurée, avec sa **phrase de récupération** (seed phrase : les 12 ou 24 mots secrets qui restaurent le portefeuille) notée sur papier et gardée hors ligne. Ne tapez jamais cette phrase ailleurs : aucune plateforme, aucun site et aucun « support » n'en aura jamais besoin.

## Étape 1 — Copiez l'adresse de réception de votre portefeuille

1. Ouvrez l'appli de votre portefeuille et appuyez sur **Receive** (Recevoir ; parfois **Deposit**).
2. Choisissez la crypto, par exemple Bitcoin ou USDT.
3. Si le portefeuille le demande, choisissez le réseau. Notez lequel, par exemple « USDT sur TRON (TRC20) » ou « USDT sur Ethereum (ERC20) ».
4. Appuyez sur **Copy** (Copier) à côté de l'adresse. Ne la recopiez pas à la main.

Une adresse est une longue suite de lettres et de chiffres. Les adresses Bitcoin commencent souvent par **bc1**, celles d'Ethereum et de BNB Smart Chain par **0x**, celles de TRON par **T**.

## Étape 2 — Ouvrez Withdraw sur la plateforme

Dans l'appli Binance, c'est **Assets → Spot → Send → Withdraw Crypto** ; sur le site, **Wallet → Overview → Withdraw**. Les autres plateformes ont un bouton **Withdraw** à côté de chaque crypto, dans l'écran portefeuille ou portfolio. Choisissez la même crypto qu'à l'étape 1.

## Étape 3 — Collez l'adresse et choisissez le réseau

1. Collez l'adresse dans le champ **Address** (Adresse).
2. Comparez les **4 premiers et les 4 derniers caractères** avec votre portefeuille. Certains logiciels malveillants remplacent l'adresse copiée par celle du voleur.
3. Choisissez le **réseau**. Ce doit être celui que le portefeuille vous a montré à l'étape 1. Binance peut proposer un réseau automatiquement : vérifiez-le quand même. Ne choisissez pas un réseau seulement parce que ses frais sont les plus bas.
4. Si un champ **Memo** ou **Tag** apparaît et que votre portefeuille vous en a donné un, remplissez-le. Si votre portefeuille n'affiche aucun mémo, il n'en a en général pas besoin, mais vérifiez dans son aide.

Astuce : en cas de doute, enregistrez l'adresse dans l'**Address Management** (carnet d'adresses) de la plateforme. Binance propose aussi une **liste blanche** (whitelist) : une fois activée, les retraits ne peuvent aller que vers des adresses enregistrées, ce qui vous protège si quelqu'un vole votre mot de passe.

## Étape 4 — Envoyez un petit test

1. Saisissez un petit montant, juste au-dessus du retrait minimum affiché.
2. Regardez les lignes **frais de réseau** et **vous recevrez**. Les frais sont fixes par retrait : sur un tout petit montant, ils peuvent représenter une grosse part.
3. Appuyez sur **Withdraw** et confirmez avec votre code 2FA ou votre passkey. Certaines plateformes envoient aussi un e-mail de confirmation : ouvrez-le et cliquez sur **Confirm**.

## Étape 5 — Vérifiez l'arrivée, puis envoyez le reste

1. Patientez. Un transfert peut prendre de quelques secondes à environ une heure, selon le réseau et le trafic.
2. Sur la plateforme, ouvrez l'historique des retraits pour voir le statut et le **TxID** (l'identifiant de la transaction, que vous pouvez chercher sur un explorateur de blocs).
3. Quand les cryptos apparaissent dans votre portefeuille, refaites les étapes 2 à 4 avec le reste. L'adresse est déjà dans l'historique ou le carnet, donc c'est plus rapide la deuxième fois.

Ajoutez les cryptos à [votre portefeuille de suivi]({lang}/me/) pour suivre leur valeur au même endroit, où qu'elles soient conservées.

> **⚠️ Attention**
> - **Mauvais réseau.** L'USDT existe sur de nombreux réseaux. Envoyer de l'USDT « TRC20 » vers une adresse qui n'attend que de l'« ERC20 » peut faire perdre les jetons. Vérifiez le réseau deux fois.
> - **Mémo ou tag oublié.** Les plateformes et portefeuilles qui exigent un mémo ne savent pas à qui appartiennent les jetons arrivés sans lui. La récupération, quand elle est possible, est lente et payante.
> - **Faux support et sites de « vérification d'adresse ».** Personne de sérieux ne vous demande votre phrase de récupération ni de « vérifier » un portefeuille en envoyant des cryptos. Retirez uniquement dans l'appli ou sur le site officiel.

## Ce que cela signifie si vous achetez régulièrement

Si vous achetez un peu chaque semaine ou chaque mois, inutile de retirer après chaque achat : chaque retrait a des frais. Beaucoup de gens laissent les cryptos s'accumuler sur la plateforme et les transfèrent de temps en temps vers leur portefeuille, par exemple une fois par trimestre, en un seul envoi plus gros. Exemple tiré de notre calculateur : 10 $ par jour en Bitcoin pendant 3 ans ({{dcainv:3}} au total) sont devenus {{dca:btc:3}} ({{dcaroi:btc:3}}). Ce sont des résultats passés, pas une prévision. Le Bitcoin vaut {{price:btc}} en ce moment ; voir la [page Bitcoin]({lang}/btc/).

Leçon précédente : [Comment programmer un achat récurrent]({lang}/blog/how-to-set-up-a-recurring-buy/). Leçon suivante : comment vendre ses cryptos et récupérer l'argent sur son compte bancaire. Comparez les plateformes sur notre [page des plateformes]({lang}/exchanges/) ; toutes les leçons sont sur la [page Apprendre]({lang}/learn/).

## Sources

- [Binance Support : comment déposer et retirer des cryptos sur Binance (mis à jour en mars 2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support : comment récupérer un dépôt avec un tag ou un mémo erroné ou manquant](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center : comment retirer des cryptos de votre compte Binance.US (juin 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*Ceci n'est pas un conseil en investissement.*
