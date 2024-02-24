import os
from datetime import datetime
os.system("cls")

class TiketKonser:
    def __init__(self, konser, tanggal, lokasi, harga, jumlah_tiket):
        self.konser = konser
        self.tanggal = tanggal
        self.lokasi = lokasi
        self.harga = harga
        self.jumlah_tiket = jumlah_tiket

class KonserManager:
    def __init__(self):
        self.daftar_tiket = {"The Eras Tour": TiketKonser("The Eras Tour", "14/05/2024", "Jakarta International Stadium", 1000000, 150)}

    def tambah_tiket(self, tiket):
        self.daftar_tiket[tiket.konser] = tiket
        print(f"\n  <<< Tiket konser {tiket.konser} telah ditambahkan >>>")

    def tampilkan_daftar_tiket(self):
        while True:
            if self.daftar_tiket:
                for konser, tiket in self.daftar_tiket.items():
                    print(f"""
    Nama Konser  : {tiket.konser}
    Tanggal      : {tiket.tanggal}
    Lokasi       : {tiket.lokasi}
    Harga        : Rp {tiket.harga}
    Jumlah Tiket : {tiket.jumlah_tiket}""")
            else:
                print("     Belum ada tiket konser yang terdaftar")
            break

    def ubah_tiket(self, konser, tanggal, lokasi, harga, jumlah_tiket):
        while True :
            if konser in self.daftar_tiket:
                self.daftar_tiket[konser].tanggal = tanggal
                self.daftar_tiket[konser].lokasi = lokasi
                self.daftar_tiket[konser].harga = harga
                self.daftar_tiket[konser].jumlah_tiket = jumlah_tiket
                print(f"    Informasi tiket konser {konser} berhasil diubah.")
            break

    def hapus_tiket(self, konser):
        while True :
            if konser in self.daftar_tiket:
                del self.daftar_tiket[konser]
                print(f"    Tiket konser {konser} berhasil dihapus.")
            break

manager = KonserManager()

def create():
    print("""
    +-----------------------------------+
    |        TAMBAH TIKET KONSER        |
    +------------------------------------""")
    while True:
        konser = input("    Masukkan nama konser: ")
        if konser.strip():
            break
        else:
            print("> INPUT TIDAK BOLEH KOSONG")

    while True:
        tanggal = input("    Masukkan tanggal konser (format: DD/MM/YYYY): ")
        if tanggal.strip():
            try:
                datetime.strptime(tanggal, "%d/%m/%Y")
                break
            except ValueError:
                print("> FORMAT TANGGAL TIDAK VALID")
        else :
            print("> INPUT TIDAK BOLEH KOSONG")

    while True:
        lokasi = input("    Masukkan lokasi konser: ")
        if lokasi.strip():
            break
        else:
            print("> INPUT TIDAK BOLEH KOSONG")

    while True:
        try:
            harga = float(input("    Masukkan harga tiket: Rp "))
            if harga <= 0:
                print("> INPUT HARUS LEBIH DARI 0")
            break
        except ValueError:
            print("> INPUT HARUS BERUPA ANGKA")

    while True:
        try:
            jumlah_tiket = int(input("    Masukkan jumlah tiket yang tersedia: "))
            if jumlah_tiket <= 0:
                print("> INPUT HARUS LEBIH DARI 0")
            else:
                break
        except ValueError:
            print("> INPUT HARUS BERUPA ANGKA")

    tiket_baru = TiketKonser(konser, tanggal, lokasi, harga, jumlah_tiket)
    manager.tambah_tiket(tiket_baru)

def read():
    print("\n   +-------- DAFTAR TIKET KONSER --------+")
    manager.tampilkan_daftar_tiket()

def update():
    print("""
    +-----------------------------------+
    |         UBAH TIKET KONSER         |
    +-----------------------------------+""")
    read()
    while True:
        tanya = input("\n    apakah anda ingin mengubah data (y/t): ").lower()
        if tanya == "y" :
            konser = input("\n    Masukkan nama konser yang ingin diubah informasinya: ")
            if konser.strip():
                break
            else:
                print("> NAMA KONSER TIDAK BOLEH KOSONG")
        elif  tanya == "t" :
            return
        else :
            print("> PILIHAN TIDAK TERSEDIA")

    if konser in manager.daftar_tiket:
        while True:
            tanggal = input("    Masukkan tanggal konser yang baru (format: DD/MM/YYYY): ")
            if tanggal.strip():
                try:
                    datetime.strptime(tanggal, "%d/%m/%Y")
                    break
                except ValueError:
                    print("> FORMAT TANGGAL TIDAK VALID")
            else:
                print("> TANGGAL KONSER TIDAK BOLEH KOSONG")

        while True:
            lokasi = input("    Masukkan lokasi konser yang baru: ")
            if lokasi.strip():
                break
            else:
                print("> LOKASI KONSER TIDAK BOLEH KOSONG")

        while True:
            try:
                harga = float(input("    Masukkan harga tiket yang baru: Rp "))
                break
            except ValueError:
                print("> INPUT HARUS BERUPA ANGKA")

        while True:
            try:
                jumlah_tiket = int(input("    Masukkan jumlah tiket yang tersedia: "))
                break
            except ValueError:
                print("> PERHATIKAN FORMAT INPUT")

        manager.ubah_tiket(konser, tanggal, lokasi, harga, jumlah_tiket)
    else:
        print("> TIKET KONSER TIDAK DITEMUKAN")

def delete():
    print("\n   +-------- HAPUS TIKET KONSER --------+")
    read()
    while True:
        tanya = input("\n    apakah anda ingin menghapus data (y/t): ").lower()
        if tanya == "y":
            konser = input("\n    Masukkan nama konser yang ingin dihapus: ")
            if konser.strip():
                if konser in manager.daftar_tiket:
                    manager.hapus_tiket(konser)
                else:
                    print("> TIKET KONSER TIDAK DITEMUKAN")
            else:
                print("> NAMA KONSER TIDAK BOLEH KOSONG")
        elif tanya == "t":
            return
        else:
            print("> PILIHAN TIDAK TERSEDIA")

def main():
    while True:
        print("""
    =======================================
            PENDATAAN TIKET KONSER        
    =======================================
""")
        print("    [1] Tambah Tiket Konser")
        print("    [2] Tampilkan Daftar Tiket Konser")
        print("    [3] Ubah Informasi Tiket Konser")
        print("    [4] Hapus Tiket Konser")
        print("    [5] Keluar\n")
        pilihan = input("   Masukkan pilihan (1/2/3/4/5): ")
        if pilihan == '1':
            os.system("cls")
            create()
        elif pilihan == '2':
            os.system("cls")
            read()
        elif pilihan == '3':
            os.system("cls")
            update()
        elif pilihan == '4':
            os.system("cls")
            delete()
        elif pilihan == '5':
            os.system("cls")
            print("""
    =======================================
            PROGRAM TELAH SELESAI
        Terima kasih! dan sampai jumpa :)
    =======================================
        """)
            break
        else:
            print("   > Pilihan tidak valid. Silakan pilih kembali")

main()