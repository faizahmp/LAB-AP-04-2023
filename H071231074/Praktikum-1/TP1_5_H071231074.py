#Nomor 5(Program yang merubah detik ke dalam format jam:menit:detik)
print("Konversi detik ke jam")
detik = int(input("Masukkan jumlah detik = "))

jam = detik//3600
detik %= 3600
menit = detik//60
detik %= 60

print(f"{jam:02}:{menit:02}:{detik:02}")