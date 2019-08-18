import re

s = input()
k = input().strip()

matches = list(re.finditer(r'(?={})'.format(k), s))

if matches:
    print(
        '\n'.join(
            str((match.start(), match.start() + len(k) - 1))
            for match in matches
        )
    )

else:
    print('(-1, -1)')
