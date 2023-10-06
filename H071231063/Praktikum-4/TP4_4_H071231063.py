def catAndMouse(catA, catB, mouseC):
    jarakA = abs(catA - mouseC)
    jarakB = abs(catB - mouseC)
    if jarakA < jarakB:
        return "Cat A"
    elif jarakB < jarakA:
        return "Cat B"
    else:
        return "Mouse C"
catA = int(input())
catB = int(input())
mouseC = int(input())
result = catAndMouse(catA, catB, mouseC)
print(result)