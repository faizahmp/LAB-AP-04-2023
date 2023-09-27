hargabarang = int(input("masukaan harga barang :"))
uang = int(input("masukkan uang anda :"))
if uang < hargabarang:
    print("uang anda tidak cukup")
    exit()

kembalian = uang - hargabarang

pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]

for pecahan in pecahan_uang:
    jumlah_uang = kembalian // pecahan
    kembalian %= pecahan                
    print(f"{jumlah_uang} uang sejumlah Rp.{pecahan}")

