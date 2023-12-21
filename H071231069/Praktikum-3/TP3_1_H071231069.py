n = int(input("Masukkan nilai n : ")) #N = Berapa banyak suku yang ingin ditentukan
if n < 0 : #Bilangan fibonacci tidak bisa bernilai mines atau 0
    print("Bukan bilangan fibonacci") #karena fibonaci nda boleh mines dan < 0
elif n == 1:
    print(0)
else :
    u1 = 0
    u2 = 1
    print(u1, u2, end=" ") #fungsi end itu agar outputnya tidak membuat baris baru, namun kekanan terus menerus   
    for i in range(1, n-1): 
        u3 = u1 + u2
        u1, u2 = u2, u3
        print(u3, end=" ")
