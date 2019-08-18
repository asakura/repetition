import re

n = int(input())

for _ in range(n):
    uid = input()

    tests = [
        bool(re.match(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$', uid)),
        not bool(re.search(r'(\d)-?\1-?\1-?\1', uid)),
    ]

    if all(tests):
        print('Valid')

    else:
        print('Invalid')
