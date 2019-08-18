from functools import reduce
from collections import Counter

n = int(input())
x = list(map(int, input().split()))[:n]

x.sort()

mean = reduce(lambda acc, value: value + acc, x, 0) / n
middle = n // 2
median = x[middle] if n % 2 != 0 else (x[middle - 1] + x[middle]) / 2

mode = Counter(x).most_common(n=1)[0][0]

print(mean)
print(median)
print(mode)
