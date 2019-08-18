import re

text = ' '.join(input() for _ in range(int(input())))

for _ in range(int(input())):
    word = input()[:-2]

    print(len(re.findall(r'\b{}[zs]e\b'.format(word), text)))
