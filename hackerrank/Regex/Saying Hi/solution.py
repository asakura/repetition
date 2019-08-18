import re

for _ in range(int(input())):
    line = input()

    if re.match(r'\b[hH][iI]\s[^dD]', line):
        print(line)
