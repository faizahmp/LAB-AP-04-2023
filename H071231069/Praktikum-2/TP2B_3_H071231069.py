gol = input("Golongan = ")
daya = int(input("Daya = "))
p = int(input("Pemakaian = "))

ket = 'Jumlah tagihan anda sebesar : Rp. ' #dibuatkan variabel tersendiri biar titk di Rp itu tdk iku

if gol == "R1" :
    if daya == 900 :
        t = p * 1352
        print(ket + f"{t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    elif daya == 1300 :
        t = p * 1444.70
        print(ket + f"{t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    elif daya == 2200 :
        t = p * 1444.70
        print(ket + f"{t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    else :
        print("data tidak valid")
elif gol == "R2" :
    if daya >= 3500 and daya <= 5500 :
        t = p * 1699.53
        print(ket + f"{t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    else :
        print("data tidak valid")
elif gol == "R3" :
    if daya >= 6600 :
        t = p * 1699.53
        print(ket + f"{t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    else :
        print("data tidak valid")
elif gol == "B2" :
    if daya >= 6600 and daya <= 200000 :
        t = p * 1444.70
        print(ket + f"{t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    else :
        print("data tidak valid")
elif gol == "B3" :
    if daya >= 200000 :
        t = p * 1114.74
        print(ket + f"{t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    else :
        print("data tidak valid")
elif gol == "I3" :
    if daya >= 200000 :
        t = p * 1314.12
        print(ket + f"{t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    else :
        print("data tidak valid")
elif gol == "P1" :
    if daya >= 6600 and daya <= 200000 :
        t = p * 1523.28
        print(ket + f"{t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    else :
        print("data tidak valid")
else :
        print("data tidak valid")



