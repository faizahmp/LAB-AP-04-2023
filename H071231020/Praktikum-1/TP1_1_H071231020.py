# hitung luas dan keliling segitiga 
# X = tinggi segitiga 
# Y = alasa segitiga
# z = sisi miring 
print ("menghitung luas permukaan dan keliling segitiga XYZ")
X = int (input ("panjang sisi X : "))
Y = int (input ("panjang sisi Y : "))
Z = ((X**2) + (Y**2))**0.5 #rumus mencari sisi miring

luas_permukaan = 1/2 * Y * X
keliling = X  + Y + Z

print(f"luas permukaan segitiga XYZ adalah {luas_permukaan:.2f} ")
print(f"keliling segitiga XYZ adalah {keliling:.2f} ")
