cube = lambda x: pow(x, 3)

def fibonacci(n):
    lst = [0, 1]

    for i in range(2, n):
        lst.append(lst[i - 2] + lst[i - 1])

    return lst[:n]

if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
