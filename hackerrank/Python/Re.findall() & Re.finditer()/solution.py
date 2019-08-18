import re

prog = re.compile(
    r'''
    (?<=[qwrtypsdfghjklzxcvbnm]) # preceded by a single consonant
    [aeiou]{2,}                  # match 2 or more vowels
    (?=[qwrtypsdfghjklzxcvbnm])  # followed by a consonant
    ''',
    re.IGNORECASE | re.VERBOSE
)

matches = prog.findall(input())

if matches:
    for match in matches:
        print(match)

else:
    print(-1)
