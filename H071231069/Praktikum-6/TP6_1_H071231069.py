data = {}

print("Selamat datang untuk memulai silahkan input data anda")
nama = input("Input nama: ")
umur = input("Input umur: ")
alamat = input("Input alamat: ")

data["nama"] = nama # kode utk menambah key "nama" pada dictionary data dengan value nama
data["umur"] = umur
data["alamat"] = alamat

while True: 

    print("=" * 70)
    print(f"Selamat datang {data['nama']} silahkan pilih opsi")
    print("=" * 70)
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("=" * 70)

    opsi = int(input("Input opsi: "))

    if opsi == 1:
        print("=" * 70)
        print("Data anda adalah")
        print(f"Nama: {data['nama']}")
        print(f"Umur: {data['umur']}")
        print(f"Alamat: {data['alamat']}")

    elif opsi == 2:
        nama = input("Silahkan Input nama baru: ")
        data["nama"] = nama
        print("Data anda sukses di diperbarui")

    elif opsi == 3:
        umur = input("Silahkan Input umur baru: ")
        data["umur"] = umur
        print("Data anda sukses di diperbarui")

    elif opsi == 4:
        alamat = input("Silahkan Input alamat baru: ")
        data["alamat"] = alamat
        print("Data anda sukses di diperbarui")

    elif opsi == 5:
        print(f"selamat tinggal",data['nama'])
        break

    else:
        print("Pilihan tidak valid")