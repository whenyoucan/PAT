n = input()
records = [raw_input().split() for i in xrange(n)]
print sorted(records, key=lambda x: x[1])[0][0],
print sorted(records, key=lambda x: x[2])[-1][0]