import re
import sys

code = sys.stdin.read()

if re.search(r'#include.*$', code, re.MULTILINE):
    print('C')

if re.search(r'(import\s+java\.io\..*;|(public|private\s+class\s+.*{})|System\.out)', code, re.MULTILINE):
    print('Java')

elif re.search(r'(class\s+.*:|def\s+.*:|print[\s+][^\(])', code, re.MULTILINE):
    print('Python')
