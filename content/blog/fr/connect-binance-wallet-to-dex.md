---
title: Connecter Binance Wallet à un DEX et rapatrier ses cryptos : étape par étape
description: Connectez Binance Wallet à un DEX en sécurité, renvoyez vos cryptos sur Binance sur le bon réseau et supprimez les anciennes autorisations, pas à pas.
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: petit transfert test avant chaque nouvelle adresse ou nouveau réseau
---
**Comment connecter Binance Wallet à un DEX ?** Ouvrez le site officiel du DEX, cliquez sur **Connect Wallet** (connecter le wallet), choisissez Binance Wallet (ou WalletConnect et scannez le QR code avec l'appli Binance) et confirmez dans l'appli. Pour rapatrier vos cryptos, copiez votre **adresse de dépôt** Binance pour la même crypto et le même réseau, puis envoyez-les depuis le wallet — d'abord un petit montant test.

> **À retenir**
> - Un DEX (exchange décentralisé — un site où l'on échange des tokens directement depuis son propre wallet) n'a jamais besoin de votre mot de passe de récupération ni de votre phrase de récupération. La connexion permet seulement au site de vous *demander* une signature ; rien ne bouge sans votre confirmation.
> - Le réseau doit être le même des deux côtés (BNB Smart Chain vers BNB Smart Chain, Solana vers Solana). Un mauvais réseau ou une mauvaise adresse peut faire perdre les cryptos.
> - Chaque « Approve » autorise un site à dépenser un token à votre place. Donnez de petites autorisations et supprimez celles dont vous ne vous servez plus.

Cette leçon fait suite à [Comment créer un Binance Wallet]({lang}/blog/how-to-create-binance-wallet/). Les memecoins sont extrêmement risqués : n'utilisez que de l'argent que vous pouvez vous permettre de perdre.

## Étape 1. Ouvrez le vrai site

Les faux sites de DEX avec le même logo sont l'un des pièges les plus courants.

1. Tapez l'adresse vous-même ou utilisez un favori. Ne cliquez pas sur les publicités des moteurs de recherche ni sur les liens reçus dans des discussions.
2. Vérifiez la barre d'adresse lettre par lettre.
3. Vérifiez que le DEX fonctionne sur le réseau où se trouvent vos cryptos.

## Étape 2. Connectez le wallet

Trois façons, selon votre appareil :

- **Sur ordinateur avec l'extension de navigateur Binance Wallet** (Chrome ou Brave). Connectez-vous à l'extension en scannant son QR code avec l'appli Binance. Sur le DEX, cliquez ensuite sur **Connect** ou **Connect Wallet**, choisissez Binance Wallet et confirmez la fenêtre qui s'ouvre.
- **Sur ordinateur sans l'extension.** Sur le DEX, cliquez sur **Connect Wallet → WalletConnect**. Un QR code s'affiche. Scannez-le avec le scanner de l'appli Binance et touchez **Connect**.
- **Sur téléphone.** Ouvrez le DEX dans le navigateur du téléphone, touchez **Connect Wallet**, choisissez Binance Wallet dans la liste et confirmez dans l'appli.

Avant de confirmer, lisez la fenêtre : le nom du site, l'adresse et le réseau. Si quelque chose cloche, touchez Cancel (annuler).

## Étape 3. Faites le swap et lisez chaque signature

1. Choisissez la crypto avec laquelle vous payez et le token voulu (cherchez le token par son **adresse de contrat**, pas par son nom).
2. Saisissez un petit montant et vérifiez le taux, le slippage (la plus forte variation de prix que vous acceptez) et les frais de réseau.
3. La première fois que vous vendez un token, le site demande un **Approve** (l'autorisation de dépenser ce token). Si l'appli le permet, indiquez un montant au lieu de « illimité ».
4. Confirmez le swap dans l'appli. Si une demande de signature n'est qu'une page de code illisible ou n'a aucun sens — **ne signez pas**.

## Étape 4. Renvoyez vos cryptos sur votre compte Binance

1. Dans l'appli Binance, passez sur **Exchange** → **Assets** (actifs) → **Deposit** (dépôt). Choisissez la crypto (par exemple BNB).
2. Choisissez le **réseau** (par exemple BNB Smart Chain). Copiez l'adresse de dépôt. Certaines cryptos demandent aussi un **memo/tag** — copiez-le aussi.
3. Passez sur **Wallet** → **Send** (envoyer). Choisissez la même crypto et le même réseau. Collez l'adresse (et le memo s'il y en a un).
4. Envoyez d'abord un petit montant test. Quand il arrive sur votre compte Binance, envoyez le reste.

Gardez un peu de BNB ou de SOL dans le wallet : chaque action on-chain, même ratée, coûte des frais de réseau. Certains memecoins ne peuvent pas du tout être déposés sur l'exchange (il ne les liste pas) — pour encaisser, échangez-les d'abord contre du BNB, du SOL ou de l'USDT dans le wallet.

## Étape 5. Déconnectez-vous et faites le ménage

1. Une fois terminé, déconnectez le site (dans les réglages des sites connectés ou de WalletConnect du wallet, ou avec le bouton **Disconnect** du DEX).
2. De temps en temps, vérifiez vos autorisations de tokens et révoquez (annulez) celles dont vous n'avez plus besoin. Une révocation coûte de petits frais.
3. Sur un ordinateur partagé, déconnectez-vous de l'extension.

Vous pouvez suivre les tokens achetés dans [votre portefeuille]({lang}/me/) et voir les données des memecoins en direct sur notre [page memecoins]({lang}/memes/).

> **⚠️ Attention**
> - **Un site ou un « support » demande votre mot de passe de récupération, votre phrase de récupération ou une « synchronisation du wallet ».** Aucun vrai DEX ni employé de Binance ne le fait jamais. Fermez la page.
> - **Autorisations illimitées et signatures à l'aveugle.** Une autorisation ou une signature malveillante peut permettre à un escroc de vider ce token plus tard, sans nouvelle confirmation de votre part.
> - **Mauvais réseau, memo oublié ou adresse collée qui a changé.** Un logiciel malveillant peut remplacer une adresse copiée. Comparez à chaque fois les premiers et derniers caractères, et testez avec un petit montant.

Prochaine leçon : comment vérifier un memecoin avant d'acheter. Toutes les leçons sont sur la [page Apprendre]({lang}/learn/).

## Sources

- [Binance : What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy : How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance : How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US : How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*Ceci n'est pas un conseil en investissement. Ce guide explique le fonctionnement des outils et ne recommande d'acheter aucun token. Binance Wallet peut ne pas être disponible dans tous les pays.*
