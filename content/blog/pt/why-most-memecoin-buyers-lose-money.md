---
title: "Por que a maioria de quem compra memecoins perde dinheiro: a matemática dos lançamentos, slippage e taxas"
description: Só 0,41% das carteiras da pump.fun lucraram mais de US$ 10 mil. A matemática simples de lançamentos, slippage e taxas que joga contra quem compra memecoins.
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: 0,41%
stat_label: de 13,55 milhões de carteiras da pump.fun tinham realizado mais de US$ 10 mil de lucro (dados da Dune, janeiro de 2025)
---
**Por que a maioria das pessoas que compram memecoins perde dinheiro?** Porque a matemática joga contra elas antes mesmo de o preço se mexer: a maioria dos tokens novos morre em menos de um dia, cada compra e venda custa taxas e slippage (deslizamento de preço), e os primeiros compradores (muitas vezes bots e insiders) vendem para quem chega depois. Para ganhar, um token precisa sobreviver *e* subir o bastante para cobrir tudo isso.

> **Pontos principais**
> - Dados da Dune divulgados em janeiro de 2025 mostraram que só cerca de **0,41%** de 13,55 milhões de carteiras da pump.fun tinham realizado mais de **US$ 10 mil** de lucro.
> - A CoinGecko descobriu que **68,67%** dos tokens da pump.fun fizeram a última negociação no dia do lançamento (dados de janeiro de 2024 a junho de 2026).
> - Cada ida e volta (compra + venda) num token novo pode custar **2,5% ou mais** só em taxas da plataforma, além das taxas de rede e do slippage.

## Parte 1 — A matemática da sobrevivência

A maioria das memecoins não é "barata" — ela simplesmente dura pouco.

- **Morte no dia do lançamento.** A CoinGecko contou 18,67 milhões de tokens na pump.fun; 68,67% fizeram a última negociação no mesmo dia em que foram lançados (relatório de 25 de junho de 2026).
- **Poucos chegam a um mercado de verdade.** "Graduar" (graduation) significa que o token sai da curva inicial da pump.fun e ganha um pool de negociação normal. Segundo dados da Dune, a taxa semanal de graduação ficou abaixo de **1%** por quatro semanas a partir de 17 de fevereiro de 2025; a melhor semana, em novembro de 2024, foi de **1,67%**. Em março de 2026 chegou a **2,01%**, a maior desde julho de 2025.

Então, se você escolher lançamentos novos ao acaso, vai ficar principalmente com moedas que param de ser negociadas. Alguns grandes vencedores não pagam por muitas moedas que vão a zero, a não ser que você escolha muito bem — e no primeiro dia ninguém sabe quais vão sobreviver.

## Parte 2 — Taxas: você paga na entrada e na saída

A página de ajuda da pump.fun (setembro de 2025) indica uma taxa de **1,25%** em cada negociação antes da graduação (0,95% para a plataforma e 0,30% para o criador). Depois da graduação, a taxa cai conforme o token cresce: de 1,25% nos menores até 0,30% nos maiores. Por cima disso vêm as taxas de rede da Solana e as taxas opcionais de "prioridade" e de proteção contra MEV (0,003–0,03 SOL por negociação, segundo a página deles).

**Exemplo prático (ilustração, não são preços reais):** você compra US$ 50 de um token novo e paga uma taxa de prioridade de 0,02 SOL em cada direção. A taxa de 1,25% na entrada e na saída dá cerca de US$ 1,25, e duas taxas de prioridade podem somar mais alguns dólares. Só para voltar aos US$ 50, o token precisa subir talvez **5–10%**. Com operações de US$ 10 é bem pior: as taxas fixas comem uma fatia muito maior.

## Parte 3 — Slippage: o preço muda enquanto você compra

**Slippage** (deslizamento) é a diferença entre o preço que você vê e o preço que você realmente paga (veja o [glossário de memecoins]({lang}/memes/glossary/)). Tokens novos têm pools minúsculos, então a sua própria compra empurra o preço para cima — e as compras de todo mundo no mesmo segundo também. Se você define um slippage de 10–20% (muitos apps sugerem isso para moedas novas), está aceitando pagar até esse tanto a mais. Na venda acontece o mesmo, só que ao contrário: num pool raso, a sua venda derruba o preço.

## Parte 4 — Quem está do outro lado

Os primeiros compradores costumam ser snipers, bundlers e a carteira do desenvolvedor (veja [snipers, bundlers e carteiras do desenvolvedor]({lang}/blog/snipers-bundlers-dev-wallets/)). Eles compram pelo menor preço e vendem na primeira onda de demanda. Se você compra depois do primeiro candle verde, muitas vezes você é a "liquidez de saída" (exit liquidity) — o dinheiro para quem eles vendem.

## Passo a passo: faça as contas antes de tocar em «Comprar»

1. **Passo 1 — Some as taxas.** Olhe a linha de taxa na tela de swap e acrescente a taxa de rede/prioridade. Multiplique por dois (compra + venda).
2. **Passo 2 — Confira o slippage.** Deixe o mais baixo que a operação permitir (por exemplo, 1–3% numa moeda com pool grande). Se uma moeda precisa de 20% de slippage, isso é um alerta.
3. **Passo 3 — Veja o tamanho do pool.** Na nossa [página de memecoins]({lang}/memes/), abra o token e olhe a liquidez. Pool pequeno = slippage grande nos dois sentidos.
4. **Passo 4 — Faça a checagem de segurança.** Use [como checar uma memecoin antes de comprar]({lang}/blog/how-to-check-a-memecoin-before-buying/).
5. **Passo 5 — Decida o prejuízo máximo antes.** Use só dinheiro que você pode perder por completo e defina o valor antes de começar.

> **⚠️ Atenção**
> - **"Custa só US$ 0,0001, pode subir 1000×."** Preço baixo não quer dizer nada; muitos tokens existem aos bilhões. O que importa é se o token sobrevive e quem está vendendo para você.
> - **Muitas operações pequenas.** As taxas fixas de rede e de prioridade podem comer mais de 10% de uma operação de US$ 10 antes de o preço se mexer.
> - **Prints de vencedores.** Você vê os 0,41% que ganharam muito, não os milhões que perderam; "gurus" muitas vezes vendem as moedas que divulgam.

## O que isso significa se você compra regularmente

Compras pequenas e regulares funcionam com ativos que continuam existindo anos depois — não com tokens que podem parar de ser negociados hoje à noite. Se você quer cripto, o caminho comum para iniciantes é uma moeda grande e líquida, comprada aos poucos; para comparar, a moeda da própria Solana, SOL, está agora em {{price:sol}} ({{chg1y:sol}} em 12 meses) — resultados passados, não uma previsão. Você pode testar "US$ 10 por dia" em qualquer ativo na nossa calculadora e acompanhar na sua [página de carteira]({lang}/me/).

Aula anterior: [snipers, bundlers e carteiras do desenvolvedor]({lang}/blog/snipers-bundlers-dev-wallets/). Todas as lições estão na [página Aprender]({lang}/learn/).

## Fontes

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data (11 de janeiro de 2025)](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive (14 de março de 2025)](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, dados da Dune: pump.fun graduation rate hits 2.01% (17 de março de 2026)](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / dados da CoinGecko: nearly 70% of pump.fun tokens disappear on launch day (25 de junho de 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [Central de ajuda da pump.fun: Transaction fees on pump.fun (setembro de 2025)](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*Não é recomendação de investimento.*
