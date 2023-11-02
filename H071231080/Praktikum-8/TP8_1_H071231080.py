import re

Karakter = input()
if len(Karakter) == 45:
    pola = r'^[A-Za-z02468]{40}[13579\s]{5}$' 
    kata = re.search(pola, Karakter) 
    if kata:
        print("True")
    else:
        print("False")
else:
    print("Panjang karakter harus 45!")
