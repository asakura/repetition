import re

rows, columns = tuple(map(int, input().split()))
code = []

for line in zip(*[list(input())[:columns] for _ in range(rows)]):
    code.append(''.join(line))

code = ''.join(code)

print(re.sub(r'(?<=\w\b)(.*?)(?=\b\w)', ' ', code))
