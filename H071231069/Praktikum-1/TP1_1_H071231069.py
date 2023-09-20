x = float(input("Panjang sisi X : "))
y = float(input("Panjang sisi Y : "))

luas = x * y / 2
#menggunakan rumus teorema phytagoras
z = (x ** 2 + y ** 2) ** 0.5

keliling = x + y + z

print(f"Luas Permukaan : {luas:.2f}")
print(f"Keliling : {keliling:.2f}")
