# Input detik dari pengguna
detik = int(input("Masukkan jumlah detik: "))
# Menghitung jam, menit, dan sisa detik
jam = detik // 3600
detik_sisa = detik % 3600
menit = detik_sisa // 60
detik_terakhir = detik_sisa % 60
# Membuat format output dengan 2 digit di setiap bagian waktu
format_waktu = f"{jam:02}:{menit:02}:{detik_terakhir:02}"
# Menampilkan hasil
print(f"Hasil: {format_waktu}")