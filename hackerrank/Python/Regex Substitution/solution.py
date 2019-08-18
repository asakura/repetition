import re

def replace(match):
    g = match.group(0)

    if g == '&&':
        return 'and'

    elif g == '||':
        return 'or'


code = '\n'.join(input() for _ in range(int(input())))

print(re.sub(r'(?<=\s)(&&|\|\|)(?=\s)', replace, code))
