n, c = [int(i) for i in raw_input().split()]
students = []
for i in xrange(n):
    ID, name, grade = raw_input().split()
    students.append((ID, name, grade))
if c == 1:
    students.sort(key=lambda x: x[0])
elif c == 2:
    students.sort(key=lambda x: (x[1], x[0]))
else:
    students.sort(key=lambda x: (x[2], x[0]))
for ID, name, grade in students:
    print ID, name, grade