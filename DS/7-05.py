l1 = sorted(map(int, raw_input().split()[1:]))
l2 = sorted(map(int, raw_input().split()[1:]))
d1, d2 = 0, 0
for i in xrange(min(len(l1), len(l2))):
    if l1[i] * l2[i] > 0:
        d1 += l1[i] * l2[i]
    if l1[-i - 1] * l2[-i - 1] > 0:
        d2 += l1[-i - 1] * l2[-i - 1]
print max(d1, d2)