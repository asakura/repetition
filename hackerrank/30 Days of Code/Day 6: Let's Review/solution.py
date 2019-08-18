n = int(input())

for _ in range(n):
    s = input()
    left = []
    right = []

    for i in range(0, len(s), 2):
        left.append(s[i])

        if i + 1 < len(s):
            right.append(s[i + 1])

    print(''.join([*left, ' ', *right]))
