---
title: Pearl (PEARL) explicado: minería con GPU y Proof of Useful Work, tope de 2.100 millones
description: Pearl explicado fácil: cómo su minería con GPU se une a la computación de IA, el tope de 2.100 millones, el lanzamiento de abril de 2026, críticas y riesgos.
date: 2026-11-28
kind: analysis
---
**Pearl** es una blockchain de capa 1 nueva que se mina con tarjetas gráficas de Nvidia. En lugar de los acertijos de hash sin utilidad que resuelven los mineros de Bitcoin, su "prueba de trabajo útil" (Proof of Useful Work) pide multiplicar matrices, las mismas cuentas con las que funcionan los modelos de IA, de modo que en teoría una GPU puede atender a clientes de IA y proteger la red a la vez. La creó Pearl Research Labs, cofundada por el informático Omri Weinstein, y su red principal arrancó el 27 de abril de 2026. Hoy vale {{mcap:pearl}} ({{rank:pearl}} entre las criptomonedas).

> **Claves**
> - Nunca habrá más de 2.100 millones de monedas, 100 veces los 21 millones de Bitcoin; la recompensa de minería baja de forma gradual, sin halvings.
> - Su máximo histórico es {{ath:pearl}} ({{athd:pearl}}); hoy el precio está {{fromath:pearl}} respecto a él.
> - El proyecto afirma que no hubo preminado, ni reparto para inversores, ni tesorería del equipo: todas las monedas salen de la minería.
> - Un estudio de junio de 2026 concluyó que la minería de ese momento no producía ningún trabajo útil de IA.

## Cómo funciona

Los mineros hacen en sus GPU multiplicaciones de matrices "con ruido", calculan el hash de pequeños trozos del resultado y envuelven el trabajo en una prueba de conocimiento cero, para que cualquiera pueda verificarlo rápido sin repetirlo. El método viene de un artículo de criptografía de 2025 firmado, entre otros, por Weinstein. El minero oficial se integra en vLLM, un programa muy usado para servir modelos de IA, en tarjetas de centro de datos como las Nvidia H100 y H200, mientras que mineros creados por la comunidad funcionan también en tarjetas RTX para juegos. Por dentro Pearl se parece a Bitcoin: se basa en btcd, un programa de nodo de Bitcoin, y cada pocos minutos llega un bloque nuevo. La moneda suele aparecer con el ticker PRL, y en algunas webs de precios otro token sin relación usa el mismo ticker.

## Para qué sirve el token

Las monedas solo se crean como recompensa para los mineros y se usan para pagar las comisiones. El primer ejemplo comercial llegó en mayo de 2026: la empresa de nube de IA Together AI ofreció un modelo Gemma que corría sobre mineros de Pearl a un precio más de un 25% inferior al habitual, con el descuento pagado por recompensas en PRL. Si los clientes de IA usan de verdad la red así, la minería deja de ser puro gasto de energía; si no, Pearl es solo otra moneda de prueba de trabajo con una oferta grande.

## Las cifras actuales

- Precio hoy: {{price:pearl}}
- Máximo histórico: {{ath:pearl}} ({{athd:pearl}}), {{fromath:pearl}} desde él
- Valor de mercado: {{mcap:pearl}} ({{rank:pearl}} entre las criptomonedas)
- Variación del precio en 12 meses: {{chg1y:pearl}}

## Su historia

El artículo de base se publicó en abril de 2025 y la red principal se puso en marcha el 27 de abril de 2026 sin monedas repartidas por adelantado. A finales de mayo, tras el acuerdo con Together AI, llegó una fiebre de jugadores y dueños de GPU que se pusieron a minar, y en pocas semanas las ganancias diarias de una RTX 5090 cayeron más o menos a la mitad por la competencia. Al principio la moneda solo cotizaba en exchanges pequeños con poca liquidez, como MEXC. En junio de 2026 un artículo en arXiv, "The Usefulness Gap in Proof-of-Useful-Work", señaló que los miles de mineros de la red no hacían cálculos útiles de IA y que el software de minería más usado ni siquiera tenía código de IA. Pearl añadió soporte para modelos de IA tipo mixture-of-experts en una bifurcación (hard fork) de junio, y en octubre de 2026 ya se había minado cerca del 16% de la oferta máxima.

## Alternativas

[Bitcoin]({lang}/btc/) es la moneda clásica de prueba de trabajo, minada con chips especializados y no con GPU. Entre los proyectos de IA y computación, [Bittensor]({lang}/tao/) premia a quienes ejecutan modelos de IA, mientras que [Render]({lang}/render/), [Akash Network]({lang}/akt/) e [io.net]({lang}/io/) alquilan directamente potencia de GPU. La idea de Pearl es otra: la propia minería debería ser el trabajo útil de IA.

## Principales riesgos

- **Muy nueva:** la moneda tiene solo unos meses de historial de precios, y las monedas jóvenes pueden perder casi todo su valor rápido.
- **Utilidad sin demostrar:** investigadores independientes encontraron poco trabajo real de IA hasta ahora; su principal argumento podría no cumplirse.
- **Economía de la minería:** la dificultad al alza y la recompensa a la baja recortan lo que ganan los mineros, que a menudo venden monedas para pagar la luz.
- **Concentración:** en las primeras semanas minar era barato, así que los primeros participantes tienen una parte grande.
- **Liquidez e imitaciones:** se negocia menos que las grandes monedas y existe otro token con el mismo ticker PRL; revisa bien el contrato y el exchange.

## Qué significa si compras con regularidad

Pearl cotiza desde hace solo unos meses, así que no hay un historial útil de lo que habría dado comprar con regularidad. Comprar una cantidad fija según un calendario reparte el riesgo de elegir mal el momento, pero con una moneda recién nacida no elimina el riesgo de perder gran parte del dinero. Mucha gente limita este tipo de monedas experimentales a una parte muy pequeña de sus ahorros. Los resultados pasados no garantizan rentabilidades futuras.

*No es asesoramiento de inversión.*

## Fuentes

- [What is Pearl blockchain? How it uses GPU mining to price AI compute (KuCoin, October 2026)](https://www.kucoin.com/blog/pearl-blockchain-ai-mining-prl-token)
- [New AI-compute cryptocurrency Pearl sparks a GPU mining rush, but profitability is sliding (Tom's Hardware, 31 May 2026)](https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding)
- [Pearl (PRL): the AI-compute cryptocurrency (Hashrate Index, June 2026)](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
- [The Usefulness Gap in Proof-of-Useful-Work (arXiv 2606.04819, June 2026)](https://arxiv.org/abs/2606.04819)
