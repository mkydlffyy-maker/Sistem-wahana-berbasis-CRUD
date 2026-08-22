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