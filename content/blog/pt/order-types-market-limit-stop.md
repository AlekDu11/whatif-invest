---
title: "Tipos de ordem: a mercado, limitada e stop, explicadas passo a passo"
description: O que fazem os botões Market, Limit e Stop no app da corretora ou exchange, com um exemplo com números e os 3 erros que custam dinheiro.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: tipos básicos de ordem — a mercado (rápida, preço não fixo), limitada (preço fixo, execução incerta), stop (dispara num preço)
---
**Quais são os tipos de ordem?** Uma **ordem a mercado** (Market) compra ou vende agora mesmo pelo melhor preço disponível. Uma **ordem limitada** (Limit) compra ou vende só pelo seu preço ou melhor, então pode nunca ser executada. Uma **ordem stop** (Stop) espera o preço chegar ao nível que você escolheu e então envia uma ordem a mercado — muito usada para limitar uma perda.

> **O essencial**
> - Market = rapidez, mas você não controla o preço exato. Limit = controle do preço, mas sem garantia de execução.
> - Uma ordem stop vira ordem a mercado quando dispara. Numa queda rápida, ela pode ser executada bem abaixo do seu preço de stop.
> - Antes de apertar «Comprar», confira sempre três coisas: tipo de ordem, quantidade e preço.

## Os três botões, em palavras simples

Quando você abre a tela de negociação no app de uma exchange ou corretora, normalmente vê abas: **Market** (a mercado), **Limit** (limitada) e **Stop** (às vezes «Stop-limit», stop limitada).

- **Ordem a mercado (Market).** «Compre agora, pelo preço que for». Ela é executada quase na hora pela melhor oferta (o **ask**, o menor preço pelo qual alguém quer vender). Em criptos grandes e ações grandes, o preço costuma ficar bem perto do que você vê. Em mercados pequenos e com pouca liquidez, pode ser bem pior.
- **Ordem limitada (Limit).** «Compre só a US$ X ou mais barato» (ou «venda só a US$ X ou mais caro»). Sua ordem fica esperando no **livro de ofertas** (order book, a lista de todas as ordens de compra e venda pendentes) até alguém aceitar o seu preço. Se o preço nunca chegar lá, nada acontece.
- **Ordem stop (Stop, stop loss).** «Se o preço cair para US$ X, venda». Até lá ela fica invisível e não faz nada. Quando o preço toca US$ X, ela vira uma ordem a mercado e vende pelo próximo preço disponível.
- **Ordem stop limitada (Stop-limit).** Como um stop, mas vira uma ordem *limitada*. Você não vai vender abaixo do seu limite — mas, numa queda rápida, pode não vender nada.

## Um exemplo com números simples

Digamos que uma ação mostre **US$ 100,00**. O melhor comprador oferece US$ 99,95 (o **bid**) e o melhor vendedor pede US$ 100,05 (o ask). A diferença de US$ 0,10 é o **spread**.

1. Você aperta **Market, comprar 10 ações** → paga cerca de US$ 100,05 cada = **US$ 1.000,50** mais a taxa, se houver.
2. Você coloca **Limit, comprar 10 ações a US$ 98** → nada acontece até um vendedor aceitar US$ 98. Se o preço for para US$ 105, sua ordem só espera e você não compra nada.
3. Você já tem as ações e coloca um **Stop em US$ 90** → se o preço cair para US$ 90, uma venda a mercado é enviada. Num mercado calmo, você talvez receba US$ 89,95. Mas se sair uma notícia ruim antes da abertura e a ação abrir a US$ 80, o seu stop dispara e você vende perto de **US$ 80**, não de US$ 90.

Esse terceiro caso é real. Em 6 de maio de 2010 (o «flash crash»), os preços nos EUA desabaram em minutos e algumas ordens stop foram executadas muito abaixo dos seus níveis de stop; algumas ações chegaram a ser negociadas a um centavo, segundo o relatório da SEC e da CFTC.

## Passo a passo: coloque sua primeira ordem limitada com segurança

Pratique primeiro com um valor bem pequeno.

1. **Passo 1 — Abra a tela de negociação** da cripto ou da ação e escolha **Comprar** (Buy).
2. **Passo 2 — Aperte a aba «Limit»**, não «Market».
3. **Passo 3 — Digite o seu preço.** Olhe antes o preço atual (por exemplo, o bitcoin está em {{price:btc}} agora). Um limite muito abaixo dele pode nunca ser executado.
4. **Passo 4 — Digite a quantidade.** Confira se o campo é em moedas/ações ou em dinheiro (USD, EUR). Esse é o erro de digitação mais comum.
5. **Passo 5 — Confira o resumo**: tipo, preço, quantidade, total e taxa. Depois confirme.
6. **Passo 6 — Encontre sua ordem** em «Ordens abertas» (Open orders). Lá você pode cancelá-la a qualquer momento enquanto ela não for executada. Depois de executada, ela vai para o «Histórico de ordens» (Order history).

> **⚠️ Atenção**
> - **Ordens a mercado em mercados com pouca liquidez.** Em criptos pequenas ou fora do horário normal, uma ordem a mercado pode sair bem pior do que o preço da tela (isso se chama **slippage**, ou derrapagem). Nesses casos, use ordem limitada.
> - **Achar que o stop loss garante o seu preço.** Não garante: ele garante a venda, não o preço. Gaps e quedas fortes podem empurrar a execução bem para baixo. Uma stop limitada protege o preço, mas pode não vender.
> - **Confundir os campos.** Lado errado (Vender em vez de Comprar), um zero a mais na quantidade ou preço digitado no campo errado. Leia o resumo antes de confirmar.

## O que significa se você compra regularmente

Se você só compra um pouco toda semana ou todo mês, não precisa de ordens complicadas. Uma ordem a mercado num ativo grande e líquido costuma bastar, ou uma ordem limitada um pouco acima do preço atual, se quiser um teto. O resultado de verdade vem do tempo no mercado: US$ 10 por dia em bitcoin durante 3 anos valeriam hoje {{dca:btc:3}} (você teria aplicado {{dcainv:3}}) — resultados passados, não uma previsão.

A seguir no WhatIfStack: veja como o livro de ofertas e os grandes traders movem o mercado na [seção de Trading]({lang}/trading/) e no [rastreador de baleias da Hyperliquid]({lang}/trading/hyperliquid/), compare taxas nas [exchanges]({lang}/exchanges/) e encontre todas as aulas na [página Aprender]({lang}/learn/).

## Fontes

- [Investor.gov (SEC): Tipos de ordem](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Boletim ao investidor — ordens stop, stop limitada e trailing stop](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Tipos de ordem](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC e SEC: Relatório sobre os eventos de mercado de 6 de maio de 2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Não é recomendação de investimento.*
