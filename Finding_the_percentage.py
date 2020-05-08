if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()   
    average_marks = student_marks[query_name]
    average_marks = round(sum(average_marks)/len(average_marks), 2)
    print("%.2f" % average_marks)
