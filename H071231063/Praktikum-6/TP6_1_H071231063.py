data = {
    "Nama": "",
    "Umur": "",
    "Alamat": ""
}
print("Selamat datang! Untuk memulai, silakan input data Anda.")
data["Nama"] = input("Input nama: ")
data["Umur"] = input("Input umur: ")
data["Alamat"] = input("Input alamat: ")
while True:
    print("=" * 50)
    print(f"Selamat datang {data['Nama']}! Silakan pilih opsi:")
    print("=" * 50)
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("=" * 50)
    opsi = input("Input opsi: ")
    if opsi == "1":
        print("=" * 50)
        print("Data Anda adalah:")
        print("Nama:", data["Nama"])
        print("Umur:", data["Umur"])
        print("Alamat:", data["Alamat"])
        print("=" * 50)
    elif opsi == "2":
        data["Nama"] = input("Masukkan nama baru: ")
        print("Data anda sukses di diperbarui ")
    elif opsi == "3":
        data["Umur"] = input("Masukkan umur baru: ")
        print("Data anda sukses di diperbarui ")
    elif opsi == "4":
        data["Alamat"] = input("Masukkan alamat baru: ")
        print("Data anda sukses di diperbarui ")
    elif opsi == "5":
        print("Selamat Tinggal", data["Nama"])
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi yang benar.")
