from abc import ABC, abstractmethod
class Bunga(ABC):
    def __init__(self, nama, warna):
        self._nama = nama
        self._warna = warna
    @abstractmethod
    def tumbuh(self):
        pass
    def berkembang(self):
        pass
    def getNama(self):
        return self._nama
    def setnama(self, nama):
        self._nama = nama
    def getWarna(self):
        return self._warna
    def setwarna(self, warna):
        self._warna = warna
class Mawar(Bunga):
    def __init__(self, nama, warna):
        super().__init__(nama, warna)
    def tumbuh(self):
        return "Mawar sedang tumbuh"
    def berkembang(self):
        return "Mawar sedang berkembang"
class Melati(Bunga):
    def __init__(self, nama, warna):
        super().__init__(nama, warna)
    def tumbuh(self):
        return "Melati sedang tumbuh"
    def berkembang(self):
        return "Melati sedang berkembang"
class BungaMatahari(Bunga):
    def __init__(self, nama, warna):
        super().__init__(nama, warna)
    def tumbuh(self):
        return "Bunga Matahari sedang tumbuh"
    def berkembang(self):
        return "Bunga Matahari sedang berkembang"
if __name__ == "__main__":
    mawar = Mawar("Mawar", "Merah")
    melati = Melati("Melati", "Putih")
    matahari = BungaMatahari("Bunga Matahari", "Kuning")
    print(f"{mawar.getNama()} memiliki warna {mawar.getWarna()}")
    print(mawar.tumbuh())
    print(mawar.berkembang())
    melati.setwarna("pink")
    print(f"{melati.getNama()} memiliki warna {melati.getWarna()}")
    print(melati.tumbuh())
    print(melati.berkembang())
    print(f"{matahari.getNama()} memiliki warna {matahari.getWarna()}")
    print(matahari.tumbuh())
    print(matahari.berkembang())