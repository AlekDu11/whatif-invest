---
title: O que é uma DEX e qual a diferença para uma corretora de criptomoedas?
description: O que é uma DEX? Guia simples sobre exchanges descentralizadas: AMMs, pools de liquidez, carteiras, taxas de gás e vantagens e desvantagens frente a uma CEX.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**O que é uma DEX?** Uma DEX (exchange descentralizada) é um conjunto de contratos inteligentes em uma blockchain que permite trocar um token por outro diretamente da sua própria carteira. Não há empresa guardando seu dinheiro, não há conta e normalmente não há verificação de identidade. Uniswap na Ethereum, e Raydium, Orca e Meteora na Solana, são exemplos conhecidos.

Uma corretora de cripto comum como Binance, Coinbase ou Kraken é uma **CEX** (exchange centralizada): uma empresa que guarda seus fundos, cruza compradores e vendedores no próprio sistema e precisa seguir regras financeiras.

## Como funciona uma DEX

### Formadores de mercado automatizados (AMMs)

A maioria das DEXs não tem um livro de ofertas com compradores e vendedores. Em vez disso, usam um **formador de mercado automatizado** (AMM): uma fórmula que define o preço.

A versão clássica, usada pela Uniswap v2, é a regra do "produto constante": um pool tem dois tokens, e a quantidade do token A multiplicada pela quantidade do token B precisa continuar igual depois de cada operação. Quando você compra o token A, coloca token B no pool e tira token A, então A fica mais escasso no pool e o preço dele sobe.

Você não precisa fazer as contas. A ideia principal: **quanto maior o pool, menos a sua operação mexe no preço.**

### Pools de liquidez

Os tokens do pool vêm dos **provedores de liquidez**: pessoas que depositam pares de tokens e ganham uma parte das taxas de negociação (muitas vezes 0,05–1% por swap). O risco delas é os preços dos dois tokens se afastarem, o que pode deixá-las em situação pior do que se simplesmente tivessem guardado os tokens ("perda impermanente").

Em tokens recém-lançados, normalmente é o criador quem monta o primeiro pool. Por isso o bloqueio de liquidez importa: quem controla o pool pode retirá-lo.

### Sua carteira é a sua conta

Para usar uma DEX, você conecta uma carteira de autocustódia como MetaMask (Ethereum e redes parecidas) ou Phantom (Solana). Cada operação é uma transação que você mesmo assina. Sua **frase-semente** é a chave mestra: perdeu, o dinheiro some; compartilhou, outra pessoa leva o dinheiro.

### Gás e taxas

Toda operação em uma DEX paga uma taxa de rede, chamada de **gás** na Ethereum. Na Ethereum ela sobe quando a rede está congestionada; redes de camada 2 e a Solana costumam ser bem mais baratas: a taxa básica da Solana é de 0,000005 SOL por assinatura. Além do gás, você paga a taxa do pool e pode enfrentar **slippage** e **impacto no preço** em tokens pequenos ou que se movem rápido.

## DEX vs CEX: as principais diferenças

- **Quem guarda seus fundos:** na DEX, você (sua carteira); na CEX, a exchange.
- **Conta e verificação de identidade:** a DEX normalmente não exige nada; a CEX exige verificação de identidade (KYC).
- **Variedade de tokens:** a DEX oferece quase qualquer token, inclusive os recém-criados; a CEX só lista tokens selecionados.
- **Comprar com cartão ou banco:** normalmente não dá direto na DEX; é o padrão na CEX.
- **Taxas:** DEX, gás, taxa do pool e slippage; CEX, taxa de negociação, spread e taxa de saque.
- **Ajuda se algo der errado:** a DEX não tem central de atendimento; a CEX tem suporte ao cliente e às vezes mecanismos de proteção.
- **Principais riscos:** DEX, tokens golpe, aprovações perigosas e seus próprios erros; CEX, ataques hacker, bloqueio de conta e insolvência.

## Vantagens de uma DEX

- **Autocustódia.** Ninguém pode congelar sua conta nem perder seu dinheiro em uma falência.
- **Acesso aberto.** Qualquer pessoa com uma carteira pode negociar, de quase qualquer lugar.
- **Tokens novos primeiro.** Os tokens aparecem nas DEXs muito antes de qualquer listagem em exchange (ou no lugar dela).
- **Transparência.** Pools, operações e holders ficam visíveis na blockchain.

## Desvantagens de uma DEX

- **Você é o banco.** Um erro (endereço errado, site falso, aprovação maliciosa) e os fundos se perdem para sempre.
- **Tokens golpe.** Qualquer um cria um token e um pool em minutos. A maioria dos tokens novos perde quase todo o valor; veja o nosso [checklist para identificar um rug pull]({lang}/blog/how-to-spot-a-rug-pull/).
- **Custos escondidos.** Slippage e impacto no preço podem custar mais do que a taxa visível.
- **Sem porta de entrada fácil.** Normalmente você precisa comprar cripto em uma CEX primeiro e enviar para a sua carteira.
- **Risco de contrato inteligente.** Bugs ou ataques no código de DEXs já causaram grandes perdas.

## Qual um iniciante deve usar?

Muita gente usa as duas: uma CEX regulamentada para converter moeda local em cripto e uma DEX para tokens que só existem on-chain. Para compras recorrentes e de longo prazo de ativos grandes como Bitcoin ou Ethereum, uma CEX com taxas baixas costuma ser mais simples; compare opções na nossa [página de exchanges]({lang}/exchanges/).

Se quiser explorar memecoins e outros tokens on-chain, comece com valores bem pequenos, uma carteira separada e as moedas mais consolidadas da nossa [página de memecoins]({lang}/memes/). O nosso passo a passo [como comprar uma memecoin na Solana]({lang}/blog/how-to-buy-memecoins-on-solana/) mostra o processo completo, incluindo ferramentas como a [GMGN](/go/gmgn?from=blog&l=pt).

## Termos comuns de DEX

- **Swap**: trocar um token por outro.
- **Par**: os dois tokens de um pool, como SOL/USDC.
- **Tolerância de slippage**: a variação máxima de preço que você aceita.
- **Approve**: permissão para um contrato movimentar um token da sua carteira (principalmente em redes do tipo Ethereum). Revogue aprovações antigas que você não usa mais.
- **Agregador**: um serviço que divide sua operação entre várias DEXs para conseguir um preço melhor, como Jupiter na Solana ou 1inch na Ethereum.

## Perguntas frequentes

### Uma DEX é mais segura que uma CEX?

Elimina o risco de a exchange perder ou congelar seus fundos, mas acrescenta o risco dos seus próprios erros e dos tokens golpe. Nenhuma das duas é livre de risco.

### Preciso de documento para usar uma DEX?

Normalmente não, porque você negocia a partir da sua própria carteira. As leis e os impostos do seu país continuam valendo para você.

### Por que minha operação na DEX falhou?

Motivos comuns: falta de moeda nativa para o gás, slippage baixo demais para um preço que muda rápido ou um token que bloqueia vendas.

### Operações em DEX pagam imposto?

Em muitos países, sim: trocar um token por outro pode contar como venda. Guarde o registro das suas operações.

## Fontes

- [Como a Uniswap funciona (documentação da Uniswap)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gás e taxas (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Documentação da Solana: estrutura de taxas](https://solana.com/docs/core/fees/fee-structure)

*Não é recomendação de investimento. Este guia explica como as DEXs funcionam e não recomenda nenhuma plataforma nem token.*
