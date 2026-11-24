---
title: Kaspa (KAS) expliqué simplement : un blockDAG en preuve de travail depuis 2021, 10 blocs par seconde et 28,7 milliards au maximum
description: Kaspa expliqué simplement : blockDAG et GHOSTDAG, un lancement équitable sans pré-minage, les mises à jour Crescendo et Toccata, son histoire et ses risques.
date: 2026-11-24
kind: analysis
---
**Kaspa** est une cryptomonnaie en preuve de travail, minée comme le bitcoin, mais conçue pour être bien plus rapide : au lieu d'une seule chaîne de blocs, elle utilise un « blockDAG » où de nombreux blocs peuvent s'ajouter en même temps. Elle a été lancée en novembre 2021 sans pré-minage ni vente de jetons, et sa monnaie **KAS** vaut {{mcap:kas}} aujourd'hui ({{rank:kas}} parmi les cryptomonnaies).

> **À retenir**
> - Il n'y aura jamais plus d'environ 28,7 milliards de KAS, et environ 97 % d'entre eux étaient déjà minés fin 2026.
> - Son record est de {{ath:kas}} ({{athd:kas}}) ; aujourd'hui, le cours est {{fromath:kas}} par rapport à ce sommet.
> - Depuis la mise à jour Crescendo de mai 2025, le réseau produit 10 blocs par seconde au lieu d'un.
> - Kaspa n'a eu ni pré-minage, ni prévente, ni pièces réservées à ses fondateurs : chaque KAS provient du minage.

## Comment il fonctionne

Avec le bitcoin, si deux mineurs trouvent un bloc au même moment, l'un des deux est rejeté ; les blocs doivent donc être lents (environ toutes les 10 minutes). Kaspa conserve tous ces blocs parallèles et les relie dans un graphe, un **blockDAG** (graphe orienté acyclique). Son protocole **GHOSTDAG**, issu des recherches universitaires de Yonatan Sompolinsky et Aviv Zohar, range ensuite tous les blocs et transactions dans un ordre commun. Kaspa peut ainsi créer des blocs très souvent et confirmer les paiements en quelques secondes, tout en gardant un minage à la bitcoin avec son propre algorithme kHeavyHash. L'émission baisse en douceur : la récompense diminue un peu chaque mois et se divise par deux environ une fois par an.

## Pourquoi on lui prête de la valeur

Ses partisans voient Kaspa comme un « argent numérique rapide » : il garde ce qu'on aime dans le bitcoin — preuve de travail, offre fixe, aucune entreprise et aucune pièce distribuée à l'avance — mais les paiements se règlent en secondes plutôt qu'en minutes. Le lancement équitable compte pour beaucoup de détenteurs, car aucune équipe ni aucun fonds n'a reçu de pièces bon marché à revendre plus tard. En 2026, le réseau a aussi commencé à devenir programmable : la mise à jour Toccata a apporté les « covenants » (des règles sur la façon de dépenser les pièces), la vérification de preuves à divulgation nulle et des jetons natifs, ce qui pourrait permettre de bâtir des applications sur Kaspa.

## Les chiffres actuels

- Cours actuel : {{price:kas}}
- Record : {{ath:kas}} ({{athd:kas}}), {{fromath:kas}} depuis
- Valeur de marché : {{mcap:kas}} ({{rank:kas}} parmi les cryptomonnaies)
- Variation du cours sur 12 mois : {{chg1y:kas}}
- 10 $ par jour pendant 3 ans : {{dca:kas:3}} pour {{dcainv:3}} investis ({{dcaroi:kas:3}})

## Son histoire

Kaspa est né de la recherche et de la société DAGlabs ; son réseau principal a démarré le 7 novembre 2021. La première année, il ne s'échangeait que sur de petites plateformes pour des fractions de centime. En 2023, de plus grandes plateformes l'ont listé et le cours s'est multiplié jusqu'à son record d'environ 0,21 $ à la mi-2024. Les développeurs ont réécrit le logiciel du nœud en Rust (« Rusty Kaspa »), ce qui a rendu possible le saut de vitesse : le 5 mai 2025, le hard fork Crescendo a fait passer le réseau d'un à dix blocs par seconde. Le cours a fortement chuté en 2025 et 2026, et en 2026 le hard fork Toccata a fait de Kaspa une couche 1 programmable.

## Alternatives

Kaspa concurrence surtout d'autres monnaies de paiement en preuve de travail comme [Bitcoin]({lang}/btc/), [Litecoin]({lang}/ltc/) et [Bitcoin Cash]({lang}/bch/). Pour des transferts rapides et bon marché et pour les applications, on utilise aussi des réseaux en preuve d'enjeu comme [Solana]({lang}/sol/), et pour les paiements du quotidien beaucoup se servent simplement de stablecoins en dollars.

## Principaux risques

- **Fortes variations :** le KAS a déjà perdu plus de 80 % depuis son record de 2024 ; cela peut se reproduire.
- **Minage concentré :** quelques grands pools et fabricants d'ASIC contrôlent une grande partie de la puissance de calcul.
- **Petite équipe :** le développement repose sur un groupe de développeurs principaux financés surtout par des dons de la communauté, pas sur une grande entreprise.
- **Adoption :** la vitesse seule ne crée pas de demande ; les applications Toccata et les vrais paiements doivent encore s'imposer.
- **Accès au marché :** une grande partie des échanges se fait sur des plateformes de taille moyenne, et les règles sur les cryptos peuvent changer selon les pays.

## Ce que cela signifie si vous achetez régulièrement

Kaspa est une monnaie jeune aux hausses et aux baisses très brutales. Acheter un montant fixe régulièrement répartit votre prix d'entrée entre bons et mauvais mois, mais ne protège pas d'un long repli. La plupart des KAS sont déjà minés : les mouvements futurs du cours dépendront surtout de la demande. Beaucoup ne gardent ce type de monnaie que comme une petite part de leurs cryptos. Les performances passées ne garantissent pas les performances futures.

*Ceci n'est pas un conseil en investissement.*

## Sources

- [Kaspa — official website (kaspa.org)](https://kaspa.org/)
- [PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus — Sompolinsky, Wyborski, Zohar (IACR ePrint 2018/104)](https://eprint.iacr.org/2018/104.pdf)
- [Kaspa Covenants++ «Toccata» hard-fork outlook — Michael Sutton, Kaspa core developer (Medium)](https://medium.com/@michaelsuttonil/kaspa-covenants-toccata-hard-fork-outlook-a4d81a40900c)
- [Kaspa price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/kaspa)
