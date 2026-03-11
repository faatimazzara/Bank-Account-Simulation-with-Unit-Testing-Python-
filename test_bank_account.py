"""
File ini berisi unit testing untuk class BankAccount.
Unit testing digunakan untuk memastikan bahwa setiap method
dalam class bekerja dengan benar pada berbagai kondisi.

Framework yang digunakan adalah unittest yang merupakan
testing framework bawaan dari Python.
"""

import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """
        Method setUp() dijalankan sebelum setiap test case.

        Tujuannya adalah membuat objek BankAccount baru
        agar setiap test berjalan dalam kondisi yang sama
        dan tidak dipengaruhi oleh test sebelumnya.
        """
        self.account = BankAccount("Fatimah", 100)

    def test_account_owner(self):
        """Memastikan nama pemilik akun tersimpan dengan benar."""
        self.assertEqual(self.account.owner, "Fatimah")

    def test_initial_balance(self):
        """Memastikan saldo awal akun sesuai dengan yang diberikan."""
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit_valid(self):
        """Memastikan deposit menambah saldo dengan benar."""
        result = self.account.deposit(50)
        self.assertEqual(result, 150)

    def test_deposit_updates_balance(self):
        """Memastikan saldo berubah setelah deposit."""
        self.account.deposit(200)
        self.assertEqual(self.account.get_balance(), 300)

    def test_deposit_zero(self):
        """Deposit 0 tidak diperbolehkan."""
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_negative(self):
        """Deposit negatif harus menghasilkan error."""
        with self.assertRaises(ValueError):
            self.account.deposit(-20)

    def test_withdraw_valid(self):
        """Withdraw valid harus mengurangi saldo."""
        result = self.account.withdraw(40)
        self.assertEqual(result, 60)

    def test_withdraw_updates_balance(self):
        """Memastikan saldo berkurang setelah withdraw."""
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 50)

    def test_withdraw_all_balance(self):
        """Withdraw seluruh saldo harus menghasilkan saldo 0."""
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 0)

    def test_withdraw_insufficient_balance(self):
        """Withdraw lebih besar dari saldo harus menghasilkan error."""
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_withdraw_negative(self):
        """Withdraw negatif tidak diperbolehkan."""
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_multiple_transactions(self):
        """
        Menguji beberapa transaksi berturut-turut
        untuk memastikan saldo tetap konsisten.
        """
        self.account.deposit(100)
        self.account.withdraw(50)
        self.account.deposit(25)
        self.assertEqual(self.account.get_balance(), 175)

    def test_balance_after_many_operations(self):
        """Mengukur konsistensi saldo setelah banyak transaksi."""
        self.account.deposit(300)
        self.account.withdraw(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 250)

    def test_get_balance_method(self):
        """Memastikan method get_balance() mengembalikan tipe data integer."""
        balance = self.account.get_balance()
        self.assertIsInstance(balance, int)

if __name__ == "__main__":
    unittest.main(verbosity=2)