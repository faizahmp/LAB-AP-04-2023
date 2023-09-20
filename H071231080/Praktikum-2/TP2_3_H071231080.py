g = input("Golongan = ")
d = int(input("Daya = "))
p = int(input("Pemakaian = "))

match g, d:
    case "R1", 900:
        t = p * 1352
        print(f"Jumlah Tagihan Anda : Rp, {t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R1", 1300:
        t = p * 1444.70
        print(f"Jumlah Tagihan Anda : Rp, {t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R1", 2200:
        t = p * 1444.70
        print(f"Jumlah Tagihan Anda : Rp, {t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R2", daya:
        if daya >=3500 and daya <=5500:
            t = p * 1699.53
            print(f"Jumlah Tagihan Anda : Rp, {t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R3", daya:
        if daya >=6600:
            t = p * 1699.53
            print(f"Jumlah Tagihan Anda : Rp, {t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "B2", daya:
        if daya >=6600 and daya <=200000:
            t = p * 1444.70
            print(f"Jumlah Tagihan Anda : Rp, {t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "B3", daya:
        if daya >200000:
            t = p * 1114.74
            print(f"Jumlah Tagihan Anda : Rp, {t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "I3", daya:
        if daya >=200000:
            t = p * 1314.12
            print(f"Jumlah Tagihan Anda : Rp, {t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "P1", daya:
        if daya >=66000 and daya <=20000:
            t = p * 1523.28
            print(f"Jumlah Tagihan Anda : Rp, {t:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case _:
        print("Data tidak valid")
