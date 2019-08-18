import re
from collections import defaultdict

result = defaultdict(list)

for _ in range(int(input())):
    for match in re.finditer(r'<\s*?([^\/].*?)(?:\s+(.*?)?)?\s*?>', input()):
        tag = match.group(1)
        attrs = match.group(2)

        if attrs:
            attrs = re.findall(r'(\S*?)=["\'].*?["\']', attrs)

        else:
            attrs = []

        result[tag].extend(attrs)

for tag, attrs in sorted(result.items()):
    print(tag, ':', sep='', end='')
    print(*sorted(set(attrs)), sep=',')
