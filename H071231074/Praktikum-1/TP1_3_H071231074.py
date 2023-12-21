#Nomor 3
a = float(input("Masukkan nilai a: "))
if a == 0:
    print("a tidak boleh sama dengan 0")
else:
    b = float(input("Masukkan nilai b: "))
    c = float(input("Masukkan nilai c: "))

diskriminan = b**2 - 4*a*c
x1 = f"{(-b + (diskriminan**0.5))/(2*a):.2f}"
x2 = f"{(-b - (diskriminan**0.5))/(2*a):.2f}"

print(f"x1 = {x1}")
print(f"x2 = {x2}")