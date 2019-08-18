import re

text = ' '.join(input() for _ in range(int(input())))
domains = sorted(
    set(
        re.findall(
            r'(?:https?:\/\/(?:ww[w2]\.)?)([-\w\.]+\.[a-z]{2,3})(?=[^a-z])',
            text,
            re.IGNORECASE
        )
    )
)

print(';'.join(domains))
