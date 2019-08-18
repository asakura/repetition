a = set(map(int, input().split()))
test = []

for _ in range(int(input())):
    b = set(map(int, input().split()))
    test.append(a.issuperset(b))

print(all(test))
