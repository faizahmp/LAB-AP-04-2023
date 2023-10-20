# Mengambil input panjang sisi X dan Y
x = float(input("Masukkan panjang sisi X: "))
y = float(input("Masukkan panjang sisi Y: "))
# Mencari panjang sisi Z menggunakan rumus Pythagoras
z = (x**2 + y**2)**0.5
# Menghitung luas segitiga 
luas = (x*y)/2
# Menghitung keliling segitiga
keliling = x + y + z
# print(f"Panjang sisi Z: {z:.2f}")
print(f"Luas permukaan: {luas:.2f}")
print(f"Keliling: {keliling:.2f}")