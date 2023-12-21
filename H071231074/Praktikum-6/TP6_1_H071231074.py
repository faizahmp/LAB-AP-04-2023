dictkosong = {}
print("Selamat datang untuk memulai silahkan input data anda")
dictkosong["nama"] = input("Input nama: ")
dictkosong["umur"] = int(input("Input umur: "))
dictkosong["alamat"] = input("Input alamat: ")

while True:
    print(f"\n{'='*50}\nSelamat datang {dictkosong['nama']}, Silahkan pilih opsi\n{'='*50}\n1. Detail Anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar\n{'='*50}")
    input_opsi = input("Input opsi: ")

    if input_opsi == "1":
        print(f"{'='*50}\nData anda adalah\nNama: {dictkosong['nama']}\nUmur: {dictkosong['umur']}\nAlamat: {dictkosong['alamat']}\n")
    elif input_opsi == "2":
        dictkosong["nama"] = input("Silahkan Input nama baru: ")
        print("Data anda sukses diperbarui\n")
    elif input_opsi == "3":
        dictkosong["umur"] = input("Silahkan Input umur baru: ")
        print("Data anda sukses diperbarui\n")
    elif input_opsi == "4":
        dictkosong["alamat"] = input("Silahkan Input alamat baru: ")
        print("Data anda sukses diperbarui\n")
    elif input_opsi == "5":
        print(f"Selamat tinggal {dictkosong['nama']}")
        break
    else:
        print("Opsi tidak valid. Mohon masukkan inputan yang benar")