print("Konversi Suhu dari celcius ke Reamur, Kelvin, dan Farenheit")
c = int(input("Masukkan Suhu = "))

#Rumus Konversi
K = c + 273
R = int(4/5 * c)
F = int(32+ (9/5 * c))

print(f"Konversi suhu {c} Celcius ke Kelvin = {K}K")
print(f"Konversi suhu {c} Celcius ke Reamur = {R}R")
print(f"Konversi suhu {c} Celcius ke Fahrenheit = {F}F")
