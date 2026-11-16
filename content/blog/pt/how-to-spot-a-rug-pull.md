---
title: Como identificar um rug pull: checklist de 10 pontos antes de comprar um token novo
description: Como identificar um rug pull antes de comprar: checklist de 10 pontos sobre liquidez travada, autoridade de mint e freeze, holders, honeypots e volume falso.
date: 2026-11-16
category: guides
assets: sol, pepe, bonk
---
**Como identificar um rug pull?** Rug pull ("puxada de tapete") é quando as pessoas por trás de um token pegam o dinheiro e deixam os compradores com algo que ninguém quer. Pode ser repentino (o criador retira a liquidez do pool) ou lento (quem está por dentro vende aos poucos suas posições enormes). De qualquer forma, o preço vai quase a zero.

Rug pulls não são raros. No relatório de 2025, a empresa de análise de blockchain Solidus Labs classificou **98,6%** dos mais de 7 milhões de tokens lançados na plataforma Pump.fun como rug pulls ou esquemas de pump-and-dump, e descobriu que só cerca de 97 mil mantiveram pelo menos US$ 1.000 de liquidez. Use o checklist abaixo antes de comprar qualquer token novo.

## Dois exemplos recentes

- **HAWK (dezembro de 2024).** Uma memecoin promovida por uma celebridade da internet chegou a um valor de mercado de cerca de US$ 490 milhões logo após o lançamento e depois caiu cerca de 91% em menos de três horas. Analistas on-chain disseram que um grupo de carteiras de insiders e "snipers" detinha 80–90% da oferta no lançamento; uma carteira comprou 17,5% da oferta segundos após o lançamento e vendeu ao longo da hora e meia seguinte. A promotora negou que ela ou sua equipe tenham vendido.
- **LIBRA (fevereiro de 2025).** Um token promovido nas redes sociais pelo presidente da Argentina, Javier Milei, disparou e desabou em poucas horas. Insiders embolsaram cerca de US$ 107 milhões, segundo dados on-chain divulgados pelo The Block, e Milei retirou seu apoio.

Os dois tinham nomes famosos, volume enorme e redes sociais em euforia. Nada disso protegeu os compradores.

## O checklist de 10 pontos

### 1. A liquidez está travada ou queimada?

Um token é negociado contra um pool de liquidez (por exemplo token + SOL). Se o criador tem os tokens LP do pool, ele pode retirar o pool a qualquer momento. Procure liquidez **queimada** ou **travada** por muito tempo em um serviço de bloqueio conhecido e confira a data de término do bloqueio. "Confia, está travada" em um chat não é prova.

### 2. A autoridade de mint foi revogada?

Na Solana, a autoridade de mint permite que alguém crie tokens novos. Se ainda estiver ativa, o criador pode emitir bilhões de tokens novos e vendê-los no pool. As páginas de tokens em ferramentas como GMGN, Solscan ou RugCheck mostram se ela foi revogada.

### 3. A autoridade de congelamento (freeze) foi revogada?

A autoridade de freeze permite congelar contas de tokens. Um criador que mantém isso pode impedir você de vender enquanto ele vende. Para uma memecoin, não há nenhum bom motivo para mantê-la.

### 4. Qual é a concentração dos maiores holders?

Abra a lista de holders. Ignore o pool e as carteiras conhecidas de exchanges e some os 10 primeiros. Se um punhado de carteiras tem uma grande fatia da oferta, são elas que decidem o preço. Cuidado com muitas carteiras "diferentes" que receberam fundos da mesma origem: ferramentas de bubble map mostram esses grupos.

### 5. Você consegue mesmo vender? (teste de honeypot)

Um honeypot deixa você comprar, mas não vender, ou cobra uma enorme taxa escondida na venda. Sinais de alerta: quase nenhuma venda no histórico de negociações, vendas que falham ou um contrato com regras de transferência incomuns (mais comum em Ethereum e BNB Chain). Ferramentas de simulação podem testar uma venda antes de você comprar.

### 6. As redes sociais são reais?

Confira o site e as contas no X/Telegram. Sinais de alerta: conta criada na semana passada, milhares de seguidores mas nenhuma conversa de verdade, texto do site copiado, uma "equipe" com fotos de banco de imagens, comentários desativados ou links diferentes dos que aparecem na página do token.

### 7. O volume é real?

Uma onda repentina de volume vinda de carteiras novas, operações de tamanho quase idêntico ou as mesmas carteiras comprando e vendendo entre si (wash trading) podem ser usadas para colocar um token nas listas de "em alta". Interesse real costuma vir com muitas carteiras diferentes e crescimento gradual.

### 8. Como foi o lançamento?

Poucas carteiras compraram uma grande fatia nos primeiros segundos? A carteira do desenvolvedor vendeu logo após o lançamento? Muitas ferramentas mostram o histórico da carteira "dev", incluindo tokens que ela lançou antes: um criador com um rastro de tokens mortos é um alerta claro.

### 9. Quem está promovendo e por quê?

Influenciadores pagos, lançamentos de celebridades e mensagens de "100x garantido" muitas vezes marcam o topo. Pergunte: se essa pessoa está promovendo, quando ela comprou e a que preço?

### 10. O gráfico de preço faz sentido?

Um candle vertical em um token de poucas horas significa que os primeiros compradores estão com grandes lucros, e muitos vão vender para os próximos compradores. O medo de ficar de fora (FOMO) é exatamente a sensação que um rug pull foi feito para criar.

## Uma rotina rápida antes de cada compra

1. Copie o endereço do contrato de uma fonte confiável.
2. Confira o status de mint, freeze e liquidez.
3. Olhe os maiores holders e os grupos de carteiras.
4. Procure vendas no histórico de negociações.
5. Decida o máximo que você aceita perder e depois corte pela metade.

Se algum ponto falhar, caia fora. Sempre vai haver outro token.

## Até tokens "limpos" podem cair 90%

Passar no checklist só reduz o risco de fraude direta. Não transforma um token em um bom investimento. Até as memecoins mais conhecidas caíram muito desde seus picos; você pode ver as quedas atuais na nossa [página de memecoins]({lang}/memes/) e no [rastreador de máximas históricas]({lang}/ath/). A CoinGecko considerou mortos, no fim de 2025, mais da metade dos tokens que acompanha desde 2021.

## Perguntas frequentes

### Rug pull é crime?

Depende do país e dos detalhes. Muitos rug pulls são tratados como fraude, mas fundos on-chain raramente são recuperados, então prevenir é muito melhor do que esperar por justiça.

### Um pool de liquidez travado significa que o token é seguro?

Não. Isso elimina uma das formas de rug pull, mas os insiders ainda podem despejar uma grande fatia da oferta, e o bloqueio pode expirar.

### Consigo recuperar meu dinheiro depois de um rug pull?

Normalmente não. Registre um boletim de ocorrência e denuncie à plataforma, e desconfie de "serviços de recuperação" que cobram uma taxa: muitas vezes são um segundo golpe.

### Quais ferramentas ajudam a verificar um token?

Páginas de tokens na GMGN e em DEX screeners, exploradores de blocos como o Solscan e verificadores como o RugCheck mostram liquidez, autoridades e holders. Use mais de uma.

## Fontes

- [98% dos tokens da Pump.fun foram rug pulls ou fraude, diz novo relatório (CoinDesk)](https://hotfix.coindesk.com/business/2025/05/07/98-of-tokens-on-pump-fun-have-been-rug-pulls-or-an-act-of-fraud-new-report-says)
- [Memecoin Hawk Tuah despenca 90% (Cointelegraph)](https://cointelegraph.com/news/hawk-tuah-memecoin-dumps-90-percent-outrage-token-launch-insider)
- [Milei retira apoio ao LIBRA depois que insiders embolsam US$ 107 milhões (The Block)](https://www.theblock.co/post/341206/argentinian-president-javier-milei-retracts-libra-endorsement-after-insiders-cash-out-107-million)
- [Moedas mortas: mais de 50% das criptomoedas fracassaram, relatório da CoinGecko (Crowdfund Insider)](https://www.crowdfundinsider.com/2026/01/257221-dead-coins-over-50-of-cryptocurrencies-have-failed-report-reveals/)

*Não é recomendação de investimento. Este checklist reduz o risco, mas não o elimina; a maioria dos tokens novos perde quase todo o valor.*
