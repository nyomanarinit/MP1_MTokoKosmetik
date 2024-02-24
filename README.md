# MP1_MTokoKosmetik


NAMA: NYOMAN ARINI TRIRAHAYU

NIM: 2309116002

KELAS: SISTEM INFORMASI A

MATA KULIAH: PTRAKTIKUM ALGORITMA DAN STRUKTUR DATA

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
