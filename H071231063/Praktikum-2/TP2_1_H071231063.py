# Input jenis kelamin
print("Pilih Gender Anda")
print("1. Pria")
print("2. Wanita")
jenis_gender= int(input("= "))
# Memasukkan tinggi badan dan berat badan
tinggi_badan_cm = float(input("Masukkan tinggi badan (cm) : "))
berat_badan_kg = float(input("Masukkan berat badan (kg) : "))
# Menghitung BMI
tinggi_badan_m = tinggi_badan_cm / 100
bmi = berat_badan_kg / (tinggi_badan_m ** 2)
# Menentukan kategori BMI berdasarkan jenis kelamin
kategori = ""
if jenis_gender == 1:  # Pria
    if bmi < 18:
        kategori = "Underweight"
    elif 18 <= bmi <= 23.9:
        kategori = "Normal"
    elif 24 <= bmi <= 26.9:
        kategori = "Overweight"
    else:
        kategori = "Obesitas"
elif jenis_gender == 2:  # Wanita
    if bmi < 17:
        kategori = "Underweight"
    elif 17 <= bmi <= 23.9:
        kategori = "Normal"
    elif 24 <= bmi <= 27.9:
        kategori = "Overweight"
    else:
        kategori = "Obesitas"
# Menampilkan hasil
print(f"Anda tergolong {kategori} dengan BMI {bmi:.2f}")