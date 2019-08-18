import re

text = ' '.join(input() for _ in range(int(input())))

for _ in range(int(input())):
    word = input()

    print(
        len(
            re.findall(
                r'(?<=[a-z0-9_]){}(?=[a-z0-9_])'.format(word),
                text,
                re.IGNORECASE
            )
        )
    )
