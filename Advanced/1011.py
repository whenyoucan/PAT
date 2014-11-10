odd = 1.0
for i in xrange(3):
    odds = [float(i) for i in raw_input().split()]
    odd *= max(odds)
    print 'WTL'[odds.index(max(odds))],
print '{:.2f}'.format((odd * 0.65 - 1) * 2)