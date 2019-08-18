n = int(input())
a = set(list(map(int, input().split()))[:n])
n = int(input())
b = set(list(map(int, input().split()))[:n])

print(len(a.union(b)))
