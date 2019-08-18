if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    marks = student_marks[query_name]
    mean = sum(marks) / 3.0

    print("{:.02f}".format(round(mean, 2)))