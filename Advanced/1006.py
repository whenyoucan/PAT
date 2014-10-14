n = int(raw_input())
students = []
for i in xrange(n):
    students.append(raw_input().split())
students.sort(key=lambda x: x[1])
print students[0][0],
students.sort(key=lambda x: x[2])
print students[-1][0]