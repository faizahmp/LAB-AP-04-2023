#Nomor 1(Membuat program yang menghitung luas dan keliling segitiga XYZ)
print("Menghitung luas permukaan dan keliling segitiga")
x = int(input("Panjang sisi X (Sebagai Tinggi) = " ))
y = int(input("Panjang sisi y (Sebagai Alas) = " ))
z = (x**2 + y**2)**0.5
luas = 0.5 * x * y
keliling = x + y + z

print(f"Luas Permukaan : {luas:.2f}")
print(f"Keliling : {keliling:.2f}")

