---
title: Ataque à Optimizely colocou script que troca endereços cripto em 178 grandes sites
description: Uma falha na ferramenta da Optimizely deixou um hacker trocar endereços de carteiras cripto em sites como CNN, BBC e Zoom em 16 de novembro. Como se proteger.
date: 2026-11-17 10:40
tags: hacks, bitcoin
assets: btc, eth, sol
---
Na segunda-feira, 16 de novembro, um hacker explorou uma falha no Optimizely Web Experimentation, ferramenta de testes A/B usada por grandes empresas, e injetou JavaScript malicioso nos sites de pelo menos 178 organizações, entre elas CNN, BBC, Zoom, HSBC e a fabricante de carteiras físicas Ledger. O script trocava, sem ninguém perceber, endereços de carteiras cripto pelos do atacante.

## O que aconteceu

- **Ataque à cadeia de fornecimento.** O código era servido pela própria CDN da Optimizely, com certificado válido, então os sites pareciam normais. A empresa Report URI o encontrou em 188 de 1.611 trechos analisados e diz que o número real deve ser maior.
- **Troca em todo lugar.** O alvo eram endereços de bitcoin, ether e outras redes EVM, Tron, Solana, TON, Litecoin, Bitcoin Cash e Dogecoin — no texto, formulários, links e até na área de transferência.
- **Cartões e iPhone também.** Às 13:43 UTC entrou um skimmer de cartões, e um quadro oculto tentou carregar exploits para versões antigas do iOS. Nenhum iPhone comprometido foi confirmado.
- **Roubo pequeno até agora.** As carteiras do atacante receberam cerca de $7.040 em umas nove horas, a maior parte em BTC. A Optimizely diz que removeu o código e protegeu as contas afetadas.

## O que isso significa para você

Se você enviou cripto na segunda copiando um endereço de algum site, confira se o valor chegou à carteira certa. Um bom hábito em toda transferência: compare os primeiros e os últimos caracteres do endereço e confirme na tela da sua carteira física. Atualize o iPhone para o iOS 18.7.3 / 26.3 ou mais recente. O bitcoin está em {{price:btc}}, bem longe do recorde de $126.080; veja como está cada moeda na nossa [página de distância da máxima]({lang}/ath/) e escolha a plataforma com cuidado no nosso [comparativo de corretoras]({lang}/exchanges/).

## Fontes

- [Report URI — World's largest brands infected with malware via Optimizely](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)
- [The Hacker News — Hijacked Optimizely scripts served card skimmer and iOS exploit kits](https://thehackernews.com/2026/11/hijacked-optimizely-scripts-served-card.html)
- [U.Today — Crypto-stealing exploit in JavaScript emerges](https://u.today/major-crypto-stealing-exploit-in-javascript-emerges-zoom-cnn-hsbc-affected)

*Não é recomendação de investimento. Os artigos da WhatIfStack são preparados com ajuda de ferramentas de IA, incluindo o Claude, da Anthropic.*
