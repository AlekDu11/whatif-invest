---
title: Celestia (TIA) expliqué simplement : un réseau de données pour les rollups, actif depuis 2023, 1 milliard de jetons au lancement
description: Celestia expliqué simplement : sa couche de disponibilité des données, l'usage du TIA, les baisses d'émission, son histoire, ses rivaux, ses risques.
date: 2026-11-24
kind: analysis
---
**Celestia** est une blockchain qui n'a qu'un seul travail, bien précis : elle stocke et publie les données de transactions d'autres blockchains, surtout des « rollups », pour que chacun puisse les vérifier. Lancée en octobre 2023 comme le premier réseau « modulaire » de ce type, elle a un jeton, le TIA, qui vaut {{mcap:tia}} au total ({{rank:tia}} parmi les cryptomonnaies). Ceux qui la suivent parient que beaucoup de futures blockchains loueront ce service plutôt que de construire le leur.

> **À retenir**
> - Celestia ne fait tourner ni applications ni contrats intelligents : elle garantit seulement que les données ont été publiées, et vend cet espace contre du TIA.
> - Au lancement, il existait 1 milliard de TIA ; il n'y a pas de plafond fixe, mais l'émission annuelle a été réduite d'environ 7,2 % à environ 5 % en juillet 2025, puis à environ 2,5 % en novembre 2025.
> - Son record est de {{ath:tia}} ({{athd:tia}}) ; aujourd'hui le cours est à {{fromath:tia}} de ce niveau.
> - D'importants déblocages de jetons pour les premiers investisseurs et l'équipe, à partir d'octobre 2024, ont lourdement pesé sur le cours.

## Comment il fonctionne

Les rollups sont des réseaux qui traitent eux-mêmes les transactions, puis publient un enregistrement compressé de celles-ci sur une autre chaîne. Celestia est un endroit où publier cet enregistrement. Les rollups paient pour placer des « blobs » de données dans les blocs de Celestia, et le réseau s'assure que les données sont bien là. Son astuce principale est l'échantillonnage de disponibilité des données : un nœud léger sur un téléphone ou un ordinateur portable ordinaire télécharge quelques petits morceaux aléatoires d'un bloc et, s'ils sont tous présents, peut être quasi certain que le bloc entier a été publié. Celestia est construite avec le Cosmos SDK et sécurisée par preuve d'enjeu (proof of stake). La mise à jour Matcha, fin 2025, a porté la taille maximale d'un bloc de 8 Mo à 128 Mo.

## À quoi sert le jeton

Le TIA a trois usages. Les rollups et les applications paient en TIA l'espace de blobs qu'ils utilisent. Les détenteurs mettent leurs TIA en staking auprès de validateurs, qui produisent les blocs, et reçoivent en récompense des jetons nouvellement émis. Enfin, les détenteurs de TIA votent sur les changements du réseau, comme les deux baisses d'émission. La demande pour le jeton dépend donc du nombre de rollups qui choisissent vraiment Celestia et de la quantité de données qu'ils publient.

## Les chiffres actuels

- Cours actuel : {{price:tia}}
- Record : {{ath:tia}} ({{athd:tia}}), {{fromath:tia}} depuis
- Valeur de marché : {{mcap:tia}} ({{rank:tia}} parmi les cryptomonnaies)
- Variation du cours sur 12 mois : {{chg1y:tia}}
- 10 $ par jour pendant 3 ans : {{dca:tia:3}} pour {{dcainv:3}} investis ({{dcaroi:tia:3}})

## Son histoire

L'idée est née en 2019 sous le nom de LazyLedger, un article de recherche de Mustafa Al-Bassam ; le projet a été rebaptisé Celestia en 2021. Le Mainnet Beta a démarré le 31 octobre 2023, avec un important airdrop de TIA pour les développeurs et les utilisateurs. Lors de la hausse des cryptos de 2024, le cours est monté à environ 20 $ en février 2024. À partir d'octobre 2024 sont arrivés de gros déblocages pour les premiers soutiens, et en juin 2025 le TIA était tombé à environ 1,32 $, soit une chute d'environ 93 % ; il a continué de glisser en 2026. Le cofondateur Mustafa Al-Bassam affirmait alors que le projet disposait d'un trésor de guerre de 100 millions de dollars et de six ans de financement. Les mises à jour Lotus (juillet 2025) et Matcha (novembre 2025) ont réduit l'émission étape par étape vers un taux de long terme de 1,5 % par an.

## Alternatives

Le principal rival de Celestia est [Ethereum]({lang}/eth/) lui-même : depuis mars 2024, Ethereum dispose de son propre espace de « blobs », moins cher, pour les rollups. Parmi les autres réseaux de disponibilité des données figurent [Avail]({lang}/avail/), EigenDA d'[EigenCloud]({lang}/eigen/) et la couche de données de NEAR ([NEAR]({lang}/near/)). Beaucoup de rollups, comme [Arbitrum]({lang}/arb/) et [Optimism]({lang}/op/), publient toujours leurs données sur Ethereum.

## Principaux risques

- **Concurrence :** les blobs d'Ethereum, Avail et EigenDA se disputent les mêmes clients, ce qui maintient les frais bas.
- **Peu de revenus de frais :** pour l'instant, les rollups paient peu par rapport à la valeur du réseau.
- **Hausse de l'offre :** il n'y a pas de plafond fixe, et de nouveaux TIA sont émis en continu pour les stakers.
- **Déblocages et concentration :** les premiers investisseurs, l'équipe et la fondation détiennent de grosses parts, et leurs ventes peuvent faire bouger le cours.
- **Fortes variations :** le TIA a perdu plus de 90 % depuis son pic de 2024 en environ 16 mois.

## Ce que cela signifie si vous achetez régulièrement

La courte histoire du TIA est surtout une longue baisse après un pic précoce, ponctuée de rebonds brutaux. Acheter un montant fixe à intervalles réguliers étale le prix d'entrée dans le temps, mais ne vous protège pas si l'adoption ne vient jamais — et pour un jeton aussi jeune, trois ans d'historique disent peu de choses sur les trois suivants. Beaucoup limitent ce genre de cryptos à une petite part de leur épargne. Les performances passées ne garantissent pas les performances futures.

*Ceci n'est pas un conseil en investissement.*

## Sources

- [Staking, gouvernance et offre (documentation Celestia)](https://docs.celestia.org/learn/TIA/staking-governance-supply/)
- [La mise à jour Matcha : vers des blocs de 128 Mo (blog Celestia)](https://blog.celestia.org/matcha/)
- [Le cofondateur de Celestia évoque un trésor de guerre de 100 millions de dollars (The Block, juin 2025)](https://www.theblock.co/post/359387/celestia-co-founder-cites-100-million-war-chest-and-six-year-runway-to-play-the-long-game-as-native-token-drops-over-90-from-peak)
