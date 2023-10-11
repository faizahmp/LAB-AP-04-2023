def cek_palindrom(kata):

    kata = kata.lower()
    kata_dibalik = kata[::-1]
     
    if kata == kata_dibalik:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
    
kata = input("Masukkan kata: ")
print(cek_palindrom(kata)) 


