def maksimum(daftar_angka):
    if not daftar_angka:
        return None
    max_angka = daftar_angka[0]
    for angka in daftar_angka:
        if angka > max_angka:
            max_angka = angka 
    return max_angka
test_case =input()
angka_list = [int(angka) for angka in test_case.split()]
result = maksimum(angka_list) 
print(">>", result)