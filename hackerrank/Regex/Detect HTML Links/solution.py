import re

prog = re.compile(
    r'<\s*a\s+.*?href\s*=\s*[\'\"](.*?)[\'\"].*?>(?:<.*?>)*\s*(.*?)\s*(?:<.*?>)*<\/+\s*a\s*>',
    re.IGNORECASE
)

n = int(input())

for _ in range(n):
    for match in prog.finditer(input()):
        if match:
            print('{},{}'.format(*match.group(1, 2)))
