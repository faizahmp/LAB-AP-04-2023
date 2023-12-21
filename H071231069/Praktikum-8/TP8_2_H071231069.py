import re

jumlah_inputan = int(input())

list_karakter = []

for i in range(jumlah_inputan):
    karakter = input()
    list_karakter.append(karakter)

def IPv4(teks):
    cekIpv4 =  r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(cekIpv4, teks)

def IPv6(teks):
    cekIpv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return re.match(cekIpv6, teks)

def cek_ip(teks):
    for karakter in teks:
        if IPv4(karakter):
            print("IPv4")
        elif IPv6(karakter):
            print("IPv6")
        else:
            print("Bukan IP Address")

cek_ip(list_karakter)