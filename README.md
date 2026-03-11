# Bank Account Simulation with Unit Testing (Python)

## Deskripsi
Repository ini berisi implementasi sederhana dari sistem **Bank Account** menggunakan bahasa pemrograman **Python**. Proyek ini dibuat untuk mempelajari konsep **Object Oriented Programming (OOP)** serta penerapan **Unit Testing** dalam pengembangan perangkat lunak.

Program ini mensimulasikan beberapa transaksi dasar pada akun bank seperti **deposit**, **withdraw**, dan **pengecekan saldo**. Selain itu, proyek ini juga dilengkapi dengan **pengujian otomatis (unit testing)** untuk memastikan setiap metode dalam class bekerja dengan benar.

## Struktur Proyek
Proyek ini terdiri dari tiga file utama:
### 1. `bank_account.py`
File ini berisi implementasi **class BankAccount** yang menjadi inti dari program.  
Class ini menyimpan informasi pemilik akun dan saldo, serta menyediakan beberapa metode untuk melakukan transaksi keuangan.
Metode yang tersedia pada class ini adalah:
- `deposit(amount)` → menambahkan saldo ke akun
- `withdraw(amount)` → menarik saldo dari akun
- `get_balance()` → mengambil saldo akun saat ini

Class ini juga memiliki validasi untuk memastikan bahwa transaksi yang dilakukan sesuai dengan aturan yang berlaku.

### 2. `main.py`
File ini digunakan untuk menjalankan **simulasi program**.  
Pada file ini dibuat sebuah objek dari class `BankAccount` kemudian dilakukan beberapa transaksi seperti:
- membuat akun bank
- melakukan deposit
- melakukan withdraw
- menampilkan saldo akhir akun

Program ini juga menggunakan **error handling** (`try-except`) untuk menangani kesalahan transaksi seperti deposit negatif atau withdraw melebihi saldo.

### 3. `test_bank_account.py`
File ini berisi **unit testing** untuk menguji seluruh metode dalam class `BankAccount`.
Pengujian dilakukan menggunakan framework bawaan Python yaitu: unittest

Unit testing dilakukan untuk memastikan bahwa setiap fungsi bekerja dengan benar dalam berbagai kondisi.
Jumlah unit test yang dibuat dalam proyek ini adalah **14 test case** yang mencakup:
- pengujian saldo awal
- deposit valid
- deposit tidak valid
- withdraw valid
- withdraw melebihi saldo
- withdraw bernilai negatif
- transaksi berturut-turut
- konsistensi saldo setelah banyak operasi

## Konsep yang Digunakan
Proyek ini menerapkan beberapa konsep dalam pemrograman berorientasi objek, antara lain:
- **Class dan Object**
- **Encapsulation**
- **Method**
- **Validation**
- **Unit Testing**

Dengan menggunakan unit testing, kualitas kode dapat diuji secara otomatis sehingga meminimalkan kesalahan dalam program.
