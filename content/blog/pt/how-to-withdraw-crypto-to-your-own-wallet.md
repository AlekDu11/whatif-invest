---
title: Como sacar cripto de uma corretora para a sua própria carteira: passo a passo
description: Leve suas moedas da corretora para a sua carteira com segurança: copie o endereço certo, escolha a mesma rede, use o memo se precisar e teste antes.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 rede
stat_label: a corretora e a carteira precisam usar a mesma, senão as moedas podem se perder
---
**Como sacar cripto para a sua própria carteira?** Na sua carteira, você copia o seu **endereço de recebimento** da moeda. Depois, na corretora, abre **Withdraw** (Sacar), cola esse endereço, escolhe **a mesma rede** que a sua carteira usa, digita um valor pequeno de teste e confirma com 2FA. Quando o teste chegar, você envia o resto.

> **Pontos principais**
> - Três coisas precisam bater: a **moeda**, o **endereço** e a **rede** (a blockchain por onde as moedas viajam, por exemplo Ethereum, BNB Smart Chain, TRON ou Solana). A Binance avisa que moedas enviadas pela rede errada podem se perder para sempre.
> - Algumas moedas (como XRP, XLM ou ATOM) também pedem um **memo** ou **tag** (um número curto que diz a quem recebe de quem são as moedas). Sem ele, a transferência pode travar ou ir para a pessoa errada.
> - **Sempre envie um teste pequeno primeiro.** Um saque não pode ser cancelado depois que as moedas saíram da corretora.

Esta lição continua [Como programar uma compra recorrente]({lang}/blog/how-to-set-up-a-recurring-buy/). Por que vale a pena ter a sua própria carteira está explicado em [carteiras quentes e frias]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Antes de começar

Você precisa de duas coisas. Uma conta numa corretora com moedas, protegida com 2FA — veja [Como se cadastrar numa corretora de cripto]({lang}/blog/how-to-register-on-a-crypto-exchange/). E o seu próprio app de carteira já configurado, com a **seed phrase** (as 12 ou 24 palavras secretas que restauram a carteira) anotada em papel e guardada offline. Nunca digite a seed phrase em nenhum outro lugar — nenhuma corretora, site ou pessoa do "suporte" vai precisar dela.

## Passo 1 — Copie o endereço de recebimento da sua carteira

1. Abra o app da carteira e toque em **Receive** (Receber; às vezes **Deposit**).
2. Escolha a moeda, por exemplo Bitcoin ou USDT.
3. Se a carteira pedir, escolha a rede. Anote qual é — por exemplo "USDT na TRON (TRC20)" ou "USDT na Ethereum (ERC20)".
4. Toque em **Copy** (Copiar) ao lado do endereço. Não digite à mão.

Um endereço é uma linha longa de letras e números. Endereços de Bitcoin costumam começar com **bc1**, os de Ethereum e BNB Smart Chain com **0x** e os de TRON com **T**.

## Passo 2 — Abra o Withdraw na corretora

No app da Binance, o caminho é **Assets → Spot → Send → Withdraw Crypto**; no site, **Wallet → Overview → Withdraw**. Outras corretoras têm um botão **Withdraw** ao lado de cada moeda na tela de carteira ou portfólio. Escolha a mesma moeda do passo 1.

## Passo 3 — Cole o endereço e escolha a rede

1. Cole o endereço no campo **Address** (Endereço).
2. Compare os **4 primeiros e os 4 últimos caracteres** com a sua carteira. Alguns malwares trocam o endereço copiado pelo do ladrão.
3. Escolha a **rede**. Ela precisa ser a que a carteira mostrou no passo 1. A Binance pode sugerir uma rede automaticamente — confira mesmo assim. Não escolha uma rede só porque a taxa dela é a mais baixa.
4. Se aparecer um campo **Memo** ou **Tag** e a sua carteira deu um, preencha. Se a sua carteira não mostra nenhum memo, normalmente ela não precisa de um — mas confirme nas páginas de ajuda da carteira.

Dica: se estiver em dúvida, salve o endereço no **Address Management** (catálogo de endereços) da corretora. A Binance também tem uma **whitelist** (lista de permissões): com ela ativada, os saques só podem ir para endereços salvos, o que ajuda se alguém roubar a sua senha.

## Passo 4 — Envie um teste pequeno

1. Digite um valor pequeno — um pouco acima do saque mínimo que aparece na tela.
2. Olhe as linhas **taxa da rede** e **você vai receber**. A taxa é fixa por saque, então num valor bem pequeno ela pode ser uma parte grande.
3. Toque em **Withdraw** e confirme com o código 2FA ou a passkey. Algumas corretoras também mandam um e-mail de confirmação — abra e clique em **Confirm**.

## Passo 5 — Confira se chegou e envie o resto

1. Espere. Uma transferência pode levar de alguns segundos a cerca de uma hora, dependendo da rede e do movimento.
2. Na corretora, abra o histórico de saques para ver o status e o **TxID** (o ID da transação, que você pode procurar num explorador de blocos).
3. Quando as moedas aparecerem na carteira, repita os passos 2 a 4 com o resto. O endereço já está no histórico ou no catálogo, então a segunda vez é mais rápida.

Adicione as moedas ao [seu portfólio]({lang}/me/) para acompanhar o valor delas num só lugar, onde quer que estejam guardadas.

> **⚠️ Atenção**
> - **Rede errada.** O USDT existe em muitas redes. Enviar USDT "TRC20" para um endereço que só espera "ERC20" pode fazer as moedas se perderem. Confira a rede duas vezes.
> - **Memo ou tag faltando.** Corretoras e carteiras que pedem memo não sabem de quem são as moedas que chegaram sem ele. A recuperação, quando é possível, é lenta e cobra uma taxa.
> - **Falso suporte e sites de "verificação de endereço".** Ninguém sério pede a sua seed phrase ou pede para você "verificar" uma carteira enviando moedas. Saque só pelo app ou site oficial.

## O que isso significa se você compra regularmente

Se você compra um pouco toda semana ou todo mês, não precisa sacar depois de cada compra — cada saque tem uma taxa. Muita gente deixa as moedas juntarem na corretora e, de vez em quando, passa tudo para a própria carteira, por exemplo uma vez por trimestre, numa transferência maior. Exemplo da nossa calculadora: US$ 10 por dia em bitcoin durante 3 anos ({{dcainv:3}} no total) viraram {{dca:btc:3}} ({{dcaroi:btc:3}}). São resultados passados, não uma previsão. Agora o bitcoin está em {{price:btc}}; veja a [página do Bitcoin]({lang}/btc/).

Lição anterior: [Como programar uma compra recorrente]({lang}/blog/how-to-set-up-a-recurring-buy/). Próxima lição: como vender cripto e receber o dinheiro na sua conta bancária. Compare corretoras na nossa [página de corretoras]({lang}/exchanges/); todas as lições estão na [página Aprender]({lang}/learn/).

## Fontes

- [Binance Support: como depositar e sacar criptomoedas na Binance (atualizado em março de 2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: como recuperar um depósito com tag ou memo errado ou faltando](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: como sacar cripto da sua conta Binance.US (junho de 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*Não é recomendação de investimento.*
