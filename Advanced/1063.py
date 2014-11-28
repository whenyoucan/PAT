n = input()
sets = []
for i in xrange(n):
    sets.append(set([int(i) for i in raw_input().split()][1:]))
for i in xrange(input()):
    a, b = [int(i) - 1 for i in raw_input().split()]
    common = len(sets[a].intersection(sets[b]))
    print '{:.1f}%'.format(common * 100.0 / (len(sets[a]) + len(sets[b]) - common))