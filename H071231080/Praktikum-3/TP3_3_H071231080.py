M = float(input())
while True:
    try:
        Detik = int(M * 240) # 1 derajat sama dengan 4 menit (240 detik)

        Jam = Detik // 3600 + 6
        if Jam >=  24:
            Jam = Jam % 24
        Menit = Detik % 3600 // 60
        r_Detik = Detik % 60

        if 6 <= Jam < 11:
            print('Selamat Pagi')
        elif 11 <= Jam < 15:
            print('Selamat Siang')
        elif 15 <= Jam < 18:
            print('Selamat Sore')
        else:
            print('Selamat Malam')

        print(f'{Jam:02}:{Menit:02}:{r_Detik:02}')
        M = float(input()) 

    except ValueError :
        print("End Of File")
        break