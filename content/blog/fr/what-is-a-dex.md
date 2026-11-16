---
title: Qu'est-ce qu'un DEX et quelle différence avec une plateforme d'échange crypto ?
description: Qu'est-ce qu'un DEX ? Le guide simple des exchanges décentralisés : AMM, pools de liquidité, wallets, frais de gas, avantages et inconvénients face à un CEX.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**Qu'est-ce qu'un DEX ?** Un DEX (exchange décentralisé) est un ensemble de smart contracts sur une blockchain qui vous permet d'échanger un token contre un autre directement depuis votre propre wallet. Aucune entreprise ne garde votre argent, pas de compte et généralement pas de vérification d'identité. Uniswap sur Ethereum, ainsi que Raydium, Orca et Meteora sur Solana, en sont des exemples connus.

Une plateforme d'échange crypto classique comme Binance, Coinbase ou Kraken est un **CEX** (exchange centralisé) : une entreprise qui conserve vos fonds, met en relation acheteurs et vendeurs dans son propre système et doit respecter les règles financières.

## Comment fonctionne un DEX

### Les teneurs de marché automatisés (AMM)

La plupart des DEX n'ont pas de carnet d'ordres avec des acheteurs et des vendeurs. Ils utilisent à la place un **teneur de marché automatisé** (AMM) : une formule qui fixe le prix.

La version classique, utilisée par Uniswap v2, est la règle du « produit constant » : un pool contient deux tokens, et la quantité du token A multipliée par la quantité du token B doit rester la même après chaque échange. Quand vous achetez le token A, vous ajoutez du token B dans le pool et en retirez du token A : A devient plus rare dans le pool et son prix monte.

Pas besoin de faire le calcul. L'idée clé : **plus le pool est gros, moins votre transaction fait bouger le prix.**

### Les pools de liquidité

Les tokens du pool proviennent des **fournisseurs de liquidité** : des personnes qui déposent des paires de tokens et touchent une part des frais de trading (souvent 0,05 à 1 % par swap). Leur risque : que les prix des deux tokens s'écartent, ce qui peut les laisser moins bien lotis que s'ils avaient simplement conservé leurs tokens (« perte impermanente »).

Pour les tokens tout juste lancés, c'est généralement le créateur qui met en place le premier pool. C'est pour cela que le verrouillage de la liquidité compte : celui qui contrôle le pool peut le retirer.

### Votre wallet est votre compte

Pour utiliser un DEX, vous connectez un wallet en auto-garde comme MetaMask (Ethereum et réseaux similaires) ou Phantom (Solana). Chaque échange est une transaction que vous signez vous-même. Votre **phrase de récupération** est la clé maîtresse : perdez-la et l'argent est perdu ; partagez-la et quelqu'un d'autre le prend.

### Gas et frais

Chaque échange sur un DEX paie des frais de réseau, appelés **gas** sur Ethereum. Sur Ethereum, ils augmentent quand le réseau est chargé ; les réseaux de couche 2 et Solana sont généralement bien moins chers : les frais de base de Solana sont de 0,000005 SOL par signature. En plus du gas, vous payez les frais du pool, et vous pouvez subir du **slippage** et de l'**impact sur le prix** sur les petits tokens ou ceux qui bougent vite.

## DEX vs CEX : les principales différences

- **Qui détient vos fonds :** sur un DEX, vous (votre wallet) ; sur un CEX, la plateforme.
- **Compte et vérification d'identité :** un DEX n'en demande généralement pas ; un CEX exige une vérification d'identité (KYC).
- **Choix de tokens :** un DEX propose presque n'importe quel token, y compris les tout nouveaux ; un CEX ne liste que des tokens sélectionnés.
- **Achat par carte ou virement :** généralement impossible directement sur un DEX ; standard sur un CEX.
- **Frais :** DEX, gas, frais du pool et slippage ; CEX, frais de trading, spread et frais de retrait.
- **Aide en cas de problème :** un DEX n'a pas de service client ; un CEX a un support et parfois des mécanismes de protection.
- **Principaux risques :** DEX, tokens frauduleux, autorisations dangereuses et vos propres erreurs ; CEX, piratages, gels de compte et faillite.

## Les avantages d'un DEX

- **Auto-garde.** Personne ne peut geler votre compte ni perdre votre argent dans une faillite.
- **Accès ouvert.** Toute personne disposant d'un wallet peut trader, depuis presque n'importe où.
- **Les nouveaux tokens d'abord.** Les tokens apparaissent sur les DEX bien avant tout listing sur une plateforme (ou à la place).
- **Transparence.** Les pools, les transactions et les détenteurs sont visibles sur la blockchain.

## Les inconvénients d'un DEX

- **Vous êtes la banque.** Une erreur (mauvaise adresse, faux site, autorisation malveillante) et les fonds sont perdus pour de bon.
- **Tokens frauduleux.** N'importe qui peut créer un token et un pool en quelques minutes. La plupart des nouveaux tokens perdent presque toute leur valeur ; voir notre [checklist anti-rug pull]({lang}/blog/how-to-spot-a-rug-pull/).
- **Coûts cachés.** Le slippage et l'impact sur le prix peuvent coûter plus cher que les frais affichés.
- **Pas de porte d'entrée simple.** Il faut généralement acheter des cryptos sur un CEX d'abord, puis les envoyer vers votre wallet.
- **Risque lié aux smart contracts.** Des bugs ou des piratages dans le code des DEX ont causé de lourdes pertes.

## Lequel choisir quand on débute ?

Beaucoup de gens utilisent les deux : un CEX régulé pour convertir leur monnaie locale en crypto, et un DEX pour les tokens disponibles uniquement on-chain. Pour des achats réguliers et de long terme de grands actifs comme le Bitcoin ou l'Ethereum, un CEX aux frais bas est généralement plus simple ; comparez les options sur notre [page des exchanges]({lang}/exchanges/).

Si vous voulez explorer les memecoins et les autres tokens on-chain, commencez avec de tout petits montants, un wallet séparé et les cryptos les plus établies de notre [page des memecoins]({lang}/memes/). Notre guide pas à pas [comment acheter un memecoin sur Solana]({lang}/blog/how-to-buy-memecoins-on-solana/) montre tout le processus, y compris des outils comme [GMGN](/go/gmgn?from=blog&l=fr).

## Le vocabulaire courant des DEX

- **Swap** : échanger un token contre un autre.
- **Paire** : les deux tokens d'un pool, comme SOL/USDC.
- **Tolérance de slippage** : la variation de prix maximale que vous acceptez.
- **Approve** : l'autorisation donnée à un contrat de déplacer un token depuis votre wallet (surtout sur les réseaux de type Ethereum). Révoquez les anciennes autorisations dont vous n'avez plus besoin.
- **Agrégateur** : un service qui répartit votre échange entre plusieurs DEX pour obtenir un meilleur prix, comme Jupiter sur Solana ou 1inch sur Ethereum.

## FAQ

### Un DEX est-il plus sûr qu'un CEX ?

Il supprime le risque que la plateforme perde ou gèle vos fonds, mais ajoute le risque de vos propres erreurs et des tokens frauduleux. Aucun des deux n'est sans risque.

### Faut-il une pièce d'identité pour utiliser un DEX ?

Généralement non, puisque vous tradez depuis votre propre wallet. Les lois et la fiscalité de votre pays continuent de s'appliquer à vous.

### Pourquoi mon échange sur un DEX a-t-il échoué ?

Raisons courantes : pas assez de crypto native pour le gas, un slippage trop bas pour un prix qui bouge vite, ou un token qui bloque les ventes.

### Les échanges sur un DEX sont-ils imposables ?

Dans de nombreux pays, oui : échanger un token contre un autre peut compter comme une vente. Gardez une trace de vos transactions.

## Sources

- [Comment fonctionne Uniswap (documentation Uniswap)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas et frais (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Documentation Solana : structure des frais](https://solana.com/docs/core/fees/fee-structure)

*Ceci n'est pas un conseil en investissement. Ce guide explique le fonctionnement des DEX et ne recommande aucune plateforme ni aucun token.*
