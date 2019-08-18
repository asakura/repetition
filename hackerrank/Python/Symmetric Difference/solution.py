x = int(input())
m = set(list(map(int, input().split()))[:x])
y = int(input())
n = set(list(map(int, input().split()))[:y])

#                or m.symmetric_difference(n)
for i in sorted([*m.difference(n), *n.difference(m)]):
    print(i)
