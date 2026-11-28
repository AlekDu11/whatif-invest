---
title: Pearl (PEARL) explicado: mineração com GPU e Proof of Useful Work, teto de 2,1 bilhões
description: Pearl explicado: como a mineração com GPU se liga à computação de IA, o teto de 2,1 bilhões, o lançamento de abril de 2026, as críticas, rivais e riscos.
date: 2026-11-28
kind: analysis
---
**Pearl** é uma blockchain de camada 1 nova, minerada com placas de vídeo da Nvidia. Em vez dos quebra-cabeças de hash sem utilidade que os mineradores de Bitcoin resolvem, sua "prova de trabalho útil" (Proof of Useful Work) pede multiplicação de matrizes — a mesma matemática que roda os modelos de IA —, então, em teoria, uma GPU pode atender clientes de IA e proteger a rede ao mesmo tempo. Foi criada pela Pearl Research Labs, cofundada pelo cientista da computação Omri Weinstein, e a rede principal começou em 27 de abril de 2026. O valor de mercado hoje é {{mcap:pearl}} ({{rank:pearl}} entre as criptomoedas).

> **Pontos principais**
> - Nunca existirão mais de 2,1 bilhões de moedas, 100 vezes os 21 milhões do Bitcoin; a recompensa da mineração cai aos poucos, sem halvings.
> - A máxima histórica é {{ath:pearl}} ({{athd:pearl}}); hoje o preço está {{fromath:pearl}} em relação a ela.
> - O projeto diz que não houve pré-mineração, nem fatia para investidores, nem tesouraria da equipe: todas as moedas vêm da mineração.
> - Um estudo de junho de 2026 concluiu que a mineração daquele momento não produzia nenhum trabalho útil de IA.

## Como funciona

Os mineradores fazem nas GPUs multiplicações de matrizes "com ruído", calculam o hash de pedaços do resultado e embrulham o trabalho numa prova de conhecimento zero, para que qualquer pessoa possa conferir rapidamente sem refazê-lo. O método vem de um artigo de criptografia de 2025 do qual Weinstein é coautor. O minerador oficial se conecta ao vLLM, software popular para rodar modelos de IA, em placas de data center como as Nvidia H100 e H200, enquanto mineradores feitos pela comunidade rodam também em placas RTX de jogos. Por dentro o Pearl lembra o Bitcoin: é baseado no btcd, um programa de nó do Bitcoin, e um bloco novo chega a cada poucos minutos. A moeda costuma aparecer com o ticker PRL, e em alguns sites de cotação outro token sem relação usa o mesmo ticker.

## Para que serve o token

As moedas só são criadas como recompensa aos mineradores e servem para pagar taxas. O primeiro exemplo comercial veio em maio de 2026: a empresa de nuvem de IA Together AI ofereceu um modelo Gemma rodando em mineradores do Pearl por mais de 25% abaixo do preço normal, com o desconto pago por recompensas em PRL. Se os clientes de IA usarem mesmo a rede assim, a mineração deixa de ser só gasto de energia; se não, o Pearl é apenas mais uma moeda de prova de trabalho com oferta grande.

## Os números agora

- Preço hoje: {{price:pearl}}
- Máxima histórica: {{ath:pearl}} ({{athd:pearl}}), {{fromath:pearl}} desde ela
- Valor de mercado: {{mcap:pearl}} ({{rank:pearl}} entre as criptomoedas)
- Variação do preço em 12 meses: {{chg1y:pearl}}

## Sua história

O artigo de base saiu em abril de 2025, e a rede principal entrou no ar em 27 de abril de 2026 sem moedas distribuídas antes. No fim de maio, depois do acordo com a Together AI, veio uma corrida de gamers e donos de GPU, e em poucas semanas o ganho diário de uma RTX 5090 caiu mais ou menos pela metade com a concorrência. No começo a moeda só era negociada em corretoras pequenas e com pouca liquidez, como a MEXC. Em junho de 2026 um artigo no arXiv, "The Usefulness Gap in Proof-of-Useful-Work", relatou que os milhares de mineradores da rede não faziam computação útil de IA e que o software de mineração mais usado nem tinha código de IA. O Pearl adicionou suporte a modelos de IA do tipo mixture-of-experts num hard fork em junho, e até outubro de 2026 cerca de 16% da oferta máxima já tinha sido minerada.

## Alternativas

O [Bitcoin]({lang}/btc/) é a moeda clássica de prova de trabalho, minerada com chips especializados, e não com GPUs. Entre os projetos de IA e computação, o [Bittensor]({lang}/tao/) recompensa quem roda modelos de IA, enquanto [Render]({lang}/render/), [Akash Network]({lang}/akt/) e [io.net]({lang}/io/) alugam poder de GPU diretamente. A ideia do Pearl é outra: a própria mineração deveria ser o trabalho útil de IA.

## Principais riscos

- **Muito nova:** a moeda tem só alguns meses de histórico de preço, e moedas jovens podem perder quase todo o valor rapidamente.
- **Utilidade não comprovada:** pesquisadores independentes acharam pouco trabalho real de IA até agora; o principal argumento pode não se confirmar.
- **Economia da mineração:** dificuldade em alta e recompensa em queda cortam os ganhos, e mineradores costumam vender moedas para pagar a energia.
- **Concentração:** nas primeiras semanas minerar era barato, então os primeiros participantes têm uma fatia grande.
- **Liquidez e imitações:** o volume é menor que o das grandes moedas e existe outro token com o mesmo ticker PRL — confira bem o contrato e a corretora.

## O que isso significa se você compra regularmente

O Pearl é negociado há só alguns meses, então ainda não há um histórico útil do que teriam dado compras regulares. Comprar um valor fixo num calendário espalha o risco de errar o momento, mas com uma moeda recém-criada não elimina o risco de perder boa parte do dinheiro. Muita gente deixa moedas experimentais como esta numa parte bem pequena das economias. Resultados passados não garantem resultados futuros.

*Não é recomendação de investimento.*

## Fontes

- [What is Pearl blockchain? How it uses GPU mining to price AI compute (KuCoin, October 2026)](https://www.kucoin.com/blog/pearl-blockchain-ai-mining-prl-token)
- [New AI-compute cryptocurrency Pearl sparks a GPU mining rush, but profitability is sliding (Tom's Hardware, 31 May 2026)](https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding)
- [Pearl (PRL): the AI-compute cryptocurrency (Hashrate Index, June 2026)](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
- [The Usefulness Gap in Proof-of-Useful-Work (arXiv 2606.04819, June 2026)](https://arxiv.org/abs/2606.04819)
