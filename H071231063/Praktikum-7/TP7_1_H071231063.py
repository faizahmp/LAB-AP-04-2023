import os
import random
import datetime
def generate_transaction_id(cashier_name):
    now = datetime.datetime.now()
    upper_name = cashier_name[0] + cashier_name[len(cashier_name) // 2] + cashier_name[-1]
    transaction_id = f"{upper_name.upper()}{now.strftime('%y%m%d%H%M')}{random.randint(100, 999)}"
    return transaction_id
def print_invoice(transaction_id, cashier_name, products):
    invoice_filename = f"invoices/{transaction_id}.txt"
    with open(invoice_filename, "w") as invoice_file:
        total_amount = 0
        now = datetime.datetime.now()
        toko = f'Toko {cashier_name.upper()}'
        invoice_file.write("\n"f"{toko.center(60)}\n")
        invoice_file.write("\n")
        invoice_file.write('=' * 60 + '\n')
        invoice_file.write(f"{'Kasir          : ' + cashier_name}\n")
        invoice_file.write(f"{'Waktu transaksi: ' + now.strftime('%d/%m/%y %H:%M')}\n")
        invoice_file.write('=' * 60 + '\n')
        invoice_file.write("\n")
        invoice_file.write(f"{'Daftar Produk'.center(60)}\n")
        invoice_file.write("\n")
        invoice_file.write('  ' + '=' * 55 + '\n')
        invoice_file.write('  |' + 'Nama Produk'.ljust(20) + '|' + 'Harga'.rjust(10) + '|' + 'Jumlah'.rjust(10) + '|' + 'Total'.rjust(10) + '|\n')
        invoice_file.write('  ' + '=' * 55 + '\n')   
        for product in products:
            product_name, price, quantity = product
            total_price = price * quantity
            total_amount += total_price
            invoice_file.write(f"  |{product_name.ljust(20)}|Rp.{str(price).rjust(7)}|{str(quantity).rjust(10)}|Rp.{str(total_price).rjust(7)}|\n")        
        invoice_file.write('  ' + '=' * 55 + '\n')
        invoice_file.write(f"  |{'TOTALv'.ljust(42)}|Rp.{str(total_amount).rjust(7)}|\n")
        invoice_file.write('  ' + '=' * 55 + '\n')
        invoice_file.write('=' * 60 + '\n')
        invoice_file.write(f"{'TERIMA KASIH TELAH BERBELANJA'.center(60)}\n")
        invoice_file.write('=' * 60)
    return invoice_filename
def search_invoice_by_id(transaction_id):
    invoice_filename = f"invoices/{transaction_id}.txt"
    if os.path.exists(invoice_filename):
        with open(invoice_filename, "r") as invoice_file:
            content = invoice_file.read()
        return content
    else:
        return "Invoice tidak ditemukan."
def record_transaction_history(transaction_id, total_amount):
    now = datetime.datetime.now()
    history_entry = f"|{now.strftime('%d/%m/%y %H:%M')} | {transaction_id.rjust(15)}|Rp.{str(total_amount).rjust(14)}|\n"
    if not os.path.exists("trx_history.txt"):
        with open("trx_history.txt", "w") as history_file:
            history_file.write('=' * 53 + '\n')
            history_file.write(f"|{'RIWAYAT TRANSAKSI'.center(51)}|\n")
            history_file.write('=' * 53 + '\n')
            history_file.write(f"|{'Waktu'.ljust(15)}|{'ID Transaksi'.rjust(17)}|{'Nominal Transaksi'.rjust(15)}|\n")
            history_file.write('=' * 53 + '\n')
    with open("trx_history.txt", "a") as history_file:
        history_file.write(history_entry)
        history_file.write('=' * 53 + '\n')
if __name__ == "__main__":
    if not os.path.exists("invoices"):
        os.makedirs("invoices")
    print("=" * 50)
    print(f"{'SELAMAT DATANG'.center(50)}")
    print("=" * 50)
    cashier_name = input("Masukkan nama kasir   : ")
    while True:
        print("=" * 50)
        print("\nPilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        print("=" * 50)
        choice = input("Masukkan opsi pilihan  : ")
        print("=" * 50)
        if choice == "1":
            products = []
            while True:
                product_name = input("Masukkan nama produk   : ")
                price = int(input("Masukkan harga produk  : "))
                quantity = int(input("Masukkan jumlah produk : "))
                products.append((product_name, price, quantity))
                print("=" * 50)
                add_another = input("Tambah produk? (y/t)   : ")
                if add_another.lower() != 'y':
                    break
            if not products:
                print("Transaksi dibatalkan.")
            else:
                transaction_id = generate_transaction_id(cashier_name)
                invoice_filename = print_invoice(transaction_id, cashier_name, products)
                record_transaction_history(transaction_id, sum(price * quantity for _, price, quantity in products))
                print("=" * 50)
                print(f"{'TRANSAKSI BERHASIL'.center(50)}")
        elif choice == "2":
            search_id = input("Masukkan ID transaksi: ")
            result = search_invoice_by_id(search_id)
            print(result)
        elif choice == "3":
            print("Terima kasih! Aplikasi selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
