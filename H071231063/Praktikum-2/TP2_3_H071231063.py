# Input golongan, daya, dan pemakaian
golongan = input("Golongan = ").upper()
daya = int(input("Daya = "))
pemakaian = int(input("Pemakaian = "))
tarif_per_kwh = 0
# Aturan tarif yang diberikan
if golongan == "R1":
    if daya == 900:
        tarif_per_kwh = 1352
    elif daya == 1300 or daya == 2200:
        tarif_per_kwh = 1444.70
elif golongan == "R2":
    if 3500 <= daya <= 5500:
        tarif_per_kwh = 1699.53
elif golongan == "R3":
    if daya >= 6600:
        tarif_per_kwh = 1444.70
elif golongan == "B2":
    if 6600 <= daya <= 200000:
        tarif_per_kwh = 1444.70
elif golongan == "B3":
    if daya >= 200000:
        tarif_per_kwh = 1114.74
elif golongan == "I3":
    if daya >= 200000:
        tarif_per_kwh = 1314.12
elif golongan == "P1":
    if daya >= 6600:
        tarif_per_kwh = 1523.28
#Hitung total tagihan
if tarif_per_kwh > 0:
    pemakaian_kwh = pemakaian / 1000
    tagihan = (pemakaian_kwh * tarif_per_kwh)
    print(f"Jumlah tagihan anda sebesar: Rp. {tagihan}")
else:
    print("Data tidak valid")