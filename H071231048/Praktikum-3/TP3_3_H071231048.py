print(f"{'PROGRAM MENGUBAH DERAJAT KE DALAM':^40}")
print(f"{'SATUAN JAM':^40}")
print(f"{'_'*40:^40}")


while True:
    try:
        posisi = float(input())
     
        detik = (posisi / 360) * 24 * 3600
        jam = (detik // 3600) + 6 #ditambah 6 karena 0 derajat pada jam 6
        if jam >= 24:
            jam %= 24 #jika melebihi jam 24:00:00 akan mulai lagi jam 00:00:00
        detik = detik % 3600
        menit = detik // 60
        detik = detik % 60

        if 6 <= jam <= 10 :
            print('\nSelamat Pagi')
        elif 11 <= jam < 15:
            print('\nSelamat Siang')
        elif 15 <= jam < 18:
            print('\nSelamat Sore')
        elif 18 <= jam < 24 or 0 <= jam < 6:
            print('\nSelamat Malam') 

        print(f'{jam:02.0f}:{menit:02.0f}:{detik:02.0f}\n')

    except ValueError:
        print('EOF')
        break