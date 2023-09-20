# Menerima tiga inputan string
input_pertama = input("Masukkan Input Pertama : ")
input_kedua = input("Masukkan Input Kedua : ")
input_ketiga = input("Masukkan Input Ketiga : ")
# Menampilkan hashasilil atau pesan "Invalid input"
def main_case(input_pertama, input_kedua, input_ketiga):
    # Membuat kamus (dictionary) yang berisi informasi sesuai dengan pola yang diberikan
    pola = {
        ("vertebrado", "ave", "carnivoro"): "aguia",
        ("vertebrado", "ave", "onivoro"): "pomba",
        ("vertebrado", "mamifero", "onivoro"): "homem",
        ("vertebrado", "mamifero", "herbivoro"): "vaca",
        ("invertebrado", "inseto", "hematofago"): "pulga",
        ("invertebrado", "inseto", "herbivoro"): "lagarta",
        ("invertebrado", "anelideo", "hematofago"): "sanguessuga",
        ("invertebrado", "anelideo", "onivoro"): "minhoca"
    }

    # Menggunakan tuple input sebagai kunci untuk mencari hasil
    kunci = (input_pertama, input_kedua, input_ketiga)
    if kunci in pola:
        return pola[kunci]
    else:
        return "Invalid input"
# Memanggil main_case untuk mendapatkan hasil
hasil = main_case(input_pertama, input_kedua, input_ketiga)
# Menampilkan hasil atau pesan "Invalid input"
print(hasil)