# MINI PROJECT
NAMA: NYOMAN ARINI TRIRAHAYU
NIM: 2309116002
KELAS: SISTEM INFORMASI A
MATA KULIAH: PTRAKTIKUM ALGORITMA DAN STRUKTUR DATA

## MP1_MTokoKosmetik
~Penejlasan Program

Program ini merupakan aplikasi manajemen produk kosmetik sederhana dengan menggunakan terminal sebagai antarmuka pengguna. 

1.  program akan membersihkan terminal dan mengimport modul yang dibutuhkan, yaitu `os` untuk membersihkan terminal dan `PrettyTable` untuk menampilkan data dalam bentuk tabel.

2. terdapat definisi kelas `Produk` yang digunakan untuk merepresentasikan produk kosmetik. Kelas ini memiliki atribut seperti kode, nama, harga, stok, dan kategori.

3. ada definisi kelas `TokoKosmetik` yang digunakan untuk manajemen produk. Kelas ini memiliki fungsi-fungsi seperti `tambah_produk`, `lihat_produk`, `update_produk`, dan `hapus_produk`.

4. Di dalam fungsi utama (`main()`):
   - Program membuat objek dari kelas `TokoKosmetik` sebagai toko kosmetik default.
   - Program akan memasuki loop utama yang menampilkan menu utama kepada pengguna.
   - Pengguna diminta untuk memilih opsi (angka) sesuai dengan menu yang ditampilkan.
   - Setiap pilihan akan memicu fungsi-fungsi yang sesuai pada objek `TokoKosmetik` atau memberikan pesan kesalahan jika input tidak valid.
   - Pilihan 1 berfungsi untuk menambahkan produk
   - Pilihan 2 berfungsi untuk lihat produk
   -  Pilihan 3 berfungsi untuk update produk
   -  Pilihan 4 berfungsi untuk hapus produk
   -  Pilihan 0 berfungsi untuk menghentikan program
   - Loop akan terus berjalan sampai pengguna memilih untuk keluar (pilihan 0).

5. Output yang mungkin dihasilkan:
   - Pesan kesalahan jika data produk tidak lengkap atau ada duplikat kode produk saat menambahkan produk baru.
   - Daftar produk dalam bentuk tabel jika pengguna memilih untuk melihat daftar produk.
   - Pesan sukses atau pesan bahwa produk tidak ditemukan saat mengupdate atau menghapus produk.
   - Pesan terima kasih saat pengguna memilih untuk keluar.

## MP2_MTokoKosmetik

### Penjelasan dan Output Program.
1. Tampilan Awal Program
   Pada tampilan awal program user di berikan 5 pilihan yaitu 1.Tambah Produk, 2.Lihat Daftar Produk, 3.Update Produk, 4.Hapus Produk, dan 0.Keluar.
![Cuplikan layar 2024-03-02 084512](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/9f0e108f-0843-4a3c-a6fa-d754153e7db7)

   -1.Tambah Barang
   Jika User memilih 1.Tambah Barang maka akan diberikan menu lagi dengan 4 pilihan menu tambah barang yaitu 1.Tambah Barang di Awal, 2.Tambah Barang      di Akhir, 3.Tambh Barangf di antara Node, dan 0.Kembali.
   ![Cuplikan layar 2024-03-02 084533](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/bc5e9916-9a0f-4b13-a857-5a108d6df60a)
   ![Cuplikan layar 2024-03-02 084548](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/1d439f35-5760-484e-b0b9-8c5bad777f44)

      *1.Tambah Barang di Awal
         Tambah barang di awal artinya barang yang akan user tambahkan akan otomatis berada di awal atau di paling atas pada list barang. Jika user              memilih 1.Tambah Produk di Awal maka user diminta untuk memasukkan kode produk, nama produk, harga produk, stok produk, dan kategori produk             (dengan catatan kode produk tidak boleh sama dan tidak boleh di kosongkan, harga dan stok bersifat integer).

         ![Cuplikan layar 2024-03-02 093913](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/3bdb0a8c-70d1-432d-b871-91f19de0c5bb)
         ![Cuplikan layar 2024-03-02 094154](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/494c3b84-3521-4dfb-982e-f0ecb59120c7)


      *2.Tambah Barang di Akhir
         Tambah barang di akhir artinya barang yang akan user tambahkan akan otomatis berada di akhir atau di paling bawah pada list barang. Jika user          memilih 2.Tambah Produk di Akhir maka user diminta untuk memasukkan kode produk, nama produk, harga produk, stok produk, dan kategori produk            (dengan catatan kode produk tidak boleh sama dan tidak boleh di kosongkan, harga dan stok bersifat integer).

         ![Cuplikan layar 2024-03-02 094208](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/ae557c45-c6e8-40ce-8d4e-057b09e730ff)
         ![Cuplikan layar 2024-03-02 094237](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/7937cf3f-e805-4e7f-a300-c0de700fc471)

         
      *3.Tambah Barang di anatara Node
         Tambah barang di antara node artinya barang yang akan user tambahkan akan otomatis berada di bawah kode barang yang di pilih. Jika user                 memilih 3.Tambah Produk di antara node maka user diminta untuk memasukkan kode produk setelah node baru di tambahkan,  kode produk yang ingin           di tambahkan, nama produk, harga produk, stok produk, dan kategori produk (dengan catatan kode produk tidak boleh sama dan tidak boleh di               kosongkan, harga dan stok bersifat integer).

         ![Cuplikan layar 2024-03-02 094333](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/4d77dcef-3792-4e21-98dc-96c3793bd17e)

      *0.Kembali
      Jika User memilih 0.kembali maka program akan kembali kemenu utama.
      ![Cuplikan layar 2024-03-02 085027](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/c41118a1-a98e-4ab5-97fa-0e2891c3d571)
      ![Cuplikan layar 2024-03-02 084512](https://github.com/nyomanarinit/MP1_MTokoKosmetik/assets/145880551/010ed561-466c-4723-a174-1c7642e4aefb)

   
