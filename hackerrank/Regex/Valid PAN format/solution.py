import re

for _ in range(int(input())):
    pan = input()

    if re.match(r'^[A-Z]{5}\d{4}[A-Z]$', pan):
        print('YES')

    else:
        print('NO')
