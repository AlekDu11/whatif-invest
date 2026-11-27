---
title: "Double authentification (2FA) : comment l'activer, étape par étape"
description: La 2FA ajoute un second verrou à votre compte. Activer une appli d'authentification ou une passkey pas à pas, et pourquoi le SMS est le plus faible.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: 68 M$
stat_label: perdus en 2021 à cause des fraudes au SIM swap, sur 1 611 plaintes reçues par le FBI (IC3, février 2022)
---
**Qu'est-ce que la 2FA et comment l'activer ?** La double authentification (2FA, ou authentification à deux facteurs) signifie que pour vous connecter ou retirer de l'argent, il faut deux choses : votre mot de passe *et* une seconde preuve, comme un code à 6 chiffres affiché par une appli sur votre téléphone ou une passkey (votre empreinte digitale ou votre visage). Activez-la dans les paramètres **Security** (Sécurité) de votre plateforme d'échange et choisissez une appli d'authentification ou une passkey plutôt que le SMS.

> **À retenir**
> - Avec la 2FA, un mot de passe volé ne suffit pas à vider votre compte.
> - **Les codes SMS sont l'option la plus faible :** lors d'un « SIM swap » (échange de carte SIM), un escroc transfère votre numéro de téléphone sur sa propre carte SIM et reçoit vos codes. Le FBI a enregistré 1 611 plaintes de ce type et plus de **68 millions de dollars** de pertes en 2021, contre 320 plaintes et environ 12 millions de dollars sur 2018–2020.
> - Le FBI recommande des options plus solides : une appli d'authentification, la biométrie ou une clé de sécurité physique.

## Les options, de la plus faible à la plus solide

- **Code par SMS** — un SMS avec un code. Mieux que rien, mais votre numéro de téléphone peut être volé.
- **Code par e-mail** — aussi sûr que votre compte e-mail, pas plus (protégez-le lui aussi avec la 2FA).
- **Appli d'authentification** (Google Authenticator, Microsoft Authenticator et autres) — l'appli génère un nouveau code à 6 chiffres toutes les 30 secondes, même hors ligne. Personne ne peut l'intercepter via votre opérateur téléphonique.
- **Passkey** (clé d'accès, biométrie) — vous confirmez avec votre empreinte, votre visage ou le code PIN de votre téléphone. Elle ne fonctionne que sur le vrai site : un faux site ne peut pas la voler.
- **Clé de sécurité physique** (un petit appareil USB/NFC) — la plus solide, idéale pour les gros montants.

## Pas à pas : appli d'authentification (exemple avec l'appli Binance)

Les autres plateformes suivent presque les mêmes étapes ; cherchez **Security** (Sécurité) dans votre profil.

1. **Étape 1 — Installez l'appli.** Téléchargez Google Authenticator (ou une autre appli d'authentification) depuis l'App Store ou Google Play officiels.
2. **Étape 2 — Ouvrez les paramètres de sécurité.** Dans l'appli Binance, touchez l'icône **Account**, touchez votre profil en haut, puis **Security**.
3. **Étape 3 — Lancez la configuration.** Touchez **Authenticator App**, puis **Enable**. Vous voyez un QR code et une **setup key** (clé de configuration, un long code).
4. **Étape 4 — Notez la clé de configuration sur papier.** C'est votre solution de secours si vous perdez votre téléphone. Gardez-la hors ligne, comme une seed phrase. Ne touchez pas encore **Next**.
5. **Étape 5 — Ajoutez le compte dans l'appli d'authentification.** Dans Google Authenticator, touchez **+**, choisissez **Enter a setup key** (Saisir une clé de configuration) ou scannez le QR code, collez la clé, donnez un nom comme « Binance » et touchez **Add**.
6. **Étape 6 — Confirmez.** De retour dans Binance, touchez **Next** et tapez le code à 6 chiffres affiché par l'appli. Un message de réussite s'affiche.
7. **Étape 7 — Testez.** Déconnectez-vous puis reconnectez-vous. Si on vous demande le code, tout fonctionne.

## Pas à pas : passkey (encore plus simple)

Selon la page d'aide de Binance, il faut l'appli en version 2.60 ou plus, iOS 16+ ou Android 9+.

1. **Account → profil → Security → Passkeys (Biometrics) → Add Passkey.**
2. Confirmez avec votre 2FA actuelle si on vous le demande, puis touchez **Continue**.
3. Choisissez où l'enregistrer : Trousseau iCloud (iPhone), Gestionnaire de mots de passe de Google (Android) ou une clé de sécurité, et confirmez avec votre empreinte, votre visage ou votre code PIN.

## Une fois la 2FA activée

- Désactivez le SMS comme méthode de connexion si la plateforme le permet, ou au moins demandez à votre opérateur un verrouillage de la carte SIM / un code de portabilité protégé.
- Protégez aussi par la 2FA l'adresse e-mail liée à la plateforme.
- Activez une **liste blanche de retrait** (seules les adresses enregistrées peuvent recevoir) si votre plateforme la propose.

> **⚠️ Attention**
> - **Personne de légitime ne vous demande votre code 2FA.** Un « support » sur Telegram, un appel de « la plateforme » ou de « la banque » qui réclame le code à 6 chiffres, c'est toujours un escroc.
> - **Perdre son téléphone sans la clé de secours.** La récupération prend alors des jours de vérifications d'identité. Écrivez la clé de configuration sur papier et rangez-la en lieu sûr.
> - **Fausses applis d'authentification et pages de connexion imitées.** N'installez des applis que depuis la boutique officielle et tapez vous-même l'adresse de la plateforme, ou utilisez un favori.

## Ce que cela signifie si vous achetez régulièrement

Si vous achetez un peu chaque mois, votre compte sur la plateforme devient peu à peu une vraie somme — par exemple, le bitcoin vaut {{price:btc}} en ce moment ({{chg1y:btc}} sur 12 mois), ce sont des résultats passés, pas une prévision. Dix minutes de configuration de la 2FA protègent des années d'achats. Suivez ce que vous détenez sur votre [page portefeuille]({lang}/me/).

Leçon précédente : [seed phrase : 5 règles pour la protéger]({lang}/blog/seed-phrase-safety-rules/). Pour aller plus loin : [comment s'inscrire sur une plateforme crypto]({lang}/blog/how-to-register-on-a-crypto-exchange/), [les plateformes qui fonctionnent dans votre pays]({lang}/exchanges/). Toutes les leçons sont sur la [page Apprendre]({lang}/learn/).

## Sources

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8 février 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app (mis à jour le 10 décembre 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account (mis à jour le 10 décembre 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Ceci n'est pas un conseil en investissement.*
