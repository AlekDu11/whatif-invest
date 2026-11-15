---
title: Qu'est-ce que le staking crypto et est-ce sans risque ?
description: Le staking crypto expliqué simplement : son fonctionnement, le blocage des fonds, staking sur plateforme ou on-chain, et les vrais risques avant de staker.
date: 2026-11-16
category: guides
assets: eth, sol, ada, dot, atom
---
Le **staking** consiste à bloquer des cryptos pour aider une blockchain à fonctionner — et à recevoir de nouveaux jetons en récompense. On le compare souvent à un livret d'épargne, mais il fonctionne de façon très différente et comporte ses propres risques.

Ce guide explique comment marche le staking, ce que signifie la période de blocage, en quoi le staking sur une plateforme diffère du staking on-chain, et ce qui peut mal tourner.

## Comment fonctionne le staking

Beaucoup de blockchains récentes — Ethereum, Solana, Cardano, Polkadot, Cosmos et d'autres — utilisent un système appelé **preuve d'enjeu** (proof of stake). Au lieu de dépenser de l'électricité pour sécuriser le réseau (comme le minage du Bitcoin), elles s'appuient sur des **validateurs** : des ordinateurs qui vérifient les transactions et ajoutent de nouveaux blocs.

Pour devenir validateur, il faut mettre des jetons en jeu, en garantie d'un comportement honnête. En quelques étapes :

1. Vous bloquez (stakez) des jetons sur le réseau, soit en faisant tourner vous-même un validateur, soit en les déléguant à un validateur.
2. Les validateurs confirment les transactions et produisent les blocs.
3. Le réseau verse des récompenses en nouveaux jetons, plus une part des frais de transaction.
4. Si un validateur triche ou reste trop longtemps hors ligne, une partie de la mise peut être amputée. C'est ce qu'on appelle le **slashing**.

Le Bitcoin lui-même ne peut pas être staké de cette façon — il utilise la preuve de travail. Les produits qui proposent du « rendement sur Bitcoin » relèvent généralement du prêt ou d'autres montages, pas du staking.

## D'où viennent les récompenses de staking

Les récompenses ne sont pas de l'argent gratuit. Elles proviennent surtout :

- **De nouveaux jetons** créés par le réseau (l'inflation de l'offre),
- **Des frais de transaction** payés par les utilisateurs.

C'est important : si un réseau crée de nouveaux jetons à, disons, 5 % par an et que vous gagnez 5 %, vous conservez surtout votre part du réseau plutôt que de vous enrichir. Et les récompenses sont versées dans la crypto elle-même — si son prix baisse, la valeur totale de vos avoirs peut quand même fortement chuter.

Les taux de récompense changent en permanence selon le nombre de stakers et les règles du réseau. Considérez tout pourcentage affiché comme une photo à un instant donné, pas comme une promesse.

## Blocage et unbonding : quand récupérer vos jetons

Staker signifie en général que vos jetons ne sont pas disponibles immédiatement. Chaque réseau a ses propres règles :

- **Ethereum** — les retraits sont possibles depuis la mise à jour « Shapella » de 2023, mais la sortie passe par une file d'attente qui peut durer de quelques jours à plusieurs semaines quand beaucoup de gens sortent en même temps.
- **Solana** — le déstaking prend effet à la fin d'une « epoch », en général au bout de deux ou trois jours.
- **Cosmos et Polkadot** — des périodes de « unbonding » de plusieurs semaines, pendant lesquelles les jetons ne rapportent rien et ne peuvent pas être vendus.
- **Cardano** — les jetons restent dans votre portefeuille et ne sont pas bloqués du tout.

Pourquoi c'est important : si le marché chute pendant la période de unbonding, vous ne pouvez pas vendre. Vérifiez toujours les règles exactes et actuelles de la crypto avant de staker.

## Staking sur plateforme ou staking on-chain

Il existe deux grandes façons de staker pour un particulier.

### Le staking sur une plateforme d'échange (custodial)

Vous appuyez sur « Staker » ou « Earn » dans l'application d'une plateforme, et elle s'occupe de la partie technique.

- ✅ Très simple, les petits montants passent, pas de portefeuille à configurer.
- ❌ C'est la plateforme qui détient vos jetons. Si elle fait faillite, se fait pirater ou bloque les retraits, vos jetons sont en danger.
- ❌ La plateforme garde une partie des récompenses en guise de frais.
- ❌ Certains produits « earn » sont en réalité du prêt, pas du staking — un risque très différent.

Les régulateurs surveillent ces services de près. En 2023, la SEC américaine a poursuivi Kraken pour son programme de staking ; Kraken a payé 30 millions de dollars et fermé le service pour ses clients américains. En 2025, les services de la SEC ont indiqué que certaines formes de « staking de protocole » direct ne sont pas des opérations sur titres. Les règles varient selon les pays et évoluent sans cesse.

### Le staking on-chain (non custodial)

Vous gardez vos jetons dans votre propre portefeuille et les déléguez à un validateur, ou vous faites tourner votre propre validateur.

- ✅ Vous détenez vos clés ; personne ne peut geler votre compte.
- ✅ Des frais généralement plus faibles.
- ❌ Plus technique : mauvaises adresses, phishing et validateurs peu fiables sont votre affaire.
- ❌ Faire tourner son propre validateur Ethereum demande 32 ETH et un matériel fiable.

### Le staking liquide

Une option intermédiaire : vous stakez via un protocole et recevez un jeton qui représente vos jetons stakés (par exemple un jeton « staked ETH »). Vous pouvez l'échanger pendant que vos jetons produisent des récompenses. La contrepartie : un **risque de smart contract** supplémentaire et la possibilité que ce jeton s'échange sous la valeur des jetons qu'il représente.

## Les principaux risques du staking

Le staking est-il sûr ? Il est moins risqué que beaucoup de produits crypto « à haut rendement », mais il n'est jamais sans risque :

1. **Le risque de prix.** Le plus important. Une récompense de quelques pourcents ne pèse pas lourd si la crypto perd 50 %. Voyez à quel point les cours sont volatils sur la [page Ethereum]({lang}/eth/) ou la [page Solana]({lang}/sol/).
2. **Le risque de blocage.** Vous risquez de ne pas pouvoir vendre pendant un krach.
3. **Le risque de plateforme.** Les plateformes d'échange et de prêt peuvent faire faillite. Lors de l'effondrement de Celsius en 2022, les utilisateurs de son programme « earn » ont perdu l'accès à leurs cryptos.
4. **Le slashing.** Un validateur défaillant peut perdre une partie de la mise — y compris les jetons délégués sur certains réseaux.
5. **Le risque de smart contract** dans le staking liquide et la DeFi.
6. **Les impôts.** Dans de nombreux pays, les récompenses de staking sont imposables comme un revenu au moment où on les reçoit. Renseignez-vous sur les règles locales.
7. **Les arnaques.** Les faux sites de staking et les offres « 20 % garantis par mois » sont fréquents. Lisez notre guide pour [éviter les arnaques crypto]({lang}/blog/how-to-avoid-crypto-scams/).

## Une check-list prudente avant de staker

- Ne stakez que des cryptos que vous comptiez déjà garder longtemps.
- Vérifiez la période de unbonding et si vous risquez d'avoir besoin de l'argent plus tôt.
- Comprenez qui détient vos jetons — vous ou une plateforme.
- Comparez les frais : quelle part des récompenses la plateforme garde-t-elle ?
- Évitez les offres à rendement fixe très élevé — les vraies récompenses de staking varient.
- Commencez petit et testez un retrait.

Le staking ne change pas la question principale : la crypto elle-même a-t-elle sa place dans votre plan à long terme ? Un plan d'achats réguliers (DCA) dépend du prix de l'actif sur plusieurs années — testez-le avec notre [calculateur DCA]({lang}/compare/). Voici ce qu'auraient donné 10 $ par jour en Ethereum sur 5 ans — sans aucune récompense de staking : {{dca:eth:5}} pour {{dcainv:5}} investis ({{dcaroi:eth:5}}).

{{card:eth}}
{{card:sol}}

## FAQ

### Le staking, c'est comme toucher des intérêts ?

Non. Les intérêts viennent d'un emprunteur ; les récompenses de staking viennent du réseau lui-même, en échange de votre aide pour le sécuriser. Elles sont versées dans la crypto, donc leur valeur suit son prix.

### Peut-on perdre de l'argent avec le staking ?

Oui. Le prix de la crypto peut baisser, une plateforme peut faire faillite et, dans de rares cas, le slashing peut amputer votre mise. Les récompenses ne vous protègent pas d'une baisse de prix.

### Peut-on staker du Bitcoin ?

Pas nativement — le Bitcoin utilise la preuve de travail. Les offres de « rendement sur Bitcoin » sont généralement du prêt ou d'autres produits aux risques différents.

### Vaut-il mieux staker sur une plateforme ou depuis son portefeuille ?

Le staking sur plateforme est plus simple ; le staking depuis un portefeuille vous laisse le contrôle de vos clés. Le bon choix dépend de votre aisance à gérer un portefeuille — voir notre guide des [portefeuilles chauds et froids]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Sources

- [ethereum.org — Le staking sur Ethereum](https://ethereum.org/en/staking/)
- [ethereum.org — Les retraits de staking](https://ethereum.org/en/staking/withdrawals/)
- [Solana — Staking](https://solana.com/staking)
- [SEC américaine — Kraken arrête son programme de staking et paie 30 millions de dollars (2023)](https://www.sec.gov/news/press-release/2023-25)
- [Skadden — SEC : certaines activités de staking de protocole ne sont pas des opérations sur titres (2025)](https://www.skadden.com/insights/publications/2025/06/sec-certain-protocol-staking-activities-are-not-securities-transactions)

*Ceci n'est pas un conseil en investissement. Ce guide explique le fonctionnement du staking et ne recommande aucune crypto, plateforme ni validateur.*
