class Human:
    def __init__(self, nama, posisi):
        self.nama = nama
        self.__posisi = posisi 
        self._speed = 0

    # Method
    def movement(self, arah):
        for i in arah :
            if i == "L":
                self.__posisi -= self._speed
            elif i == "R":
                self.__posisi += self._speed
            else :
                pass

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def get_posisi(self): # Memanggil nilai
        return self.__posisi

    def set_posisi(self, posisi): # Mengubah nilai
        self.__posisi = posisi

class Hero(Human): # inheritance
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    # Method
    def attack(self, target):
        target._health -= self._power

    def get_power(self):
        return self._power

    def set_power(self, power):
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
    
    # Method
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power

class Assassin(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._power = 35
        self._speed = 4

    # Method
    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health -= self._power

class Support(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._health = 500
        self._armor = 8
        self._speed = 4

    # Method
    def special(self, target):
        self._speed = 6
        target._health += 150

# Contoh penggunaan Objek
warrior = Warrior("zilong", posisi=10)
assassin = Assassin("ling", posisi=25)
support = Support("angela", posisi=30)

# Memanggil Method Class Human
print(warrior.get_posisi())
#support.set_speed(5)
warrior.movement("LLLLL")
print(warrior.get_posisi())

print('-' * 10)

# Memanggil Method Class Hero
# Sebelum
print("Health (before):", warrior.get_health())
assassin.attack(warrior)
# Sesudah
print("Health (after):", warrior.get_health())
print("-" * 10)

# Memanggil Method Special 
# Sebelum
print("Warrior (health):", warrior.get_health())
print("Support (speed):", warrior.get_speed())
support.special(warrior)
# Sesudah
print("Warrior (health):", warrior.get_health())
print("Support (speed):", warrior.get_speed())