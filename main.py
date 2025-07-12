from datetime import datetime
from collections import defaultdict

transaksi = [
    {"tanggal": "2025-06-25", "jenis": "pemasukan", "jumlah": 3000000, "kategori": "gaji", "keterangan": "Gaji bulan Juli"},
    {"tanggal": "2025-06-28", "jenis": "pengeluaran", "jumlah": 50000, "kategori": "makan", "keterangan": "Makan malam"},
    {"tanggal": "2025-07-03", "jenis": "pengeluaran", "jumlah": 50000, "kategori": "makan", "keterangan": "Sarapan"},
    {"tanggal": "2025-07-05", "jenis": "pengeluaran", "jumlah": 100000, "kategori": "transportasi", "keterangan": "Bensin"},
]

def lihat_transaksi_pemasukan(data_transaksi):
    print("=== Daftar Transaksi Pemasukan ===")
    found = False
    for transaksi in data_transaksi:
        if transaksi["jenis"] == "pemasukan":
            found = True
            print(f"ID: {transaksi['id']}")
            print(f"Tanggal: {transaksi['tanggal']}")
            print(f"Kategori: {transaksi['kategori']}")
            print(f"Jumlah: Rp{transaksi['jumlah']}")
            print("-" * 30)
    if not found:
        print("lihat_transaksi_pemasukan(transaksi)")

def lihat_kategori_pengeluaran():
    print("\n📊 Total Pengeluaran per Kategori:")

    kategori_total = {}

    for t in transaksi:
        if t["jenis"] == "pengeluaran":
            kategori = t["kategori"]
            jumlah = t["jumlah"]
            if kategori in kategori_total:
                kategori_total[kategori] += jumlah
            else:
                kategori_total[kategori] = jumlah

    if kategori_total:
        print("{:<20} {:>15}".format("Kategori", "Total Pengeluaran (Rp)"))
        print("-" * 40)
        for kategori, total in kategori_total.items():
            print("{:<20} {:>15,}".format(kategori.capitalize(), total))
    else:
        print("Belum ada data pengeluaran.")

# lihat_kategori_pengeluaran()
def laporan_bulanan():
    laporan = defaultdict(lambda: {"pemasukan": 0, "pengeluaran": 0})

    for t in transaksi:
        # Ambil bulan dari tanggal (format YYYY-MM)
        bulan = datetime.strptime(t["tanggal"], "%Y-%m-%d").strftime("%Y-%m")
        if t["jenis"] == "pemasukan":
            laporan[bulan]["pemasukan"] += t["jumlah"]
        elif t["jenis"] == "pengeluaran":
            laporan[bulan]["pengeluaran"] += t["jumlah"]

    # Cetak laporan
    print("\n📅 Laporan Keuangan Bulanan")
    print("{:<10} {:>15} {:>15} {:>15}".format("Bulan", "Pemasukan", "Pengeluaran", "Saldo"))
    print("-" * 60)
    for bulan in sorted(laporan):
        pemasukan = laporan[bulan]["pemasukan"]
        pengeluaran = laporan[bulan]["pengeluaran"]
        saldo = pemasukan - pengeluaran
        print("{:<10} {:>15,} {:>15,} {:>15,}".format(bulan, pemasukan, pengeluaran, saldo))


# Data transaksi disimpan sebagai list of dictionary
def tampilkan_transaksi(filter_jenis=None):
    print("\n📋 Daftar Transaksi:")
    print("{:<5} {:<12} {:<12} {:<15} {:<20} {}".format(
        "No", "Tanggal", "Jenis", "Kategori", "Jumlah (Rp)", "Keterangan"))
    print("-" * 80)

    count = 0
    for i, t in enumerate(transaksi, 1):
        if filter_jenis is None or t["jenis"] == filter_jenis:
            count += 1
            print("{:<5} {:<12} {:<12} {:<15} {:<20} {}".format(
                count,
                t["tanggal"],
                t["jenis"],
                t["kategori"],
                f"{t['jumlah']:,}",
                t["keterangan"]
            ))
    
    if count == 0:
        print("Belum ada transaksi yang sesuai.")

def menu_lihat_transaksi():
    while True:
        print("\n=== MENU LIHAT TRANSAKSI ===")
        print("1. Lihat semua transaksi")
        print("2. Lihat hanya pemasukan")
        print("3. Lihat hanya pengeluaran")
        print("4. Lihat Laporan Bulanan")
        print("5. Kembali")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_transaksi()
        elif pilihan == "2":
            tampilkan_transaksi("pemasukan")
        elif pilihan == "3":
            tampilkan_transaksi("pengeluaran")
        elif pilihan == "4":
            laporan_bulanan()
        elif pilihan == '5':
            print("Kembali ke menu utama...")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Jalankan menu
menu_lihat_transaksi()