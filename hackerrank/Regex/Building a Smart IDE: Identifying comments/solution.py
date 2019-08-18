import re
import sys

text = sys.stdin.read()

for comment in re.findall(r'(//.*?$|/\*.*?\*/)', text, re.MULTILINE | re.DOTALL):
    print(re.sub(r'\n\s+', '\n', comment))
