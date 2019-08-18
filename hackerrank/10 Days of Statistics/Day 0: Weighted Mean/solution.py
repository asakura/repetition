from functools import reduce

n = int(input())
x = list(map(int, input().split()))[:n]
w = list(map(int, input().split()))[:n]

x = reduce(lambda acc, value: acc + value[1] * w[value[0]], enumerate(x), 0)
w = reduce(lambda acc, value: acc + value, w, 0)

print(round(x / w, 1))
