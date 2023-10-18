angka1 = map(int, input("Masukkan array ke-1: ").split())  # Membagi input berdasarkan spasi atau karakter pemisah lainnya
angka2 = map(int, input("Masukkan array ke-2: ").split())  # Membagi input berdasarkan spasi atau karakter pemisah lainnya

hasil = tuple(set(angka1) & set(angka2)) #kumpulan data yang tdk bisa diubah IRISAN Opertor set & (interection)
panjang = len(hasil)
if hasil : 
    print(f"Terdapat {panjang} buah duplikat, yaitu {hasil}")
else:
    print("Tidak ada duplikasi ditemukan")
