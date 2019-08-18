if __name__ == '__main__':
    n = int(input())
    state = []

    for _ in range(n):
        rest = list(map(lambda x: x.strip(), input().split()))
        e = None
        i = None

        if len(rest) >= 2:
            e = int(rest.pop())

        if len(rest) == 2:
            i = int(rest.pop())

        command = rest.pop()

        if command == 'insert':
            state.insert(i, e)

        elif command == 'print':
            print(state)

        elif command == 'remove':
            state.remove(e)

        elif command == 'append':
            state.append(e)

        elif command == 'sort':
            state.sort()

        elif command == 'pop':
            state.pop()

        elif command == 'reverse':
            state.reverse()
