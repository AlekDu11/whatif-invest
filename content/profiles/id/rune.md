---
title: THORChain (RUNE) dijelaskan sederhana: tukar bitcoin asli dan koin lain antar-blockchain, tanpa wrapped token
description: THORChain dengan bahasa sederhana: swap lintas chain dan pool likuiditas RUNE, bond node, peretasan 2021, pembekuan pinjaman 2025, risiko dan pembelian rutin.
date: 2026-11-26
kind: analysis
---
**THORChain (RUNE)** adalah blockchain yang memungkinkan orang menukar koin antarjaringan yang berbeda — misalnya bitcoin asli dengan ether asli — tanpa bursa terpusat dan tanpa salinan koin yang "dibungkus" (wrapped). RUNE adalah token di pusatnya: setiap pool perdagangan dipasangkan dengan RUNE, dan komputer yang menjalankan jaringan wajib mengunci RUNE sebagai deposit jaminan. Seluruh RUNE yang beredar kini bernilai {{mcap:rune}} ({{rank:rune}} di antara mata uang kripto).

> **Poin penting**
> - THORChain menukar aset asli antar-chain seperti Bitcoin, Ethereum, BNB Chain, Dogecoin, dan lainnya dalam satu langkah.
> - Setiap pool likuiditas dipasangkan dengan RUNE, dan operator node mengunci RUNE sebagai bond yang bisa disita jika mereka berbuat curang.
> - Rekor tertingginya {{ath:rune}} ({{athd:rune}}); kini harganya {{fromath:rune}} dari rekor itu.
> - Jaringan ini diretas dua kali pada 2021 dan membekukan produk pinjaman serta tabungannya pada Januari 2025.

## Cara kerjanya

THORChain dibangun dengan Cosmos SDK. Sekelompok node independen bersama-sama mengendalikan "vault" — alamat di Bitcoin, Ethereum, dan chain lain yang terhubung — memakai tanda tangan ambang (threshold signature), sehingga tidak ada satu node pun yang bisa memindahkan dana sendirian. Saat Anda menukar BTC dengan ETH, Anda mengirim bitcoin ke vault; jaringan menjualnya menjadi RUNE di pool BTC, lalu menjual RUNE itu menjadi ETH di pool ETH, dan sebuah vault mengirimi Anda ether asli. Harga ditentukan oleh saldo pool, seperti di [Uniswap]({lang}/uni/). Penyedia likuiditas menyetor koin ke pool dan mendapat bagian dari biaya swap. Node harus mengunci RUNE yang nilainya lebih besar daripada dana yang mereka jaga, agar pencurian tidak menguntungkan.

## Kenapa orang menganggapnya bernilai

Memindahkan nilai antar-blockchain biasanya lambat, berisiko, atau memerlukan bursa terpusat dengan verifikasi akun. THORChain menawarkan jalur langsung antar-koin asli, sebab itu banyak dompet kripto dan aplikasi swap mengarahkan transaksi lewat THORChain. Permintaan RUNE datang dari tiga sumber: RUNE adalah separuh dari setiap pool, menjadi bond yang wajib disetor node, dan sebagian biaya swap mengalir ke pemegang yang melakukan staking. Volume perdagangan yang lebih tinggi berarti lebih banyak biaya untuk pemegang RUNE.

## Angka saat ini

- Harga hari ini: {{price:rune}}
- Rekor tertinggi: {{ath:rune}} ({{athd:rune}}), {{fromath:rune}} dari rekor itu
- Nilai pasar: {{mcap:rune}} ({{rank:rune}} di antara mata uang kripto)
- Perubahan harga dalam 12 bulan: {{chg1y:rune}}
- $10 per hari selama 5 tahun: {{dca:rune:5}} dari {{dcainv:5}} yang diinvestasikan ({{dcaroi:rune:5}})

## Kisahnya sejauh ini

RUNE pertama kali dijual lewat Binance Launchpad pada Juli 2019. "Chaosnet" dengan uang sungguhan, yang sengaja dibatasi, aktif pada 2020, disusul perdagangan multi-chain pada April 2021. Dalam lonjakan 2021, RUNE mencapai sekitar $20 pada Mei 2021, tetapi pada Juli 2021 jaringan ini terkena dua eksploit senilai jutaan dolar. Mainnet penuh dinyatakan pada Juni 2022. Pada Januari 2025, THORChain menghentikan produk pinjaman dan "savers" setelah kewajibannya menumpuk sekitar $200 juta; utang itu kemudian dikonversi menjadi token terpisah bernama TCY. Pada Februari 2025, peretas di balik pencurian $1,4 miliar dari bursa Bybit memakai THORChain untuk menukar ether curian menjadi bitcoin, yang membawa volume rekor sekaligus kritik tajam.

## Alternatif

Bursa terpusat tetap menjadi cara termudah untuk bertukar antar-chain. Pesaing on-chain mencakup layanan bridge dan agregator serta Maya Protocol, fork dari THORChain. Untuk swap di dalam satu jaringan, orang memakai bursa terdesentralisasi seperti [Uniswap]({lang}/uni/) atau [PancakeSwap]({lang}/cake/). Untuk menghubungkan blockchain secara umum, [Cosmos]({lang}/atom/) dan [Chainlink]({lang}/link/) menawarkan pendekatan lain.

## Risiko utama

- **Naik-turun tajam:** RUNE sudah lebih dari sekali jatuh lebih dari 80% dari puncaknya.
- **Peretasan:** vault lintas chain menyimpan dana besar dan pernah diserang; bug baru bisa membuat pengguna rugi.
- **Produk gagal:** pembekuan pinjaman 2025 menunjukkan fitur baru bisa menimbulkan kerugian bagi pengguna dan tekanan pada RUNE.
- **Regulasi:** penggunaan oleh peretas untuk mencuci dana menarik perhatian regulator dan bisa berujung pada pembatasan.
- **Ketergantungan pada RUNE:** karena setiap pool dipasangkan dengan RUNE, penurunan tajam RUNE memukul seluruh sistem.

## Artinya jika Anda membeli secara rutin

RUNE adalah taruhan bahwa orang akan terus memakai THORChain untuk swap lintas chain, dan sejarahnya mencakup peretasan dan produk yang dibekukan selain reli yang cepat. Membeli jumlah tetap secara rutin meratakan harga masuk Anda, tetapi tidak melindungi Anda dari guncangan khusus proyek ini. Banyak orang membatasi token khusus seperti RUNE pada sebagian kecil tabungan mereka. Hasil masa lalu tidak menjamin hasil di masa depan.

*Bukan nasihat investasi.*

## Sumber

- [Dokumentasi THORChain — pengantar (docs.thorchain.org)](https://docs.thorchain.org/)
- [RUNE naik 15% saat THORChain memulai lagi sebagian besar swap setelah gangguan (Cointelegraph)](https://cointelegraph.com/markets/rune-rallies-15-as-thorchain-restarts-most-swaps-after-outage)
- [Harga THORChain, kapitalisasi pasar dan rekor tertinggi (CoinGecko)](https://www.coingecko.com/en/coins/thorchain)
