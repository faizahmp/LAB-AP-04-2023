#Meminta Input
x = str(input("Masukkan Input Pertama = "))
y = str(input("Masukkan Input Kedua = "))
z = str(input("Masukkan Input Ketiga = "))

match (x, y) :
    case ("vertebrado", "ave") :
        match z :
            case "carnivoro" :
                print("agula")
            case "onivoro" :
                print("pomba")
            case _:
                print("Invalid input")
    case ("vertebrado", "mamivero") :
        match z :
            case ("onivoro") :
                print("homem")
            case ("herbivoro") :
                print("vaca")
            case _:
                print("Invalid input")
    case ("invertebrado", "inseto"):
        match z :
            case ("hematofago"):
                print("pulga")
            case ("herbivoro") :
                print("lagarta")
            case _:
                print("Invalid input")
    case ("invertebrado", "anelideo"):
        match z :
            case ("hematofago"):
                print("sanguessuga")
            case ("onivoro"):
                print("minhoca")
            case _:
                print("Invalid input")
    case _:
        print("Invalid input")
        
        
        
