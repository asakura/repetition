import re

counter = 0

for _ in range(int(input())):
    counter += len(re.findall(r'[@#]?hackerrank', input(), re.IGNORECASE))

print(counter)
