---
title: The Graph (GRT) dijelaskan sederhana: protokol pengindeksan data blockchain, aktif sejak 2020, di Ethereum dan Arbitrum
description: The Graph dengan bahasa sederhana: cara indexer mengubah data blockchain jadi kueri cepat, fungsi GRT, staking dan delegasi, sejarah, pesaing dan risiko utama.
date: 2026-11-25
kind: analysis
---
**The Graph** sering disebut "Google-nya blockchain": protokol ini merapikan data mentah blockchain agar aplikasi bisa menemukan yang dibutuhkan dalam hitungan milidetik. Dompet, bursa, dan aplikasi DeFi memakainya untuk menampilkan saldo, transaksi, dan harga tanpa harus menjalankan server data sendiri. Tokennya, **GRT**, dipakai untuk membayar pekerjaan itu sekaligus mengamankan jaringan, dan saat ini bernilai {{mcap:grt}} ({{rank:grt}} di antara mata uang kripto).

> **Poin penting**
> - Jaringan ini aktif pada Desember 2020 dengan 10 miliar GRT; token baru diterbitkan setiap tahun sebagai imbalan, sehingga tidak ada batas pasokan tetap.
> - Rekor tertingginya {{ath:grt}} ({{athd:grt}}); harga hari ini {{fromath:grt}} dari rekor itu.
> - GRT adalah token kerja: indexer wajib melakukan staking GRT untuk melayani data, dan aplikasi membayar biaya kueri dengannya.
> - GRT adalah taruhan pada permintaan data blockchain, bukan mata uang — penggunaan dan harganya sering bergerak ke arah berbeda.

## Cara kerjanya

Membaca data langsung dari blockchain itu lambat dan merepotkan. Pengembang di The Graph menjelaskan data yang mereka butuhkan dalam "subgraph" terbuka, misalnya setiap transaksi di sebuah bursa terdesentralisasi. **Indexer** — operator independen yang menjalankan server — memproses subgraph tersebut dan menjawab kueri dari aplikasi, lalu mendapat biaya serta GRT yang baru diterbitkan. **Curator** memberi sinyal subgraph mana yang layak diindeks, dan **delegator** meminjamkan GRT mereka kepada indexer yang mereka percayai dengan imbalan sebagian hadiah. Indexer yang menyajikan data salah bisa kehilangan sebagian stake-nya ("slashing"). Kini The Graph mendukung puluhan blockchain, dan sejak 2024 hadiah serta pembayarannya berjalan di Arbitrum, layer 2 Ethereum, agar biayanya tetap rendah. Pada 2025 proyek ini mulai meluncurkan **Horizon**, pembaruan yang memungkinkan sistem staking yang sama mengamankan jenis layanan data baru.

## Kegunaan tokennya

GRT punya tiga fungsi. Indexer wajib melakukan staking sebelum bisa bekerja, sehingga sebagian besar pasokan terkunci. Aplikasi membayar kueri dengan GRT (sering dikonversi otomatis dari stablecoin atau pembayaran kartu). Pemegang juga bisa mendelegasikannya untuk mendapat sebagian hadiah tanpa menjalankan server. Sebagian kecil biaya kueri dan pajak staking dibakar, sementara penerbitan baru sekitar 3% per tahun diberikan kepada indexer dan delegator. Naik tidaknya nilai GRT bergantung pada apakah permintaan berbayar atas data tumbuh lebih cepat daripada pasokan baru.

## Angka saat ini

- Harga hari ini: {{price:grt}}
- Rekor tertinggi: {{ath:grt}} ({{athd:grt}}), {{fromath:grt}} dari rekor itu
- Nilai pasar: {{mcap:grt}} ({{rank:grt}} di antara mata uang kripto)
- Perubahan harga dalam 12 bulan: {{chg1y:grt}}
- $10 per hari selama 5 tahun: {{dca:grt:5}} dari {{dcainv:5}} yang diinvestasikan ({{dcaroi:grt:5}})

## Kisahnya sejauh ini

The Graph dimulai pada 2018 oleh Yaniv Tal, Brandon Ramirez, dan Jannis Pohlmann, yang perusahaannya kemudian menjadi Edge & Node. Selama bertahun-tahun proyek ini menjalankan "hosted service" gratis yang diandalkan banyak aplikasi Ethereum. Jaringan terdesentralisasi dan token GRT aktif pada 17 Desember 2020, dan di tengah booming kripto GRT naik hingga sekitar $2,84 pada Februari 2021. Setelah itu harganya anjlok lebih dari 90% sepanjang 2021 dan 2022. Pada 2023 dan 2024 proyek ini memindahkan hadiahnya ke Arbitrum dan menutup hosted service pada Juni 2024, sehingga semua pengguna beralih ke jaringan berbayar. Reli token AI pada awal 2024 sempat mengangkat GRT, tetapi kemudian harganya jatuh ke titik terendah baru.

## Alternatif

The Graph bersaing dengan perusahaan dan protokol pengindeksan seperti Goldsky, SubQuery, dan Covalent, serta dengan API data blockchain dari Alchemy dan QuickNode, yang menurut banyak pengembang lebih sederhana. Beberapa aplikasi besar memilih menjalankan indexer sendiri. Di antara token yang terkait data blockchain, [Chainlink]({lang}/link/) dan [Pyth Network]({lang}/pyth/) sering dibandingkan dengan GRT, meskipun keduanya mengirim data harga ke smart contract, bukan menyediakan pencarian atas data masa lalu.

## Risiko utama

- **Pasokan baru:** penerbitan tahunan menambah GRT baru, dan indexer sering menjual hadiahnya untuk menutup biaya server.
- **Kaitan lemah dengan penggunaan:** biaya kueri sejak lama kecil dibandingkan hadiahnya, sehingga penggunaan yang tinggi tidak otomatis mengangkat harga.
- **Persaingan:** penyedia data terpusat cepat dan murah, dan aplikasi bisa dengan mudah beralih ke mereka.
- **Ketergantungan pada satu perusahaan:** Edge & Node dan The Graph Foundation masih mengarahkan sebagian besar pengembangan.
- **Regulasi:** aturan untuk token staking dan imbalannya berbeda di tiap negara dan bisa berubah.

## Artinya jika Anda membeli secara rutin

Sepanjang sebagian besar usianya, GRT berada jauh di bawah puncaknya pada 2021, jadi pembeli rutin terus mendapat lebih banyak token di harga yang lebih rendah — hal ini baru menguntungkan jika harganya pulih. Membeli jumlah tetap secara rutin menyebarkan risiko salah waktu, tetapi tidak menghilangkan risiko rugi. Banyak orang hanya menyimpan token seperti ini sebagai bagian kecil dari tabungan. Hasil masa lalu tidak menjamin hasil di masa depan.

*Bukan nasihat investasi.*

## Sumber

- [Tentang The Graph (dokumentasi The Graph)](https://thegraph.com/docs/en/about/)
- [Panduan implementasi Horizon: apa yang berubah bagi peserta jaringan (blog The Graph)](https://thegraph.com/blog/horizon-implementation-guide/)
- [Harga, kapitalisasi pasar, dan rekor tertinggi The Graph (CoinGecko)](https://www.coingecko.com/en/coins/the-graph)
