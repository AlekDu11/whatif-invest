---
title: Kaspa (KAS) dijelaskan sederhana: blockDAG proof of work sejak 2021, 10 blok per detik dan batas 28,7 miliar
description: Kaspa secara sederhana: cara kerja blockDAG dan GHOSTDAG, peluncuran adil tanpa premine, upgrade Crescendo dan Toccata, kisahnya, dan risiko utamanya.
date: 2026-11-24
kind: analysis
---
**Kaspa** adalah mata uang kripto proof of work yang ditambang seperti bitcoin, tetapi dirancang jauh lebih cepat: alih-alih satu rantai blok, Kaspa memakai "blockDAG", tempat banyak blok bisa ditambahkan bersamaan. Kaspa diluncurkan pada November 2021 tanpa premine dan tanpa penjualan token, dan nilai koinnya, **KAS**, kini {{mcap:kas}} ({{rank:kas}} di antara mata uang kripto).

> **Poin penting**
> - Jumlah KAS tidak akan pernah lebih dari sekitar 28,7 miliar, dan hingga akhir 2026 sekitar 97% di antaranya sudah ditambang.
> - Rekor tertingginya {{ath:kas}} ({{athd:kas}}); harga hari ini {{fromath:kas}} dari rekor itu.
> - Sejak upgrade Crescendo pada Mei 2025, jaringan menghasilkan 10 blok per detik, bukan lagi satu.
> - Kaspa tidak punya premine, prapenjualan, atau koin yang disisihkan untuk pendirinya — setiap KAS berasal dari penambangan.

## Cara kerjanya

Di bitcoin, jika dua penambang menemukan blok pada saat yang sama, salah satunya dibuang, sehingga blok harus lambat (sekitar setiap 10 menit). Kaspa menyimpan semua blok paralel itu dan menghubungkannya dalam sebuah graf — **blockDAG** (graf asiklik berarah). Protokol **GHOSTDAG**, yang berlandaskan riset akademis Yonatan Sompolinsky dan Aviv Zohar, lalu menyusun semua blok dan transaksi dalam satu urutan yang disepakati. Dengan begitu Kaspa bisa membuat blok sangat sering dan mengonfirmasi pembayaran dalam hitungan detik, sambil tetap memakai penambangan ala bitcoin dengan algoritma kHeavyHash miliknya. Penerbitan koin turun secara halus: hadiah penambang berkurang sedikit setiap bulan dan menjadi separuh kira-kira setahun sekali.

## Kenapa orang menganggapnya bernilai

Para pendukung melihat Kaspa sebagai "perak digital yang cepat": ia mempertahankan hal yang disukai dari bitcoin — proof of work, pasokan tetap, tanpa perusahaan, dan tanpa koin yang dibagikan lebih dulu — tetapi pembayaran selesai dalam hitungan detik, bukan menit. Peluncuran yang adil penting bagi banyak pemegang, karena tidak ada tim atau dana yang mendapat koin murah untuk dijual belakangan. Pada 2026 jaringan juga mulai bisa diprogram: upgrade Toccata membawa covenant (aturan cara koin boleh dibelanjakan), verifikasi bukti zero-knowledge, dan token asli, sehingga pengembang bisa membangun aplikasi di Kaspa.

## Angka saat ini

- Harga hari ini: {{price:kas}}
- Rekor tertinggi: {{ath:kas}} ({{athd:kas}}), {{fromath:kas}} dari rekor itu
- Nilai pasar: {{mcap:kas}} ({{rank:kas}} di antara mata uang kripto)
- Perubahan harga dalam 12 bulan: {{chg1y:kas}}
- $10 per hari selama 3 tahun: {{dca:kas:3}} dari {{dcainv:3}} yang diinvestasikan ({{dcaroi:kas:3}})

## Kisahnya sejauh ini

Kaspa lahir dari riset dan perusahaan DAGlabs; mainnet-nya mulai berjalan pada 7 November 2021. Pada tahun pertama koin ini hanya diperdagangkan di bursa kecil dengan harga pecahan sen. Pada 2023 bursa yang lebih besar mencatatkannya, dan harga naik berlipat-lipat hingga rekor sekitar $0,21 pada pertengahan 2024. Pengembang menulis ulang perangkat lunak node dengan Rust ("Rusty Kaspa"), yang memungkinkan lonjakan kecepatan: pada 5 Mei 2025 hard fork Crescendo menaikkan jaringan dari satu menjadi sepuluh blok per detik. Harga turun tajam sepanjang 2025 dan 2026, dan pada 2026 hard fork Toccata mengubah Kaspa menjadi layer 1 yang bisa diprogram.

## Alternatif

Kaspa paling langsung bersaing dengan koin pembayaran proof of work lain seperti [Bitcoin]({lang}/btc/), [Litecoin]({lang}/ltc/), dan [Bitcoin Cash]({lang}/bch/). Untuk transfer cepat dan murah serta aplikasi, orang juga memakai jaringan proof of stake seperti [Solana]({lang}/sol/), dan untuk pembayaran sehari-hari banyak yang langsung memakai stablecoin dolar.

## Risiko utama

- **Fluktuasi besar:** KAS sudah pernah turun lebih dari 80% dari rekor 2024; penurunan seperti itu bisa terulang.
- **Penambangan terkonsentrasi:** segelintir pool besar dan pembuat ASIC menguasai sebagian besar daya hash.
- **Tim kecil:** pengembangan bergantung pada sekelompok pengembang inti yang sebagian besar didanai donasi komunitas, bukan perusahaan besar.
- **Adopsi:** kecepatan saja tidak menciptakan permintaan; aplikasi Toccata dan pembayaran nyata masih harus berkembang.
- **Akses pasar:** banyak perdagangan terjadi di bursa menengah, dan aturan kripto bisa berubah di tiap negara.

## Artinya jika Anda membeli secara rutin

Kaspa adalah koin muda dengan kenaikan dan penurunan yang sangat tajam. Membeli jumlah tetap secara rutin menyebarkan harga masuk Anda ke bulan baik dan buruk, tetapi tidak melindungi dari penurunan panjang. Sebagian besar KAS sudah ditambang, jadi pergerakan harga ke depan terutama bergantung pada permintaan. Banyak orang hanya menyimpan koin seperti ini sebagai bagian kecil dari kripto mereka. Hasil masa lalu tidak menjamin hasil di masa depan.

*Bukan nasihat investasi.*

## Sumber

- [Kaspa — official website (kaspa.org)](https://kaspa.org/)
- [PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus — Sompolinsky, Wyborski, Zohar (IACR ePrint 2018/104)](https://eprint.iacr.org/2018/104.pdf)
- [Kaspa Covenants++ «Toccata» hard-fork outlook — Michael Sutton, Kaspa core developer (Medium)](https://medium.com/@michaelsuttonil/kaspa-covenants-toccata-hard-fork-outlook-a4d81a40900c)
- [Kaspa price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/kaspa)
