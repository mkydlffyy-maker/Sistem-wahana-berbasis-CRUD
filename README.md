# 🎡 Sistem Manajemen Tiket Tempat Wisata (CLI + CSV)

Aplikasi berbasis *Command Line Interface* (CLI) menggunakan Python untuk mengelola transaksi tiket tempat wisata, pemesanan wahana, kalkulasi diskon otomatis, dan penyimpanan data permanen berbasis CSV.

---

## 🌟 Fitur Utama

- **Pemesanan Tiket & Wahana:** Mendukung kalkulasi tiket dewasa, tiket anak-anak, serta beragam kategori wahana (Ekstrem & Santai).
- **Sistem Promo & Diskon Otomatis:**
  - 🎂 **Promo Ulang Tahun:** Gratis tiket masuk jika tanggal pembelian sama dengan tanggal lahir.
  - 🎟️ **Diskon Grosir:** Potongan harga Rp20.000 untuk pemesanan lebih dari 10 tiket.
- **Manajemen Data (CRUD):**
  - **Create:** Menambah transaksi baru dengan validasi format tanggal (`YYYY-MM-DD`).
  - **Read:** Menampilkan seluruh riwayat transaksi pengunjung.
  - **Update:** Mengubah nama pengunjung pada transaksi yang tersimpan.
  - **Delete:** Menghapus data transaksi tertentu.
- **Penyimpanan Permanen (CSV):** Otomatis membuat dan memperbarui file `data_wisata.csv`.

---

## 🛠️ Prasyarat & Teknologi

- **Bahasa Pemrograman:** Python 3.x
- **Module bawaan:** `datetime`, `csv`, `os` (tanpa perlu *install library* pihak ketiga)

---

## 🚀 Cara Menjalankan Program

1. **Clone Repositori**
   ```bash
   git clone [https://github.com/mkydlffyy-maker/Sistem-wahana-berbasis-CRUD.git](https://github.com/mkydlffyy-maker/Sistem-wahana-berbasis-CRUD.git)
   cd Sistem-wahana-berbasis-CRUD
