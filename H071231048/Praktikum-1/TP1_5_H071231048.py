detik = int(input('masukkan jam = '))

jam_output = detik/3600
menit_output = (detik - int(jam_output)*3600)/60
detik_output = menit_output*60 - int(menit_output)*60

print(f'{int(jam_output):02d}:{int(menit_output):02d}:{int(detik_output):02d}')