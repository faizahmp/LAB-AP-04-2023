class Barang:
    def __init__(self, judul, status="Tersedia"):
        self._judul = judul       # Judul barang
        self._status = status     # Status peminjaman

    @property
    def judul(self):
        return self._judul

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status

    def pinjam(self):
        self._status = "Dipinjam"
        print(f"{self._judul} telah dipinjam.")

    def kembalikan(self):
        self._status = "Tersedia"
        print(f"{self._judul} telah dikembalikan.")

class Buku(Barang):
    def __init__(self, judul, pengarang, status="Tersedia"):
        super().__init__(judul, status)
        self._pengarang = pengarang     # Pengarang buku

    @property
    def pengarang(self):
        return self._pengarang

    def tampilkan_info(self):
        print(f"Buku: {self._judul} karya {self._pengarang} - Status: {self._status}")

if __name__ == "__main__":
    buku = Buku("The Great Gatsby", "F. Scott Fitzgerald")
    buku.tampilkan_info()

    buku.pinjam()
    buku.tampilkan_info()

    buku.kembalikan()
    buku.tampilkan_info()

    # Penggunaan getter dan setter
    print("Judul Buku:", buku.judul)
    print("Status Buku:", buku.status)

    buku.status = "Dipinjam"
    print("Status Buku setelah diubah:", buku.status)
