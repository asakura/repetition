n, m = list(map(int, input().split()))[:2]

for i in range(1, n, 2):
    print((i * '.|.').center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range(n - 2, -1, -2):
    print((i * '.|.').center(m, '-'))
