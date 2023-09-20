suhu_celcius = int(input("Masukkan Suhu dalam Celcius : "))

suhu_kelvin = suhu_celcius + 273

suhu_reamur = (4/5 * suhu_celcius)

suhu_fahrenheit = (suhu_celcius * 9//5) + 32

print(f"Hasil Konversi dari suhu {suhu_celcius} derajat Celcius ke Kelvin adalah : {suhu_kelvin}K")
print(f"Hasil Konversi dari suhu {suhu_celcius} derajat Celcius ke Reamur adalah : {suhu_reamur}R")
print(f"Hasil Konversi dari suhu {suhu_celcius} derajat Celcius ke Fahrenheit adalah : {suhu_fahrenheit}F")