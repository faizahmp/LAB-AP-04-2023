class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
    def Tampilkan_info(self):
        print("Informasi Mahasiswa:")
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"IPK: {self.ipk}")
    def Hitung_predikat(self):
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
        print(f"Predikat: {predikat}")
# Membuat objek Mahasiswa
nama_mahasiswa = input("Masukkan Nama Mahasiswa: ")
nim_mahasiswa = input("Masukkan NIM Mahasiswa: ")
jurusan_mahasiswa = input("Masukkan Jurusan Mahasiswa: ")
ipk_mahasiswa = float(input("Masukkan IPK Mahasiswa: "))
mahasiswa = Mahasiswa(nama_mahasiswa, nim_mahasiswa, jurusan_mahasiswa, ipk_mahasiswa)
# Menampilkan informasi dan predikat mahasiswa
mahasiswa.Tampilkan_info()
mahasiswa.Hitung_predikat()