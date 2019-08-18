import re

for _ in range(int(input())):
    line = input()

    if re.match(r'^(?:1?\d{1,2}\.|2[0-5]{2}\.){3}1?\d{1,2}$', line):
        print('IPv4')

    elif re.match(r'^(?:[0-9a-f]{1,4}:){7}[0-9a-f]{1,4}$', line, re.I):
        print('IPv6')

    else:
        print('Neither')
