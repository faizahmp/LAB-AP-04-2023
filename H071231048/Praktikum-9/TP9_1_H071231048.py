from hero import Warrior, Assassin, Support

if __name__ == "__main__":
    # warrior = Warrior("Dambang", position=10)
    assassin = Assassin("Joko", position=25)
    support = Support("Udin", position=30)

    nama = input("masukkan nama : ")
    posisi = int(input("posisi : " ))
    warrior = Warrior(nama,posisi)
    

    # sebelum
    print("health (before)", warrior.get_health())
    assassin.attack(warrior)
    # sesudah
    print("health (after)", warrior.get_health())

    print("-" * 10)

    # sebelum
    print("Warrior (health)", warrior.get_health())
    print("Support (speed)", support.get_speed())

    support.special(warrior)
    # sesudah
    print("Warrior (health)", warrior.get_health())
    print("Support (speed)", support.get_speed())

    print (warrior.get_position())
    warrior.movement("LLLL")
    print (warrior.get_position())