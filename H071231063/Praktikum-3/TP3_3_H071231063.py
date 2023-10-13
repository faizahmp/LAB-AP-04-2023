while True:
    try:
        derajat = float(input())
        detik = int((derajat/360) * 24 * 3600)
        jam = (detik // 3600)+6
        if jam >= 24:
            jam= jam % 24
        detik = detik % 3600
        menit = detik // 60
        detik = detik % 60
        waktu_asli = "{:02d}:{:02d}:{:02d}".format(jam, menit, detik)
        if 0 <= jam <= 11:
            print("Selamat Pagi")
        elif 12 <= jam <= 14:
            print("Selamat Siang")
        elif 15 <= jam <= 18:
            print("Selamat Sore")
        else:
            print("Selamat Malam")
        print(waktu_asli)
    except EOFError:
        pass