import re

def cek_string(input_string):

    if len(input_string) != 45:
         return False

    if not re.search(r'^[a-zA-Z02468]{40}[13579\s]{5}$', input_string[:45]): #\s Mengembalikan kecocokan dimana string berisi karakter spasi
         return False
    
    return True

'''2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57'''
input = input()
print(cek_string(input))

# test = ""
# for i in range(46):
#     test += "?"
# print(test)