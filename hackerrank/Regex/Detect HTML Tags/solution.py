import re

n = int(input())

res = set()

for _ in range(n):
    res.update(
        set(
            re.findall(
                r'<\s*([a-z][a-z0-9]*)\s*.*?\/?>',
                input(),
                re.IGNORECASE
            )
        )
    )


print(';'.join(sorted(list(res))))
