n = raw_input()
digit_counts = [(d, n.count(str(d))) for d in xrange(10) if n.count(str(d))]
print '\n'.join(['{}:{}'.format(x[0], x[1]) for x in digit_counts])