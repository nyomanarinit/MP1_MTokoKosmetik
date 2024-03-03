import os  # Import modul os untuk berinteraksi dengan sistem operasi (menghapus layar konsol).
import re  # Import modul re untuk bekerja dengan ekspresi reguler (regex).
from prettytable import PrettyTable  # Import modul PrettyTable untuk membuat tabel yang rapi dan cantik.

# Membersihkan layar konsol
os.system("cls")

# Kelas Node untuk membuat simpul dalam linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Kelas LinkedList untuk mengelola linked list dari produk
class LinkedList:
    def __init__(self):
        self.head = None

    # Menampilkan linked list dalam format sederhana
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Menampilkan linked list menggunakan PrettyTable untuk tampilan yang lebih terorganisir
    def display_pretty_table(self):
        table = PrettyTable()
        table.field_names = ["Kode", "Nama", "Harga", "Stok", "Kategori"]

        current = self.head
        while current:
            table.add_row([current.data.kode, current.data.nama, current.data.harga, current.data.stok, current.data.kategori])
            current = current.next

        print(table)

    # Menambahkan simpul di awal linked list
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Menambahkan simpul di akhir linked list
    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Menambahkan simpul setelah simpul tertentu dalam linked list
    def add_after_node(self, after_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data.kode == after_data:
                new_node.next = current.next
                current.next = new_node
                print(f"Produk setelah kode {after_data} berhasil ditambahkan.")
                return
            current = current.next

    # Menghapus simpul di awal linked list
    def delete_at_beginning(self):
        if not self.head:
            print("Daftar kosong. Tidak ada yang dapat dihapus.")
            return
        self.head = self.head.next

    # Menghapus simpul di akhir linked list
    def delete_at_end(self):
        if not self.head:
            print("Daftar kosong. Tidak ada yang dapat dihapus.")
            return
        current = self.head
        if not current.next:
            self.head = None
            return
        while current.next.next:
            current = current.next
        current.next = None

    # Menghapus simpul setelah simpul tertentu dalam linked list
    def delete_after_node(self, after_data):
        current = self.head
        while current:
            if current.data.kode == after_data and current.next:
                current.next = current.next.next
                print(f"Produk setelah kode {after_data} berhasil dihapus.")
                return
            current = current.next
        print(f"Produk dengan kode {after_data} tidak ditemukan atau merupakan simpul terakhir.")

# Kelas Produk yang mewakili produk dengan atribut seperti kode, nama, harga, stok, dan kategori
class Produk:
    def __init__(self, kode, nama, harga, stok, kategori):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori

# Kelas TokoKosmetik yang mengelola produk dan memberikan operasi pada mereka
class TokoKosmetik:
    def __init__(self):
        self.produk_list = LinkedList()

    # Menambahkan produk di awal daftar
    def tambah_produk_di_awal(self, produk):
        if self.is_kode_unique(produk.kode):
            self.produk_list.add_at_beginning(produk)
        else:
            print("Kode barang sudah ada. Gunakan kode barang yang unik.")

    # Menambahkan produk di akhir daftar
    def tambah_produk_di_akhir(self, produk):
        if self.is_kode_unique(produk.kode):
            self.produk_list.add_at_end(produk)
        else:
            print("Kode barang sudah ada. Gunakan kode barang yang unik.")

    # Menambahkan produk setelah simpul tertentu dalam daftar
    def tambah_produk_di_antara_node(self, after_data, produk):
        if self.is_kode_unique(produk.kode):
            self.produk_list.add_after_node(after_data, produk)
        else:
            print("Kode barang sudah ada. Gunakan kode barang yang unik.")

    # Memeriksa apakah suatu kode unik dalam daftar produk
    def is_kode_unique(self, kode):
        current = self.produk_list.head
        while current:
            if current.data.kode == kode:
                return False  # Kode tidak unik
            current = current.next
        return True  # Kode unik

    # Memeriksa apakah suatu kode ada dalam daftar produk
    def is_kode_exists(self, kode):
        current = self.produk_list.head
        while current:
            if current.data.kode == kode:
                return True
            current = current.next
        return False

    # Memperbarui produk dengan informasi baru
    def update_produk(self, kode, nama_baru=None, harga_baru=None, stok_baru=None, kategori_baru=None):
        current = self.produk_list.head
        while current:
            if current.data.kode == kode:
                if nama_baru is not None:
                    current.data.nama = nama_baru
                if harga_baru is not None:
                    current.data.harga = harga_baru
                if stok_baru is not None:
                    current.data.stok = stok_baru
                if kategori_baru is not None:
                    current.data.kategori = kategori_baru
                print("Produk berhasil diupdate.")
                return
            current = current.next
        print("Produk dengan kode", kode, "tidak ditemukan.")

    # Menghapus produk di awal daftar
    def hapus_produk_di_awal(self):
        self.produk_list.delete_at_beginning()
        print("Produk di awal berhasil dihapus.")

    # Menghapus produk di akhir daftar
    def hapus_produk_di_akhir(self):
        self.produk_list.delete_at_end()
        print("Produk di akhir berhasil dihapus.")

    # Menghapus produk setelah simpul tertentu dalam daftar
    def hapus_produk_di_antara_node(self, after_data):
        self.produk_list.delete_after_node(after_data)

# Menambahkan daftar produk awal ke toko_kosmetik
def tambah_list_barang_awal(toko_kosmetik):
    produk1 = Produk("P001", "Foundation", 150000, 100, "Makeup")
    produk2 = Produk("P002", "Lipstick", 80000, 150, "Makeup")
    produk3 = Produk("P003", "Shampoo", 50000, 200, "Hair Care")

    toko_kosmetik.tambah_produk_di_akhir(produk1)
    toko_kosmetik.tambah_produk_di_akhir(produk2)
    toko_kosmetik.tambah_produk_di_akhir(produk3)

# Fungsi utama program
def main():
    toko_kosmetik = TokoKosmetik()
    tambah_list_barang_awal(toko_kosmetik)

    while True:
        print("\nHallo, Selamat Datang..... ")
        print("====TOKO KOSMETIK ARINI'S====")
        print("+----+----------------------+")
        print("| No | Pilihan Menu         |")
        print("+----+----------------------+")
        print("| 1  | Tambah Produk        |")
        print("| 2  | Lihat Daftar Produk  |")
        print("| 3  | Update Produk        |")
        print("| 4  | Hapus Produk         |")
        print("| 0  | Keluar               |")
        print("+----+----------------------+")

        try:
            pilihan = int(input("Masukkan pilihan Anda: "))
            os.system("cls")
        except ValueError:
            print("Masukkan pilihan yang valid (angka).")
            continue

        if pilihan == 1:
            while True:
                toko_kosmetik.produk_list.display_pretty_table()
                print("\nHallo, Selamat Datang.....        ")
                print("========TOKO KOSMETIK ARINI'S========")
                print("+----+------------------------------+")
                print("| No | Menu Tambah Produk           |")
                print("+----+------------------------------+")
                print("| 1  | Tambah Produk di Awal        |")
                print("| 2  | Tambah Produk di Akhir       |")
                print("| 3  | Tambah Produk di Antara Node |")
                print("| 0  | Kembali Menu Utama           |")
                print("+----+------------------------------+")
                try:
                    tambah_produk = int(input("Masukkan pilihan Anda: "))
                    os.system("cls")
                except ValueError:
                    print("Masukkan pilihan yang valid (angka).")
                    continue

                if tambah_produk == 1:
                    try:
                        while True:
                            kode = input("Masukkan kode produk: ").strip()
                            if not kode:
                                print("Kode barang tidak boleh kosong. Silakan masukkan kembali.")
                                continue
                            elif not re.match("^[a-zA-Z0-9]+$", kode):
                                print("Kode barang hanya boleh berupa huruf dan angka. Silakan masukkan kembali.")
                                continue
                            elif not toko_kosmetik.is_kode_unique(kode):
                                print("Kode barang sudah ada. Gunakan kode barang yang unik.")
                                continue
                            else:
                                break

                        while True:
                            nama = input("Masukkan nama produk: ").strip()
                            if not nama:
                                print("Nama barang tidak boleh kosong. Silakan masukkan kembali.")
                                continue
                            elif not re.match("^[a-zA-Z]+$", nama):
                                print("Nama barang hanya boleh berupa huruf. Silakan masukkan kembali.")
                                continue
                            else:
                                break

                        while True:
                            try:
                                harga = float(input("Masukkan harga produk: "))
                                break
                            except ValueError:
                                print("Harga harus berupa angka. Silakan masukkan kembali.")

                        while True:
                            try:
                                stok = int(input("Masukkan stok produk: "))
                                break
                            except ValueError:
                                print("Stok harus berupa angka. Silakan masukkan kembali.")
                        
                        while True:
                                kategori = input("Masukkan kategori produk: ").strip()
                                if not kategori:
                                    print("Kategori barang tidak boleh kosong. Silakan masukkan kembali.")
                                    continue
                                elif not re.match("^[a-zA-Z]+$", kategori):
                                    print("Kategori barang hanya boleh berupa huruf. Silakan masukkan kembali.")
                                    continue
                                else:
                                    break

                        produk_baru = Produk(kode, nama, harga, stok, kategori)
                        toko_kosmetik.tambah_produk_di_awal(produk_baru)

                    except ValueError:
                        print("Inputan harus valid dan tidak boleh kosong.")
                    else:
                        print("Produk berhasil ditambahkan di awal daftar.")
                
                elif tambah_produk == 2:
                    try:
                        while True:
                            kode = input("Masukkan kode produk: ").strip()
                            if not kode:
                                print("Kode barang tidak boleh kosong. Silakan masukkan kembali.")
                                continue
                            elif not re.match("^[a-zA-Z0-9]+$", kode):
                                print("Kode barang hanya boleh berupa huruf dan angka. Silakan masukkan kembali.")
                                continue
                            elif not toko_kosmetik.is_kode_unique(kode):
                                print("Kode barang sudah ada. Gunakan kode barang yang unik.")
                                continue
                            else:
                                break

                        while True:
                            nama = input("Masukkan nama produk: ").strip()
                            if not nama:
                                print("Nama barang tidak boleh kosong. Silakan masukkan kembali.")
                                continue
                            elif not re.match("^[a-zA-Z]+$", nama):
                                print("Nama barang hanya boleh berupa huruf. Silakan masukkan kembali.")
                                continue
                            else:
                                break

                        while True:
                            try:
                                harga = float(input("Masukkan harga produk: "))
                                break
                            except ValueError:
                                print("Harga harus berupa angka. Silakan masukkan kembali.")

                        while True:
                            try:
                                stok = int(input("Masukkan stok produk: "))
                                break
                            except ValueError:
                                print("Stok harus berupa angka. Silakan masukkan kembali.")

                        while True:
                            kategori = input("Masukkan kategori produk: ").strip()
                            if not kategori:
                                print("Kategori barang tidak boleh kosong. Silakan masukkan kembali.")
                                continue
                            elif not re.match("^[a-zA-Z]+$", kategori):
                                print("Kategori barang hanya boleh berupa huruf. Silakan masukkan kembali.")
                                continue
                            else:
                                break

                        produk_baru = Produk(kode, nama, harga, stok, kategori)
                        toko_kosmetik.tambah_produk_di_akhir(produk_baru)

                    except ValueError:
                        print("Inputan harus valid dan tidak boleh kosong.")
                        continue
                    else:
                        print("Produk berhasil ditambahkan di akhir daftar.")


                elif tambah_produk == 3:
                    try:
                        after_data = input("Masukkan kode produk setelahnya: ").strip()
                        if not after_data:
                            print("Kode barang tidak boleh kosong. Silakan masukkan kembali.")
                            continue
                        elif not re.match("^[a-zA-Z0-9]+$", after_data):
                            print("Kode barang hanya boleh berupa huruf dan angka. Silakan masukkan kembali.")
                            continue
                        elif not toko_kosmetik.is_kode_exists(after_data):
                            print("Produk dengan kode", after_data, "tidak ditemukan.")
                            continue

                        while True:
                            kode = input("Masukkan kode produk: ").strip()
                            if not kode:
                                print("Kode barang tidak boleh kosong. Silakan masukkan kembali.")
                                continue
                            elif not re.match("^[a-zA-Z0-9]+$", kode):
                                print("Kode barang hanya boleh berupa huruf dan angka. Silakan masukkan kembali.")
                                continue
                            elif not toko_kosmetik.is_kode_unique(kode):
                                print("Kode barang sudah ada. Gunakan kode barang yang unik.")
                                continue
                            else:
                                break

                        while True:
                            nama = input("Masukkan nama produk: ").strip()
                            if not nama:
                                print("Nama barang tidak boleh kosong. Silakan masukkan kembali.")
                                continue
                            elif not re.match("^[a-zA-Z]+$", nama):
                                print("Nama barang hanya boleh berupa huruf. Silakan masukkan kembali.")
                                continue
                            else:
                                break

                        while True:
                            try:
                                harga = float(input("Masukkan harga produk: "))
                                break
                            except ValueError:
                                print("Harga harus berupa angka. Silakan masukkan kembali.")

                        while True:
                            try:
                                stok = int(input("Masukkan stok produk: "))
                                break
                            except ValueError:
                                print("Stok harus berupa angka. Silakan masukkan kembali.")

                        while True:
                            kategori = input("Masukkan kategori produk: ").strip()
                            if not kategori:
                                print("Kategori barang tidak boleh kosong. Silakan masukkan kembali.")
                                continue
                            elif not re.match("^[a-zA-Z]+$", kategori):
                                print("Kategori barang hanya boleh berupa huruf. Silakan masukkan kembali.")
                                continue
                            else:
                                break

                        produk_baru = Produk(kode, nama, harga, stok, kategori)
                        toko_kosmetik.tambah_produk_di_antara_node(after_data, produk_baru)

                    except ValueError:
                        print("Inputan harus valid dan tidak boleh kosong.")
                        continue
                    else:
                        print(f"Produk setelah kode {after_data} berhasil ditambahkan.")

                elif tambah_produk == 0:
                    break
                else:
                    print("Pilihan tidak valid. Masukkan pilihan yang benar.")

        elif pilihan == 2:
            toko_kosmetik.produk_list.display_pretty_table()

        elif pilihan == 3:
            while True:
                toko_kosmetik.produk_list.display_pretty_table()
                kode = input("Masukkan kode produk yang ingin diupdate: ")
                if not kode:
                    print("Kode produk tidak boleh kosong. Silakan masukkan kembali.")
                    continue
                elif not toko_kosmetik.is_kode_exists(kode):
                    print("Produk dengan kode", kode, "tidak ditemukan. Silakan masukkan kembali.")
                    continue
                else:
                    break

            try:
                nama_baru_input = input("Masukkan nama baru produk (kosongkan jika tidak ingin diubah): ")
                nama_baru = nama_baru_input if nama_baru_input.strip() != "" else None

                harga_baru_input = input("Masukkan harga baru produk (kosongkan jika tidak ingin diubah): ")
                harga_baru = float(harga_baru_input) if harga_baru_input.strip() != "" else None

                stok_baru_input = input("Masukkan stok baru produk (kosongkan jika tidak ingin diubah): ")
                stok_baru = int(stok_baru_input) if stok_baru_input.strip() != "" else None

                kategori_baru_input = input("Masukkan kategori baru produk (kosongkan jika tidak ingin diubah): ")
                kategori_baru = kategori_baru_input if kategori_baru_input.strip() != "" else None

                toko_kosmetik.update_produk(kode, nama_baru, harga_baru, stok_baru, kategori_baru)
                toko_kosmetik.produk_list.display_pretty_table()
            except ValueError:
                print("Masukkan nilai yang valid untuk harga dan stok.")
                continue
            
        elif pilihan == 4:
            while True:
                toko_kosmetik.produk_list.display_pretty_table()
                print("\nHallo, Selamat Datang.....        ")
                print("========TOKO KOSMETIK ARINI'S========")
                print("+----+------------------------------+")
                print("| No | Menu Hapus Produk            |")
                print("+----+------------------------------+")
                print("| 1  | Hapus Produk di Awal         |")
                print("| 2  | Hapus Produk di Akhir        |")
                print("| 3  | Hapus Produk Antara          |")
                print("| 0  | Kembali Menu Utama           |")
                print("+----+------------------------------+")
                try:
                    hapus_produk = int(input("Masukkan pilihan Anda: "))
                    toko_kosmetik.produk_list.display_pretty_table()
                except ValueError:
                    print("Masukkan pilihan yang valid (angka).")
                    continue

                if hapus_produk == 1:
                    toko_kosmetik.hapus_produk_di_awal()

                elif hapus_produk == 2:
                    toko_kosmetik.hapus_produk_di_akhir()

                elif hapus_produk == 3:
                    try:
                        kode = input("Masukkan kode produk setelahnya: ")
                        if not kode:
                            print("Kode barang tidak boleh kosong. Silakan masukkan kembali.")
                            continue
                        elif not re.match("^[a-zA-Z0-9]+$", kode):
                            print("Kode barang hanya boleh berupa huruf dan angka. Silakan masukkan kembali.")
                            continue
                        elif not toko_kosmetik.is_kode_exists(kode):
                            print("Produk dengan kode", kode, "tidak ditemukan.")
                            continue

                        toko_kosmetik.hapus_produk_di_antara_node(kode)

                    except ValueError:
                        print("Inputan harus valid dan tidak boleh kosong.")
                        continue
                    else:
                        print(f"Produk setelah kode {kode} berhasil dihapus.")

                elif hapus_produk == 0:
                    break
                else:
                    print("Pilihan tidak valid. Masukkan pilihan yang benar.")

        elif pilihan == 0:
            print("Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Masukkan pilihan yang benar.")
            
# Memanggil untuk jalankan program
main()
