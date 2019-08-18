import re

text = ' '.join(input() for _ in range(int(input())))

for _ in range(int(input())):
    words = re.sub(r'our', r'o[u]?r', input())
    print(len(re.findall(r'\b' + words + r'\b', text)))
