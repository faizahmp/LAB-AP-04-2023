def maksimum(*args): # menerima sbuar argumen guna mencari nilai maksimum argumen tersebt
    max = args[0]
    for angka_terbesar in args:
        if angka_terbesar > max:
            max = angka_terbesar

    return max #mengembalikan nilai max

result = map(int, input('Masukkan angka = ').split(','))
print(maksimum(*result))
  
