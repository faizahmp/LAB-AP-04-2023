def kategori_angka(input_angka):
    list_angka = list(map(int, input_angka.split()))

    ganjil = []
    genap = []
    habis_dibagi_5 = []

    for i in list_angka:
        if i % 2 == 1:
            ganjil.append(i)
        elif i % 2 == 0:
            genap.append(i)
        if i % 5 == 0:
            habis_dibagi_5.append(i)

    return ganjil, genap, habis_dibagi_5

input_angka = input("Masukkan beberapa angka: ")

ganjil, genap, habis_dibagi_5 = kategori_angka(input_angka)

print("Angka yang habis dibagi 5:", habis_dibagi_5)
print("Angka genap:", genap)
print("Angka ganjil:", ganjil)


