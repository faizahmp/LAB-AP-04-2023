def kata_polindrom(kata):
   kata = kata.lower()
   balik = kata[::-1]
   if kata == balik:
      return "Kata Polindrom"
   else:
      return "Bukan Kata Polindrom"

kata = input("Masukan Kata : ")
hasil = kata_polindrom(kata)
print(f"Kata {kata} Adalah {hasil}")