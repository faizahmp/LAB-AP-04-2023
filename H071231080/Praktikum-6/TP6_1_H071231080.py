simpan = {} #Dictionary

print("Selamat datang untuk memulai silahkan input data anda")
simpan['nama'] = input("Input nama: ")
simpan['umur'] = input("Input umur: ")
simpan['alamat'] = input("Input alamat: ")
while True:
    print("="*50)
    print(f"Selamat datang {simpan['nama']} silahkan pilih opsi")
    print("="*50)
    print("1. Detail anda" )
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("="*50)
    opsi = int(input("Input opsi: "))

    if opsi == 1:
        print("="*50)
        print(f"Data anda adalah\nNama: {simpan['nama']}\nUmur: {simpan['umur']}\nAlamat: {simpan['alamat']}")
    elif opsi == 2:
        nama1 = input("Silahkan Input nama baru: ")
        simpan['nama'] = nama1
        print("Data anda sukses diperbarui")
    elif opsi == 3:
        umur1 = input("Silahkan Input umur baru: ")
        simpan['umur'] = umur1
        print("Data anda sukses diperbarui")
    elif opsi == 4:
        alamat1 = input("Silahkan Input alamat baru: ")
        simpan['alamat'] = alamat1
        print("Data anda sukses diperbarui")
    elif opsi == 5:
        print("="*50)
        print(f"Selamat Tinggal {simpan['nama']}")
        break
    else:
        print("opsi tidak valid")
       