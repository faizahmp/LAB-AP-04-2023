import re

def validate_file(input_string):
    pattern= r'^[a-zA-Z0-9]{40}[13579\s]{5}$'
    if re.match(pattern, input_string):
        return True
    else:
        return False
input_string= input("masukkan str: ")
hasil= validate_file(input_string)
print(hasil)
