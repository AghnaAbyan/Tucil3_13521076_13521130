# Tugas Kecil 3 IF2211 Strategi Algoritma 2022/2023: Implementasi Algoritma UCS dan A* untuk Menentukan Lintasan Terpendek
<p align="center">
  <img width="1000" alt="image" src="https://user-images.githubusercontent.com/110531746/231323706-deb3d6a1-9801-4e08-8d7d-f72e853edaa3.png">
 </p>
Program ini dibuat untuk memenuhi capaian kurikulum Tugas Kecil 3 IF2211 Strategi Algoritma 2022/2023, yaitu implementasi algoritma UCS dan A* dalam pencarian lintasan terpendek pada sebuah peta.

## *Table of Contents*
- [Deskripsi Singkat](#deskripsi)
- [*Requirement* Program](#req)
- [Cara Menggunakan Program](#penggunaan)
- [Identitas pembuat](#author)

## Deskripsi Singkat <a name="deskripsi"></a>
Program akan menerima masukan dasar berupa matriks ketetanggaan, dengan tiap baris menyatakan satu node dan tiap kolom menyatakan hubungan node dengan node lainnya. Program akan menghasilkan keluaran berupa visualisasi graf berdasarkan matriks ketetanggan yang sudah dibuat, rute yang dicapai berdasarkan algoritma yang dipakai (UCS atau A*), dan jarak tempuh yang dicapai.

## *Requirement* Program <a name="req"></a>
Sebelum menjalankan program, diperlukan instalasi Python 3 dikarenakan program secara keseluruhan menggunakan bahasa Python. Python dapat diunduh melalui tautan berikut: https://www.python.org/downloads/

Diperlukan juga instalasi beberapa *library* dari python supaya keseluruhan program dapat berjalan, yaitu:
- flask
- googlemaps
- networkx
- colorama

## Cara Menggunakan Program <a name="penggunaan"></a>
1. Pastikan direktori sudah berada pada folder ``src``.
2. Ketik ``python3 main.py`` pada terminal.

<img width="683" alt="image" src="https://user-images.githubusercontent.com/110531746/231324279-2d3d9358-cc7b-4c40-a327-ab27cc0a1db0.png">

3. Program akan meminta masukan dari pengguna, antara 1 (menjalankan program penelusuran lintasan) atau 2 (keluar dari program). Ketik 1 untuk menjalankan program.

<img width="150" alt="image" src="https://user-images.githubusercontent.com/110531746/231324553-8328c08d-49c6-449f-a5f7-06f7147ee50f.png">

4. Selanjutnya, program akan meminta masukan file.txt dari program. Masukan nama file.txt yang sudah tersedia pada folder "test".

<img width="423" alt="image" src="https://user-images.githubusercontent.com/110531746/231324784-eeaaa372-c5a0-4b41-b723-131228dd8a19.png">

5. Setelah itu, pengguna akan diminta memasukan salah satu dari 2 pilihan metode kalkulasi. Untuk contoh, kita akan menggunakan opsi 2, karena masukan yang digunakan adalah node pada posisi bujur dan lintang.

<img width="215" alt="image" src="https://user-images.githubusercontent.com/110531746/231325382-9bb717e1-49f7-47ee-bf24-f8138c6fac8c.png">

6. Kemudian, pengguna akan diminta memasukan salah satu algoritma yang tersedia, opsi 1 (UCS) atau opsi 2 (A*).

<img width="217" alt="image" src="https://user-images.githubusercontent.com/110531746/231325502-3359d2e9-09c9-4841-982e-a5aaf9a9e6ea.png">

7. Akan ditampilkan daftar node yang tersedia, pilih node awal dan node akhir.

<img width="176" alt="image" src="https://user-images.githubusercontent.com/110531746/231325854-988fd33c-3e2d-4b89-bd15-f3a52e715b3f.png">

8. Ditampilkan jarak yang ditempuh program melalui algoritma yang dipilih. Pengguna akan diminta untuk memasukan bentuk visualisasi yang diinginkan, antara opsi 1 (graf), opsi 2 (map), atau opsi 3 (tidak perlu visualisasi).

  - Jika 1 dipilih, akan menampilkan graf sebagai berikut:

![FigureTC3](https://user-images.githubusercontent.com/110531746/231337307-6227a075-d943-4ab1-87ac-e3bee0d336ce.png)

    Garis merah menunjukkan rute yang dilalui oleh algoritma.

<img width="233" alt="image" src="https://user-images.githubusercontent.com/110531746/231337502-46ea6957-91f9-41e0-b595-c55bc3f2ee99.png">

9. Jika sudah selesai, program akan kembali ke tampilan awal. Tekan opsi 1 jika ingin mencoba lagi, tekan opsi 2 jika ingin keluar dari program.

<img width="752" alt="image" src="https://user-images.githubusercontent.com/110531746/231337661-d59b9118-c895-430d-8531-cc87ade791b9.png">

10. Program selesai dijalankan!

## Identitas Pembuat <a name="author"></a>
<table>
  <tr>
    <td align="center" colspan="3">No. Kelompok : 14</td>
  </tr>
  <tr>
    <td align="center" colspan="3">Kelas : 02</td>
  </tr>   
    <td align="center">NIM</td>
    <td align="center">Nama</td>
    <td align="center">Username</td>
  </tr>
    <td align="center">13521076</td>
    <td align="center">Moh. Aghna Maysan Abyan</td>
    <td align="center"><a href=https://github.com/AghnaAbyan>AghnaAbyan</a></td>
  </tr>
    <td align="center">13521130</td>
    <td align="center">Althaaf Khasyi Atisomya</td>
    <td align="center"><a href=https://github.com/althaafka>althaafka</a></td>
  </tr>

</table>
