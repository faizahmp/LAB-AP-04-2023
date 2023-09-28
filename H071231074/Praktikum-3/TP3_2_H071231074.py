# Meminta Inputan atas harga barang dan nilai uang yang dibayarkan
print("Harga Barang anda :")
harga_barang = int(input())
print("Nilai Uang anda : ")
nilai_uang = int(input())

# Penghitungan Kembalian
kembalian = nilai_uang - harga_barang

# Daftar pecahan uang beserta nilai pecahannya
pecahan_uang = [
    (100000, "Rp.100000"),
    (50000, "Rp.50000"),
    (20000, "Rp.20000"),
    (10000, "Rp.10000"),
    (5000, "Rp.5000"),
    (2000, "Rp.2000"),
    (1000, "Rp.1000")
]

# Mencetak Pecahan Uang yang akan dikembalikan
for pecahan, nama in pecahan_uang:
    jumlah = kembalian // pecahan
    print(f"{jumlah} uang sejumlah {nama}")
    kembalian %= pecahan 
