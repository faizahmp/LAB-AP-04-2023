import re
def cek_string(inputstring):
    if len(inputstring) != 45:
        return False
    if not re.match(r'^[a-zA-Z0-9]*[02468]*$', inputstring[:40]):
        return False
    if not re.match(r'^[13579\s]*$', inputstring[40:]):
        return False
    return True
print("True") if cek_string(input()) else print("False")