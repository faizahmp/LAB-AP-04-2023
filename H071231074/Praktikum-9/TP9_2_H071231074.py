class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print("Informasi Mahasiswa:")
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan)
        print("IPK:", self.ipk)

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            predikat = "Cumlaude"
        elif self.ipk >= 3.0:
            predikat = "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            predikat = "Memuaskan"
        elif self.ipk >= 2.0:
            predikat = "Cukup"
        else:
            predikat = "Kurang"
        print("Predikat:", predikat)

# Contoh penggunaan class Mahasiswa
mahasiswa1 = Mahasiswa("John Doe", "123456", "Informatika", 3.8)
mahasiswa2 = Mahasiswa("Jane Doe", "654321", "Sistem Informasi", 2.7)

mahasiswa1.tampilkan_info()
mahasiswa1.hitung_predikat()

print("\n")

mahasiswa2.tampilkan_info()
mahasiswa2.hitung_predikat()

namamahasiswa = input("Masukkan Nama Mahasiswa : ")
nimmahasiswa = input("Masukkan NIM: ")
jurusan = input("Masukkan Jurusan : ")
ipk = int(input("Masukkan IPK : "))
print("\n")

Mahasiswa(namamahasiswa, nimmahasiswa, jurusan, ipk).tampilkan_info()
Mahasiswa(namamahasiswa, nimmahasiswa, jurusan, ipk).hitung_predikat()
