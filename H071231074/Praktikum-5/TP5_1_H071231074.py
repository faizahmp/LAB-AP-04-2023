def fungsi_string(s1, s2):
    i, j = 0, len(s2) - 1
    campur = []

    while i < len(s1) or j >= 0:
        if i < len(s1):
            campur.append(s1[i])
            i += 1
        if j >= 0:
            campur.append(s2[j])
            j -= 1

    result = ''.join(campur)
    print("Hasil mixed =", result)

# Input
print("Masukkan string pertama: ")
s1 = input("s1 = ")
print("Masukkan string kedua: ")
s2 = input("s2 = ")

# Panggil fungsi untuk membuat string campuran
fungsi_string(s1, s2)