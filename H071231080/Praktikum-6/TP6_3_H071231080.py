angka = input("Masukkan beberapa angka: ").split()

genap, ganjil, habisbagilima = [], [], [] #List

for item in angka:
    i = int(item)  # Mengonversi elemen input ke integer
    if i % 2 == 0:
        genap.append(i)
    elif i % 2 == 1:
        ganjil.append(i)
    if i % 5 == 0:
        habisbagilima.append(i)

print(f"Angka genap: {genap}\nAngka ganjil: {ganjil}\nAngka yang habis dibagi 5: {habisbagilima}")