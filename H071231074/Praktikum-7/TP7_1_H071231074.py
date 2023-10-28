import os, random, datetime

if not os.path.exists("invoices"):
    os.makedirs("invoices")  # Membuat folder "Invoices" jika belum ada

def cetak_invoices(nama_kasir, transaksi):
    sekarang = datetime.datetime.now()
    id_transaksi = f"{nama_kasir[:1].upper()}{sekarang.strftime('%y%m%d%H%M%S')}{random.randint(100, 999)}"

    invoice_file = f"invoices/{id_transaksi}.txt"

    with open(invoice_file, "w") as file:
        file.write(f"{('TOKO KELVIN').center(60)}\n\n{'='*60}\n")
        file.write(f"ID Transaksi: {id_transaksi}\n")
        file.write(f"Nama Kasir: {nama_kasir}\n")
        file.write(f"Waktu Transaksi: {sekarang}\n{'='*60}\n")
        file.write(f"{('Daftar Produk').center(60)}\n\n{'='*60}\n")

        file.write(f"|{('Nama').center(14)}|{('Harga').center(13)}|{('Jumlah').center(12)}|{('Total').center(16)}|\n{'='*60}\n")

        for produk in transaksi:
            nama_produk, harga, jumlah = produk
            total = 'Rp' + str(jumlah * harga)
            harga = 'Rp' + str(harga)
            file.write(f"|{nama_produk.ljust(14)}|{(harga).ljust(13)}|{str(jumlah).center(12)}|{str(total).ljust(16)}|\n{'='*60}\n")
        
        total_harga = sum([produk[2] * produk[1] for produk in transaksi])
        file.write(f"|{('Total.').ljust(41)}|Rp{str(total_harga).ljust(14)}|\n{'='*60}\n\n{'='*60}\n")
        file.write(f"{('TERIMA KASIH TELAH BERBELANJA').center(60)}")

    print(f"Invoice telah dicetak dengan ID Transaksi: {id_transaksi}")
    return id_transaksi

def tampilkan_invoice(id_transaksi): #Nomor 2
    invoice_file = f"invoices/{id_transaksi}.txt"

    if os.path.exists(invoice_file):
        with open(invoice_file, "r") as file:
            print(file.read())
    else:
        print(f"Invoice dengan ID Transaksi {id_transaksi} tidak ditemukan")

def catat_riwayat(id_transaksi, total_harga): #Nomor 3
    riwayat_file = "trx_history.txt"
    now = datetime.datetime.now()

    with open(riwayat_file, 'a') as file:
        file.write(f"{now} - {id_transaksi} - {total_harga}\n")

while True:
    print(f"{'='*50}\n{('SELAMAT DATANG').center(50)}\n{'='*50}")
    print(f"1. Transaksi Baru\n2. Cari Transaksi\n3. Keluar\n{'='*50}")
    pilihan = input("Masukkan opsi pilihan : ")

    if pilihan == "1":
        nama_kasir = input("Masukkan nama kasir : ")
        transaksi = []

        while True:
            nama_produk = input("Nama Produk : ")
            harga = float(input("Harga Produk : "))
            jumlah = int(input("Jumlah Produk : "))

            transaksi.append((nama_produk, harga, jumlah))

            lagi = input("Tambah produk lain? (y/n): ")
            if lagi.lower() != 'y':
                break

        id_transaksi = cetak_invoices(nama_kasir, transaksi)  # Menyimpan ID Transaksi
        total_harga = sum([float(harga) * jumlah for _, harga, jumlah in transaksi])
        catat_riwayat(id_transaksi, total_harga)  # Menggunakan ID Transaksi yang disimpan

    elif pilihan == "2":
        id_transaksi = input("Masukkan ID Transaksi : ")
        tampilkan_invoice(id_transaksi)

    elif pilihan == "3":
        break
    else:
        print("Masukkan inputan sesuai yang diminta")