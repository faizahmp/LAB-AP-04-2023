hargabarang = int(input("Masukkan Harga Barang : "))
uang = int(input("Masukkan Berapa uang anda : "))
kembalian = uang - hargabarang
if kembalian < 0:
    print("Uang anda kurang!")
else:
    pecahan = (100000, 50000, 20000, 10000, 5000, 2000, 1000)
    # pecahan = tuple(int(x) for x in p)
    for i in pecahan:
        jumlah = kembalian // i
        kembalian = kembalian - jumlah * i
        print(f"{jumlah} Jumlah uang bernilai Rp.{i}")