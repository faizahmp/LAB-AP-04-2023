def anagram(word1, word2):
    # Menghapus spasi putih dan mengubah huruf menjadi huruf kecil
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    if len(word1) != len(word2): # Memeriksa panjang kata pertama dan kedua
        return False

    # Menghitung frekuensi masing-masing karakter dalam kedua kata
    char_count1 = {}
    char_count2 = {}

    for char in word1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in word2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    return char_count1 == char_count2 # Membandingkan frekuensi karakter dalam kedua kata

# Input kata pertama
word1 = input("Masukkan kata pertama: ")

# Input kata kedua
word2 = input("Masukkan kata kedua: ")

# Memeriksa apakah kata-kata tersebut adalah anagram
result = anagram(word1, word2)

# Cetak hasil
if result:
    print("True")
else:
    print("false")
