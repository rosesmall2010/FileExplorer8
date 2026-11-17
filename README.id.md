<p align="center">
  <img src="images/icon-1024.png" width="128" alt="FileExplorer8">
</p>

<h1 align="center">FileExplorer8</h1>

<p align="center"><strong>Pengelola berkas asli macOS · Pengelola berkas / dua panel / empat panel dalam satu jendela</strong></p>

<p align="center">Satu inti operasi berkas, tiga model interaksi · Uji coba sebelum menulis · Urungkan tiga tingkat · Tetap lancar pada puluhan ribu entri</p>

<p align="center">
  <a href="https://rosesmall2010.github.io/FileExplorer8/"><img src="https://img.shields.io/badge/Dukungan-blue" alt="Site"></a>
  <a href="https://rosesmall2010.github.io/FileExplorer8/privacy.id.html"><img src="https://img.shields.io/badge/Privasi-green" alt="Privacy"></a>
  <img src="https://img.shields.io/badge/version-1.1.6-lightgrey" alt="Version">
</p>

<p align="center"><a href="README.md" hreflang="zh-Hans" lang="zh-Hans">简体中文</a> · <a href="README.zh-Hant.md" hreflang="zh-Hant" lang="zh-Hant">繁體中文</a> · <a href="README.en.md" hreflang="en" lang="en">English</a> · <a href="README.ja.md" hreflang="ja" lang="ja">日本語</a> · <a href="README.ko.md" hreflang="ko" lang="ko">한국어</a> · <a href="README.de.md" hreflang="de" lang="de">Deutsch</a> · <a href="README.fr.md" hreflang="fr" lang="fr">Français</a> · <a href="README.es.md" hreflang="es" lang="es">Español</a> · <a href="README.pt-BR.md" hreflang="pt-BR" lang="pt-BR">Português (Brasil)</a> · <a href="README.ru.md" hreflang="ru" lang="ru">Русский</a> · <a href="README.vi.md" hreflang="vi" lang="vi">Tiếng Việt</a> · <strong>Bahasa Indonesia</strong> · <a href="README.ms.md" hreflang="ms" lang="ms">Bahasa Melayu</a> · <a href="README.th.md" hreflang="th" lang="th">ไทย</a></p>

---

## Apa ini

FileExplorer8 adalah **pengelola berkas** yang berjalan asli di macOS. Ia menggabungkan tiga model interaksi — pengelola berkas, dua panel, dan empat panel — ke dalam satu jendela, bergilir dengan `⇧⌘D`. Tiap mode menyimpan statusnya sendiri: jalur, tab, pengurutan, lebar kolom, pilihan. Bolak-balik tidak ada yang hilang.

Ini bukan pengganti Finder, dan bukan pula kulit lain untuk Finder. Ia mengisi kekosongan Finder: **pemindahan massal dengan kedua tangan di papan tuts**.

Acuannya adalah pengelola berkas dua panel klasik: tidak menetapkan aplikasi pembuka bawaan, tidak membuat ekstensi Finder, tidak membaca atau menulis preferensi Finder. Satu-satunya yang dipakai bersama adalah sistem berkasnya sendiri. Karena itu ia bisa hidup berdampingan dengan Finder tanpa saling mengganggu.

---

## Tangkapan layar

### Pengelola berkas: tampilan kisi dengan panel detail

![Pengelola berkas: tampilan kisi dengan panel detail](images/readme/01-explorer.png)

### Dua panel: sumber dan tujuan

![Dua panel: sumber dan tujuan](images/readme/02-dual-pane.png)

### Empat panel: tata letak 2×2

![Empat panel: tata letak 2×2](images/readme/03-quad-pane.png)

---

## Fitur

### Uji coba sebelum setiap penulisan

Sebelum menyalin, memindahkan, atau menimpa, aplikasi menjalankan uji coba: apakah tujuan bisa ditulisi, cukup ruang, nama mana yang bentrok — semuanya ditampilkan lebih dulu. **Langkah ini tidak menulis satu bita pun.**

Empat strategi bentrok: ganti (cadangkan dulu, bisa diurungkan), pertahankan keduanya, lewati, tanya satu per satu. Dengan lima bentrok atau kurang, Anda bisa memutuskan satu per satu.

Kemajuan menampilkan kecepatan nyata, terkirim / total / sisa, dan berakhir dengan rekap lengkap: berapa berhasil, dilewati, gagal — tiap kegagalan disebutkan namanya beserta alasannya.

### Urungkan tiga tingkat

Pemindahan dalam volume sama, penggantian nama, hapus ke Tempat Sampah, serta pemadatan dan ekstraksi ZIP **dijamin 100% dapat diurungkan**. Menyalin dan memindahkan antarvolume dilakukan sebaik mungkin. Yang tidak dapat diurungkan meminta konfirmasi sebelum berjalan.

### Enam tampilan dan pratinjau sungguhan

Ikon sangat besar / besar / sedang / kecil, daftar, dan detail. Ikon dipilih pada ukuran piksel sebenarnya (256 / 128 / 64 / 32) sehingga tetap tajam di layar Retina.

Tekan `Spasi` untuk pratinjau, lalu `←` / `→` atau `PgUp` / `PgDn` untuk berpindah:

- Teks dan kode sumber tampil dalam mode baca-saja berhuruf monospace, dengan penyorotan sintaks lebih dari 50 bahasa dan nomor baris
- PDF tampil melalui PDFKit
- Gambar diperkecil atau diperbesar agar pas di panel dengan rasio tetap
- Format kaya diserahkan ke Pratinjau Cepat sistem
- Yang tidak bisa ditampilkan mendapat kartu informasi

### Pemadatan dan ekstraksi

**Buat ZIP**: ZIP64, tingkat pemadatan dapat diatur, format yang sudah padat dilewati otomatis, pilihan mengikuti tautan simbolik, dan hasilnya dapat diurungkan.

**Klik ganda untuk mengekstrak**, sama seperti Finder: satu folder tingkat atas tunggal tidak dibuat bersarang, saat bentrok seluruh arsip diganti nama, hanya `__MACOSX` yang dibersihkan, dan bit izin Unix dipulihkan.

### Folder SSH jarak jauh

SSH / SFTP bawaan: hubungkan dengan sandi atau kunci privat di jalur mana pun, lalu jelajahi, salin, hapus, ganti nama, dan urungkan di sisi jarak jauh persis seperti lokal — lewat saluran penulisan yang sama.

Bilah tab menandai koneksi dengan ikon disk jaringan dan status merah atau hijau, serta menyambung ulang dengan satu klik setelah terputus. **Sandi boleh tidak disimpan**, diganti kotak masuk sekali pakai per koneksi. Berkas jarak jauh hingga 10 MB tampil seketika.

### Detail

- Tujuh tag warna Finder, bisa ditumpuk; saat semua dilepas, tag teks buatan sendiri tetap dipertahankan
- Palet perintah `⌘K`, diurutkan menurut kecocokan → terakhir dipakai → abjad
- Trio jalur: salin jalur, salin jalur folder induk, salin nama berkas, plus “Buka di Terminal”
- Checksum: SHA-256 / SHA-512 / SHA-1 / MD5 / BLAKE3 / CRC32 / CRC64
- Volume ditemukan otomatis: flashdisk, disk eksternal, image disk yang terpasang; keluarkan dengan satu klik
- Pemulihan sesi: posisi jendela, tab, lebar kolom, pengurutan, dan rasio dua panel diingat; penulisan yang mengantre dilanjutkan setelah aplikasi sempat berhenti mendadak
- Salin-tempel dua arah dengan Finder, seret-lepas berjalan di ketiga arah
- Pergantian bahasa ada di menu Bahasa tingkat satu — satu langkah, langsung berlaku

### 14 bahasa

Tionghoa sederhana, Tionghoa tradisional, Inggris, Jepang, Korea, Jerman, Prancis, Spanyol, Portugis Brasil, Rusia, Vietnam, Indonesia, Melayu, Thai.

Thai mendapat aturan pengurutan sendiri — vokal di depan, tanda nada, dan urutan aksara semuanya bukan urutan titik kode, jadi mengurutkan menurut titik kode akan kacau.

---

## Privasi

**Tidak ada data yang dikumpulkan.** Tanpa akun, tanpa analitik, tanpa SDK iklan, tanpa laporan kerusakan.

Selain koneksi SSH yang Anda mulai sendiri, aplikasi tidak mengirim satu bita pun ke server mana pun. Berkas, riwayat, dan kredensial server Anda tetap di Mac Anda: sandi dan frasa sandi di Keychain sistem, berkas kunci privat di tempat Anda meletakkannya.

Aplikasi berjalan di App Sandbox dan hanya membaca atau menulis di folder yang Anda berikan. Ia tidak meminta kontak, kamera, mikrofon, perekaman layar, atau akses seluruh disk.

[Baca kebijakan privasi selengkapnya](https://rosesmall2010.github.io/FileExplorer8/privacy.id.html)

---

## Dukungan

Terjebak, punya ide, atau menemukan bug?

- Lihat [halaman dukungan](https://rosesmall2010.github.io/FileExplorer8/) untuk pertanyaan umum
- Atau buka [issue](https://github.com/rosesmall2010/FileExplorer8/issues) dengan versi macOS, versi FileExplorer8, dan langkah mereproduksi

Nomor versi ada di “FileExplorer8 › Tentang FileExplorer8”.

### Pertanyaan umum

**Mengapa muncul permintaan izin saat membuka beberapa folder?**
Aplikasi berjalan di App Sandbox. Desktop, Unduhan, Dokumen, dan disk eksternal berada di luar sandbox, jadi macOS meminta izin saat pertama kali masuk ke folder tersebut. Itu rancangan keamanan sistem, bukan cacat. Pilih “Izinkan akses ke folder ini” dan folder akan diingat — satu jalur hanya ditanyai sekali per sesi jalan.

**Apakah aplikasi membaca kontak, kamera, atau layar saya?**
Tidak. FileExplorer8 hanya meminta akses berkas yang Anda pilih, folder standar (Unduhan / Dokumen / Musik / Gambar / Film), dan akses jaringan keluar. Tidak ada akses kontak, kamera, mikrofon, perekaman layar, atau seluruh disk.

**Di mana sandi SSH disimpan?**
Di Keychain macOS. Titik koneksi server disimpan di kontainer sandbox lokal, dienkripsi dengan AES-256-GCM. Anda juga bisa tidak menyimpan sandi dan menerima kotak masuk sekali pakai pada setiap koneksi. Lihat <a href="https://rosesmall2010.github.io/FileExplorer8/privacy.id.html">kebijakan privasi</a>.

**Apakah mendukung Apple Silicon dan Intel?**
Keduanya. Pemasangnya adalah biner universal. Diperlukan macOS 15.0 atau lebih baru.

**Bagaimana membersihkan sisa data setelah menghapus aplikasi?**
Hapus aplikasi, lalu hapus <code>~/Library/Containers/com.donghuazhu.FileExplorer8/</code> untuk membersihkan preferensi, status sesi, dan titik koneksi server (aplikasi dalam sandbox menyimpan data di kontainer ini, bukan di lokasi bersama sistem). Sandi SSH ada di Keychain dan terhapus bersama koneksinya.

---

## Persyaratan sistem

- macOS 15.0 atau lebih baru
- Apple Silicon atau Intel (biner universal)

---

<p align="center"><sub>macOS adalah merek dagang Apple Inc. Aplikasi ini tidak berafiliasi dengan Apple Inc.</sub></p>
