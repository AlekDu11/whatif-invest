---
title: Pearl (PEARL) expliqué : du minage sur GPU en Proof of Useful Work, 2,1 milliards maximum
description: Pearl expliqué simplement : un minage sur GPU lié au calcul d'IA, 2,1 milliards de jetons, un lancement en avril 2026, les critiques, rivaux et risques.
date: 2026-11-28
kind: analysis
---
**Pearl** est une nouvelle blockchain de couche 1 minée avec des cartes graphiques Nvidia. Au lieu des énigmes de hachage inutiles que résolvent les mineurs de Bitcoin, sa « preuve de travail utile » (Proof of Useful Work) demande de multiplier des matrices — les calculs mêmes qui font tourner les modèles d'IA —, si bien qu'en théorie un GPU peut à la fois servir des clients d'IA et sécuriser le réseau. Elle a été créée par Pearl Research Labs, cofondée par l'informaticien Omri Weinstein, et son réseau principal a démarré le 27 avril 2026. Sa valeur de marché est aujourd'hui de {{mcap:pearl}} ({{rank:pearl}} parmi les cryptomonnaies).

> **À retenir**
> - Il n'existera jamais plus de 2,1 milliards de jetons, 100 fois les 21 millions de Bitcoin ; la récompense de minage baisse en douceur, sans halving.
> - Son record est de {{ath:pearl}} ({{athd:pearl}}) ; le cours actuel se situe {{fromath:pearl}} par rapport à ce sommet.
> - Le projet affirme qu'il n'y a eu ni préminage, ni part pour les investisseurs, ni trésorerie de l'équipe : tous les jetons viennent du minage.
> - Une étude de juin 2026 a conclu que le minage de l'époque ne produisait aucun travail d'IA utile.

## Comment il fonctionne

Les mineurs effectuent sur leurs GPU des multiplications de matrices « bruitées », hachent de petits morceaux du résultat et emballent le travail dans une preuve à divulgation nulle de connaissance, pour que chacun puisse le vérifier vite sans le refaire. La méthode vient d'un article de cryptographie de 2025 cosigné par Weinstein. Le mineur officiel se branche sur vLLM, un logiciel répandu pour faire tourner des modèles d'IA, sur des cartes de centre de données comme les Nvidia H100 et H200, tandis que des mineurs créés par la communauté tournent aussi sur des cartes RTX de jeu. Sous le capot, Pearl ressemble à Bitcoin : il repose sur btcd, un logiciel de nœud Bitcoin, et un nouveau bloc arrive toutes les quelques minutes. Le jeton est souvent coté sous le symbole PRL, et sur certains sites de cours un autre jeton sans lien porte le même symbole.

## À quoi sert le jeton

Les jetons ne sont créés qu'en récompense pour les mineurs et servent à payer les frais de transaction. Le premier exemple commercial est arrivé en mai 2026 : la société de cloud d'IA Together AI a proposé un modèle Gemma tournant sur des mineurs Pearl à plus de 25 % sous son prix habituel, la remise étant financée par des récompenses en PRL. Si les clients de l'IA utilisent vraiment le réseau ainsi, le minage n'est plus une simple dépense d'énergie ; sinon, Pearl n'est qu'un jeton en preuve de travail de plus, avec une offre abondante.

## Les chiffres actuels

- Cours actuel : {{price:pearl}}
- Record : {{ath:pearl}} ({{athd:pearl}}), {{fromath:pearl}} depuis
- Valeur de marché : {{mcap:pearl}} ({{rank:pearl}} parmi les cryptomonnaies)
- Variation du cours sur 12 mois: {{chg1y:pearl}}

## Son histoire

L'article de base est paru en avril 2025, et le réseau principal a démarré le 27 avril 2026 sans aucun jeton distribué à l'avance. Fin mai, après l'accord avec Together AI, une ruée de joueurs et de propriétaires de GPU s'est mise à miner, et en quelques semaines le gain quotidien d'une RTX 5090 a été divisé environ par deux avec la concurrence. Au début, le jeton ne s'échangeait que sur de petites plateformes peu liquides comme MEXC. En juin 2026, un article sur arXiv, « The Usefulness Gap in Proof-of-Useful-Work », a rapporté que les milliers de mineurs du réseau ne produisaient aucun calcul d'IA utile et que le logiciel de minage le plus utilisé ne contenait même pas de code d'IA. Pearl a ajouté la prise en charge des modèles d'IA de type mixture-of-experts lors d'un hard fork en juin, et en octobre 2026 environ 16 % de l'offre maximale avait été minée.

## Alternatives

[Bitcoin]({lang}/btc/) est le jeton classique en preuve de travail, miné avec des puces spécialisées et non des GPU. Parmi les projets d'IA et de calcul, [Bittensor]({lang}/tao/) récompense ceux qui font tourner des modèles d'IA, tandis que [Render]({lang}/render/), [Akash Network]({lang}/akt/) et [io.net]({lang}/io/) louent directement de la puissance GPU. L'idée de Pearl est différente : le minage lui-même doit être le travail d'IA utile.

## Principaux risques

- **Très récent :** le jeton n'a que quelques mois d'historique de cours, et les jeunes jetons peuvent perdre vite l'essentiel de leur valeur.
- **Utilité non prouvée :** des chercheurs indépendants ont trouvé peu de vrai travail d'IA jusqu'ici ; la promesse centrale pourrait ne pas tenir.
- **Économie du minage :** la hausse de la difficulté et la baisse de la récompense rognent les gains, et les mineurs vendent souvent des jetons pour payer l'électricité.
- **Concentration :** miner était bon marché les premières semaines, donc les premiers participants détiennent une grosse part.
- **Liquidité et homonymes :** les échanges sont plus faibles que pour les grands jetons, et un autre jeton utilise le même symbole PRL — vérifiez bien le contrat et la plateforme.

## Ce que cela signifie si vous achetez régulièrement

Pearl n'est coté que depuis quelques mois : il n'existe pas encore d'historique parlant pour des achats réguliers. Investir un montant fixe à intervalles réguliers répartit le risque de mal choisir son moment, mais avec un jeton tout neuf cela n'élimine pas le risque de perdre l'essentiel de la mise. Beaucoup limitent ce genre de jetons expérimentaux à une toute petite part de leur épargne. Les performances passées ne préjugent pas des performances futures.

*Ceci n'est pas un conseil en investissement.*

## Sources

- [What is Pearl blockchain? How it uses GPU mining to price AI compute (KuCoin, October 2026)](https://www.kucoin.com/blog/pearl-blockchain-ai-mining-prl-token)
- [New AI-compute cryptocurrency Pearl sparks a GPU mining rush, but profitability is sliding (Tom's Hardware, 31 May 2026)](https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding)
- [Pearl (PRL): the AI-compute cryptocurrency (Hashrate Index, June 2026)](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
- [The Usefulness Gap in Proof-of-Useful-Work (arXiv 2606.04819, June 2026)](https://arxiv.org/abs/2606.04819)
