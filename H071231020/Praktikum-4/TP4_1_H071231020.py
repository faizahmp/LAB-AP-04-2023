# def permutasi_kata(kata):
#     try:
#         kata = str(input())
#         if type(kata) != int:
#             raise TypeError("Input harus berupa string")
#     except TypeError:
#         print("Input harus berupa string")

#         for i in range(len(kata)):
#             kata = kata[-1] + kata[:-1]
#             print(kata, end=' | ')

# permutasi_kata(kata)

def permutasi_kata(kata):
    try:
        n = int(kata)
        print('input harus berupa string')
    except :
        for i in range(len(kata)):
            kata = kata[-1] + kata[:-1]
            print(kata, end=' | ')

permutasi_kata(input())