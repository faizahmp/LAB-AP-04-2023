import os
class UserData:
    def __init__(self):
        self.nama = ""
        self.email = ""
        self.password = ""
    def is_empty(self):
        return not self.nama and not self.email and not self.password
    def display_details(self):
        if self.is_empty():
            print("Data saat ini kosong")
        else:
            print("Detail Anda:")
            print(f"Nama: {self.nama}")
            print(f"Email: {self.email}")
            print("Password: ********")  
    def change_name(self):
        if self.is_empty():
            print("Data saat ini kosong")
        else:
            new_name = input("Masukkan nama baru: ")
            self.nama = new_name
            print("Nama telah diubah")
    def validasi_email(self):
        email = input("Masukkan Email: ")
        if not email.endswith("@student.unhas.ac.id") or any(char in email for char in ["_", "/", "-", " ", "A-Z"]):
            print("="*50)
            print("Email yang Anda Masukkan Salah")
            print("="*50)
            return self.validasi_email()
        return email
    def validasi_password(self):
        password = input("Masukkan Password: ")
        if not (8 <= len(password) <= 20):
            print("="*50)
            print("Password harus memiliki Panjang 8 - 20 karakter")
            print("="*50)
            return self.validasi_password()
        if not any(char.isdigit() for char in password) or not any(
        char.islower() for char in password
        ) or not any(char.isupper() for char in password):
            print("="*50)
            print("Password yang Anda masukkan terlalu lemah")
            print("Gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
            print("="*50)
            return self.validasi_password()
        return password
    def create_new_data(self):
        nama = input ("Masukkan nama: ")
        email = self.validasi_email()
        password = self.validasi_password()
        self.nama = nama  
        self.email = email
        self.password = password
        print("Data baru telah dibuat")
    def count_data_in_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
            return len(lines) // 4
        except FileNotFoundError:
            return 0
    def save_to_file(self):
        if self.is_empty():
            print("Data saat ini kosong")
        else:
            file_name = input("Masukkan nama file : ")
            if not os.path.exists(f"{file_name}"):
                with open(f"{file_name}", "w") as file:
                    file.write("="*50+"\n")
                    file.write("|"+"Data yang tersimpan"+"\n")
                    file.write("="*50+"\n")
            with open(f"{file_name}", "a") as file:
                file.write(f"|Nama: {self.nama}\n|Email: {self.email}\n|Password: {self.password}\n")
                file.write("="*50+"\n")
            self.clear_data()
            print("Berhasil")
    def clear_data(self):
        self.nama = ""
        self.email = ""
        self.password = ""
def menu(user_data):
    while True:
        print("="*50)
        print("Selamat Datang Silahkan Pilih Opsi Menu Anda")
        print("1. Detail Anda")
        print("2. Ubah Nama")
        print("3. Jumlah Data pada File")
        print("4. Save Data pada File")
        print("5. Buat Data Baru")
        print("6. Keluar")
        choice = input("Silahkan pilih opsi anda: ")
        if choice == "1":
            print("="*50)
            user_data.display_details()
        elif choice == "2":
            print("="*50)
            user_data.change_name()
        elif choice == "3":
            print("="*50)
            file_name = input("Masukkan nama file: ")
            data_count = user_data.count_data_in_file(file_name)
            print(f"Jumlah Data pada File {file_name}: {data_count} data")
        elif choice == "4":
            print("="*50)
            user_data.save_to_file()
        elif choice == "5":
            print("="*50)
            user_data.create_new_data()
        elif choice == "6":
            print("="*50)
            print("Sampai Jumpa Lagi")
            print("="*50)
            break
        else:
            print("="*50)
            print("Pilihan tidak valid, silakan pilih kembali.")
if __name__ == "__main__":
    user = UserData()
    menu(user)