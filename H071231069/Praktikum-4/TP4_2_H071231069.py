def palindrom(word: str) -> str:
    # Menghilangkan spasi dan mengubah huruf menjadi huruf kecil agar tidak terpengaruh dngn penentuan
    word = word.replace(" ", "").lower()
    
    # Memeriksa apakah kata adalah palindrom
    if word == word[::-1]: #AKAN MEMBACA DARI BELAKANG KE DEPAN
        return "Palindrom"
    else:
        return "Bukan Palindrom"

word = input("Masukkan kata : ")
print(palindrom(word)) 



