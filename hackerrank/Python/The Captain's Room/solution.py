n = int(input())
k = list(map(int, input().split()))

a = set()
b = set()

for i in k:
    if i not in a:
        a.add(i)

    else:
        b.add(i)

print(a.difference(b).pop())
