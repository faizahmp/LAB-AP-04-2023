#Nomor 4(Program untuk menentukan karakter dari inputan yang dilemparkan.)
print("Pengujian jenis Karakter")
print("--------------------------")
karakter = input("Karakter = ")

cek_hurufKapital = 'A' <= karakter <= 'Z'
print(f"Huruf kapital? {cek_hurufKapital}")
cek_hurufKecil = 'a' <= karakter <= 'z'
print(f"Huruf kecil? {cek_hurufKecil}")
cek_angka = '0' <= karakter <= '9'
print(f"Angka? {cek_angka}")