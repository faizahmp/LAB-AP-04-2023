import os
import datetime
import random

def Garis(n):
    print("=" * n)

def Inisial_Nama(Nama):
    Huruf = Nama.title() #MENGUBAH HURUF AWAL PADA SETIAP NAMA PADA SETIAP SPASI
    Inisial = '' 
    for i in Huruf:
        if i.isupper(): # MENGECEK HRUF KAPITAL PADA NAMA
            Inisial += i # AKAN MENAMBAHKAN HURUF KAPITAL KEDALAM VAR INISIAL
    return Inisial
def ID_Transaksi(Nama):
     Waktu = datetime.datetime.now()

     ID = f"{Inisial_Nama(Nama)}{Waktu.strftime('%y%m%d%H%M')}{random.randint(100,999)}"
     return ID

# BERIKUT YANG AKAN MUNCUL DI DALAM FILE TRANSAKSI
def waktu(): # Fungsi ini utk memunculkan susunan waktu utk sekarang
    waktu = datetime.datetime.now()
    waktu = f'{waktu.strftime("%x %H:%M")}' # %x akan mengambil format tanggal yg menggunakan "/"
    return waktu

def Bagian_Atas(Nama, Waktu):
    data.write(f"\n{f'TOKO {Nama}':^70}\n\n")
    
    data.write(f"{'=' * 70}\n")
    data.write(f"{'Nama Kasir':<20}: {Nama}\n")
    data.write(f"{'Waktu transaksi':<20}: {Waktu}\n")
    data.write(f"{'=' * 70}\n\n")

    data.write(f"{f'Daftar Produk':^70}\n\n")
    
    data.write(f"{60 * '=':^70}\n")
    data.write(f"{5 * ' '}|{'Nama':^20}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^15}|\n")
    data.write(f"{60 * '=':^70}\n")
def Bagian_Tengah(Nama, Harga, Jumlah, Total):
    if len(Nama) >= 20 :
        Nama = Nama[:15] + "..."
    data.write(f"{5 * ' '}| {Nama:<18} | {'Rp' + str(Harga):^10} |{Jumlah:^8}| {'Rp' + str(Total):>13} |\n")
def Bagian_Bawah(total_belanja):
    data.write(f"{60 * '=':^70}\n")
    data.write(f"{' ' * 5}|{' ' * 7}{'TOTAL':^35}|{'Rp'+str(total_belanja):>15}|\n")
    data.write(f"{60 * '=':^70}\n\n")
    data.write(f"{'=' * 70}\n")
    data.write(f"{'TERIMA KASIH TELAH BERBELANJA':^70}\n")
    data.write(f"{'=' * 70}\n")

# Tabel yang akan muncul di dalam File Riwayat
def Riwayat_Transaksi():
    with open('trx_history.txt', 'w') as R:
        R.write(f"{'=' * 70}\n")
        R.write(f"|{'RIWAYAT TRANSAKSI':^68}|\n")
        R.write(f"{'=' * 70}\n")
        R.write(f"|{'Waktu':^18}|{'ID Transaksi':^24}|{'Nominal Transaksi':^24}|\n")
        R.write(f"{'=' * 70}\n")
def Tabel_Riwayat_Transaksi(Waktu, ID, Nominal):
    with open('trx_history.txt', 'a') as R:
        R.write(f"|{Waktu:^18}|{ID:^24}| {'Rp' + Nominal:>22} |\n")
        R.write(f"{'=' * 70}\n")



# YANG AKAN MUNCUL DITERMINAL
Garis(60)
print(f"{'SELAMAT DATANG':^60}")
Garis(60)
Nama = input("Masukkan nama kasir \t: ")
Garis(60)

while True:
    print("Pilih Opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    Garis(60)
    opsi = int(input('Masukkan opsi pilihan \t: '))
    Garis(60)

    match opsi :
        case 1:
            # Membuat File Transaksi
            ID = ID_Transaksi(Nama)
            Nama_File = f'{ID}.txt'
            Nama_Folder = "invoices" #<-DENGAN NAMA
            File_Path = os.path.join(Nama_Folder, Nama_File) #maka id akan masuk keini
            
            Waktu = waktu()

            # Membuat Folder jika Foldernya belum ada
            if not os.path.exists(Nama_Folder) :
                os.mkdir(Nama_Folder)

            data = open(File_Path, 'w') # utk menulis jika sdh ada mka akan terhpus dengan tulisan yg baru
            
            Bagian_Atas(Nama, Waktu)

            Total_Produk = 0
            while True :
                Nama_Produk = str(input("Masukkan nama produk \t: "))
                Harga = int(input("Masukkan harga produk \t: "))
                Jumlah = int(input("Masukkan jumlah produk \t: "))
                Total = Harga * Jumlah
                Garis(60)

                Total_Produk += Total

                Bagian_Tengah(Nama_Produk, Harga, Jumlah, Total)

                Tambah = input("Tambah Produk? (y/t) \t: ").lower()
                if Tambah == "y" :
                    Garis(60)
                    continue
                elif Tambah == "t" :
                    Garis(60)
                    print(f'{"TRANSAKSI BERHASIL":^60}')
                    Garis(60)
                    
                    Bagian_Bawah(Total_Produk)
                    data.close()
                
                    # Membuat File Riwayat jika File belum ada
                    if not os.path.exists('trx_history.txt'):
                        Riwayat_Transaksi()
                    
                    Nominal = str(Total_Produk)
                    Tabel_Riwayat_Transaksi(Waktu, ID, Nominal)

                    break
                else:
                    Garis(60)
                    print('Invalid pilihan')
                    break

        case 2:
            Cari = input('Masukkan ID transaksi \t: ')
            Nama_Folder = 'invoices'
            Cari_Path = os.path.join(Nama_Folder, f'{Cari}.txt')

            if os.path.exists(Cari_Path): # jika cari path ada pada berkas maka kondisi akan terpenuhi
                with open(Cari_Path, "r") as file:
                    print('_' * 70)
                    print(f"\n{file.read()}")
                    print('_' * 70)   
            else:
                print(f"File dengan ID {Cari} tidak ditemukan")
        
        case 3:
            print('SAMPAI JUMPA'.center(60))
            Garis(60)
            break

        case _:
            print('Invalid Opsi'.center(60))
            Garis(60)
            break