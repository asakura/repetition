thousand = r'M{,3}'
hundred = r'(?:C[MD]|D?C{,3})'
ten = r'(?:X[CL]|L?X{,3})'
digit = r'(?:I[VX]|V?I{,3})'

regex_pattern = r'^{}{}{}{}$'.format(thousand, hundred, ten, digit)

import re
print(str(bool(re.match(regex_pattern, input()))))
