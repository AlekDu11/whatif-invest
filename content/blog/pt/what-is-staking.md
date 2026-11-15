---
title: O que é staking de criptomoedas e se ele é seguro
description: Staking de cripto explicado de forma simples: como funciona, prazos de bloqueio, staking na corretora vs on-chain e os riscos reais antes de fazer staking.
date: 2026-11-16
category: guides
assets: eth, sol, ada, dot, atom
---
**Staking** é travar criptomoedas para ajudar uma blockchain a funcionar e receber moedas novas como recompensa. Muita gente compara com uma poupança, mas o funcionamento é bem diferente e os riscos também.

Este guia explica como o staking funciona, o que significa o "bloqueio", qual a diferença entre fazer staking na corretora e on-chain, e o que pode dar errado.

## Como o staking funciona

Muitas blockchains modernas (Ethereum, Solana, Cardano, Polkadot, Cosmos e outras) usam um sistema chamado **prova de participação** (*proof of stake*). Em vez de gastar energia elétrica para proteger a rede (como a mineração do Bitcoin), elas dependem de **validadores**: computadores que conferem as transações e adicionam novos blocos.

Para virar validador, é preciso colocar moedas em jogo como garantia de bom comportamento. Passo a passo:

1. Você trava (faz staking de) moedas na rede, rodando um validador próprio ou delegando para um.
2. Os validadores confirmam transações e produzem blocos.
3. A rede paga recompensas em moedas novas, mais uma parte das taxas de transação.
4. Se um validador trapaceia ou fica fora do ar de forma grave, parte do valor em staking pode ser cortada. Isso se chama **slashing**.

O Bitcoin em si não pode ser usado em staking dessa forma: ele usa prova de trabalho. Produtos que oferecem "rendimento em Bitcoin" costumam ser empréstimo ou outros esquemas, não staking.

## De onde vêm as recompensas do staking

Recompensa não é dinheiro grátis. Ela vem principalmente de:

- **Moedas novas** criadas pela rede (inflação da oferta),
- **Taxas de transação** pagas pelos usuários.

Isso importa: se uma rede cria moedas novas a, digamos, 5% ao ano e você ganha 5%, na prática você só está mantendo sua fatia da rede, não ficando mais rico. E as recompensas são pagas na própria moeda: se o preço cair, o valor total pode diminuir bastante.

As taxas de recompensa mudam o tempo todo, conforme o número de participantes e as regras da rede. Encare qualquer percentual anunciado como uma foto do momento, não como promessa.

## Bloqueio e desvinculação: quando você recebe as moedas de volta

No staking, suas moedas normalmente não ficam disponíveis na hora. Cada rede tem suas regras:

- **Ethereum**: os saques são possíveis desde a atualização "Shapella" de 2023, mas a saída passa por uma fila que pode levar de dias a semanas quando muita gente sai ao mesmo tempo.
- **Solana**: o fim do staking vale ao final de uma "época" (*epoch*), geralmente uns dois dias.
- **Cosmos e Polkadot**: períodos de "desvinculação" (*unbonding*) de várias semanas, em que as moedas não rendem nada e não podem ser vendidas.
- **Cardano**: as moedas ficam na sua carteira e não são travadas.

Por que isso importa: se o mercado cair durante a desvinculação, você não consegue vender. Confira sempre as regras atuais da moeda antes de fazer staking.

## Staking na corretora vs staking on-chain

Existem duas formas principais de uma pessoa comum fazer staking.

### Staking na corretora (custodiado)

Você aperta "Stake" ou "Earn" no app de uma corretora e ela faz a parte técnica.

- ✅ Muito fácil, aceita valores pequenos, sem configurar carteira.
- ❌ A corretora guarda suas moedas. Se ela quebrar, for hackeada ou congelar saques, suas moedas correm risco.
- ❌ A corretora fica com uma parte das recompensas como taxa.
- ❌ Alguns produtos "earn" na verdade são empréstimo, não staking: um risco bem diferente.

Os reguladores estão de olho nesses serviços. Em 2023, a SEC dos EUA acusou a Kraken por causa do seu programa de staking; a Kraken pagou US$ 30 milhões e encerrou o serviço para clientes americanos. Em 2025, a equipe da SEC afirmou que algumas formas de "staking de protocolo" direto não são operações com valores mobiliários. As regras variam de país para país e continuam mudando.

### Staking on-chain (não custodiado)

Você mantém as moedas na sua própria carteira e delega para um validador, ou roda seu próprio validador.

- ✅ Você controla suas chaves; ninguém pode congelar sua conta.
- ✅ Geralmente taxas menores.
- ❌ Mais técnico: endereço errado, phishing e validadores ruins são problema seu.
- ❌ Rodar seu próprio validador de Ethereum exige 32 ETH e um equipamento confiável.

### Staking líquido

Uma opção intermediária: você faz staking por meio de um protocolo e recebe um token que representa suas moedas em staking (por exemplo, um token de "ETH em staking"). Dá para negociar esse token enquanto as moedas rendem. Em troca, há um **risco de contrato inteligente** extra e a chance de o token ser negociado abaixo do valor das moedas que o lastreiam.

## Os principais riscos do staking

Staking é seguro? É menos arriscado que muitos produtos cripto de "alto rendimento", mas nunca é livre de risco:

1. **Risco de preço.** O maior de todos. Uma recompensa de alguns por cento vale pouco se a moeda cair 50%. Veja como as moedas oscilam na [página do Ethereum]({lang}/eth/) ou na [página da Solana]({lang}/sol/).
2. **Risco de bloqueio.** Talvez você não consiga vender durante uma queda forte.
3. **Risco de plataforma.** Corretoras e plataformas de empréstimo podem quebrar. Quando a Celsius quebrou em 2022, os usuários do programa "earn" perderam o acesso às moedas.
4. **Slashing.** Um validador que se comporta mal pode perder parte do valor em staking, inclusive moedas delegadas em algumas redes.
5. **Risco de contrato inteligente** no staking líquido e em DeFi.
6. **Impostos.** Em muitos países, as recompensas de staking são tributadas como renda quando recebidas. Confira as regras locais.
7. **Golpes.** Sites de staking falsos e ofertas de "20% ao mês garantido" são comuns. Leia nosso guia sobre [como evitar golpes com cripto]({lang}/blog/how-to-avoid-crypto-scams/).

## Checklist antes de fazer staking

- Faça staking só de moedas que você já pretendia manter por muito tempo.
- Confira o prazo de desvinculação e se você pode precisar do dinheiro antes.
- Entenda quem guarda suas moedas: você ou uma plataforma.
- Compare taxas: que parte das recompensas fica com a plataforma?
- Fuja de ofertas com retorno fixo muito alto: recompensas reais de staking variam.
- Comece com pouco e teste um saque.

O staking não muda a pergunta principal: a moeda em si combina com o seu plano de longo prazo? Um plano de aportes regulares, que você pode simular na nossa [calculadora de DCA]({lang}/compare/), depende do preço do ativo ao longo dos anos. Veja como teriam ido US$ 10 por dia em Ethereum durante 5 anos, sem nenhuma recompensa de staking: {{dca:eth:5}} a partir de {{dcainv:5}} investidos ({{dcaroi:eth:5}}).

{{card:eth}}
{{card:sol}}

## Perguntas frequentes

### Staking é a mesma coisa que receber juros?

Não. Os juros vêm de quem pega emprestado; as recompensas do staking vêm da própria rede, por ajudar a protegê-la. Elas são pagas na moeda, então o valor acompanha o preço dela.

### Dá para perder dinheiro com staking?

Sim. O preço da moeda pode cair, uma plataforma pode quebrar e, em casos raros, o slashing pode cortar parte do valor em staking. As recompensas não protegem você de uma queda de preço.

### Dá para fazer staking de Bitcoin?

Não de forma nativa: o Bitcoin usa prova de trabalho. Ofertas de "rendimento em Bitcoin" costumam ser empréstimo ou outros produtos, com riscos diferentes.

### O que é melhor: staking na corretora ou na carteira?

O staking na corretora é mais simples; o staking pela carteira dá a você o controle das chaves. A escolha depende de quanto você se sente à vontade para cuidar de uma carteira. Veja nosso guia de [carteiras quentes e frias]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Fontes

- [ethereum.org — Staking no Ethereum](https://ethereum.org/en/staking/)
- [ethereum.org — Saques do staking](https://ethereum.org/en/staking/withdrawals/)
- [Solana — Staking](https://solana.com/staking)
- [SEC dos EUA — Kraken vai encerrar programa de staking e pagar US$ 30 milhões (2023)](https://www.sec.gov/news/press-release/2023-25)
- [Skadden — SEC: certas atividades de staking de protocolo não são operações com valores mobiliários (2025)](https://www.skadden.com/insights/publications/2025/06/sec-certain-protocol-staking-activities-are-not-securities-transactions)

*Não é recomendação de investimento. Este guia explica como o staking funciona e não recomenda nenhuma moeda, plataforma ou validador.*
