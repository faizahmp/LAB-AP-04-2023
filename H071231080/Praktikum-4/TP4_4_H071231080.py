# def CatAndMouse(CatA, CatB, MouseC):
#     a = abs(CatA - MouseC)
#     b = abs(CatB - MouseC)
#     if a > b:
#         return "Cat B"
#     elif a < b:
#         return"Cat A"
#     elif a == b:
#         return "Mouse C"
    
# CatA = int(input("Masukkan posisi Cat A: "))
# CatB = int(input("Masukkan posisi Cat B: "))
# MouseC = int(input("Masukkan posisi MouseC: "))

# hasil = CatAndMouse(CatA, CatB, MouseC)
# print(hasil)

def maksimum(*args):
    if not args:
        return None  # Mengembalikan None jika tidak ada argumen yang diberikan

    max_num = args[0]  # Menggunakan elemen pertama sebagai angka terbesar awalnya

    for num in args:
        if num > max_num:
            max_num = num  # Memperbarui angka terbesar jika ditemukan angka yang lebih besar

    return max_num

# Test case 1
result1 = maksimum(1, 2, 4, 6, 9, 3, 1, 9, 10)
print(result1)  # Output: 10

# Test case 2
result2 = maksimum(0, 1, 90, 430, 23, 212, 34)
print(result2)  # Output: 430
