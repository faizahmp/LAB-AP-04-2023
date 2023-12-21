
Kata1 = input('Masukkan kata pertama = ').replace(' ', '').lower()
Kata2 = input('Masukkan kata kedua = ').replace(' ', '').lower()

if len(Kata1) != len(Kata2):
    print('False')
    exit()

for char in Kata1:
    if Kata1.count(char) == Kata2.count(char):
        print(True)
        exit()
    else:
        print(False)
        
# if sorted(Kata1) == sorted(Kata2):
#     print ("True")
# else:
    # print ("False")