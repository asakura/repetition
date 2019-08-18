import re

for _ in range(int(input())):
    if re.match(r'^[_\.]\d+[a-z]*_?$', input(), re.IGNORECASE):
        print('VALID')

    else:
        print('INVALID')
