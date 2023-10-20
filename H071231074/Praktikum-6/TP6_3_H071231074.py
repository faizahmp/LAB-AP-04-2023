input_angka = input("Masukkan beberapa angka: ").split()

angka_ganjil = []
angka_genap = []
angka_bagi_5 = []

for angka in input_angka:
    angka = int(angka)
    if angka % 2 == 0:
        angka_genap.append(angka)
    else:
        angka_ganjil.append(angka)
    if angka % 5 == 0:
        angka_bagi_5.append(angka)

print(f"Angka Genap: {angka_genap}\nAngka Ganjil: {angka_ganjil}\nAngka yang habis dibagi 5: {angka_bagi_5}" )