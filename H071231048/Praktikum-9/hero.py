class Human:
    def __init__(self, name, position):
        self.name = name
        self.__position = position
        self._speed = 1  

    def set_position(self, value):
        self.__position = value

    def get_position(self):
        return self.__position

    def set_speed(self, value):
        self._speed = value

    def get_speed(self):
        return self._speed
    def movement(self, arah):
        for i in arah:
            if i == "R":
                self.__position += self._speed 
            elif i == "L":
                self.__position -= self._speed
            else:
                pass

class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target.set_health(target.get_health() - self._power)

    def set_health(self, value):
        self._health = value

    def get_health(self):
        return self._health

    def set_power(self, value):
        self._power = value

    def get_power(self):
        return self._power


class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power=26
        self._armor=30

    def special(self, target):
        self._armor=45
        self._power=32
        target._health=target.health-self._power


class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power=35
        self._speed=4

    def special(self, target):
        # Special ability: Increase speed and attack
        self._speed=7
        self._power=42
        target.set_health(target.get_health() - self.get_power())


class Support(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def set_health(self, value):
        self._health = value

    def get_health(self):
        return self._health

    def special(self, target):
        # Special ability: Increase speed and heal
        self._speed = 6 
        target.set_health(target.get_health() + 150)

