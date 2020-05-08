def get_final_list(student_grades, sorted_grades):
    final = []
    for students in student_grades:
        if students[1] == sorted_grades:
            final.append(students[0])
    for names in sorted(final):
        print(names)

if __name__ == '__main__':
    student_name_grades = []
    student_grades = []
    n = int(input())
    if n in range(2, 6):
        for _ in range(n):
            name = input()
            score = float(input())
            
            student_name_grades.append([name, score])
            student_grades.append(score)
        
        sorted_grades = sorted(set((student_grades)), reverse = True)[-2]
        get_final_list(student_name_grades, sorted_grades)
