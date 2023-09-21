#Nomor1()
#Menentukan Gender
print("Pilih Gender Anda")
print("1. Pria")
print("2. Wanita")
jenis_kelamin = int(input("= "))

#Input TB (cm) & BB (kg)
tb = float(input("Masukkan tinggi badan (cm) : "))
bb = float(input("Masukkan berat badan (kg) : "))

#Menghitung BMI
bmi = round(bb / ((tb/100)**2), 2)

#Hasil berdasarkan Jenis Kelamin
if jenis_kelamin == 1:
    if bmi < 18:
        print(f"Anda tergolong Underweight dengan BMI {bmi}")
    elif bmi <= 23.9:
        print(f"Anda tergolong Normal dengan BMI {bmi}")
    elif bmi <= 26.9:
        print(f"Anda tergolong Overweight dengan BMI {bmi}")
    else:
        print(f"Anda tergolong Obese dengan BMI {bmi}")
elif jenis_kelamin == 2:
    if bmi < 17:
        print(f"Anda tergolong Underweight dengan BMI {bmi}")
    elif bmi <= 23.9:
        print(f"Anda tergolong Normal dengan BMI {bmi}")
    elif bmi <= 27.9:
        print(f"Anda tergolong Overweight dengan BMI {bmi}")
    else:
        print(f"Anda tergolong Obese dengan BMI {bmi}")
else:
    print("Harap Masukkan Jenis Kelamin anda dengan benar!!!")
