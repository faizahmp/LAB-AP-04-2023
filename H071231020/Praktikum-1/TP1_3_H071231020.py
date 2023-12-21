#Tugas 3 Persamaan Kuadrat
a = float(input("Input a = "))
if a == 0:
    print("Input a tidak boleh 0!")
    exit()
b = float(input("Input b = "))
c = float(input("Input C = "))

#Rumus Persamaan Kuadrat
x1 =(- b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 =(- b - (b**2 - 4*a*c)**0.5)/(2*a)

print(f'x1= {x1: .2f}')
print(f'x2= {x2: .2f}')