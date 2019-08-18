import re

for _ in range(int(input())):
    match = re.match(r'^(\d{1,3})[- ](\d{1,3})[- ](\d{4,10})$', input())

    if match:
        print(
            'CountryCode={},LocalAreaCode={},Number={}'.format(*match.group(1, 2, 3))
        )
