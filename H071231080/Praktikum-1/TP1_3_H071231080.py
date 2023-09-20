print("bentuk persamaan kuadrat  : ax**2 + bx + c")

a = float(input("Masukkan nilai a (a = 0): "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

# menghitung diskriminan
D = b**2 - 4*a*c

x1 = (-b + (D)**0.5) / 2*a
x2 = (-b - (D)**0.5) / 2*a
print(f'x1 = {x1 : .2f}')
print(f'x2 = {x2 : .2f}')