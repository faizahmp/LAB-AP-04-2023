print('menghitung luas dan permukaan dan keliling segitiga')
x=float(input('panjang sisi x : '))
y=float(input('panjang sisi y : '))

# sisi_miring=(x**2+y**2)**0.5

print(f'\nLuas permukaan : {(1/2)*x*y:.2f}')
print(f'Keliling : {((x**2+y**2)**0.5)+x+y:.2f}')