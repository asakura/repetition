import re

text = '\n'.join(input() for _ in range(int(input())))

for _ in range(int(input())):
    print(
        len(
            re.findall(
                r'(?:^|(?<=[^a-z0-9_])){}(?=[^a-z0-9_])'.format(input()),
                text,
                re.IGNORECASE | re.MULTILINE
            )
        )
    )
