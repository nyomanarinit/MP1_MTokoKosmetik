import os  # Modul os digunakan untuk berinteraksi dengan sistem operasi
import re  # Modul re digunakan untuk operasi regular expression
from prettytable import PrettyTable  # Impor modul PrettyTable untuk membuat tabel cantik


os.system("cls")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_pretty_table(self):
        table = PrettyTable()
        table.field_names = ["Kode", "Nama", "Harga", "Stok", "Kategori"]

        current = self.head
        while current:
            table.add_row([current.data.kode, current.data.nama, current.data.harga, current.data.stok, current.data.kategori])
            current = current.next

        print(table)

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_after_node(self, after_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data.kode == after_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_at_beginning(self):
        if not self.head:
            print("Daftar kosong. Tidak ada yang dapat dihapus.")
            return
        self.head = self.head.next

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

    def delete_after_node(self, after_data):
        current = self.head
        while current:
            if current.data.kode == after_data and current.next:
                current.next = current.next.next
                return
            current = current.next
        print(f"Produk dengan kode {after_data} tidak ditemukan atau merupakan simpul terakhir.")

    def sort_by_attribute(self, key, order='ascending'):
        products = [node.data for node in self.get_nodes()]
        sorted_products = sorted(products, key=lambda x: getattr(x, key), reverse=(order == 'descending'))
        self.head = None
        for product in sorted_products:
            self.add_at_end(product)

    def quick_sort(self, arr, key, order):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        if order == 'ascending':
            left = [x for x in arr if getattr(x, key) < getattr(pivot, key)]
            middle = [x for x in arr if getattr(x, key) == getattr(pivot, key)]
            right = [x for x in arr if getattr(x, key) > getattr(pivot, key)]
        elif order == 'descending':
            left = [x for x in arr if getattr(x, key) > getattr(pivot, key)]
            middle = [x for x in arr if getattr(x, key) == getattr(pivot, key)]
            right = [x for x in arr if getattr(x, key) < getattr(pivot, key)]
        else:
            raise ValueError("Invalid order. Use 'ascending' or 'descending'.")

        return self.quick_sort(left, key, order) + middle + self.quick_sort(right, key, order)

    def get_nodes(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        return nodes
    def search_by_id(self, kode):
        current = self.head
        index = 0
        while current:
            if current.data.kode.lower() == kode.lower():
                return index
            current = current.next
            index += 1
        return -1  # Return -1 if the element is not found

    def search_by_name(self, nama):
        current = self.head
        index = 0
        while current:
            if current.data.nama.lower() == nama.lower():
                return index
            current = current.next
            index += 1
        return -1  # Return -1 if the element is not found

    def jump_search(self, key, attribute):
        # Assuming the list is sorted based on the attribute to be searched
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next

        step = int(length ** 0.5)
        prev = None

        if attribute == "kode":
            while current and current.data.kode < key:
                prev = current
                for _ in range(step):
                    if current:
                        current = current.next
        elif attribute == "nama":
            while current and current.data.nama < key:
                prev = current
                for _ in range(step):
                    if current:
                        current = current.next

        while prev:
            if prev.data.kode == key or prev.data.nama == key:
                return prev.data
            prev = prev.next

        return None 

class Produk:
    def __init__(self, kode, nama, harga, stok, kategori):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori

class TokoKosmetik:
    def __init__(self):
        self.produk_list = LinkedList()

    def tambah_produk_di_awal(self, produk):
        if self.is_kode_unique(produk.kode):
            self.produk_list.add_at_beginning(produk)
        else:
            print("Kode barang sudah ada. Gunakan kode barang yang unik.")

    def tambah_produk_di_akhir(self, produk):
        if self.is_kode_unique(produk.kode):
            self.produk_list.add_at_end(produk)
        else:
            print("Kode barang sudah ada. Gunakan kode barang yang unik.")

    def tambah_produk_di_antara_node(self, after_data, produk):
        if self.is_kode_unique(produk.kode):
            self.produk_list.add_after_node(after_data, produk)
        else:
            print("Kode barang sudah ada. Gunakan kode barang yang unik.")

    def is_kode_unique(self, kode):
        current = self.produk_list.head
        while current:
            if current.data.kode == kode:
                return False
            current = current.next
        return True

    def is_kode_exists(self, kode):
        current = self.produk_list.head
        while current:
            if current.data.kode == kode:
                return True
            current = current.next
        return False

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

    def hapus_produk_di_awal(self):
        self.produk_list.delete_at_beginning()
        print("Produk di awal berhasil dihapus.")

    def hapus_produk_di_akhir(self):
        self.produk_list.delete_at_end()
        print("Produk di akhir berhasil dihapus.")

    def hapus_produk_di_antara_node(self, after_data):
        self.produk_list.delete_after_node(after_data)

def tambah_list_barang_awal(toko_kosmetik):
    produk1 = Produk("001", "Foundation", 150000, 100, "Makeup")
    produk2 = Produk("002", "Lipstick", 80000, 150, "Makeup")
    produk3 = Produk("003", "Shampoo", 50000, 200, "Hair Care")

    toko_kosmetik.tambah_produk_di_akhir(produk1)
    toko_kosmetik.tambah_produk_di_akhir(produk2)
    toko_kosmetik.tambah_produk_di_akhir(produk3)

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
        print("| 5  | Sorting dan Searching|")
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
                print("| 1  | Tambah Produk di Awal Node   |")
                print("| 2  | Tambah Produk di Akhir Node  |")
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
            while True:
                toko_kosmetik.produk_list.display_pretty_table()
                break
                
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
                print("| 1  | Hapus Produk di Awal Node    |")
                print("| 2  | Hapus Produk di Akhir Node   |")
                print("| 3  | Hapus Produk Antara Node     |")
                print("| 0  | Kembali Menu Utama           |")
                print("+----+------------------------------+")

                try:
                    hapus_produk = int(input("Masukkan pilihan Anda: "))
                    os.system("cls")
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

        # Bagian dalam fungsi main() yang menangani pilihan sorting
        elif pilihan == 5:
            while True:
                print("\nHallo, Selamat Datang.....        ")
                print("========TOKO KOSMETIK ARINI'S===============")
                print("+----+------------------------------------ +")
                print("| No | Pilihan Urutan                      |")
                print("+----+-------------------------------------+")
                print("| 1  | Sorting Berdasarkan Kode Produk     |")
                print("| 2  | Sorting Berdasarkan Nama Produk     |")
                print("| 0  | Kembali Menu Utama                  |")
                print("+----+-------------------------------------+")

                try:
                    urutan = int(input("Masukkan pilihan Anda: "))
                    os.system("cls")

                    if urutan == 1 or urutan == 2:
                        key = 'kode' if urutan == 1 else 'nama'
                        
                        masukkan_pilihan = input("Urutkan secara (ketikan asc/desc)  : ").lower()
                        if masukkan_pilihan in ['asc', 'desc']:
                            order = 'ascending' if masukkan_pilihan == 'asc' else 'descending'
                            toko_kosmetik.produk_list.sort_by_attribute(key, order)
                            
                            # Tampilkan hasil sorting menggunakan pretty table
                            print("\nHasil Sorting:")
                            toko_kosmetik.produk_list.display_pretty_table()
                            while True:
                                print("\nHallo, Selamat Datang.....        ")
                                print("========TOKO KOSMETIK ARINI'S===============")
                                print("+----+------------------------------------ +")
                                print("| No | Pilihan Urutan                      |")
                                print("+----+-------------------------------------+")
                                print("| 1  | Searching Berdasarkan Kode Produk   |")
                                print("| 2  | Searching Berdasarkan Nama Produk   |")
                                print("| 0  | Kembali Menu Sorting                |")
                                print("+----+-------------------------------------+")
                                try:
                                    pilihan_search = int(input("Masukkan pilihan Anda: "))
                                    os.system("cls")
                                    if pilihan_search == 1:
                                        kode_produk = input("Masukkan kode produk yang ingin dicari: ")
                                        index = toko_kosmetik.produk_list.search_by_id(kode_produk)
                                        if index != -1:
                                            print("Produk ditemukan di indeks:", index)
                                            # Tampilkan produk yang ditemukan dalam tabel cantik
                                            print("\nProduk yang Ditemukan:")
                                            table = PrettyTable()
                                            table.field_names = ["Kode", "Nama", "Harga", "Stok", "Kategori"]
                                            table.add_row([toko_kosmetik.produk_list.get_nodes()[index].data.kode,
                                                        toko_kosmetik.produk_list.get_nodes()[index].data.nama,
                                                        toko_kosmetik.produk_list.get_nodes()[index].data.harga,
                                                        toko_kosmetik.produk_list.get_nodes()[index].data.stok,
                                                        toko_kosmetik.produk_list.get_nodes()[index].data.kategori])
                                            print(table)
                                        else:
                                            print("Produk tidak ditemukan.")
                                    elif pilihan_search == 2:
                                        nama_produk = input("Masukkan nama produk yang ingin dicari: ")
                                        index = toko_kosmetik.produk_list.search_by_name(nama_produk)
                                        if index != -1:
                                            print("Produk ditemukan di indeks:", index)
                                            # Tampilkan produk yang ditemukan dalam tabel cantik
                                            print("\nProduk yang Ditemukan:")
                                            table = PrettyTable()
                                            table.field_names = ["Kode", "Nama", "Harga", "Stok", "Kategori"]
                                            table.add_row([toko_kosmetik.produk_list.get_nodes()[index].data.kode,
                                                        toko_kosmetik.produk_list.get_nodes()[index].data.nama,
                                                        toko_kosmetik.produk_list.get_nodes()[index].data.harga,
                                                        toko_kosmetik.produk_list.get_nodes()[index].data.stok,
                                                        toko_kosmetik.produk_list.get_nodes()[index].data.kategori])
                                            print(table)
                                        else:
                                            print("Produk tidak ditemukan.")

                                    elif pilihan_search == 0:
                                        break
                                    else:
                                        print("Pilihan tidak valid.")
                                except ValueError:
                                    print("Masukkan angka.")

                        else:
                            print("Pilihan tidak valid. Silakan masukkan 'asc' atau 'desc'.")
                    elif urutan == 0:
                        os.system("cls")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan masukkan kembali.")

                except ValueError:
                    print("Masukkan pilihan yang valid (angka).")
                    continue

        elif pilihan == 0:
            print("Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan kembali.")

main()
