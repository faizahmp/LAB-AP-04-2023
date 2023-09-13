a = float (input("masukkan nilai a ="))
b = float (input("masukkan nilai b ="))
c = float (input("masukkan nilai c ="))
if a != 0 : 
    x1 = (-b +(b**2 - 4*a*c)**(1/2)) / (2*a)
    x2 = (-b -(b**2 - 4*a*c)**(1/2)) / (2*a)

    print (f'x1 = {x1:.2f}')
    print (f'x2 = {x2:.2f}')
  
else : 
    print ("nilai a tidal boleh sama dengan 0")


    