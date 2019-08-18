n = int(input())

for _ in range(n):
    x, y = input().split()

    try:
        print(int(x) // int(y))

    except Exception as e:
        print('Error Code: {}'.format(e))
