if __name__ == '__main__':
    n = int(input())
    state = set(list(map(int, input().split()))[:n])
    n = int(input())

    for _ in range(n):
        rest = list(map(lambda x: x.strip(), input().split()))
        e = int(rest.pop())
        command = rest.pop()

        data = set(list(map(int, input().split()))[:e])

        if command == 'intersection_update':
            state.intersection_update(data)

        elif command == 'symmetric_difference_update':
            state.symmetric_difference_update(data)

        elif command == 'difference_update':
            state.difference_update(data)

        elif command == 'update':
            state.update(data)

    print(sum(state))
