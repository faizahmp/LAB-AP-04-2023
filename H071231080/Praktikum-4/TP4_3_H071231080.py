def maksimum_angka (*angka):
    angka_terbesar = int(angka[0])

    for i in angka:
        if int(i) > angka_terbesar:
            angka_terbesar = int(i)
    
    return angka_terbesar

angka_string = input("Masukkan Angka = ").split() 
daftarAngka = maksimum_angka(*angka_string)
print(f">> {daftarAngka}")