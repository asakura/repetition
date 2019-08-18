def median(numbers):
    n = len(numbers)
    middle = n // 2

    if n % 2 == 0:
        return (numbers[middle - 1] + numbers[middle]) / 2

    return numbers[middle]

n = int(input())
x = list(map(int, input().split()))[:n]

x.sort()

middle = n // 2
q2 = median(x)

if n % 2 == 0:
    q1 = median(x[:middle])
    q3 = median(x[middle:])

else:
    q1 = median(x[:middle])
    q3 = median(x[middle+1:])

print(int(q1))
print(int(q2))
print(int(q3))
