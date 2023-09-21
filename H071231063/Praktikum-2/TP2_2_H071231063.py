# Menerima tiga inputan string
input_pertama = input("Masukkan Input Pertama : ")
input_kedua = input("Masukkan Input Kedua : ")
input_ketiga = input("Masukkan Input Ketiga : ")
# Menampilkan hasil atau pesan "Invalid input"
match (input_pertama, input_kedua, input_ketiga):
    case "vertebrado", "ave", "carnivoro": 
        print("aguia")
    case "vertebrado", "ave", "onivoro":
        print("pomba")
    case "vertebrado", "mamifero", "onivoro":
        print("homem")
    case "vertebrado", "mamifero", "herbivoro": 
       print("vaca")
    case "invertebrado", "inseto", "hematofago":
        print("pulga")
    case "invertebrado", "inseto", "herbivoro":
        print("lagarta")
    case "invertebrado", "anelideo", "hematofago":
        print("sanguessuga")
    case "invertebrado", "anelideo", "onivoro":
        print("minhoca")
    case _:
        print('invalid')