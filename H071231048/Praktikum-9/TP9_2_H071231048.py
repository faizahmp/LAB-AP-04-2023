class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = float(ipk)  
    
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"IPK: {self.ipk}")

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Cukup"
        else:
            return "Kurang"

nama = input("Nama: ")
nim = input("NIM: ")
jurusan = input("Jurusan: ")
ipk = input("IPK: ")

mahasiswa1 = Mahasiswa(nama, nim, jurusan, ipk)

mahasiswa1.tampilkan_info()
print("Predikat:", mahasiswa1.hitung_predikat())

