---
title: Como conectar a Binance Wallet a uma DEX e devolver moedas: passo a passo
description: Conecte a Binance Wallet a uma DEX com segurança, devolva moedas à sua conta Binance na rede certa e remova aprovações antigas — em passos simples.
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: pequena transferência de teste antes de cada endereço ou rede nova
---
**Como conectar a Binance Wallet a uma DEX?** Abra o site oficial da DEX, clique em **Connect Wallet** (conectar carteira), escolha Binance Wallet (ou WalletConnect e escaneie o QR code com o app da Binance) e confirme no app. Para devolver moedas, copie o seu **endereço de depósito** da Binance para a mesma moeda e rede e envie para ele a partir da carteira — primeiro um valor pequeno de teste.

> **Pontos principais**
> - Uma DEX (exchange descentralizada — um site onde você troca tokens direto da sua própria carteira) nunca precisa da sua senha de recuperação nem da frase-semente. Conectar só permite que o site *peça* assinaturas; nada se move até você confirmar.
> - A rede precisa ser a mesma dos dois lados (BNB Smart Chain para BNB Smart Chain, Solana para Solana). Rede ou endereço errado pode significar perder as moedas.
> - Cada «Approve» deixa um site gastar um token por você. Dê aprovações pequenas e remova as que não usa mais.

Esta lição continua [Como criar uma Binance Wallet]({lang}/blog/how-to-create-binance-wallet/). Memecoins são extremamente arriscadas — use só dinheiro que você pode perder.

## Passo 1. Abra o site verdadeiro

Sites falsos de DEX com o mesmo logo são uma das armadilhas mais comuns.

1. Digite o endereço você mesmo ou use um favorito. Não clique em anúncios na busca nem em links de chats.
2. Confira a barra de endereço letra por letra.
3. Verifique se a DEX funciona na rede em que estão as suas moedas.

## Passo 2. Conecte a carteira

Há três formas, dependendo do aparelho:

- **No computador com a extensão Binance Wallet** (Chrome ou Brave). Entre na extensão escaneando o QR code dela com o app da Binance. Depois, na DEX clique em **Connect** ou **Connect Wallet**, escolha Binance Wallet e confirme a janela.
- **No computador sem a extensão.** Na DEX clique em **Connect Wallet → WalletConnect**. Aparece um QR code. Escaneie com o leitor do app da Binance e toque em **Connect**.
- **No celular.** Abra a DEX no navegador do celular, toque em **Connect Wallet**, escolha Binance Wallet na lista e confirme no app.

Antes de confirmar, leia a janela: nome do site, endereço e rede. Se algo parecer errado, toque em Cancel (cancelar).

## Passo 3. Faça o swap e leia cada assinatura

1. Escolha a moeda com que você paga e o token que quer (procure o token pelo **endereço do contrato**, não pelo nome).
2. Digite um valor pequeno e confira a cotação, o slippage (derrapagem — a maior mudança de preço que você aceita) e a taxa de rede.
3. Na primeira vez que vende um token, o site pede **Approve** (permissão para gastar esse token). Se o app permitir, defina um valor em vez de «unlimited» (ilimitado).
4. Confirme o swap no app. Se um pedido de assinatura for uma página de código ilegível ou não fizer sentido, **não assine**.

## Passo 4. Mande moedas de volta para a sua conta Binance

1. No app da Binance, mude para **Exchange** → **Assets** → **Deposit** (exchange → ativos → depositar). Escolha a moeda (por exemplo, BNB).
2. Escolha a **rede** (por exemplo, BNB Smart Chain). Copie o endereço de depósito. Algumas moedas também precisam de **memo/tag** (etiqueta) — copie também.
3. Mude para **Wallet** → **Send** (carteira → enviar). Escolha a mesma moeda e a mesma rede. Cole o endereço (e o memo, se houver).
4. Envie primeiro um valor pequeno de teste. Quando ele chegar na sua conta Binance, envie o resto.

Deixe um pouco de BNB ou SOL na carteira: toda ação na blockchain, mesmo uma que falhe, custa taxa de rede. Algumas memecoins não podem ser depositadas na exchange (ela não as lista) — para sacar, troque-as antes na carteira por BNB, SOL ou USDT.

## Passo 5. Desconecte e faça a limpeza

1. Ao terminar, desconecte o site (nas configurações de sites conectados ou de WalletConnect da carteira, ou no botão **Disconnect** da DEX).
2. De vez em quando, confira as aprovações de tokens e revogue (cancele) as que não precisa. Revogar custa uma pequena taxa.
3. Em computador compartilhado, saia da extensão.

Acompanhe os tokens que comprou na [sua carteira]({lang}/me/) e veja dados ao vivo de memecoins na nossa [página de memecoins]({lang}/memes/).

> **⚠️ Atenção**
> - **Um site ou «suporte» pede sua senha de recuperação, frase-semente ou «sincronizar a carteira».** Nenhuma DEX de verdade nem funcionário da Binance faz isso. Feche a página.
> - **Aprovações ilimitadas e assinatura às cegas.** Uma aprovação ou assinatura maliciosa pode deixar um golpista esvaziar esse token depois, sem nova confirmação sua.
> - **Rede errada, memo esquecido ou um endereço colado que mudou.** Um malware pode trocar um endereço copiado. Compare sempre os primeiros e os últimos caracteres e teste com pouco.

Próxima lição: como checar uma memecoin antes de comprar. Todas as lições na seção [Aprender]({lang}/learn/).

## Fontes

- [Binance: What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy: How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US: How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*Não é recomendação de investimento. Este guia explica como as ferramentas funcionam e não recomenda comprar nenhum token. A Binance Wallet pode não estar disponível em todos os países.*
