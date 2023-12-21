print('''Pilih Gender Anda
1. Pria
2. Wanita''')
pilihan = int(input('= '))
if pilihan != 1 and pilihan != 2: 
    print('gender invalid') 
    exit() 

Tinggi = float(input('Masukan tinggi badan(cm) : ')) 
Berat = float(input('masukkan berat badan(kg) : '))

Tinggi = Tinggi / 100 # Ubah tinggi dari cm ke m

BMI = Berat / Tinggi**2

if pilihan == 1:
    if  BMI < 18:
        print(f'Anda tergolong underweight dengan BMI {BMI:.2f}')
    elif 18 <= BMI < 24:
        print(f'Anda tergolong normal dengan BMI {BMI:.2f}')
    elif 24 <= BMI < 27:
        print(f'Anda tergolong overweight dengan BMI {BMI:.2f}')
    else:
        print(f'Anda tergolong obese dengan BMI {BMI:.2f}')
elif pilihan == 2:
    if BMI < 17:
        print(f'Anda tergolong underweight dengan BMI {BMI:.2f}')
    elif 17 <= BMI < 23.9:
        print(f'Anda tergolong normal dengan BMI {BMI:.2f}')
    elif 24 <= BMI < 28:
        print(f'Anda tergolong overweight dengan BMI {BMI:.2f}')
    else:
        print(f'Anda tergolong obese dengan BMI {BMI:.2f}')
