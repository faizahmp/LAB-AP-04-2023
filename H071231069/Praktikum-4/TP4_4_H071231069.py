def catAndMouse(catA, catB, mosC):
    A = abs(catB - mosC)
    B = abs(catA - mosC)
    # abs merupkn nilai absoluted berguna untuk mengubah nilai negatif menajdi positif
    
    if A > B:
        return "Cat A"
    elif B > A:
        return "Cat B"
    else:
        return "Mouse C"

catA = int(input("catA= "))
catB = int(input("catB= "))
mosC = int(input("mosC= "))
print(catAndMouse(catA, catB,mosC)) 

# # Test Case 1
# result1 = catAndMouse(catA=16, catB=24, mosC=15)
# print(result1)

# # Test Case 2
# result2 = catAndMouse(catA=20, catB=10, mosC=15)
# print(result2) 
