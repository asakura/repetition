import sys
import re

text = sys.stdin.read()
matches = re.findall(r'question-summary-(\d+?)\D.*?question-hyperlink.*?>(.*?)</.*?asked.*?>(.*?)</', text, re.IGNORECASE | re.DOTALL)

for match in matches:
    print(';'.join(match))
