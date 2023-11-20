from abc import ABC, abstractmethod
class MinumanHangatDingin(ABC):
    def __init__(self, nama, temperatur):
        self.__nama = nama
        self.__temperatur = temperatur
    @abstractmethod
    def mix_kopi(self):
        pass
        
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
        
    def get_temperatur(self):
        return self.__temperatur
    
    def set_temperatur(self, temperatur):
        self.__temperatur = temperatur
    
class KopiHangat(MinumanHangatDingin):
    def __init__(self, nama, temperatur):
        super().__init__(nama, temperatur)
    
    def mix_kopi(self):
        return f"Siap minum kopi hangat yang ditawarkan diseduh"

    def suara(self):
        return f"Siap minum kopi hangat yang ditawarkan {self.get_nama()} dengan temperatur {self.get_temperatur()} derajat Celsius"



class KopiDingin(MinumanHangatDingin):
    def __init__(self, nama, temperatur):
        super().__init__(nama, temperatur)

    def mix_kopi(self):
        return f"Siap minum kopi hangat yang ditawarkan diblen"

    def suara(self):
        return f"Siap minum kopi dingin yang ditawarkan {self.get_nama()} dengan temperatur {self.get_temperatur()} derajat Celsius"


def mengeluarkan_suara(kopi):
    return kopi.suara()

kopi_hangat = KopiHangat("Kopi Mocha", 80)
kopi_dingin = KopiDingin("Kopi Espresso", 30)

print(mengeluarkan_suara(kopi_hangat))
print(kopi_hangat.mix_kopi())
print(mengeluarkan_suara(kopi_dingin))
print(kopi_dingin.mix_kopi())