n = int(input("Masukkan nilai N : "))
if n <= 0:
    print("Bukan fibonacci!") #Syarat Bilangan Fibonacci tidak mines atau 0!
else:
    s1 = 0 #Suku pertama bilangan fibonacci
    s2 = 1 #Suku kedua bilangan fibonacci
    print(s1, s2, end=" ") #Fungsi End yaitu agar outputnya terus ke kanan bukan membuat line baru
    for i in range(n-2): #Perulangan dari index ke 2 sampai ke n
        s3 = s1 + s2    #Penentuan suku ke 3 yaitu penjumlahan dua suku sebelumnya
        s1, s2 = s2, s3 #Otomatis dua suku sebelumnya berubah menjadi seperti ini
        print(s3, end=" ")

["Bilangan fibonacci adalah bilangan yang suku berikutnya ditentukan"]
["dari penjumlahan dua suku sebelumnya"]