# CARA 1:
Kata = input('Masukkan Kata : ')
#mix = Kata[0] + Kata[len(Kata) // 2] + Kata[-1]
if len(Kata) < 3 :
   print ("eror")
   exit()
else:
    mix = Kata[0] + Kata[len(Kata) // 2] + Kata[-1]
print(mix)

# # CARA 2:
# def first_middle_last(Kata):
#     if len(Kata) % 2 == 0:
#         return Kata[0] + Kata[len(Kata) // 2] + Kata[-1]
#     else:
#         return Kata[0] + Kata[len(Kata) // 2] + Kata[-1]

# print(first_middle_last(Kata))