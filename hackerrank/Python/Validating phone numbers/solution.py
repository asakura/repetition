import re

prog = re.compile(
    r'''
    ^
    [789]
    \d{9}
    $
    ''',
    re.VERBOSE
)

n = int(input())

for _ in range(n):
    if prog.match(input()):
        print('YES')

    else:
        print('NO')
