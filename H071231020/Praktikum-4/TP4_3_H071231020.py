def angka_terbesar(*daftar_angka):
    angka_terbesar = daftar_angka[0]
    for angka in daftar_angka:
        if angka > angka_terbesar:
            angka_terbesar = angka
    return angka_terbesar

print("\nUji")
while True:
    daftar_angka = int(input("Jumlah item = "))                                       
    nums = []
    for i in range(daftar_angka):
        y = int(input("Angka = "))
        nums.append(y)
                                                                                                      
    print(f'angka terbesar adalah {angka_terbesar(*nums)}')
    break  