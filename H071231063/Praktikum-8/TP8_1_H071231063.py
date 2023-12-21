import re
def validasi_string(input_string):
    if len(input_string) != 45:
        return False
    if not re.match("^[A-Za-z02468]{40}$", input_string[:40]):
        return False
    if not re.match("^[13579\s]{5}$", input_string[40:]):
        return False
    return True
input_string = input("Masukkan string: ")
if validasi_string(input_string):
    print("true")
else:
    print("false")