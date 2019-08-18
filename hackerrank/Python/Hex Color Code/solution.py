import re

n = int(input())
string = ''.join([input() for _ in range(n)])

prog = re.compile(r'[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', re.IGNORECASE | re.MULTILINE)

matches = prog.findall(string)

for match in matches:
    print(match)
