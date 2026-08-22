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