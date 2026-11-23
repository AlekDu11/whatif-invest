---
title: Arbitrum (ARB) expliqué simplement : couche 2 d'Ethereum, optimistic rollup et 10 milliards d'ARB au maximum
description: Arbitrum en clair : comment fonctionne cette couche 2 d'Ethereum, à quoi sert l'ARB dans la DAO, les déblocages de jetons, son histoire et ses risques.
date: 2026-11-23
kind: analysis
---
**Arbitrum** est un réseau construit au-dessus d'Ethereum qui rend les transactions plus rapides et bien moins chères tout en s'appuyant sur Ethereum pour sa sécurité : c'est ce qu'on appelle une « couche 2 ». Il a été créé par la société américaine Offchain Labs, et son jeton **ARB** permet à ses détenteurs de voter sur la gestion du réseau et de sa trésorerie. L'ARB vaut aujourd'hui {{mcap:arb}} ({{rank:arb}} parmi les cryptomonnaies).

> **À retenir**
> - Il n'y aura jamais plus de 10 milliards d'ARB ; au lancement, en mars 2023, environ 42 % sont allés à la trésorerie de la DAO, environ 27 % à l'équipe et 17,5 % aux investisseurs.
> - Son record est de {{ath:arb}} ({{athd:arb}}) ; aujourd'hui, le cours est {{fromath:arb}} par rapport à ce sommet.
> - L'ARB est un jeton de gouvernance : les frais sur Arbitrum se paient en ETH, pas en ARB.
> - Des jetons de l'équipe et des investisseurs sont débloqués chaque mois depuis mars 2024, ce qui ajoute une nouvelle offre sur le marché.

## Comment il fonctionne

Arbitrum est un **optimistic rollup**. Au lieu que chaque nœud d'Ethereum traite chaque transaction, Arbitrum les exécute sur sa propre chaîne et publie sur Ethereum des lots de données compressés. Un opérateur unique, le **séquenceur** (géré par Offchain Labs), met les transactions dans l'ordre et les confirme en une fraction de seconde. Les résultats sont présumés corrects (« de façon optimiste ») tant que personne ne les conteste : n'importe quel validateur peut soumettre une **preuve de fraude**, et le litige est tranché sur Ethereum. Depuis février 2025, le protocole **BoLD** permet à chacun de participer à la validation, et un seul validateur honnête suffit à défendre la chaîne. Le logiciel **Nitro** est compatible avec les applications Ethereum, et le programme **Orbit** permet à d'autres projets de lancer leurs propres chaînes sur la technologie Arbitrum.

## À quoi sert le jeton

L'ARB est avant tout un jeton de vote. Les détenteurs, ou les délégués qu'ils choisissent, votent au sein de la **DAO Arbitrum** sur les mises à jour du réseau et sur l'utilisation de la trésorerie, qui détient des milliards d'ARB ainsi que les revenus des frais du séquenceur. Il n'est pas nécessaire d'avoir de l'ARB pour utiliser Arbitrum : le gaz se paie en ETH. La valeur du jeton dépend donc des droits de vote et de ce que la DAO décide de faire de son argent, et non directement de l'usage du réseau.

## Les chiffres actuels

- Cours actuel : {{price:arb}}
- Record : {{ath:arb}} ({{athd:arb}}), {{fromath:arb}} depuis
- Valeur de marché : {{mcap:arb}} ({{rank:arb}} parmi les cryptomonnaies)
- Variation du cours sur 12 mois : {{chg1y:arb}}
- 10 $ par jour pendant 3 ans : {{dca:arb:3}} pour {{dcainv:3}} investis ({{dcaroi:arb:3}})

## Son histoire

Offchain Labs est née de recherches menées à l'université de Princeton. Arbitrum One s'est ouvert au public fin août 2021, et la mise à jour Nitro d'août 2022 a réduit les frais et augmenté la capacité. Le 23 mars 2023, le jeton ARB a été lancé avec un important airdrop pour les utilisateurs. Quelques jours plus tard, la première proposition, AIP-1, a provoqué un tollé, car la Fondation avait déjà commencé à utiliser une enveloppe de 750 millions d'ARB avant le vote ; elle a ensuite scindé la proposition et donné plus de contrôle à la DAO. L'ARB a atteint son sommet, environ 2,39 $, en janvier 2024. Le 16 mars 2024, environ 1,1 milliard de jetons de l'équipe et des investisseurs ont été débloqués, suivis de déblocages mensuels. En 2025, BoLD a été activé, et le cours a fortement baissé au cours de 2025 et 2026.

## Alternatives

Arbitrum est en concurrence avec d'autres réseaux de couche 2 d'Ethereum : [Optimism]({lang}/op/) et les chaînes bâties sur son OP Stack, dont Base de Coinbase, qui n'a pas de jeton propre ; les rollups à preuve à divulgation nulle comme [ZKsync]({lang}/zk/) et [Starknet]({lang}/strk/) ; ainsi que [Mantle]({lang}/mnt/) et [POL (ex-MATIC)]({lang}/pol/). [Ethereum]({lang}/eth/) lui-même est aussi une alternative, puisque ses propres mises à jour le rendent de moins en moins cher à utiliser.

## Principaux risques

- **Nouvelle offre :** les déblocages pour l'équipe et les investisseurs se poursuivent, et la trésorerie de la DAO détient une grande partie de tous les ARB.
- **Séquenceur centralisé :** un seul opérateur ordonne les transactions ; s'il tombe en panne ou agit mal, les utilisateurs dépendent de voies de secours plus lentes.
- **Concurrence :** Base et les autres couches 2 se disputent les mêmes utilisateurs, applications et frais.
- **Lien faible avec l'usage :** les frais se paient en ETH, donc une forte utilisation d'Arbitrum n'augmente pas automatiquement la demande d'ARB.
- **Réglementation :** les règles sur les jetons, les DAO et les sociétés qui les portent peuvent changer d'un pays à l'autre.

## Ce que cela signifie si vous achetez régulièrement

L'ARB a passé l'essentiel de son existence à baisser depuis son premier sommet : un acheteur régulier a donc accumulé de plus en plus de jetons à des prix plus bas, ce qui n'aide que si le cours se redresse. Acheter un montant fixe à intervalles réguliers lisse le risque de mauvais timing, mais n'élimine pas le risque de pertes. Beaucoup gardent ce type de jetons comme une petite part de leur épargne. Les performances passées ne préjugent pas des performances futures.

*Ceci n'est pas un conseil en investissement.*

## Sources

- [A gentle introduction to Arbitrum (documentation Arbitrum)](https://docs.arbitrum.io/intro/)
- [A gentle introduction to the Arbitrum DAO (Arbitrum Foundation)](https://docs.arbitrum.foundation/gentle-intro-dao-governance)
- [Offchain Labs releases Arbitrum BoLD on mainnet (The Block, 12 février 2025)](https://www.theblock.co/post/340278/offchain-labs-releases-arbitrum-bold-on-mainnet-for-permissionless-validation)
- [Arbitrum price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/arbitrum)
