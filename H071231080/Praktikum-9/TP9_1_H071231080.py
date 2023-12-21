class Human:
    def __init__(self, nama, posisi): #Dipanggil otomatis untuk inisialisasi instance baru 
        self.nama = nama
        self.__posisi = posisi 
        self._speed = 0

    def movement(self, arah): 
        for i in arah:
            if i == "L":
                self.__posisi -= self._speed
            elif i == "R":
                self.__posisi += self._speed

    def get_posisi(self): #memanggil posisinya
        return self.__posisi

    def set_posisi(self, posisi): #untuk mengubah angka posisi karena dia private
        self.__posisi = posisi

class Hero(Human): #mewarisi
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi) #untuk mengambil yg ada di human(super)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target): #menyerang target
        target._health -= self._power

    def get_power(self):#memanggil power
        return self._power
    def set_power(self, power): #mengubah power
        self._power = power

    def get_speed(self):
        return self._speed
    def set_speed(self, speed):
        self._speed = speed

    def get_health(self):
        return self._health
    def set_health(self, health):
        self._health = health

    def get_armor(self):
        return self._armor
    def set_armor(self, armor):
        self._armor = armor


class Warrior(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self.set_armor(45)
        self.set_power(32)
        target.health -= self._power

class Assassin(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self.speed(7)
        self.set_power(42)
        target.health -= self._power

class Support(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target._health += 150

# Contoh penggunaan
warrior = Warrior("Bambang", posisi=10)
assassin = Assassin("Joko", posisi=25)
support = Support("Udin", posisi=30)


print(warrior.get_speed())
print(warrior.get_posisi())
# warrior.set_speed(5)
warrior.movement("RL")
print(warrior.get_speed())
print(warrior.get_posisi())

# Sebelum
print("Health (before):", warrior.get_health())
assassin.attack(warrior)
# Sesudah
print("Health (after):", warrior.get_health())
print("-" * 10)

# Sebelum
print("Warrior (health):", warrior.get_health())
print("Support (speed):", support._speed)

support.special(warrior)

# Sesudah
print("Warrior (health):", warrior.get_health())
print("Support (speed):", support._speed)