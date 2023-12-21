import re

def check_ip_address(input_text):
    # IPv4 pattern
    ipv4_pattern = re.compile(
        r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])$'
    )

    # IPv6 pattern
    ipv6_pattern = re.compile(
        r'^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$'
    )

    if ipv4_pattern.match(input_text):
        return "IPv4"
    elif ipv6_pattern.match(input_text):
        return "IPv6"
    else:
        return "Bukan IP Address"

# Input
N = int(input())
input_lines = [input() for _ in range(N)]

# Output
for line in input_lines:
    result = check_ip_address(line.strip())
    print(result)
