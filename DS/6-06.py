n = input()
depends = [[]] * n
for i in xrange(n):
    depends[i] = [int(j) - 1 for j in map(int, raw_input().split())[1:]]
task_sequence = [i for i in xrange(n) if not depends[i]]
wait_sequence = [i for i in xrange(n) if depends[i]]
while len(task_sequence) > 0:
    task = task_sequence.pop(0)
    for i in wait_sequence[:]:
        if task in depends[i]:
            depends[i].remove(task)
            if not depends[i]:
                task_sequence.append(i)
                wait_sequence.remove(i)
if len(wait_sequence) > 0:
    print 0
else:
    print 1