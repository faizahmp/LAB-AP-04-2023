def catAndMouse(catA, catB, mosC):
    jarak_catA = abs(mosC - catA)
    jarak_catB = abs(mosC - catB)

    if jarak_catA < jarak_catB:
        print("Cat A")
    elif jarak_catA > jarak_catB:
        print("Cat B")
    else:
        print("Mouse C")
    
# Test Case 1
catAndMouse(catA=16, catB=24, mosC=15)

# Test Case 2
catAndMouse(catA=20, catB=10, mosC=15)

# Test Case 3
catA = int(input("catA: "))
catB = int(input("catB: "))
mosC = int(input("mosC: "))
catAndMouse(catA, catB, mosC)