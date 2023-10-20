Font = input("Masukkan karakter: ")
huruf_kapital = False
huruf_kecil = False
angka = False
# for karakter in Font:
#     if ord('A') <= ord(karakter) <= ord('Z'):
#         huruf_kapital = True
#     elif ord('a') <= ord(karakter) <= ord('z'):
#         huruf_kecil = True
#     elif ord('0') <= ord(karakter) <= ord('9'):
#         angka = True


if ord('A') <= ord(Font) <= ord('Z'):
    huruf_kapital = True
elif ord('a') <= ord(Font) <= ord('z'):
    huruf_kecil = True
elif ord('0') <= ord(Font) <= ord('9'):
    angka = True

print("Huruf kapital?", huruf_kapital)
print("Huruf kecil?", huruf_kecil)
print("Angka?", angka)