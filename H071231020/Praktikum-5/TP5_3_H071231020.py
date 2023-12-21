kata1 = input("masukkan kata pertana : ").lower().replace(" ","")
kata2 = input("masukkan kata kedua : ").lower().replace(" ","")
n = 0

for i in kata1 :
    pertama = kata1.count(i)
    kedua = kata2.count(i)
    if pertama != kedua :
        n += 1
if n == 0 and len(kata1) == len(kata2) :
    print("True")
else :
    print ("False")