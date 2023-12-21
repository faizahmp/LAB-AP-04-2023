print('Pilih Gender Anda \n1.Pria \n2.Wanita')

gender = float(input('= '))
if gender!=1 and gender!=2:
    print('Harap memilih pilihan 1 atau 2')
    exit()
else:
    tinggi = float(input('Masukkan tinggi badan (cm) : '))
    berat = float(input('Masukkan berat badan (kg) : '))

bmi = berat/((tinggi/100)**2)

if gender==1: 
    if bmi<18:
        print('Anda tergolong Underweight dengan BMI {:.2f}'.format(bmi))
    elif bmi>=18 and bmi<23.9:
        print('Anda tergolong Normal dengan BMI {:.2f}'.format(bmi))
    elif bmi>=24 and bmi<26.9:
        print('Anda tergolong Overweight dengan BMI {:.2f}'.format(bmi))
    else:
        print('Anda tergolong Obese dengan BMI {:.2f}'.format(bmi))

elif gender==2:
    if bmi<17:
        print('Anda tergolong Underweight dengan BMI {:.2f}'.format(bmi))
    elif bmi>=17 and bmi<23.9:
        print('Anda tergolong Normal dengan BMI {:.2f}'.format(bmi))
    elif 24<= bmi <27.9:
        print('Anda tergolong Overweight dengan BMI {:.2f}'.format(bmi))
    else:
        print('Anda tergolong Obese dengan BMI {:.2f}'.format(bmi))