import re

n = int(input())

for _ in range(n):
    line = input()

    if re.match(r'^.* <[a-z][a-z0-9._-]*@[a-z]+\.[a-z]{1,3}>$', line):
        print(line)
