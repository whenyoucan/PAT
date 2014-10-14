import Queue

args = raw_input().split()
n, p, r = int(args[0]), float(args[1]), float(args[2])
q = Queue.Queue()
lines = [raw_input() for i in xrange(n)]
q.put(0)
q.put(-1)
total = 0.0
while not q.empty():
    cur = q.get()
    if cur == -1:
        p *= (1 + r / 100)
        if not q.empty():
            q.put(-1)
        continue
    line = [int(i) for i in lines[cur].split()]
    if line[0] != 0:
        for sub in line[1:]:
            q.put(int(sub))
    else:
        total += p * int(line[1])
print "%.1f" % total