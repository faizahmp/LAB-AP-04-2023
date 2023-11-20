from abc import ABC, abstractmethod

# Abstract class
class Bentuk(ABC): #Abstrak Base Class
    @abstractmethod
    def area(self):
        pass


class persegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.__panjang = panjang  
        self.__lebar = lebar   

    def area(self):
        return self.__panjang * self.__lebar

# get dan set Panjang
    def get_panjang(self):
        return self.__panjang
    
    def set_panjang(self, panjang):
        if panjang > 0:
            self.__panjang = panjang


 # get dan set Lebar
    def get_lebar(self):
        return self.__lebar

    def set_lebar(self, lebar):
        if lebar > 0:
            self.__lebar = lebar



class Lingkaran(Bentuk):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius  

    def area(self):
        hasil = int(3.14 * self.__radius * self.__radius)
        return hasil

    # Getter method
    def get_radius(self):
        return self.__radius

    # Setter method
    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius

# warisan dari persegipanjang
class Persegi(persegiPanjang):
    def __init__(self, sisi):
        super().__init__(sisi, sisi)

# Penggunaan
persegi_panjang = persegiPanjang(5, 8)
print("persegiPanjang Area:", persegi_panjang.area())

lingkaran = Lingkaran(3)
print("Lingkaran Area:", lingkaran.area())

persegi = Persegi(2)
print("Persegi Area:", persegi.area())
