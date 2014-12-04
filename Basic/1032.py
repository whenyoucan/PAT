n = input()
schools = [0 for i in xrange(n + 1)]
for i in xrange(n):
    sid, score = [int(i) for i in raw_input().split()]
    schools[sid] += score
max_score = max(schools)
max_school = schools.index(max_score)
print max_school, max_score