---
title: "Autenticação de dois fatores (2FA): como ativar, passo a passo"
description: A 2FA coloca uma segunda tranca na sua conta da corretora. Como ativar um app autenticador ou uma passkey passo a passo e por que o SMS é a opção mais fraca.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: US$ 68 mi
stat_label: perdidos com golpes de SIM swap em 2021, em 1.611 queixas ao FBI (IC3, fevereiro de 2022)
---
**O que é 2FA e como ativar?** A autenticação de dois fatores (2FA) significa que, para entrar na conta ou sacar, você precisa de duas coisas: a sua senha *e* uma segunda prova, como um código de 6 dígitos de um app no celular ou uma passkey (chave de acesso: a sua digital ou o seu rosto). Ative nas configurações de **Security** (Segurança) da sua corretora e use um app autenticador ou uma passkey em vez de SMS.

> **Pontos principais**
> - Com 2FA, uma senha roubada sozinha não basta para esvaziar a sua conta.
> - **Códigos por SMS são a opção mais fraca:** no "SIM swap" (troca fraudulenta do chip), um criminoso transfere o seu número de telefone para o chip dele e recebe os seus códigos. O FBI registrou 1.611 queixas desse tipo e mais de **US$ 68 milhões** em perdas em 2021, contra 320 queixas e cerca de US$ 12 milhões em 2018–2020.
> - O FBI recomenda opções mais fortes: um app autenticador, biometria ou uma chave de segurança física.

## As opções, da mais fraca à mais forte

- **Código por SMS** — uma mensagem de texto com um código. Melhor que nada, mas o seu número de telefone pode ser roubado.
- **Código por e-mail** — só é tão seguro quanto a sua conta de e-mail (proteja ela com 2FA também).
- **App autenticador** (Google Authenticator, Microsoft Authenticator e parecidos) — o app no celular gera um novo código de 6 dígitos a cada 30 segundos, mesmo offline. Ninguém consegue interceptar pela operadora.
- **Passkey** (biometria) — você confirma com a digital, o rosto ou o PIN do celular. Ela só funciona no site verdadeiro, então um site falso não consegue roubá-la.
- **Chave de segurança física** (um pequeno dispositivo USB/NFC) — a mais forte, boa para valores altos.

## Passo a passo: app autenticador (usando o app da Binance como exemplo)

Outras corretoras usam quase os mesmos passos; procure **Security** (Segurança) no seu perfil.

1. **Passo 1 — Instale o app.** Baixe o Google Authenticator (ou outro app autenticador) pela App Store ou Google Play oficiais.
2. **Passo 2 — Abra as configurações de segurança.** No app da Binance toque no ícone **Account** (Conta), toque no seu perfil no topo e depois em **Security** (Segurança).
3. **Passo 3 — Comece a configuração.** Toque em **Authenticator App** (App autenticador) e depois em **Enable** (Ativar). Vai aparecer um QR code e uma **chave de configuração** (setup key, um código longo).
4. **Passo 4 — Anote a chave de configuração no papel.** Ela é o seu backup se você perder o celular. Guarde offline, como uma seed phrase. Ainda não toque em **Next** (Próximo).
5. **Passo 5 — Adicione a conta no autenticador.** No Google Authenticator toque em **+**, escolha **Enter a setup key** (Inserir chave de configuração) ou leia o QR code, cole a chave, digite um nome como "Binance" e toque em **Add** (Adicionar).
6. **Passo 6 — Confirme.** De volta à Binance, toque em **Next** (Próximo) e digite o código de 6 dígitos do app. Vai aparecer uma mensagem de sucesso.
7. **Passo 7 — Teste.** Saia da conta e entre de novo. Se pedir o código, está funcionando.

## Passo a passo: passkey (mais simples ainda)

A página de ajuda da Binance diz que você precisa do app na versão 2.60 ou superior, iOS 16+ ou Android 9+.

1. **Account → perfil → Security → Passkeys (Biometrics) → Add Passkey** (Conta → perfil → Segurança → Passkeys (biometria) → Adicionar passkey).
2. Se pedir, confirme com a sua 2FA atual e toque em **Continue** (Continuar).
3. Escolha onde salvar: Chaves do iCloud (iPhone), Gerenciador de Senhas do Google (Android) ou uma chave de segurança, e confirme com a digital, o rosto ou o PIN.

## Depois de ativar a 2FA

- Desative o SMS como forma de login se a corretora permitir ou, pelo menos, peça à sua operadora um bloqueio contra troca de chip e portabilidade sem a sua autorização (PIN de portabilidade).
- Proteja com 2FA também o e-mail ligado à corretora.
- Ative uma **lista de endereços permitidos para saque** (withdrawal whitelist: só endereços salvos podem receber) se a sua corretora tiver.

> **⚠️ Atenção**
> - **Ninguém de verdade pede o seu código 2FA.** "Suporte" no Telegram ou uma ligação "da corretora" ou "do banco" pedindo o código de 6 dígitos é sempre golpe.
> - **Perder o celular sem a chave de backup.** A recuperação aí leva dias de verificação de identidade. Anote a chave de configuração no papel e guarde em local seguro.
> - **Apps autenticadores falsos e páginas de login clonadas.** Instale apps só pela loja oficial e digite você mesmo o endereço da corretora, ou use um favorito.

## O que isso significa se você compra regularmente

Se você compra um pouco todo mês, a sua conta na corretora vai virando aos poucos um valor de verdade — por exemplo, o bitcoin está agora em {{price:btc}} ({{chg1y:btc}} em 12 meses); resultados passados, não uma previsão. Dez minutos configurando a 2FA protegem anos de compras. Acompanhe o que você tem na sua [página de carteira]({lang}/me/).

Aula anterior: [seed phrase: 5 regras para mantê-la segura]({lang}/blog/seed-phrase-safety-rules/). Mais: [como se cadastrar em uma corretora de cripto]({lang}/blog/how-to-register-on-a-crypto-exchange/), [corretoras que funcionam no seu país]({lang}/exchanges/). Todas as lições estão na [página Aprender]({lang}/learn/).

## Fontes

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8 de fevereiro de 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Suporte da Binance: How to enable Google Authenticator for 2FA on the Binance app (atualizado em 10 de dezembro de 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Suporte da Binance: How to create a passkey for my Binance account (atualizado em 10 de dezembro de 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Não é recomendação de investimento.*
