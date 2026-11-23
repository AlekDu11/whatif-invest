---
title: Como checar uma memecoin antes de comprar: 6 verificações em 5 minutos
description: Antes de comprar uma memecoin, cheque o contrato, a liquidez, os holders, a fatia do top 10, a idade e a auditoria da Binance. Checklist simples.
date: 2026-11-23T16:30:00Z
category: learn
track: memes
step: 6
assets: sol, bnb, doge
stat: 6
stat_label: verificações antes de comprar qualquer memecoin
---
**Como checar uma memecoin antes de comprar?** Encontre o token pelo endereço do contrato e verifique seis coisas: a auditoria de segurança, a liquidez, o número de holders, quanto as 10 maiores carteiras detêm, a idade do token e se o criador ainda pode alterá-lo. Se uma verificação der vermelho, pule essa moeda. Existem milhares de outras.

> **Pontos principais**
> - Essas verificações não tornam uma memecoin segura. Elas só ajudam a evitar as armadilhas mais óbvias: tokens que você não consegue vender, cópias falsas e moedas que poucas carteiras podem derrubar.
> - A aba **Audit** (auditoria) da Binance Wallet checa riscos de contrato, de negociação e de golpe (por exemplo, um «honeypot» — um token que você compra, mas nunca consegue vender). A própria Binance diz que a auditoria não é infalível.
> - Na nossa [página de memecoins]({lang}/memes/) o filtro de qualidade já vem ligado: «Só qualidade: liquidez US$ 100 mil+, 1 dia+».

Esta lição continua [Como conectar a Binance Wallet a uma DEX]({lang}/blog/connect-binance-wallet-to-dex/). Memecoins são extremamente arriscadas — use só dinheiro que você pode perder.

## Passo 1 — Pegue o endereço de contrato certo

Todo token tem um **endereço de contrato** (a identidade única dele na blockchain, uma sequência longa de letras e números). Qualquer pessoa pode criar um token com o mesmo nome e logo, então o nome não quer dizer nada.

1. Copie o endereço da conta oficial do projeto ou de um site de dados confiável.
2. Cole na busca da sua carteira. Compare os 4 primeiros e os 4 últimos caracteres.
3. Se aparecerem vários tokens com o mesmo nome, os outros são cópias.

## Passo 2 — Abra a auditoria de segurança

No app da Binance, abra o token em **Wallet** (carteira) e toque na aba **Audit** (no site: clique no token e depois em **Audit**). Nas páginas de tokens da nossa seção de memecoins você vê a mesma checagem como **Verificação de segurança da Binance: Risco baixo / Risco médio / Risco alto**.

Olhe três grupos:

- **Contract risk** (risco do contrato) — o criador pode bloquear vendas, colocar carteiras numa lista negra, mudar a taxa ou mudar saldos?
- **Trading risk** (risco de negociação) — risco de honeypot, taxa estranha na compra ou na venda (uma cobrança em cada operação), pouca liquidez, risco de rug pull.
- **Scam risk** (risco de golpe) — token falso, golpe conhecido, spam.

Qualquer item vermelho = não compre. «Risco baixo» também não quer dizer seguro: o criador ainda pode fazer coisas depois da sua compra.

## Passo 3 — Cheque a liquidez

Liquidez é o dinheiro no pool de negociação que permite que você venda. Se ela for minúscula, até uma venda pequena derruba muito o preço, e o criador pode retirá-la (um rug pull, «puxar o tapete»). No WhatIfStack, nosso filtro padrão esconde tokens com menos de US$ 100 mil de liquidez. Se o site de dados mostrar, veja também se a liquidez do pool está bloqueada ou queimada (removida para sempre).

## Passo 4 — Conte os holders e a fatia do top 10

Na página do token, olhe **Holders** (quantas carteiras têm o token) e **Top 10 detêm** (que parte de todas as moedas está com as 10 maiores carteiras). Algumas centenas de holders e um top 10 com fatia grande significam que um punhado de pessoas pode vender e derrubar o preço. Atenção: os endereços do pool e de queima também aparecem no top 10 — essa parte é normal.

## Passo 5 — Cheque a idade

A maioria dos tokens golpe dura horas ou dias. Um token com menos de um dia não tem histórico nenhum. Nosso filtro em /memes/ mostra só tokens com pelo menos 1 dia. Mais antigo não é seguro — só é menos desconhecido.

## Passo 6 — Na Solana: o criador ainda pode mudar o token?

Na Solana, duas configurações importam:

- **Mint authority** (permissão de emissão) — o direito de criar novos tokens. Se ainda estiver ativa, o criador pode emitir mais e a sua fatia encolhe.
- **Freeze authority** (permissão de congelamento) — o direito de congelar uma carteira. Se ainda estiver ativa, o criador pode impedir que você movimente ou venda.

O estado mais seguro é «revoked» ou «disabled» (ninguém tem essa permissão). Você vê as duas na página do token num explorador de blocos como o Solscan.

> **⚠️ Atenção**
> - **Uma cópia falsa com o mesmo nome.** Compre sempre pelo endereço do contrato, nunca pelo nome ou logo.
> - **Um honeypot.** Você compra, o gráfico sobe, mas ninguém consegue vender. Um histórico com compras e sem vendas é sinal de alerta.
> - **Confiar num único sinal verde.** Auditoria, muitos holders ou um nome famoso não protegem você se o preço simplesmente cair — a maioria das memecoins termina perto de zero.

## O que isso significa se você compra regularmente

Compras pequenas e regulares funcionam melhor com ativos que provavelmente ainda vão existir daqui a cinco anos. A maioria das memecoins não é assim. Se mesmo assim quiser testar uma, use um valor minúsculo e fixo, e acompanhe junto com o resto do seu dinheiro na [sua carteira]({lang}/me/).

Próxima lição: a história do Dogecoin. Todas as lições na seção [Aprender]({lang}/learn/).

## Fontes

- [Binance: How to Use the Token Audit Feature in Binance Wallet](https://www.binance.com/en/support/faq/detail/fd1b21bac5114feda49dd185461afdda)
- [Binance.US: What is a honeypot scam?](https://support.binance.us/en/articles/15388146-what-is-a-honeypot-scam)
- [Solana docs: Set authority (mint and freeze authority)](https://solana.com/docs/tokens/basics/set-authority)
- [Solana docs: Freeze account](https://solana.com/docs/tokens/basics/freeze-account)

*Não é recomendação de investimento. Este guia explica como checar um token e não recomenda comprar nenhuma moeda.*
