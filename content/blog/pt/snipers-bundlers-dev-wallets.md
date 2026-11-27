---
title: "Snipers, bundlers e carteiras do desenvolvedor: como os insiders lucram no lançamento de uma memecoin"
description: Bots e insiders compram muitas memecoins novas no primeiro segundo e vendem em minutos. Como funcionam snipers, bundlers e dev wallets e como identificá-los.
date: 2026-11-27T09:30:00Z
category: learn
track: memes
step: 16
assets: sol, bnb
stat: 87%
stat_label: dos snipes na pump.fun feitos por carteiras ligadas ao criador deram lucro (Pine Analytics, abril 2025)
---
**Quem compra uma memecoin nova antes mesmo de você conseguir vê-la?** Muitas vezes, bots e insiders. Os **snipers** ("atiradores") compram logo no primeiro bloco, os **bundlers** compram com várias carteiras ao mesmo tempo e a **dev wallet** (a carteira do próprio criador) pode ter uma fatia grande desde o início. Eles compram mais barato e muitas vezes vendem em minutos — para quem chega depois.

> **Pontos principais**
> - A Pine Analytics descobriu que mais de **50%** dos tokens da pump.fun sofreram snipe no mesmo bloco em que foram criados (relatório de 21 de abril de 2025).
> - Em um mês (a partir de 15 de março de 2025), ela contou **mais de 15.000** snipes de carteiras abastecidas diretamente pelo criador do token; **87%** deram lucro e cerca de **85%** foram vendidos por completo em **5 minutos**.
> - A CoinGecko descobriu que **68,67%** de 18,67 milhões de tokens da pump.fun fizeram a última negociação no dia do lançamento (janeiro de 2024 – junho de 2026, dados de 25 de junho de 2026).

## Os três insiders, em palavras simples

Os três termos estão no nosso [glossário de memecoins]({lang}/memes/glossary/).

- **Sniper** — uma carteira, quase sempre um bot, que compra nos primeiros 0–3 blocos (um bloco é uma "página" da blockchain; na Solana leva menos de um segundo). Usa ferramentas especiais para entrar antes dos compradores comuns, monta uma posição grande barato e vende na primeira onda de procura.
- **Bundler** — uma única pessoa que compra com várias carteiras no mesmo bloco ou na mesma transação. No gráfico parecem 20 compradores diferentes; na verdade, é um só. Objetivo: esconder quanto uma pessoa tem e simular demanda.
- **Dev wallet** — a carteira que criou o token. Se ela fica com uma fatia grande, ou manda tokens discretamente para carteiras novas, pode vender em cima de todo mundo a qualquer momento.

O relatório da Pine Analytics "Exit Liquidity Machines" (exit liquidity, "liquidez de saída", são os compradores atrasados para quem os insiders vendem) mostrou como isso funciona na pump.fun: os criadores mandavam SOL para carteiras "descartáveis" (burner) novas, essas carteiras compravam no bloco de criação e a maioria vendia em uma ou duas operações. Mais de 55% desses snipes foram fechados por completo em menos de um minuto.

## Passo 1 — Olhe os primeiros compradores

Abra o token num rastreador (na nossa [página de memecoins]({lang}/memes/), a página do token mostra os holders e uma checagem de segurança; ferramentas como GMGN ou Solscan mostram as primeiras negociações). Se muitas carteiras compraram **no mesmo segundo do lançamento**, com **valores parecidos**, isso é sniping ou bundling.

## Passo 2 — Veja quanto os maiores holders têm

Olhe os **10 maiores holders** sem contar o pool de liquidez. O provedor de dados Mobula considera saudável o top 10 abaixo de **30%** e a fatia do dev abaixo de **5%** (ou travada/queimada), e um sinal de alerta o top 10 acima de **50%**. Várias carteiras sniper somando mais de 20% é outro.

## Passo 3 — Confira a dev wallet

Encontre o criador ("dev", "deployer" ou "creator" na página do token). Ele já vendeu? Mandou tokens para carteiras novas pouco antes ou logo depois do lançamento? A mesma carteira já lançou muitos tokens que morreram todos? Um dev que lança dezenas de moedas por semana está rodando uma máquina, não um projeto.

## Passo 4 — Procure carteiras novas abastecidas pelo mesmo lugar

Os bundles costumam vir de carteiras criadas minutos antes do lançamento e abastecidas pela mesma fonte. Ferramentas de bubble map (mapa de bolhas) desenham essas carteiras como um único grupo conectado. Se a "comunidade" é um grupo só, o preço está na mão de uma pessoa.

## Passo 5 — Nunca corra atrás do primeiro candle

O salto nos primeiros minutos é justamente quando os snipers vendem. Se ainda assim quiser comprar, espere, faça a checagem completa de [como checar uma memecoin antes de comprar]({lang}/blog/how-to-check-a-memecoin-before-buying/), use um valor pequeno e defina seu limite antes.

> **⚠️ Atenção**
> - **"Muitos holders = seguro."** Bundlers criam centenas de holders com uma só carteira. Veja quem abasteceu essas carteiras, não quantas são.
> - **"O dev queimou/travou os tokens."** Confira você mesmo na blockchain; um pool travado não impede as carteiras sniper de vender.
> - **Bots para copiar o "smart money".** Carteiras que parecem gênios muitas vezes são os próprios snipers, ou o dev; quando você copia, eles já estão vendendo.

## O que um iniciante pode aprender com isso

Num lançamento, normalmente você não chega cedo — quem chega cedo são os bots. Quase 7 em cada 10 tokens da pump.fun pararam de ser negociados no primeiro dia, então a escolha mais segura muitas vezes é nem entrar. Se entrar, trate como dinheiro que você pode perder por completo. Comprar regularmente funciona com ativos que sobrevivem por anos; para comparar, a moeda da própria Solana, SOL, está em {{price:sol}} agora ({{chg1y:sol}} em 12 meses) — são resultados passados, não uma previsão.

Lição anterior: [como funciona a Binance Alpha]({lang}/blog/how-binance-alpha-works/). Próxima lição: por que a maioria dos compradores de memecoins perde dinheiro. Todas as lições estão na [página Aprender]({lang}/learn/).

## Fontes

- [Pine Analytics: Exit Liquidity Machines — dissecando o farming na pump.fun (21 de abril de 2025)](https://pineanalytics.substack.com/p/exit-liquidity-machines)
- [BeInCrypto: snipers de memecoins na Pump.fun são um problema sistemático (22 de abril de 2025)](https://beincrypto.com/pump-fun-meme-coin-snipers-systematic-problem)
- [Documentação da Mobula: como detectar snipers e bundlers](https://docs.mobula.io/almanac/detecting-snipers-bundlers)
- [KuCoin News / dados da CoinGecko: quase 70% dos tokens da pump.fun somem no dia do lançamento (25 de junho de 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)

*Não é recomendação de investimento.*
