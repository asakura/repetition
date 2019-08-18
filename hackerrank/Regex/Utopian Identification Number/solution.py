import re

for _ in range(int(input())):
    number = input()

    if re.match(r'^[a-z]{,3}\d{2,8}[A-Z]{3,}$', number):
        print('VALID')

    else:
        print('INVALID')
