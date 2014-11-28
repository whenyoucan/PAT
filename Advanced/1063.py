n = input()
sets = []
for i in xrange(n):
    sets.append(set([int(i) for i in raw_input().split()][1:]))
for i in xrange(input()):
    a, b = [int(i) - 1 for i in raw_input().split()]
    print '{:.1f}%'.format(len(sets[a].intersection(sets[b])) * 100.0 / len(sets[a].union(sets[b])))