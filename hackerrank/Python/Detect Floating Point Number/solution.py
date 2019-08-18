import re

prog = re.compile(
    r'''
    ^
    [-+]?  # number can start with -, + or . symbol
    \d*
    [.]
    \d+    # number must contain at least 1 decimal value
    $
    ''',
    re.VERBOSE
)

n = int(input())

for _ in range(n):
    if prog.match(input()):
        print(True)

    else:
        print(False)
