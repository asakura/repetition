import re

n = int(input())

for _ in range(n):
    uid = input()

    tests = [
        bool(re.search(r'(.*[A-Z]){2,}', uid)),
        bool(re.search(r'(.*\d){3,}', uid)),
        bool(re.match(r'^[a-zA-Z0-9]{10}$', uid)),
        not bool(re.search(r'(.).*\1', uid))
    ]

    if all(tests):
        print('Valid')

    else:
        print('Invalid')
