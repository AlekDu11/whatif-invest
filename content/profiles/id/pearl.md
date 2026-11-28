---
title: Pearl (PEARL) dijelaskan sederhana: menambang dengan GPU lewat Proof of Useful Work, maks. 2,1 miliar
description: Pearl dijelaskan sederhana: kaitan penambangan GPU dengan komputasi AI, pasokan 2,1 miliar, peluncuran April 2026, kritik, pesaing, dan risiko utama.
date: 2026-11-28
kind: analysis
---
**Pearl** adalah blockchain layer-1 baru yang ditambang dengan kartu grafis Nvidia. Alih-alih teka-teki hash yang tak berguna seperti yang dipecahkan penambang Bitcoin, "bukti kerja berguna" (Proof of Useful Work) milik Pearl meminta penambang melakukan perkalian matriks — matematika yang sama dengan yang menjalankan model AI — sehingga secara teori satu GPU bisa melayani pelanggan AI sekaligus mengamankan jaringan. Pearl dibangun oleh Pearl Research Labs, yang didirikan bersama oleh ilmuwan komputer Omri Weinstein, dan jaringan utamanya diluncurkan pada 27 April 2026. Nilai pasarnya saat ini {{mcap:pearl}} ({{rank:pearl}} di antara kripto).

> **Poin penting**
> - Jumlah koin tidak akan pernah lebih dari 2,1 miliar, 100 kali 21 juta milik Bitcoin; hadiah penambangan turun perlahan, bukan lewat halving.
> - Rekor harganya {{ath:pearl}} ({{athd:pearl}}); harga saat ini {{fromath:pearl}} dari rekor itu.
> - Proyek ini menyatakan tidak ada premine, tidak ada jatah investor, dan tidak ada kas tim: semua koin berasal dari penambangan.
> - Sebuah penelitian Juni 2026 menemukan bahwa penambangan saat itu sama sekali tidak menghasilkan kerja AI yang berguna.

## Cara kerjanya

Penambang menjalankan perkalian matriks "berderau" di GPU, membuat hash dari potongan kecil hasilnya, lalu membungkus kerjanya dalam bukti tanpa pengetahuan (zero-knowledge proof), sehingga siapa pun bisa memeriksanya dengan cepat tanpa mengulanginya. Metode ini berasal dari makalah kriptografi tahun 2025 yang ditulis bersama oleh Weinstein. Penambang resminya tersambung ke vLLM, perangkat lunak populer untuk menjalankan model AI, di kartu pusat data seperti Nvidia H100 dan H200, sementara penambang buatan komunitas juga berjalan di kartu RTX untuk gim. Di balik layar, Pearl mirip Bitcoin: dibangun di atas btcd, program node Bitcoin, dan blok baru muncul setiap beberapa menit. Koin ini sering tercatat dengan ticker PRL, dan di beberapa situs harga ada token lain yang tidak terkait memakai ticker yang sama.

## Kegunaan tokennya

Koin hanya tercipta sebagai hadiah bagi penambang dan dipakai untuk membayar biaya transaksi. Contoh komersial pertama muncul pada Mei 2026: perusahaan cloud AI Together AI menawarkan model Gemma yang berjalan di penambang Pearl dengan harga lebih dari 25% di bawah biasanya, dan diskonnya dibayar dari hadiah PRL. Jika pelanggan AI benar-benar memakai jaringan dengan cara ini, penambangan tidak lagi sekadar menghabiskan energi; jika tidak, Pearl hanyalah koin proof-of-work lain dengan pasokan besar.

## Angka saat ini

- Harga hari ini: {{price:pearl}}
- Rekor tertinggi: {{ath:pearl}} ({{athd:pearl}}), {{fromath:pearl}} dari rekor itu
- Nilai pasar: {{mcap:pearl}} ({{rank:pearl}} di antara mata uang kripto)
- Perubahan harga dalam 12 bulan: {{chg1y:pearl}}

## Kisahnya sejauh ini

Makalah dasarnya terbit pada April 2025, dan jaringan utama aktif pada 27 April 2026 tanpa koin yang dibagikan lebih dulu. Akhir Mei, setelah kesepakatan dengan Together AI, para gamer dan pemilik GPU beramai-ramai menambang, dan dalam beberapa minggu penghasilan harian sebuah RTX 5090 turun kira-kira separuh karena persaingan makin ketat. Awalnya koin ini hanya diperdagangkan di bursa kecil dengan likuiditas tipis seperti MEXC. Pada Juni 2026 sebuah makalah di arXiv, "The Usefulness Gap in Proof-of-Useful-Work", melaporkan bahwa ribuan penambang di jaringan tidak menghasilkan komputasi AI yang berguna dan perangkat lunak penambangan paling populer bahkan tidak berisi kode AI. Pearl menambahkan dukungan untuk model AI jenis mixture-of-experts lewat hard fork pada Juni, dan hingga Oktober 2026 sekitar 16% dari pasokan maksimum sudah ditambang.

## Alternatif

[Bitcoin]({lang}/btc/) adalah koin proof-of-work klasik yang ditambang dengan chip khusus, bukan GPU. Di antara proyek AI dan komputasi, [Bittensor]({lang}/tao/) memberi hadiah kepada yang menjalankan model AI, sedangkan [Render]({lang}/render/), [Akash Network]({lang}/akt/), dan [io.net]({lang}/io/) menyewakan daya GPU secara langsung. Gagasan Pearl berbeda: penambangannya sendiri seharusnya menjadi kerja AI yang berguna.

## Risiko utama

- **Sangat baru:** riwayat harga koin ini baru beberapa bulan, dan koin muda bisa cepat kehilangan sebagian besar nilainya.
- **Kegunaan belum terbukti:** peneliti independen sejauh ini hanya menemukan sedikit kerja AI nyata; klaim utamanya bisa saja tidak terbukti.
- **Ekonomi penambangan:** tingkat kesulitan yang naik dan hadiah yang turun memangkas penghasilan, dan penambang sering menjual koin untuk membayar listrik.
- **Konsentrasi:** pada minggu-minggu pertama menambang masih murah, jadi peserta awal memegang porsi besar.
- **Likuiditas dan nama kembar:** perdagangannya lebih tipis daripada koin besar, dan ada token lain dengan ticker PRL yang sama — periksa kontrak dan bursanya dengan teliti.

## Artinya jika Anda membeli secara rutin

Pearl baru diperdagangkan beberapa bulan, jadi belum ada catatan berarti tentang hasil pembelian rutin. Membeli jumlah tetap secara terjadwal menyebarkan risiko salah waktu, tetapi untuk koin yang benar-benar baru hal itu tidak menghapus risiko kehilangan sebagian besar uang. Banyak orang membatasi koin eksperimental seperti ini pada bagian yang sangat kecil dari tabungan mereka. Hasil masa lalu tidak menjamin hasil di masa depan.

*Bukan nasihat investasi.*

## Sumber

- [What is Pearl blockchain? How it uses GPU mining to price AI compute (KuCoin, October 2026)](https://www.kucoin.com/blog/pearl-blockchain-ai-mining-prl-token)
- [New AI-compute cryptocurrency Pearl sparks a GPU mining rush, but profitability is sliding (Tom's Hardware, 31 May 2026)](https://www.tomshardware.com/tech-industry/cryptomining/new-ai-compute-cryptocurrency-pearl-sparks-a-gpu-mining-rush-but-profitability-is-sliding)
- [Pearl (PRL): the AI-compute cryptocurrency (Hashrate Index, June 2026)](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
- [The Usefulness Gap in Proof-of-Useful-Work (arXiv 2606.04819, June 2026)](https://arxiv.org/abs/2606.04819)
