print(f"{'PROGRAM MENENTUKAN KEMBALIAN ':^40}")
print(f"{'_'*40:^40}")

harga_barang=int(input())
uang_dibayar=int(input())


kembalian=uang_dibayar-harga_barang
pecahan_uang=[100000, 50000, 20000, 10000, 5000, 2000, 1000]
for pecahan in pecahan_uang:
    jumlah=kembalian//pecahan
    print(f'{jumlah}, uang sejumlah Rp.{pecahan}')
    kembalian -= jumlah*pecahan

