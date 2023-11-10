import re

def cek_IPaddress(address):
    IPv4_Address = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])$"   
    IPv6_Address = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

    if re.match(IPv4_Address, address):
        return "IPv4"
    elif re.match(IPv6_Address, address):
        return "IPv6"
    else:
        return "Bukan IPv4 and IPv6"

n = int(input())
listt = []

for i in range(n):
    address = input(f"Masukan alamat ip {i+1} : ")
    hasil = cek_IPaddress(address)
    listt.append(hasil)

for result in listt:
    print(result)