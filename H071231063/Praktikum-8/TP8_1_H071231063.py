import re
def validasi_string(input_string):
    if len(input_string) != 45:
        return False
    if not re.match("^[a-zA-Z0-9]*[02468]$", input_string[:40]):
        return False
    if not re.match("^[0-9\s]*[13579]$", input_string[40:]):
        return False
    return True
input_string = input("Masukkan string: ")
if validasi_string(input_string):
    print("false")
else:
    print("true")