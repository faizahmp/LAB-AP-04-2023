
def campuran(s1, s2):
    s2 = s2[::-1]
    s3 = ""
    min_len = min(len(s1), len(s2)) # untuk mengambil panjang terkecil dari s1 dan s2
    
    for i in range(min_len):
        s3 += s1[i] + s2[i] 
    
    s3 += s1[min_len:] + s2[min_len:] 
    return s3

s1 = input ("masukkan kata pertama = ")
s2 = input ("masukkan kata kedua = ")
result = campuran(s1, s2)
print(f'Hasil Mixed = "{result}"')

