def median(numbers):
    n = len(numbers)
    middle = n // 2

    if n % 2 == 0:
        return (numbers[middle - 1] + numbers[middle]) / 2

    return numbers[middle]


n = int(input())
x = list(map(int, input().split()))[:n]
f = list(map(int, input().split()))[:n]

s = []

for (i, j) in zip(x, f):
    s.extend([i] * j)

s.sort()

middle = len(s) // 2

if len(s) % 2 == 0:
    q1 = median(s[:middle])
    q3 = median(s[middle:])

else:
    q1 = median(s[:middle])
    q3 = median(s[middle+1:])

iqr = float(q3 - q1)

print(round(iqr, 1))
