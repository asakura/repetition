if __name__ == '__main__':
    n = int(input())
    state = set(list(map(int, input().split()))[:n])
    n = int(input())

    for _ in range(n):
        rest = list(map(lambda x: x.strip(), input().split()))
        e = None

        if len(rest) >= 2:
            e = int(rest.pop())

        command = rest.pop()

        if command == 'discard':
            state.discard(e)

        elif command == 'remove':
            state.remove(e)

        elif command == 'pop':
            state.pop()

    print(sum(state))
