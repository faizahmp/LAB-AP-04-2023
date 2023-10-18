data_kosong=[]

def input_data():
    print("Selamat datang untuk memulai silahkan input data anda")
    Nama = input("input Nama: ")
    Umur = input("input Umur: ")
    Alamat = input("input Alamat: ")
    return {
        "Name": Nama, 
        "Age": Umur, 
        "Address": Alamat
        }

def tampilkan_data(data):
    print("=" * 50)
    print(f"Selamat datang {data['Name']} silahkan pilih opsi")
    print("=" * 50)
    print("1. Detail anda\n2. Ubag Nama\n3.Ubah Umur\n4.Ubah Alamat\n5.Keluar")
    print("=" * 50)

def detail_data(data):
    print("=" * 50)
    print("Data anda adalah")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("=" * 50)

def program_data():
    data_kosong = input_data()
        
    while True:
        tampilkan_data(data_kosong)
        pilihan = input("Input opsi: ")
        
        if pilihan == "1":
            detail_data(data_kosong)
        elif pilihan == "2":
            nama_baru = input("Masukkan nama baru: ")
            data_kosong["Name"] = nama_baru
        elif pilihan == "3":
            umur_baru = input("Masukkan umur baru: ")
            data_kosong["Age"] = umur_baru
        elif pilihan == "4":
            alamat_baru = input("Masukkan alamat baru: ")
            data_kosong["Address"] = alamat_baru
        elif pilihan == "5":
            print(f"Selamat tinggal {data_kosong['Name']}")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-5.")

program_data()