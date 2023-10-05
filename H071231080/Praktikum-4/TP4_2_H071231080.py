def palindrom(kata: str)-> str:
    kata = kata.lower().replace(" ", "")#mengubah kapital , menghapus spasi
    
    if kata == kata [::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
    
kata = input(str("Masukkan Kata = "))
print(palindrom(kata))