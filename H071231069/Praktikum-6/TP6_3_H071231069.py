Angka = map(int, input("Masukkan Beberapa Angka :").split(" "))

Angka_Ganjil = []
Angka_Genap = []
Angka_yang_habis_dibagi_5 = []

for i in Angka :
    if i % 2 == 0:
       Angka_Genap.append(i)
    else :
        Angka_Ganjil.append(i)

    if i % 5 == 0:
        Angka_yang_habis_dibagi_5.append(i)

print(f"Angka Genap :{Angka_Genap}")
print(f"Angka Ganjil :{Angka_Ganjil}")
print(f"Angka yang habis dibagi 5 :{Angka_yang_habis_dibagi_5}")


