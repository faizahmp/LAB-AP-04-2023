class Human:
    def __init__(self, name, health=0, position=0, speed=3):
        self.name = name
        self._health = health
        self.__position = position
        self._speed = speed
    def attack(self, target):
        target._health -= self.getPower()
    def movement(self, direction):
        for i in direction:
            if i == "L":
                self.__position -= self.getSpeed()
            elif i == "R":
                self.__position += self.getSpeed()
            else:
                pass
    def getHealth(self):
        return self._health
    def getPosition(self):
        return self.__position
    def getSpeed(self):
        return self._speed
    def getPower(self):
        raise NotImplementedError("Subclass harus mengimplementasikan properti 'power'.")
    def setPower(self):
        raise NotImplementedError("Subclass harus mengimplementasikan setter 'power'.")
class Hero(Human):
    def __init__(self, name, health=400, position=0, speed=3):
        super().__init__(name, health, position, speed)
        self._power = 15
        self._armor = 15
    def getPower(self):
        return self._power
    def setPower(self, value):
        self._power = value
    def getArmor(self):
        return self._armor
    def setArmor(self, value):
        self._armor = value
class Warrior(Hero):
    def __init__(self, name, position=0):
        super().__init__(name, position=position)
        self._power = 26
        self._armor = 30
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self.getPower()
class Assassin(Hero):
    def __init__(self, name, position=0):
        super().__init__(name, position=position)
        self._power = 35
        self._speed = 4
    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health -= self.getPower()
class Support(Hero):
    def __init__(self, name, position=0):
        super().__init__(name, position=position)
        self._power = 35
        self._health = 500
        self._armor = 8
        self._speed = 4
    def special(self, target):
        self._speed = 6
        target._health += 150
warrior = Warrior("bambang", position=10)
assassin = Assassin("joko", position=25)
support = Support("udin", position=30)
# Sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# Sesudah
print("health (after)", warrior.getHealth())
print("-" * 10)
# Sebelum
print("warrior (health)", warrior.getHealth())
print("support (speed):", support.getSpeed())
support.special(warrior)
# Sesudah
print("warrior (health)", warrior.getHealth())
print("support (speed):", support.getSpeed())
print("warrior (speed):", warrior.getSpeed())
print("warrior (possition):", warrior.getPosition())
warrior.movement("")
print("warrior (speed):", warrior.getSpeed())
print("warrior (possition):", warrior.getPosition())