if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))[:n]

    print(hash(tuple(integer_list)))