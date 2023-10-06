def maksimum(*args):
    if len(args) == 0:
        return None  # Mengembalikan None jika daftar kosong

    max_num = args[0]  # Membuat variabel max_num dengan nilai pertama

    for num in args:
        if num > max_num:
            max_num = num

    return max_num

# Test Case 1
maksimum(1, 2, 4, 6, 9, 3, 1, 9, 10)

# Test Case 2
maksimum(0, 1, 90, 430, 23, 212, 34)

# Test Case 3
user_input = input("Masukkan daftar angka (pisahkan dengan spasi): ")
angka_list = [int(angka) for angka in user_input.split()]
maksimum(*angka_list)
maksimum()