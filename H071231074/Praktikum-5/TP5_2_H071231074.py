def string_baru(input_string):
    # Periksa apakah panjang string input cukup panjang
    if len(input_string) < 3:
        print("Input terlalu pendek, minimal 3 karakter diperlukan.")
        exit()

    # Ambil karakter pertama, tengah, dan terakhir dari string input
    karakter_pertama = input_string[0]
    karakter_tengah = input_string[len(input_string) // 2]
    karakter_akhir = input_string[-1]

    print(karakter_pertama + karakter_tengah + karakter_akhir)

# Input
input_string = input("Masukkan kata: ")

# Pemanggilan Fungsi
string_baru(input_string)