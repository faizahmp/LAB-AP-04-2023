def anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    if len(kata1) != len(kata2):
        return False
    
    simpan1 = {}
    simpan2 = {}

    # Menghitung jumlah kemunculan kata dalam kata1
    for kata in kata1:
        if kata in simpan1:
            simpan1[kata] += 1
        else:
            simpan1[kata] = 1
    

    # Menghitung jumlah kemunculan kata dalam kata2
    for kata in kata2:
        if kata in simpan2:
            simpan2[kata] += 1
        else:
            simpan2[kata] = 1

    return simpan1 == simpan2

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
print(anagram(kata1,kata2))
