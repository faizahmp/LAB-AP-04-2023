kata = input("Masukkan kata: ")
kata = kata.replace(" ", "")
def ATH(karakter):
    panjang = len(karakter)
    if panjang < 3:
        return "String input terlalu pendek."

    awal = karakter[0]
    tengah = karakter[panjang // 2]
    akhir = karakter[-1]
    hasil = f"{awal}{tengah}{akhir}"

    return hasil

hasil_string = ATH(kata)
print("String baru:", hasil_string)