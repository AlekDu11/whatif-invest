---
title: El hackeo de Optimizely coló un script que cambia direcciones cripto en 178 grandes webs
description: Un fallo en la herramienta de Optimizely permitió cambiar direcciones de wallets cripto en CNN, BBC y Zoom el 16 de noviembre. Qué pasó y cómo protegerte.
date: 2026-11-17 10:40
tags: hacks, bitcoin
assets: btc, eth, sol
---
El lunes 16 de noviembre un atacante aprovechó un fallo en Optimizely Web Experimentation, una herramienta de pruebas A/B que usan grandes empresas, para meter JavaScript malicioso en las webs de al menos 178 organizaciones, entre ellas CNN, la BBC, Zoom, HSBC y Ledger, el fabricante de wallets físicas. El script sustituía en silencio las direcciones de wallets cripto por las del atacante.

## Qué pasó

- **Un ataque a la cadena de suministro.** El código se servía desde la propia CDN de Optimizely con un certificado válido, así que las webs se veían normales. La firma Report URI lo encontró en 188 de 1.611 fragmentos revisados y cree que la cifra real es mayor.
- **Direcciones cambiadas por todas partes.** Afectaba a direcciones de bitcoin, ether y otras redes EVM, Tron, Solana, TON, Litecoin, Bitcoin Cash y Dogecoin: en el texto, formularios, enlaces e incluso el portapapeles.
- **También tarjetas e iPhone.** A las 13:43 UTC se añadió un skimmer de tarjetas y un marco oculto intentó cargar exploits para versiones antiguas de iOS. No hay ningún iPhone comprometido confirmado.
- **Botín pequeño por ahora.** Las wallets del atacante recibieron unos $7.040 en unas nueve horas, casi todo en BTC. Optimizely dice que ha eliminado el código y asegurado las cuentas afectadas.

## Qué significa para ti

Si el lunes enviaste cripto copiando una dirección de una web, comprueba que llegó a la wallet correcta. Un buen hábito en cada envío: compara los primeros y últimos caracteres de la dirección y confírmala en la pantalla de tu wallet física. Actualiza el iPhone a iOS 18.7.3 / 26.3 o posterior. Bitcoin cotiza a {{price:btc}}, muy lejos de su récord de $126.080; mira cómo está cada moneda en nuestra [página de distancia al máximo]({lang}/ath/) y elige plataforma con calma con nuestra [comparativa de exchanges]({lang}/exchanges/).

## Fuentes

- [Report URI — World's largest brands infected with malware via Optimizely](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)
- [The Hacker News — Hijacked Optimizely scripts served card skimmer and iOS exploit kits](https://thehackernews.com/2026/11/hijacked-optimizely-scripts-served-card.html)
- [U.Today — Crypto-stealing exploit in JavaScript emerges](https://u.today/major-crypto-stealing-exploit-in-javascript-emerges-zoom-cnn-hsbc-affected)

*No es asesoramiento de inversión. Los artículos de WhatIfStack se preparan con ayuda de herramientas de IA, entre ellas Claude de Anthropic.*
