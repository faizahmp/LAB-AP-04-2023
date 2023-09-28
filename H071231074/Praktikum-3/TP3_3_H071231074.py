# Input sudut matahari/bulan
while True:
    try:
        derajat = float(input())
    except EOFError:
        break

    # Mengonversi sudut menjadi waktu
    total_menit = derajat * 4 # Karena 360 derajat = 24 jam
    jam = int(total_menit // 60)
    if jam >= 24:
        jam %= 24
    menit = int(total_menit % 60)
    detik = int((total_menit - int(total_menit)) * 60)

    # Menentukan salam berdasarkan waktu
    if 0 <= derajat < 90:
        salam = "Selamat Pagi"
    elif 90 <= derajat < 180:
        salam = "Selamat Siang"
    elif 180 <= derajat < 270:
        salam = "Selamat Sore"
    else:
        salam = "Selamat Malam"

    # Mencetak salam dan waktu dalam format HH:MM:SS
    print(salam)
    print(f"{jam+6:02d}:{menit:02d}:{detik:02d}")

