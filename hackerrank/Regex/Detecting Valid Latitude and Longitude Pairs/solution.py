import re

for _ in range(int(input())):
    matches = re.findall(r'''
        \(
            (
                [-+]?
                (?:
                    90(?:\.0+)?
                  | [1-8]?\d(?:\.\d+)?
                )
            ),\s
            (
                [-+]?
                (?:
                    180(?:\.0+)?
                  | 1[0-7]\d(?:\.\d+)?
                  | \d?\d(?:\.\d+)?
                )
            )
        \)''',
        input(),
        re.VERBOSE
    )

    if len(matches) == 1:
        print('Valid')

    else:
        print('Invalid')
