---
title: Cómo detectar un rug pull: 10 comprobaciones antes de comprar un token nuevo
description: Cómo detectar un rug pull antes de comprar: 10 comprobaciones sobre liquidez bloqueada, autoridad de mint y freeze, top holders, honeypots y volumen falso.
date: 2026-11-16
category: guides
assets: sol, pepe, bonk
---
**¿Cómo se detecta un rug pull?** Un rug pull ("tirón de alfombra") ocurre cuando los responsables de un token se llevan el dinero y dejan a los compradores con algo que nadie quiere. Puede ser repentino (el creador retira la liquidez del pool) o lento (los de dentro venden poco a poco sus enormes posiciones). En ambos casos, el precio se va casi a cero.

Los rug pulls no son raros. En su informe de 2025, la firma de análisis blockchain Solidus Labs clasificó el **98,6%** de los más de 7 millones de tokens lanzados en la plataforma Pump.fun como rug pulls o esquemas de pump-and-dump, y comprobó que solo unos 97.000 mantenían al menos 1.000 dólares de liquidez. Usa la lista de abajo antes de comprar cualquier token nuevo.

## Dos ejemplos recientes

- **HAWK (diciembre de 2024).** Una memecoin promocionada por una celebridad de internet alcanzó un valor de mercado de unos 490 millones de dólares poco después del lanzamiento y luego cayó alrededor de un 91% en menos de tres horas. Analistas on-chain señalaron que un grupo de wallets de insiders y "snipers" tenía el 80–90% del suministro en el lanzamiento; una wallet compró el 17,5% del suministro segundos después del lanzamiento y lo vendió durante la hora y media siguiente. La promotora negó que ella o su equipo vendieran.
- **LIBRA (febrero de 2025).** Un token promocionado en redes sociales por el presidente de Argentina, Javier Milei, se disparó y se desplomó en cuestión de horas. Los insiders retiraron unos 107 millones de dólares, según datos on-chain publicados por The Block, y Milei retiró su apoyo.

Ambos tenían nombres famosos, un volumen enorme y unas redes sociales entusiasmadas. Nada de eso protegió a los compradores.

## Las 10 comprobaciones

### 1. ¿La liquidez está bloqueada o quemada?

Un token cotiza contra un pool de liquidez (por ejemplo token + SOL). Si el creador tiene los tokens LP del pool, puede retirarlo en cualquier momento. Busca liquidez **quemada** o **bloqueada** durante mucho tiempo con un servicio de bloqueo conocido, y revisa la fecha de fin del bloqueo. Un "confía en mí, está bloqueada" en un chat no es una prueba.

### 2. ¿Está revocada la autoridad de mint?

En Solana, la autoridad de mint permite a alguien crear tokens nuevos. Si sigue activa, el creador puede emitir miles de millones de tokens nuevos y venderlos en el pool. Las páginas de tokens en herramientas como GMGN, Solscan o RugCheck muestran si está revocada.

### 3. ¿Está revocada la autoridad de congelación (freeze)?

La autoridad de freeze permite congelar cuentas de tokens. Un creador que la conserva puede impedirte vender mientras él vende. En una memecoin no hay ningún buen motivo para mantenerla.

### 4. ¿Qué concentración tienen los top holders?

Abre la lista de holders. Ignora el pool y las wallets conocidas de exchanges y suma los 10 primeros. Si un puñado de wallets tiene una gran parte del suministro, ellas deciden el precio. Cuidado con muchas wallets "distintas" que se financiaron desde la misma fuente: las herramientas de bubble map muestran estos grupos.

### 5. ¿De verdad puedes vender? (prueba de honeypot)

Un honeypot te deja comprar pero no vender, o cobra un enorme impuesto oculto al vender. Señales de alerta: casi ninguna venta en el historial de operaciones, ventas fallidas o un contrato con reglas de transferencia inusuales (más frecuente en Ethereum y BNB Chain). Las herramientas de simulación pueden probar una venta antes de comprar.

### 6. ¿Las redes sociales son reales?

Revisa la web y las cuentas de X/Telegram. Señales de alerta: una cuenta creada la semana pasada, miles de seguidores pero ninguna conversación real, texto de la web copiado, un "equipo" con fotos de stock, comentarios desactivados o enlaces distintos de los de la página del token.

### 7. ¿El volumen es real?

Una ola repentina de volumen desde wallets nuevas, operaciones de tamaño casi idéntico o las mismas wallets comprándose y vendiéndose entre sí (wash trading) pueden usarse para meter un token en las listas de "tendencias". El interés real suele venir de muchas wallets distintas y con un crecimiento gradual.

### 8. ¿Cómo fue el lanzamiento?

¿Unas pocas wallets compraron una gran parte en los primeros segundos? ¿La wallet del desarrollador vendió poco después del lanzamiento? Muchas herramientas muestran el historial de la wallet "dev", incluidos los tokens que lanzó antes: un creador con un rastro de tokens muertos es una advertencia clara.

### 9. ¿Quién lo promociona y por qué?

Influencers pagados, lanzamientos de famosos y mensajes de "100x garantizado" suelen marcar el techo. Pregúntate: si esta persona lo promociona, ¿cuándo compró y a qué precio?

### 10. ¿El gráfico de precio tiene sentido?

Una vela vertical en un token de pocas horas significa que los primeros compradores acumulan grandes ganancias, y muchos venderán a los siguientes compradores. El miedo a quedarse fuera (FOMO) es justo la sensación que un rug pull está diseñado para crear.

## Una rutina rápida antes de cada compra

1. Copia la dirección del contrato de una fuente fiable.
2. Comprueba el estado del mint, del freeze y de la liquidez.
3. Mira los top holders y los grupos de wallets.
4. Revisa el historial de operaciones en busca de ventas.
5. Decide lo máximo que estás dispuesto a perder y luego divídelo por la mitad.

Si falla cualquier punto, aléjate. Siempre habrá otro token.

## Incluso los tokens "limpios" pueden caer un 90%

Pasar la lista solo reduce el riesgo de un fraude directo. No convierte un token en una buena inversión. Incluso las memecoins más conocidas han caído con fuerza desde sus máximos; puedes ver las caídas actuales en nuestra [página de memecoins]({lang}/memes/) y en el [seguimiento de máximos históricos]({lang}/ath/). CoinGecko consideró muertos a finales de 2025 más de la mitad de los tokens que sigue desde 2021.

## Preguntas frecuentes

### ¿Un rug pull es ilegal?

Depende del país y de los detalles. Muchos rug pulls se tratan como fraude, pero los fondos on-chain rara vez se recuperan, así que prevenir es mucho mejor que esperar justicia.

### ¿Un pool de liquidez bloqueado significa que el token es seguro?

No. Elimina una forma de hacer un rug pull, pero los insiders aún pueden vender de golpe una gran parte del suministro, y el bloqueo puede caducar.

### ¿Puedo recuperar mi dinero después de un rug pull?

Normalmente no. Denúncialo a la policía y a la plataforma, y desconfía de los "servicios de recuperación" que piden una comisión: a menudo son una segunda estafa.

### ¿Qué herramientas ayudan a revisar un token?

Las páginas de tokens de GMGN y de los DEX screeners, exploradores de bloques como Solscan y verificadores como RugCheck muestran la liquidez, las autoridades y los holders. Usa más de una.

## Fuentes

- [El 98% de los tokens de Pump.fun han sido rug pulls o fraudes, según un nuevo informe (CoinDesk)](https://hotfix.coindesk.com/business/2025/05/07/98-of-tokens-on-pump-fun-have-been-rug-pulls-or-an-act-of-fraud-new-report-says)
- [La memecoin Hawk Tuah se desploma un 90% (Cointelegraph)](https://cointelegraph.com/news/hawk-tuah-memecoin-dumps-90-percent-outrage-token-launch-insider)
- [Milei retira su apoyo a LIBRA después de que los insiders retiraran 107 millones de dólares (The Block)](https://www.theblock.co/post/341206/argentinian-president-javier-milei-retracts-libra-endorsement-after-insiders-cash-out-107-million)
- [Monedas muertas: más del 50% de las criptomonedas han fracasado, informe de CoinGecko (Crowdfund Insider)](https://www.crowdfundinsider.com/2026/01/257221-dead-coins-over-50-of-cryptocurrencies-have-failed-report-reveals/)

*No es asesoramiento de inversión. Esta lista reduce el riesgo pero no puede eliminarlo; la mayoría de los tokens nuevos pierden casi todo su valor.*
