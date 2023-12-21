import re
def cek_ip_address(input_string):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", input_string):
        parts = input_string.split('.')
        for part in parts:
            if int(part) > 255:
                return "Bukan IP Address"
        return "IPv4"
    if re.match(r"^[0-9a-fA-F:]+$", input_string):
        return "IPv6"
    return "Bukan IP Address"
N = int(input())
input_strings = []
for i in range(N):
    input_strings.append(input())
results = []
for input_string in input_strings:
    if len(input_string) <= 500:
        result = cek_ip_address(input_string)
        results.append(result)
    else:
        results.append("Bukan IP Address")
for result in results:
    print(result)