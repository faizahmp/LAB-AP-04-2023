def CatAndMouse(CatA, CatB, MouseC):
    a = abs(CatA - MouseC)
    b = abs(CatB - MouseC)
    if a > b:
        return "Cat B"
    elif a < b:
        return"Cat A"
    elif a == b:
        return "Mouse C"
    
CatA = int(input("Masukkan posisi Cat A: "))
CatB = int(input("Masukkan posisi Cat B: "))
MouseC = int(input("Masukkan posisi MouseC: "))

hasil = CatAndMouse(CatA, CatB, MouseC)
print(hasil)