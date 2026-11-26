---
title: THORChain (RUNE) explicado de forma simples: trocas de bitcoin nativo e outras moedas entre blockchains, sem tokens embrulhados
description: THORChain em linguagem simples: swaps entre redes e pools de RUNE, caução dos nós, os hacks de 2021, o congelamento dos empréstimos em 2025 e os riscos.
date: 2026-11-26
kind: analysis
---
**THORChain (RUNE)** é uma blockchain que permite trocar moedas entre redes diferentes — por exemplo, bitcoin de verdade por ether de verdade — sem uma corretora centralizada e sem cópias "embrulhadas" (wrapped) das moedas. O RUNE é o token no centro de tudo: cada pool de negociação é pareado com RUNE, e os computadores que rodam a rede precisam travar RUNE como depósito de garantia. Todo o RUNE em circulação vale {{mcap:rune}} hoje ({{rank:rune}} entre as criptomoedas).

> **Pontos principais**
> - O THORChain troca ativos nativos entre redes como Bitcoin, Ethereum, BNB Chain, Dogecoin e outras em um só passo.
> - Cada pool de liquidez é pareado com RUNE, e os operadores de nós depositam RUNE como caução, que pode ser tomada se agirem mal.
> - A máxima histórica é {{ath:rune}} ({{athd:rune}}); hoje o preço está {{fromath:rune}} abaixo dela.
> - A rede foi hackeada duas vezes em 2021 e congelou seus produtos de empréstimo e poupança em janeiro de 2025.

## Como funciona

O THORChain é construído com o Cosmos SDK. Um grupo de nós independentes controla em conjunto "cofres" (vaults) — endereços no Bitcoin, no Ethereum e nas outras redes conectadas — usando assinaturas de limiar, de modo que nenhum nó sozinho consegue mover os fundos. Quando você troca BTC por ETH, envia bitcoin para um cofre; a rede o vende por RUNE no pool de BTC, depois vende esse RUNE por ETH no pool de ETH, e um cofre envia ether de verdade para você. Os preços vêm dos saldos dos pools, como na [Uniswap]({lang}/uni/). Provedores de liquidez depositam moedas nos pools e recebem parte das taxas das trocas. Os nós precisam depositar como caução RUNE em valor maior do que os fundos que ajudam a guardar, o que deve tornar o roubo pouco vantajoso.

## Por que as pessoas acham que ele tem valor

Mover valor entre blockchains costuma ser lento, arriscado ou exigir uma corretora centralizada com verificação de conta. O THORChain oferece um caminho direto entre moedas nativas, e por isso muitas carteiras cripto e apps de troca passam operações por ele. A demanda por RUNE vem de três lugares: ele é metade de cada pool, é a caução que os nós precisam depositar, e parte das taxas das trocas vai para quem o mantém e faz staking. Mais volume de negociação significa, portanto, mais taxas para quem tem RUNE.

## Os números agora

- Preço hoje: {{price:rune}}
- Máxima histórica: {{ath:rune}} ({{athd:rune}}), {{fromath:rune}} desde ela
- Valor de mercado: {{mcap:rune}} ({{rank:rune}} entre as criptomoedas)
- Variação do preço em 12 meses: {{chg1y:rune}}
- US$ 10 por dia durante 5 anos: {{dca:rune:5}} com {{dcainv:5}} investidos ({{dcaroi:rune:5}})

## Sua história

O RUNE foi vendido pela primeira vez pelo Binance Launchpad em julho de 2019. Em 2020 entrou no ar uma "chaosnet" com dinheiro real e limites propositalmente baixos, e em abril de 2021 chegou a negociação entre várias redes. Na alta de 2021, o RUNE atingiu cerca de US$ 20 em maio de 2021, mas em julho de 2021 a rede sofreu dois ataques que somaram milhões de dólares. A mainnet completa foi declarada em junho de 2022. Em janeiro de 2025, o THORChain suspendeu seus produtos de empréstimo e "savers" depois que eles acumularam cerca de US$ 200 milhões em obrigações; a dívida foi depois convertida em um token separado, o TCY. Em fevereiro de 2025, os hackers por trás do roubo de US$ 1,4 bilhão da corretora Bybit usaram o THORChain para trocar o ether roubado por bitcoin, o que trouxe volumes recordes e duras críticas.

## Alternativas

As corretoras centralizadas continuam sendo o jeito mais fácil de trocar entre redes. Entre os rivais on-chain estão serviços de pontes e agregadores, além do Maya Protocol, um fork do THORChain. Para trocas dentro de uma mesma rede, as pessoas usam corretoras descentralizadas como [Uniswap]({lang}/uni/) ou [PancakeSwap]({lang}/cake/). Para conectar blockchains de modo geral, [Cosmos]({lang}/atom/) e [Chainlink]({lang}/link/) oferecem outras abordagens.

## Principais riscos

- **Grandes oscilações:** o RUNE já caiu mais de 80% desde o pico mais de uma vez.
- **Hacks:** os cofres entre redes guardam grandes somas e já foram atacados; um novo bug pode custar dinheiro aos usuários.
- **Produtos que falharam:** o congelamento dos empréstimos em 2025 mostrou que novos recursos podem gerar perdas para os usuários e pressão sobre o RUNE.
- **Regulação:** o uso por hackers para lavar dinheiro chama a atenção dos reguladores e pode levar a restrições.
- **Dependência do RUNE:** como todo pool é pareado com RUNE, uma queda forte do RUNE atinge o sistema inteiro.

## O que isso significa se você compra regularmente

O RUNE é uma aposta de que as pessoas continuarão usando o THORChain para trocas entre redes, e sua história inclui hacks e um produto congelado, além de altas rápidas. Comprar um valor fixo regularmente suaviza seu preço de entrada, mas não protege você de choques específicos do projeto. Muita gente limita um token especializado como o RUNE a uma pequena parte das economias. Resultados passados não garantem retornos futuros.

*Não é recomendação de investimento.*

## Fontes

- [Documentação do THORChain — introdução (docs.thorchain.org)](https://docs.thorchain.org/)
- [RUNE sobe 15% com THORChain retomando a maioria dos swaps após pane (Cointelegraph)](https://cointelegraph.com/markets/rune-rallies-15-as-thorchain-restarts-most-swaps-after-outage)
- [Preço do THORChain, capitalização de mercado e máxima histórica (CoinGecko)](https://www.coingecko.com/en/coins/thorchain)
