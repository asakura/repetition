from sys import stdin

book = dict([input().split()[:2] for _ in range(int(input()))])

for name in stdin:
    name = name.strip()
    number = book.get(name)

    if number:
        print('{}={}'.format(name, number))

    else:
        print('Not found')
