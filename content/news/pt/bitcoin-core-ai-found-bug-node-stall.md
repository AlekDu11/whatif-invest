---
title: Bitcoin Core corrige falha achada por IA que podia travar nós; atualize para 30.5 ou 31.3
description: Bitcoin Core 30.5 e 31.3 corrigem uma falha de gravidade média, achada por um scanner de IA da Spiral (Block), que deixava um par travar um nó por mais de 10 s.
date: 2026-11-21 14:30
tags: bitcoin, hacks, ai
assets: btc
---
O principal software do bitcoin recebeu uma correção para uma falha que uma ferramenta de IA encontrou primeiro. As versões 30.5 e 31.3 do Bitcoin Core, lançadas na sexta-feira, 20 de novembro, fecham um erro que permitia a um único par fazer um nó parar de funcionar por mais de dez segundos a cada mensagem.

## O que aconteceu

- **A falha.** Registrada como CVE-2026-117348, de gravidade média. Um par podia repetir o mesmo identificador de transação até 50.000 vezes num anúncio; o nó verificava cada cópia e travava, ignorando até blocos novos.
- **Quem achou.** O Loupe, scanner de código aberto da equipe Spiral, da Block, que usa agentes de IA, apontou o problema; o aviso credita uma varredura automática por IA no Project Loupe, de Elias Rohrer.
- **A correção.** Nós atualizados agora processam cada transação anunciada só uma vez. O ramo aposentado 29.x não terá correção, segundo o The Defiant.
- **Risco.** Nenhum fundo ou moeda esteve em risco. O CoinDesk observa que o dano realista era atraso: uma corretora mais lenta para creditar depósitos ou um minerador trabalhando por instantes numa cadeia desatualizada.

## Nossa leitura

Isso não causou a queda de sábado: o bitcoin caiu junto com as bolsas e com liquidações alavancadas. Mas mostra que a IA já encontra falhas no código cripto central, para atacantes e defensores. Se você roda um nó, atualize para 30.5 ou 31.3. Se só tem bitcoin, nada muda. O bitcoin está em {{price:btc}}, mais de 50% abaixo do recorde — veja a [página de distância da máxima]({lang}/ath/) e nossa [página de IA e mercados]({lang}/ai/). US$ 10 por dia por 5 anos ({{dcainv:5}}) valem hoje {{dca:btc:5}} ({{dcaroi:btc:5}}). É histórico, não previsão.

## Fontes

- [CoinDesk — Nós do bitcoin podiam travar com um ID repetido 50.000 vezes](https://www.coindesk.com/markets/2026/11/21/bitcoin-nodes-could-be-stalled-by-repeating-one-id-50-000-times-ai-found-the-bug)
- [The Defiant — Bitcoin Core corrige falha achada por IA](https://thedefiant.io/news/security/bitcoin-core-fixes-ai-found-bug-that-could-stall-nodes)
- [Coinotag — Bitcoin Core corrige a falha no 30.5 e 31.3](https://en.coinotag.com/bitcoin-core-fixes-node-stall-cve-2026-117348)

*Não é recomendação de investimento.*
