"""
Program ini digunakan untuk mensimulasikan penggunaan class BankAccount
dalam sebuah sistem sederhana. Tujuannya adalah untuk menunjukkan bagaimana
objek dari class BankAccount digunakan dalam skenario nyata seperti
deposit dan withdraw.
"""

from bank_account import BankAccount

def print_header():
    """
    Menampilkan judul program agar tampilan terminal lebih terstruktur
    dan mudah dibaca oleh pengguna.
    """
    print("=" * 60)
    print("              SIMPLE BANK ACCOUNT SIMULATION")
    print("=" * 60)

def print_account_info(account):
    """
    Menampilkan informasi dasar akun bank.
    Fungsi ini dipisahkan agar kode lebih modular dan mudah digunakan kembali.
    """
    print(f"Account Owner : {account.owner}")
    print(f"Current Balance : {account.get_balance()}")
    print("-" * 60)

def perform_deposit(account, amount):
    """
    Fungsi ini menangani proses deposit.

    Mengapa dibuat fungsi terpisah?
    Agar logika transaksi lebih terstruktur dan mudah dibaca.
    """
    print("\n[ DEPOSIT TRANSACTION ]")

    try:
        account.deposit(amount)
        print(f"Deposit Amount : {amount}")
        print(f"New Balance    : {account.get_balance()}")
    except ValueError as error:
        print("Deposit Failed:", error)

    print("-" * 60)

def perform_withdraw(account, amount):
    """
    Fungsi ini menangani proses withdraw dari akun bank.
    """
    print("\n[ WITHDRAW TRANSACTION ]")

    try:
        account.withdraw(amount)
        print(f"Withdraw Amount : {amount}")
        print(f"New Balance     : {account.get_balance()}")
    except ValueError as error:
        print("Withdraw Failed:", error)

    print("-" * 60)

def main():
    """
    Fungsi utama program.

    Di sini kita membuat objek BankAccount dan melakukan
    beberapa transaksi untuk menunjukkan cara kerja class tersebut.
    """

    print_header()

    # membuat objek akun bank
    account = BankAccount("Fatimah Azzahra")

    print_account_info(account)

    # simulasi beberapa transaksi
    perform_deposit(account, 100000)
    perform_withdraw(account, 30000)
    perform_deposit(account, 50000)
    perform_withdraw(account, 20000)

    # ringkasan akhir
    print("\nFINAL ACCOUNT SUMMARY")
    print("-" * 60)
    print(f"Account Owner : {account.owner}")
    print(f"Final Balance : {account.get_balance()}")
    print("=" * 60)

if __name__ == "__main__":
    main()