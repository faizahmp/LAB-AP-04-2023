s1 = input("Masukkan s1: ")
s2 = input("Masukkan s2: ")[::-1]
hasil = ""
i = 0
while i < len(s1) and i < len(s2):
    hasil += s1[i] + s2[i]
    i += 1
hasil += s1[i:] + s2[i:]
print(hasil)