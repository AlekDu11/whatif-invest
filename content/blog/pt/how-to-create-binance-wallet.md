---
title: Como criar uma Binance Wallet e comprar uma memecoin: passo a passo
description: Crie a Binance Wallet no app da Binance, faça o backup, traga moedas da sua conta Binance, encontre o token pelo contrato e faça o swap com segurança.
date: 2026-11-23T12:30:00Z
category: learn
track: memes
step: 5
assets: bnb, sol, doge
stat: 3
stat_label: partes da chave protegem uma Binance Wallet; você precisa de 2 para entrar
---
**Como criar uma Binance Wallet?** Abra o app da Binance, mude no topo para a aba **Wallet** (carteira), toque em **Create Keyless Wallet** (criar carteira sem chave) e faça o backup com uma senha de recuperação. Leva alguns minutos, não exige frase-semente e dá a você uma carteira de autocustódia (uma carteira em que você, e não a exchange, controla as moedas) para comprar tokens on-chain, como memecoins.

> **Pontos principais**
> - A Binance Wallet fica dentro do app da Binance. Você precisa de uma conta Binance verificada, mas as moedas na carteira são de autocustódia: o backup é responsabilidade sua.
> - É uma carteira "sem chave" (MPC): a chave é dividida em 3 partes, uma no seu celular, uma no seu backup na nuvem e uma com a Binance. Quaisquer 2 delas abrem a carteira.
> - Nunca pule o backup. Se você perder o celular **e** esquecer a senha de recuperação, a Binance não consegue restaurar a carteira.

Antes de começar: a maioria das memecoins novas perde quase todo o valor. Use só dinheiro que você pode perder por completo; veja [o que são memecoins]({lang}/blog/what-are-memecoins/).

## Do que você precisa

- Um celular com o app oficial da Binance (baixe só da App Store, do Google Play ou de binance.com: apps falsos são comuns).
- Uma conta Binance com a verificação de identidade feita (KYC, mostrar seu documento). Se ainda não tem, pode se cadastrar pelo nosso link: [Binance Wallet](/go/binance-web3?from=learn&l=pt).
- Um pouco de BNB ou SOL na sua conta Binance para comprar e pagar as taxas de rede.

## Passo 1. Abra a carteira

1. Entre no app da Binance.
2. No topo da tela, mude de **Exchange** para **Wallet**.
3. Toque em **Create Keyless Wallet**. (Se você já tem outra carteira, a outra opção é **Import Wallet** (importar carteira); iniciantes não precisam dela.)

A criação leva segundos. O app não mostra 12 ou 24 palavras-semente: em vez disso, usa MPC (computação multipartes: a chave é dividida em pedaços que nunca ficam no mesmo lugar).

## Passo 2. Faça o backup (não pule esta etapa)

O app oferece três formas de guardar sua parte de backup. Escolha uma:

- **iCloud** ou **Google Drive**. Você define uma **senha de recuperação** que só você conhece. A parte é criptografada com ela e salva na sua nuvem.
- **QR code.** Você define uma senha de recuperação e salva um QR code; a parte fica guardada numa nuvem descentralizada.
- **Quick Backup** (backup rápido). Você confirma com Face ID ou digital; sem senha, mas a parte fica com um provedor terceiro.

Anote a senha de recuperação no papel e guarde num lugar seguro. Depois confira: toque em **Settings** (configurações; no canto superior esquerdo de Home ou Assets) → **Wallet Management** (gerenciar carteiras). Você deve ver a etiqueta **Backed Up** (backup feito).

## Passo 3. Leve moedas da Binance para a carteira

1. Na carteira, toque em **Receive** (receber) → **Withdraw from Binance Exchange** (sacar da exchange Binance).
2. Escolha a moeda (por exemplo BNB) **e a rede** (BNB Smart Chain para BNB, Solana para SOL). A rede precisa ser a mesma.
3. Digite o valor. O app mostra a taxa e o valor final antes de você confirmar.
4. Escolha se o dinheiro sai da conta Spot ou Funding, toque em **Withdraw** (sacar), confira o endereço e a rede e toque em **Confirm** (confirmar).

Comece com um pequeno valor de teste. Uma transferência confirmada não pode ser cancelada. Deixe sempre um pouco de BNB ou SOL na carteira: toda ação na blockchain custa uma taxa de rede (gas), mesmo quando falha.

## Passo 4. Encontre o token certo pelo endereço do contrato

Muitas memecoins têm cópias com o mesmo nome e logo. A única identificação confiável é o **endereço do contrato** (uma sequência longa de letras e números, única para cada token).

1. Pegue o endereço de uma fonte confiável: a conta verificada do projeto, um grande site de dados ou a página do token na nossa [página de memecoins]({lang}/memes/).
2. Na tela **Markets** (mercados) ou **Trade** (negociar) da carteira, cole o endereço na busca em vez de digitar o nome.
3. Compare os primeiros e os últimos 4–6 caracteres com a sua fonte.

## Passo 5. Confira o token antes de comprar

Na nossa [página de memecoins]({lang}/memes/), cada página de token mostra a verificação de segurança da Binance e os números principais. Observe:

- **Liquidez**: quanto dinheiro há no pool de negociação. Pouca liquidez = talvez você não consiga vender.
- **Holders e fatia do top 10**: se poucas carteiras detêm a maior parte da oferta, elas podem derrubar o preço.
- **Idade**: um token criado há uma hora é um bilhete de loteria.
- **Alertas**: se aparecer qualquer alerta de risco ou de segurança, pare.

A própria Binance diz que não verifica os tokens listados no Meme Rush (o feed de memecoins recém-criadas), então a verificação é com você. Nossa [lição sobre golpes e rug pulls]({lang}/blog/memecoin-scams-rug-pull/) lista os sinais de alerta.

## Passo 6. Faça o swap

1. Abra **Trade** → **Swap** (troca). Escolha com o que você paga (BNB) e o token que quer, na mesma rede.
2. Digite um valor pequeno. Leia a cotação, o **slippage** (derrapagem: a maior variação de preço que você aceita antes de a operação falhar) e a taxa de rede.
3. Alguns tokens precisam antes de uma etapa de **Approve** (aprovar); ela custa uma pequena taxa.
4. Toque em **Swap** e confirme com sua passkey ou 2FA.

Para vender, faça o mesmo ao contrário. Se quiser ver os tokens mais novos, a aba Markets tem o **Meme Rush**: tokens recém-criados são negociados ali numa "curva de vinculação" (bonding curve) e não podem sair da carteira até "migrarem" para uma DEX normal (exchange descentralizada). É o canto mais arriscado do mercado.

> **⚠️ Atenção**
> - **Sem backup, ou com a senha salva em prints.** Perdeu o celular e a senha, as moedas somem para sempre.
> - **Rede errada ou endereço errado.** O FAQ da Binance diz que tokens enviados a um endereço errado não podem ser devolvidos. Envie sempre um valor de teste.
> - **Tokens falsos e mensagens de "suporte".** Busque só pelo endereço do contrato. A equipe da Binance nunca vai pedir sua senha de recuperação nem pedir para "verificar" sua carteira num site.

Próxima lição: como conectar a Binance Wallet a um site DEX e levar moedas de volta para a Binance. Todas as lições na seção [Aprender]({lang}/learn/).

## Fontes

- [Binance: Frequently Asked Questions on Binance Wallet](https://www.binance.com/en/support/faq/5a3fc86a702b43e1a4a398ebd8853b77)
- [Binance: What Is a Keyless Wallet and Why Do I Need to Back It Up?](https://www.binance.com/en/support/faq/4efebcb9a937417ca31baa2f7754c50f)
- [Binance: How to Back Up My Binance Wallet?](https://www.binance.com/en/support/faq/53521dedad474c908ec3761a935cb8d6)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance: What Is Binance Wallet Swap?](https://www.binance.com/en/support/faq/7ebe19e8ff884cc09a9dbb064aff131f)
- [Binance: Introducing Meme Rush — Fair Mode (9 Oct 2025)](https://www.binance.com/en/support/announcement/detail/c21eac66543c4a62b8b6868cb01ba4f3)

*Não é recomendação de investimento. Memecoins são extremamente arriscadas; este guia explica como o app funciona e não recomenda comprar nenhum token. A Binance Wallet pode não estar disponível em todos os países.*
