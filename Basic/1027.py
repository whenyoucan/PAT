sizes = [n * n * 2 - 1 for n in xrange(0, 24)]
N, c = raw_input().split()
N = int(N)
for i in xrange(1, len(sizes)):
    if N <= sizes[i + 1]:
        break
level = i
for i in range(level, 0, -1) + range(2, level + 1, 1):
    print ''.join([' ' * (level - i), c * (2 * i - 1)])
print N - sizes[level]