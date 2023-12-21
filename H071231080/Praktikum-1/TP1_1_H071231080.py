x = float(input("Masukkan panjang sisi x: "))
y = float(input("Masukkan panjang sisi y: "))
z = (x**2 + y**2)**0.5

luas = 0.5 * x * y
keliling = x + y + z

print(f"luas segitiga XYZ: {luas: .2f}")
print(f"keliling segitigA XYZ: {keliling: .2f}")