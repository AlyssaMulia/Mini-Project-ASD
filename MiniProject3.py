import os
from datetime import datetime
os.system("cls")

class DataTiket:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class TiketKonser:
    def __init__(self, konser, tanggal, lokasi, harga, jumlah_tiket):
        self.konser = konser
        self.tanggal = tanggal
        self.lokasi = lokasi
        self.harga = harga
        self.jumlah_tiket = jumlah_tiket

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def quickSortHarga(self, head):
        if head is None or head.next is None:
            return head
        pivot = head
        smaller_head = None
        equal_head = pivot
        larger_head = None
        current = head.next
        while current is not None:
            next_node = current.next
            if current.data.harga < pivot.data.harga:
                current.next = smaller_head
                smaller_head = current
            elif current.data.harga == pivot.data.harga:
                current.next = equal_head
                equal_head = current
            else:
                current.next = larger_head
                larger_head = current
            current = next_node
        smaller_head = self.quickSortHarga(smaller_head)
        larger_head = self.quickSortHarga(larger_head)
        if smaller_head is not None:
            temp = smaller_head
            while temp.next is not None:
                temp = temp.next
            temp.next = equal_head
        else:
            smaller_head = equal_head
        pivot.next = larger_head if larger_head is not None else None
        return smaller_head

    def sortAscendingHarga(self):
        self.head = self.quickSort(self.head)

    def sortDescendingaHarga(self):
        self.sortAscendingHarga()
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            current.prev = next_node  # Perlu mengubah arah prev
            prev = current
            current = next_node
        self.head = prev

    def quickSortKonser(self, head):
        if head is None or head.next is None:
            return head
        pivot = head
        smaller_head = None
        equal_head = pivot
        larger_head = None
        current = head.next
        while current is not None:
            next_node = current.next
            if current.data.konser < pivot.data.konser:
                current.next = smaller_head
                smaller_head = current
            elif current.data.konser == pivot.data.konser:
                current.next = equal_head
                equal_head = current
            else:
                current.next = larger_head
                larger_head = current
            current = next_node
        smaller_head = self.quickSortKonser(smaller_head)
        larger_head = self.quickSortKonser(larger_head)
        if smaller_head is not None:
            temp = smaller_head
            while temp.next is not None:
                temp = temp.next
            temp.next = equal_head
        else:
            smaller_head = equal_head
        pivot.next = larger_head if larger_head is not None else None
        return smaller_head

    def sortAscendingKonser(self):
        self.head = self.quickSortKonser(self.head)

    def sortDescendingaKonser(self):
        self.sortAscendingKonser()
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            current.prev = next_node  # Perlu mengubah arah prev
            prev = current
            current = next_node
        self.head = prev

    def tambah_tiket(self, tiket):
        while True:
            print("""
    [1] Tambah di awal
    [2] Tambah di antara
    [3] Tambah di akhir
    """)
            pilihan = input("    Pilih lokasi untuk menambah tiket (1/2/3): ")
            if pilihan == "1":
                new_node = DataTiket(tiket)
                new_node.next = self.head
                self.head = new_node
                os.system("cls")
                print(f"\n  <<< Tiket konser {tiket.konser} telah ditambahkan di awal >>>")
                break
            elif pilihan == "2":
                print("\n   Daftar Tiket Konser:")
                self.tampilkan_daftar_tiket()
                posisi = input("\n    Masukkan posisi setelah tiket mana ingin menambah tiket baru: ")
                current = self.head
                while current:
                    if current.data.konser == posisi:
                        new_node = DataTiket(tiket)
                        new_node.next = current.next
                        current.next = new_node
                        os.system("cls")
                        print(f"\n  <<< Tiket konser {tiket.konser} telah ditambahkan di antara >>>")
                        break
                    current = current.next
                else:
                    print("> TIKET TIDAK DITEMUKAN")
                    continue
                break
            elif pilihan == "3":
                if self.head is None:
                    self.head = DataTiket(tiket)
                else:
                    current = self.head
                    while current.next:
                        current = current.next
                    current.next = DataTiket(tiket)
                    os.system("cls")
                print(f"\n  <<< Tiket konser {tiket.konser} telah ditambahkan di akhir >>>")
                break
            else:
                print("> PILIHAN TIDAK VALID")

    def tampilkan_daftar_tiket(self):
        current = self.head
        if not current:
            print("     Belum ada tiket konser yang terdaftar")
            return
        while current:
            tiket = current.data
            print(f"""
    Nama Konser  : {tiket.konser}
    Tanggal      : {tiket.tanggal}
    Lokasi       : {tiket.lokasi}
    Harga        : Rp {tiket.harga}
    Jumlah Tiket : {tiket.jumlah_tiket}""")
            current = current.next

    def ubah_tiket(self, konser, tanggal, lokasi, harga, jumlah_tiket):
        current = self.head
        while current:
            if current.data.konser == konser:
                current.data.tanggal = tanggal
                current.data.lokasi = lokasi
                current.data.harga = harga
                current.data.jumlah_tiket = jumlah_tiket
                print(f"    <<< Informasi tiket konser {konser} berhasil diubah >>>")
                return
            current = current.next
        print("> TIKET KONSER TIDAK DITEMUKAN")

    def hapus_tiket(self):
        if self.head is None:
            print("     Belum ada tiket konser yang terdaftar")
            return
        print("""
    [1] Hapus di awal
    [2] Hapus di antara
    [3] Hapus di akhir
        """)
        pilihan = input("     Pilih lokasi untuk menghapus tiket (1/2/3): ")
        
        if pilihan == "1":
            konser = self.head.data.konser
            self.head = self.head.next
            print(f"    <<< Tiket konser {konser} berhasil dihapus di awal >>>")
            return

        if pilihan == "3":
            current = self.head
            prev_node = None
            while current.next:
                prev_node = current
                current = current.next
            konser = current.data.konser
            if prev_node:
                prev_node.next = None
            else:
                self.head = None
            print(f"    <<< Tiket konser {konser} berhasil dihapus di akhir >>>")
            return
        
        if pilihan == "2":
            print("\n   Daftar Tiket Konser:")
            self.tampilkan_daftar_tiket()
            konser = input("\n    Masukkan nama konser yang ingin dihapus: ")
            if self.head.data.konser == konser:
                self.head = self.head.next
                print(f"    <<< Tiket konser {konser} berhasil dihapus >>>")
                return
            current = self.head
            while current.next:
                if current.next.data.konser == konser:
                    current.next = current.next.next
                    print(f"    <<< Tiket konser {konser} berhasil dihapus >>>")
                    return
                current = current.next
            print(f"    <<< Tiket konser {konser} tidak ditemukan >>>")

manager = SingleLinkedList()

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

def delete():
    print("""
    +-----------------------------------+
    |        HAPUS TIKET KONSER         |
    +-----------------------------------+""")   
    read()
    manager.hapus_tiket()

def sorting():
    print("""
    +-----------------------------------+
    |       URUTKAN TIKET KONSER        |
    +-----------------------------------+""")  
    print("  [1] Urutkan berdasarkan harga termurah")
    print("  [2] Urutkan berdasarkan harga termahal")
    print("  [3] Urutkan berdasarkan nama konser A-Z")
    print("  [4] Urutkan berdasarkan nama konser Z-A")

    pilih = input("  Masukkan pilihan (1/2/3/4): ")

    if pilih == "1":
        manager.sortAscendingHarga()
        print("  > Daftar tiket konser berhasil diurutkan berdasarkan harga termurah")
    elif pilih == "2":
        manager.sortDescendingaHarga()
        print("  > Daftar tiket konser berhasil diurutkan berdasarkan harga termahal")
    elif pilih == "3":
        manager.sortAscendingKonser()
        print("  > Daftar tiket konser berhasil diurutkan berdasarkan nama konser A-Z")
    elif pilih == "4":
        manager.sortDescendingaKonser()
        print("  > Daftar tiket konser berhasil diurutkan berdasarkan nama konser Z-A")
    else:
        print("  > Pilihan tidak valid. Silakan pilih kembali.")
    return
    
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
    print("    [5] Urutkan Tiket Konser")
    print("    [6] Keluar\n")
    pilihan = input("    Masukkan pilihan (1/2/3/4/5/6): ")
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
        sorting()  
    elif pilihan == '6':
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