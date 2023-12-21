suhu_celcius = int(input("Masukkan suhu dalam celcius: "))

suhu_kelvin = suhu_celcius + 273.15
suhu_reamur = (4/5) * suhu_celcius
suhu_fahrenheit = (suhu_celcius * 9/5) + 32

hasil_kelvin = (int(suhu_kelvin))
hasil_reamur = (int(suhu_reamur))
hasil_fahrenheit = (int(suhu_fahrenheit))

print(f"hasil konversi dari suhu {suhu_celcius} derajat celcius ke kelvin adalah: {hasil_kelvin}K")
print(f"hasil konversi dari suhu {suhu_celcius} derajat celcius ke reamur adalah: {hasil_reamur}R")
print(f"hasil konversi dari suhu {suhu_celcius} derajat celcius ke fahrenheit adalah: {hasil_fahrenheit}F")