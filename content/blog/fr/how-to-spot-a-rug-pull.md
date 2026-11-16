---
title: Comment repérer un rug pull : 10 points à vérifier avant d'acheter un nouveau token
description: Repérer un rug pull avant d'acheter : 10 points à vérifier sur la liquidité verrouillée, l'autorité de mint et de gel, les holders, les honeypots et le volume.
date: 2026-11-16
category: guides
assets: sol, pepe, bonk
---
**Comment repérer un rug pull ?** Un rug pull (« tirer le tapis ») se produit quand les personnes derrière un token partent avec l'argent et laissent les acheteurs avec quelque chose dont personne ne veut. Il peut être brutal (le créateur retire la liquidité du pool) ou lent (les initiés revendent peu à peu leurs énormes positions). Dans les deux cas, le prix tombe presque à zéro.

Les rug pulls ne sont pas rares. Dans son rapport 2025, la société d'analyse blockchain Solidus Labs a classé **98,6 %** des plus de 7 millions de tokens lancés sur la plateforme Pump.fun comme des rug pulls ou des opérations de pump-and-dump, et a constaté que seuls environ 97 000 conservaient au moins 1 000 $ de liquidité. Utilisez la checklist ci-dessous avant d'acheter n'importe quel nouveau token.

## Deux exemples récents

- **HAWK (décembre 2024).** Un memecoin promu par une célébrité d'internet a atteint une valeur de marché d'environ 490 millions $ peu après son lancement, puis a chuté d'environ 91 % en moins de trois heures. Des analystes on-chain ont indiqué qu'un groupe de wallets d'initiés et de « snipers » détenait 80 à 90 % de l'offre au lancement ; un wallet a acheté 17,5 % de l'offre quelques secondes après le lancement et l'a revendu au cours de l'heure et demie suivante. La promotrice a nié qu'elle ou son équipe aient vendu.
- **LIBRA (février 2025).** Un token promu sur les réseaux sociaux par le président argentin Javier Milei a flambé puis s'est effondré en quelques heures. Les initiés ont encaissé environ 107 millions $, selon des données on-chain rapportées par The Block, et Milei a retiré son soutien.

Les deux avaient des noms célèbres, un volume énorme et des réseaux sociaux en ébullition. Rien de tout cela n'a protégé les acheteurs.

## La checklist en 10 points

### 1. La liquidité est-elle verrouillée ou brûlée ?

Un token s'échange contre un pool de liquidité (par exemple token + SOL). Si le créateur détient les tokens LP du pool, il peut retirer le pool à tout moment. Cherchez une liquidité **brûlée** ou **verrouillée** pour longtemps via un service de verrouillage connu, et vérifiez la date de fin du verrouillage. Un « faites-moi confiance, c'est verrouillé » dans un chat n'est pas une preuve.

### 2. L'autorité de mint est-elle révoquée ?

Sur Solana, l'autorité de mint permet à quelqu'un de créer de nouveaux tokens. Si elle est encore active, le créateur peut émettre des milliards de nouveaux tokens et les vendre dans le pool. Les pages de token d'outils comme GMGN, Solscan ou RugCheck indiquent si elle est révoquée.

### 3. L'autorité de gel (freeze) est-elle révoquée ?

L'autorité de gel permet de geler des comptes de tokens. Un créateur qui la conserve peut vous empêcher de vendre pendant que lui vend. Pour un memecoin, il n'y a aucune bonne raison de la garder.

### 4. Quelle est la concentration des principaux détenteurs ?

Ouvrez la liste des détenteurs. Ignorez le pool et les wallets d'exchanges connus, puis additionnez les 10 premiers. Si une poignée de wallets détient une grosse part de l'offre, ce sont eux qui font le prix. Méfiez-vous des nombreux wallets « différents » alimentés depuis la même source : les outils de bubble map révèlent ces groupes.

### 5. Pouvez-vous vraiment vendre ? (test du honeypot)

Un honeypot vous laisse acheter mais pas vendre, ou applique une énorme taxe cachée à la vente. Signaux d'alerte : presque aucune vente dans l'historique des transactions, des ventes qui échouent, ou un contrat avec des règles de transfert inhabituelles (plus fréquent sur Ethereum et BNB Chain). Des outils de simulation peuvent tester une vente avant que vous n'achetiez.

### 6. Les réseaux sociaux sont-ils réels ?

Vérifiez le site et les comptes X/Telegram. Signaux d'alerte : un compte créé la semaine dernière, des milliers d'abonnés mais aucune vraie conversation, un texte de site copié, une « équipe » avec des photos de banque d'images, des commentaires désactivés, ou des liens différents de ceux de la page du token.

### 7. Le volume est-il réel ?

Une vague soudaine de volume venant de nouveaux wallets, des transactions de taille presque identique, ou les mêmes wallets qui s'achètent et se revendent entre eux (wash trading) peuvent servir à propulser un token dans les listes « tendances ». Un intérêt réel s'accompagne généralement de nombreux wallets différents et d'une croissance progressive.

### 8. Comment s'est passé le lancement ?

Quelques wallets ont-ils acheté une grosse part dans les premières secondes ? Le wallet du développeur a-t-il vendu peu après le lancement ? Beaucoup d'outils montrent l'historique du wallet « dev », y compris les tokens qu'il a lancés auparavant : un créateur qui laisse derrière lui une série de tokens morts est un avertissement clair.

### 9. Qui en fait la promotion, et pourquoi ?

Influenceurs payés, lancements de célébrités et messages « x100 garanti » marquent souvent le sommet. Demandez-vous : si cette personne en fait la promotion, quand a-t-elle acheté, et à quel prix ?

### 10. Le graphique de prix a-t-il du sens ?

Une bougie verticale sur un token vieux de quelques heures signifie que les premiers acheteurs sont assis sur de gros gains, et beaucoup vont revendre aux acheteurs suivants. La peur de rater le coche (FOMO) est exactement le sentiment qu'un rug pull cherche à provoquer.

## Une routine rapide avant chaque achat

1. Copiez l'adresse du contrat depuis une source fiable.
2. Vérifiez le statut du mint, du gel et de la liquidité.
3. Regardez les principaux détenteurs et les groupes de wallets.
4. Parcourez l'historique des transactions à la recherche de ventes.
5. Fixez le montant maximum que vous êtes prêt à perdre, puis divisez-le par deux.

Si un seul point coince, passez votre chemin. Il y aura toujours un autre token.

## Même les tokens « propres » peuvent chuter de 90 %

Passer la checklist réduit seulement le risque de fraude pure et simple. Cela ne fait pas d'un token un bon investissement. Même les memecoins les plus connus ont fortement chuté depuis leurs sommets ; vous pouvez voir les baisses actuelles sur notre [page des memecoins]({lang}/memes/) et dans le [suivi des plus hauts historiques]({lang}/ath/). CoinGecko a classé comme morts, fin 2025, plus de la moitié des tokens qu'il suivait depuis 2021.

## FAQ

### Un rug pull est-il illégal ?

Cela dépend du pays et des circonstances. Beaucoup de rug pulls sont traités comme de la fraude, mais les fonds on-chain sont rarement récupérés : mieux vaut prévenir qu'espérer obtenir justice.

### Un pool de liquidité verrouillé signifie-t-il que le token est sûr ?

Non. Cela supprime une façon de faire un rug pull, mais les initiés peuvent toujours écouler une grosse part de l'offre, et le verrouillage peut expirer.

### Peut-on récupérer son argent après un rug pull ?

Généralement non. Portez plainte auprès de la police et signalez-le à la plateforme, et méfiez-vous des « services de récupération » qui demandent des frais : ce sont souvent une deuxième arnaque.

### Quels outils aident à vérifier un token ?

Les pages de token de GMGN et des DEX screeners, les explorateurs de blocs comme Solscan et les vérificateurs comme RugCheck affichent la liquidité, les autorités et les détenteurs. Utilisez-en plusieurs.

## Sources

- [98 % des tokens sur Pump.fun sont des rug pulls ou des fraudes, selon un nouveau rapport (CoinDesk)](https://hotfix.coindesk.com/business/2025/05/07/98-of-tokens-on-pump-fun-have-been-rug-pulls-or-an-act-of-fraud-new-report-says)
- [Le memecoin Hawk Tuah s'effondre de 90 % (Cointelegraph)](https://cointelegraph.com/news/hawk-tuah-memecoin-dumps-90-percent-outrage-token-launch-insider)
- [Milei retire son soutien à LIBRA après que des initiés ont encaissé 107 millions $ (The Block)](https://www.theblock.co/post/341206/argentinian-president-javier-milei-retracts-libra-endorsement-after-insiders-cash-out-107-million)
- [Cryptos mortes : plus de 50 % des cryptomonnaies ont échoué, selon CoinGecko (Crowdfund Insider)](https://www.crowdfundinsider.com/2026/01/257221-dead-coins-over-50-of-cryptocurrencies-have-failed-report-reveals/)

*Ceci n'est pas un conseil en investissement. Cette checklist réduit le risque mais ne peut pas l'éliminer ; la plupart des nouveaux tokens perdent presque toute leur valeur.*
