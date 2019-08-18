import re

for _ in range(int(input())):
    line = input()

    if re.match(r'^hackerrank(.*hackerrank)?$', line):
        print(0)

    elif re.match(r'^hackerrank', line):
        print(1)

    elif re.search(r'hackerrank$', line):
        print(2)

    else:
        print(-1)
