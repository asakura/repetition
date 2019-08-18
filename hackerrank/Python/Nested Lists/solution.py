if __name__ == '__main__':
    marks = [[input(), float(input())] for _ in range(int(input()))]

    lowest = sorted(set(mark[1] for mark in marks))[1]

    for name, score in sorted(marks):
        if score == lowest:
            print(name)
