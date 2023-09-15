# Input suhu dalam skala Celcius
celsius = float(input("Masukkan suhu dalam Celcius: "))

kelvin = int(celsius + 273.15)
reamur = int(celsius * 0.8)
fahrenheit = int((celsius * 9/5) + 32)
# Menampilkan hasil konversi dalam format string yang sesuai
output_kelvin = f"{kelvin}K"
output_reamur = f"{reamur}R"
output_fahrenheit = f"{fahrenheit}F"

print(f"Suhu dalam Kelvin: {output_kelvin}")
print(f"Suhu dalam Reamur: {output_reamur}")
print(f"Suhu dalam Fahrenheit: {output_fahrenheit}")