print('pengujian jenis karakter')
karakter=input('masukkan sebuah karakter: ')

HurufKapital = karakter >= 'A' and karakter <= 'Z'
HurufKecil = karakter >='a' and karakter <= 'z'
Angka = karakter >= '0' and karakter <= '9'

print(f'Huruf Kapital? {HurufKapital}')
print(f'Huruf Kecil? {HurufKecil}')
print(f'Angka? {Angka}')