import re

class DataProgram:
    def __init__(self):
        self.data = {}
    def detailanda(self):
        if self.data:
            print(f"{'='*50}\nData anda adalah : ")
            for key, value in self.data.items():
                print(f"{key} : {value}")
        else:
            print(f"{'='*50}\nData Saat Ini Kosong")
    def ubahnama(self):
        if self.data:
            namabaru = input(f"{'='*50}\nMasukkan Nama Baru : ")
            self.data['Nama'] = namabaru
            print("Nama Berhasil Diubah")
        else:
            print(f"{'='*50}\nData Saat Ini Kosong")
    def jumlahdata(self):
        namafile = input(f"{'='*50}\nSilahkan Masukkan Nama File : ")
        try:
            with open(f"{namafile}.txt", "r") as file:
                jumlah = sum(1 for _ in file)
                print(f"Jumlah data pada file {namafile}.txt: {jumlah}")
        except FileNotFoundError:
            print(f"Tidak terdapat file dengan nama {namafile}.txt\nJumlah Data Pada file : 0 Data")
    def savedatafile(self):
        if self.data:
            namafile = input("Masukkan nama file untuk menyimpan data : ")
            try:
                with open(f"{namafile}.txt", "a") as file:
                    file.write(f'{"-"*100}\n|Data yang Tersimpan\n{"-"*100}\n')
                    for key, value in self.data.items():
                        file.write(f"|{key} : {value}\n")
                    file.write("-"*100)
                self.data = {}
                print("Data berhasil disimpan pada file")
            except:
                print("Terjadi Kesalahan")
        else:
            print(f"{'='*50}\nData Saat Ini Kosong")
    def buatdatabaru(self):
        nama = input(f"{'='*50}\nSilahkan Masukkan Nama Anda : ")
        polaemail = re.compile(r"^[a-z0-9.]+@student.unhas.ac.id$")
        while True:
            email = input("Silahkan Masukkan Email Anda : ")
            if not polaemail.match(email):
                print(f"{'='*50}\nEmail yang anda masukkan salah\n{'='*50}")
                continue
            else:
                break

        while True:
            password = input("Masukkan Password : ")
            if not (8 <= len(password) <= 20):
                print(f"{'='*50}\nPassword harus memiliki panjang 8-20 karakter\n{'='*50}")
                continue
            elif not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password):
                print(f"{'='*50}\nPassword yang anda masukkan terlalu lemah\nGunakan minimal 1 huruf kapital, huruf kecil dan angka\n{'='*50}")
                continue
            else:
                break
        
        self.data = {'Nama': nama, 'Email': email, 'Password': password}
        print("Data baru berhasil dibuat")
    def keluar(self):
        print("Sampai Jumpa Lagi")
        exit()

if __name__ == '__main__':
    program = DataProgram()
    while True:
        print(f"{'='*50}\nSelamat Datang Silahkan Pilih Opsi Menu Anda")
        print("""1. Detail Anda\n2. Ubah Nama\n3. Jumlah Data pada file
4. Save Data pada file\n5. Buat Data Baru\n6. Keluar""")
        pilihan = input("Silahkan Pilih Opsi Anda : ")

        if pilihan == "1":
            program.detailanda()
        elif pilihan == "2":
            program.ubahnama()
        elif pilihan == "3":
            program.jumlahdata()
        elif pilihan == "4":
            program.savedatafile()
        elif pilihan == "5":
            program.buatdatabaru()
        elif pilihan == "6":
            DataProgram().keluar()
        else:
            print("Pilihan tidak valid. Silahkan pilih sesuai menu yang tersedia")       