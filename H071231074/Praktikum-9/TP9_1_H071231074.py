class Human: #Kelas kakek yang mempunyai anak (hero) dan cucu-cucu (Warrior, Assassin dan Support)
    def __init__(self, name, position, speed=1): # Constructor (Akan dijalankan tanpa dipanggil seperti method)
        self.name = name # Atribut
        self.__position = position
        self._speed = speed
    
    def Movement(self, arah):
        for i in arah:
            if i == "R":
                self.__position += self._speed
            elif i == "L":
                self.__position += self._speed
    
    def getPosition(self):
        return self.__position
    def setPosition(self, position):
        self.__position = position
    
    def getSpeed(self):
        return self._speed
    def setSpeed(self, speed):
        self._speed = speed
    
class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def Attack(self, target):
        target._health -= self._power
        print(f"{self.name} sedang menyerang. Health {target.name} berkurang sebanyak {self._power} sehingga tersisa {target._health}")
    
    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def setPower(self, power):
        self._power = power
    def setHealth(self, health):
        self._health = health
    def setArmor(self, armor):
        self._armor = armor
    
class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power
        print(f"{self.name} memakai Special Skill!")

class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self.speed = 4
    def special(self, target):
        self.speed = 7
        self._power = 32
        target._health -= self._power
        print(f"{self.name} memakai Special Skill!")

class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self.speed = 4
    def special(self, target):
        self.speed = 6
        target._health += 150
        print(f"{self.name} memakai Special Skill!")

warrior = Warrior("bambang", 10)
assassin = Assassin("joko", 25)
support = Support("udin", 30)

# sebelum
print("health (before)", warrior.getHealth())
assassin.Attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())

print("Warrior Movement (before)", warrior.getPosition()) 
warrior.Movement("LL")
print("Warrior Movement (after)", warrior.getPosition()) 




