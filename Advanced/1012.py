n, m = [int(i) for i in raw_input().split()]
students = []
for i in xrange(n):
    info = raw_input().split()
    students.append({
        'id': info[0],
        'C': int(info[1]),
        'M': int(info[2]),
        'E': int(info[3]),
        'A': (int(info[1]) + int(info[2]) + int(info[3])) / 3.0,
        'best_rank': n + 1,
        'best_course': None
    })
for course in ['A', 'C', 'M', 'E']:
    students.sort(key=lambda x: -x[course])
    rank = 0
    for i in xrange(len(students)):
        j = i
        while j > 0 and students[j][course] == students[j - 1][course]:
            j -= 1
        rank = j + 1
        if rank < students[i]['best_rank']:
            students[i]['best_rank'] = rank
            students[i]['best_course'] = course
students_dict = {}
for s in students:
    students_dict[s['id']] = s
for i in xrange(m):
    student_id = raw_input()
    if student_id in students_dict:
        print students_dict[student_id]['best_rank'], students_dict[student_id]['best_course']
    else:
        print 'N/A'