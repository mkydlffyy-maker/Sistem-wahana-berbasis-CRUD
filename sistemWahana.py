from datetime import datetime
import csv
import os

# SISTEM TEMPAT WISATA + CSV

FILE_CSV = "data_wisata.csv"

# HARGA TIKET
HARGA_DEWASA = 50000
HARGA_ANAK = 30000

# DATA WAHANA
wahana = {
    "Kategori Ekstrem": {
        1: ("Roller Coaster", 40000),
        2: ("Rumah Hantu", 25000),
        3: ("Kora-Kora", 30000),
        4: ("Bianglala", 20000)
    },
    "Kategori Santai": {
        5: ("Kolam Renang", 15000),
        6: ("Taman Air", 20000),
        7: ("Kereta Mini", 10000)
    }
}
# BUAT FILE CSV JIKA BELUM ADA
if not os.path.exists(FILE_CSV):
    with open(FILE_CSV, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Tanggal Pembelian",
            "Nama",
            "Tanggal Lahir",
            "Alamat",
            "Tiket Dewasa",
            "Tiket Anak",
            "Wahana",
            "Potongan",
            "Keterangan",
            "Total Bayar"
        ])

# SIMPAN KE CSV
def simpan_ke_csv(data):
    with open(FILE_CSV, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            data["tanggal_pembelian"],
            data["nama"],
            data["tanggal_lahir"],
            data["alamat"],
            data["tiket_dewasa"],
            data["tiket_anak"],
            ", ".join(data["wahana"]),
            data["potongan"],
            data["keterangan"],
            data["total_bayar"]
        ])

# BACA CSV
def baca_csv():
    data_pengunjung = []
    with open(FILE_CSV, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_pengunjung.append(row)
    return data_pengunjung

# UPDATE CSV
def update_csv(data_pengunjung):
    with open(FILE_CSV, mode="w", newline="") as file:
        fieldnames = [
            "Tanggal Pembelian",
            "Nama",
            "Tanggal Lahir",
            "Alamat",
            "Tiket Dewasa",
            "Tiket Anak",
            "Wahana",
            "Potongan",
            "Keterangan",
            "Total Bayar"
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_pengunjung:
            writer.writerow(data)

# HITUNG TOTAL
def hitung_total(
    tanggal_pembelian,
    tanggal_lahir,
    tiket_dewasa,
    tiket_anak,
    pilihan_wahana
):
    total_tiket = tiket_dewasa + tiket_anak
    tanggal_beli = datetime.strptime(tanggal_pembelian, "%Y-%m-%d")
    tgl_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")

    # CEK ULANG TAHUN
    gratis_ultah = (
        tanggal_beli.month == tgl_lahir.month and
        tanggal_beli.day == tgl_lahir.day
    )

    # TOTAL TIKET
    total_tiket_dewasa = tiket_dewasa * HARGA_DEWASA
    total_tiket_anak = tiket_anak * HARGA_ANAK
    total_tiket_masuk_normal = total_tiket_dewasa + total_tiket_anak

    if gratis_ultah:
        total_tiket_masuk = 0
    else:
        total_tiket_masuk = total_tiket_masuk_normal

    # TOTAL WAHANA
    total_wahana = 0
    daftar_wahana = []

    for kode in pilihan_wahana:
        for kategori in wahana.values():
            if kode in kategori:
                nama, harga = kategori[kode]
                total_wahana += harga
                daftar_wahana.append(nama)

    # TOTAL KESELURUHAN
    total_keseluruhan = total_tiket_masuk_normal + total_wahana

    # DISKON
    potongan = 0
    keterangan = []

    if gratis_ultah:
        keterangan.append("Gratis tiket masuk karena ulang tahun")

    if total_tiket > 10:
        potongan = 20000
        keterangan.append("Potongan Rp20.000 karena beli > 10 tiket")

    if len(keterangan) == 0:
        keterangan.append("Tidak ada potongan")

    # TOTAL SETELAH DISKON
    total_setelah_diskon = total_tiket_masuk + total_wahana - potongan

    return (
        daftar_wahana,
        total_tiket_dewasa,
        total_tiket_anak,
        total_wahana,
        total_keseluruhan,
        potongan,
        " | ".join(keterangan),
        total_setelah_diskon
    )

# TAMBAH DATA
def tambah_data():
    print("\n========== TAMBAH DATA ==========")
    nama = input("Nama : ")

    # INPUT TANGGAL PEMBELIAN
    while True:
        tanggal_pembelian = input("Tanggal Pembelian (YYYY-MM-DD): ")
        try:
            datetime.strptime(tanggal_pembelian, "%Y-%m-%d")
            break
        except ValueError:
            print("Format salah!")

    # INPUT TANGGAL LAHIR
    while True:
        tanggal_lahir = input("Tanggal Lahir (YYYY-MM-DD): ")
        try:
            datetime.strptime(tanggal_lahir, "%Y-%m-%d")
            break
        except ValueError:
            print("Format salah!")

    alamat = input("Alamat : ")
    tiket_dewasa = int(input("Jumlah Tiket Dewasa : "))
    tiket_anak = int(input("Jumlah Tiket Anak : "))

    # TAMPILKAN WAHANA
    print("\n========== WAHANA ==========")
    for kategori, isi in wahana.items():
        print(f"\n{kategori}")
        for kode, data in isi.items():
            print(f"{kode}. {data[0]} - Rp{data[1]}")

    pilihan = input("\nPilih wahana (contoh: 1,3,5): ")
    pilihan_wahana = list(map(int, pilihan.split(",")))

    # HITUNG TOTAL
    (
        daftar_wahana,
        total_tiket_dewasa,
        total_tiket_anak,
        total_wahana,
        total_keseluruhan,
        potongan,
        keterangan,
        total_setelah_diskon
    ) = hitung_total(
        tanggal_pembelian,
        tanggal_lahir,
        tiket_dewasa,
        tiket_anak,
        pilihan_wahana
    )

    # DETAIL PEMBAYARAN
    print("\n========== DETAIL PEMBAYARAN ==========")
    print(f"Total Tiket Dewasa : Rp{total_tiket_dewasa}")
    print(f"Total Tiket Anak : Rp{total_tiket_anak}")
    print(f"Total Biaya Wahana : Rp{total_wahana}")
    print("--------------------------------------")
    print(f"Total Keseluruhan : Rp{total_keseluruhan}")
    print(f"Potongan : Rp{potongan}")
    print("--------------------------------------")
    print(f"Keterangan : {keterangan}")
    print(f"Total Setelah Diskon : Rp{total_setelah_diskon}")

    # DATA
    data = {
        "tanggal_pembelian": tanggal_pembelian,
        "nama": nama,
        "tanggal_lahir": tanggal_lahir,
        "alamat": alamat,
        "tiket_dewasa": tiket_dewasa,
        "tiket_anak": tiket_anak,
        "wahana": daftar_wahana,
        "potongan": potongan,
        "keterangan": keterangan,
        "total_bayar": total_setelah_diskon
    }

    simpan_ke_csv(data)
    print("\nDATA BERHASIL DITAMBAHKAN!")