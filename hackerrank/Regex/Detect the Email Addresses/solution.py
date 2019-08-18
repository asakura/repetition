import re

text = ' '.join(input() for _ in range(int(input())))
emails = sorted(set(re.findall(r'\b[\w\.]+@[\w\.]+\.[a-z]{2,3}\b', text, re.IGNORECASE)))
print(';'.join(emails))
