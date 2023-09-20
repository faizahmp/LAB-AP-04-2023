I1 = input('masukkan input pertama : ')
I2 = input('masukkan input kedua : ')
I3 = input('masukkan input ketiga : ')

match I1,I2,I3:
    case "vertebrado","ave","carnivoro":
        print('aguia')
    case "vertebrado","ave","onivoro":
        print('pomba')
    case "vertebrado","mamifero","onivoro":
        print('homem')
    case "vertebrado","mamifero","herbivoro":
        print('vaca')
    case "invertebrado","inseto","hematofago":
        print('pulga')
    case "invertebrado","inseto","herbivoro":
        print('lagarta')
    case "invertebrado","anelideo","hematofago":
        print('sanguessuga')
    case "invertebrado","anelideo","onivoro":
        print('minhoca')
    case _:
        print('invalid input')
