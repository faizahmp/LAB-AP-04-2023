# # data_kosong=[]

# # def input_data():
# #     print("Selamat datang untuk memulai silahkan input data anda")
# #     Nama = input("input Nama: ")
# #     Umur = input("input Umur: ")
# #     Alamat = input("input Alamat: ")
# #     return {
# #         "Name": Nama, 
# #         "Age": Umur, 
# #         "Address": Alamat
# #         }

# # def tampilkan_data(data):
# #     print("=" * 50)
# #     print(f"Selamat datang {data['Name']} silahkan pilih opsi")
# #     print("=" * 50)
# #     print("1. Detail anda\n2. Ubah Nama\n3.Ubah Umur\n4.Ubah Alamat\n5.Keluar")
# #     print("=" * 50)

# # def detail_data(data):
# #     print("=" * 50)
# #     print("Data anda adalah")
# #     for key, value in data.items():
# #         print(f"{key}: {value}")
# #     print("=" * 50)

# # def program_data():
# #     data_kosong = input_data()
        
# #     while True:
# #         tampilkan_data(data_kosong)
# #         pilihan = input("Input opsi: ")
        
# #         if pilihan == "1":
# #             detail_data(data_kosong)
# #         elif pilihan == "2":
# #             nama_baru = input("Masukkan nama baru: ")
# #             data_kosong["Name"] = nama_baru
# #         elif pilihan == "3":
# #             umur_baru = input("Masukkan umur baru: ")
# #             data_kosong["Age"] = umur_baru
# #         elif pilihan == "4":
# #             alamat_baru = input("Masukkan alamat baru: ")
# #             data_kosong["Address"] = alamat_baru
# #         elif pilihan == "5":
# #             print(f"Selamat tinggal {data_kosong['Name']}")
# #             break
# #         else:
# #             print("Pilihan tidak valid. Silakan masukkan angka 1-5.")

# # program_data()






# print("Selamat datang, untuk memulai silakan input data Anda")
# nama = input("Input nama: ")
# umur = input("Input umur: ")
# alamat = input("Input alamat: ")

# data = {
# "gender": gender,
# "nama": nama,
# "umur": umur,
# "alamat": alamat
# }

# while True: # pengulangan
#     print("="*50)
#     print("Selamat datang", data["nama"]+ ", silakan pilih opsi")
#     print("="*50)
#     print("1. Detail Anda")
#     print("2. Ubah Nama")
#     print("3. Ubah Umur")
#     print("4. Ubah Alamat")
#     print("5. Keluar")
#     print("="*50)

#     opsi = input("Input opsi: ")

#     if opsi == "1":
#         print("="*50)
#         print("Data Anda adalah")
#         print("Nama:", data["nama"])
#         print("Umur:", data["umur"])
#         print("Alamat:", data["alamat"])
#     elif opsi == "2":
#         nama_baru = input("Silakan input nama baru: ")
#         data["nama"] = nama_baru # memperbarui data key "nama"
#         print("Data Anda sukses diperbarui")
#     elif opsi == "3":
#         umur_baru = input("Silakan input umur baru: ")
#         data["umur"] = umur_baru
#         print("Data Anda sukses diperbarui")
#     elif opsi == "4":
#         alamat_baru = input("Silakan input alamat baru: ")
#         data["alamat"] = alamat_baru
#         print("Data Anda sukses diperbarui")
#     elif opsi == "5":
#         print("="*50)
#         print("Selamat tinggal", data["nama"])
#         break # keluar dari pengulangan
#     else:
#         print("Opsi tidak valid, silakan coba lagi")
kota_negara={
"Indonesia": ["Jakarta","Bandung", "Surabaya", "Makassar", "Denpasar", "Pontianak"],
"Jepang": ["Tokyo", "Kyoto", "Fukuoka", "Osaka", "Hiroshima"],
"US" : ["New York", "Texas", "Washington", "Alaska"]
}

for key, item in kota_negara.items():
    for i in item:
        print(f"{key}: {i}")
print(kota_negara["US"])



