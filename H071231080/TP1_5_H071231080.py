detik = int(input("Masukkan jumlah detik: "))

jam =  detik // 3600
print(jam)
sisa_detik = detik % 3600
print(sisa_detik)
menit = sisa_detik // 60
print(menit)
detik = sisa_detik % 60
print(detik)
print(f"Format jam:menit:detik = {jam:02d}:{menit:02d}:{detik:02d}")