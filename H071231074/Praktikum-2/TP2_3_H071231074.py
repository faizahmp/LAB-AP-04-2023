#Meminta input
x = str(input("Golongan = "))
y = int(input("Daya = "))
z = int(input("Pemakaian = "))

#Variabel Rumus
if x == "R1" :
    if 0 < y <= 900 :
        hasil = z * 1352
    elif 901 < y <= 1300 :
        hasil = z * 1444.70
    elif 1301 < y <= 2200 :
        hasil = z * 1444.70
    else:
        print("Data Tidak Valid")
elif x == "R2" :
    if 3500 < y <= 5500 :
        hasil = z * 1699.53
    else:
        print("Data Tidak Valid")
elif x == "R3" :
    if 6600 < y :
        hasil = z * 1699.53
    else:
        print("Data Tidak Valid")
elif x == "B2" :
    if 6600 < y <= 200000 :
        hasil = z * 1444.70
    else:
        print("Data Tidak Valid")
elif x == "B3" :
    if y < 200000 :
        hasil = z * 1114.74
    else:
        print("Data Tidak Valid")
elif x == "I3" :
    if y < 200000 :
        hasil = z * 1314.12
    else:
        print("Data Tidak Valid")
elif x == "P1" :
    if 6600 < y <= 200000 :
        hasil = z * 1523.28
    else:
        print("Data Tidak Valid")
else:
    print("Data Tidak Valid")

formatted_hasil = f"{hasil:,.1f}".replace(",", "=").replace(".", ",").replace("=", ".")

print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {formatted_hasil}")