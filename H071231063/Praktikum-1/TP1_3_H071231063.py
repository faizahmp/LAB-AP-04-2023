# Menerima inputan a, b, dan c dari pengguna dengan dua angka di belakang koma
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
# Menghitung diskriminan
discriminant = b**2 - 4*a*c
    # Menentukan jenis solusi berdasarkan diskriminan
if discriminant > 0:
      x1 = (-b + (discriminant ** 0.5)) / (2*a)
      x2 = (-b - (discriminant ** 0.5)) / (2*a)
      print(f"Akar pertama (x1): {x1:.2f}")
      print(f"Akar kedua (x2): {x2:.2f}")
