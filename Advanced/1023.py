s = raw_input()
d = str(int(s) * 2)
print 'YES' if sorted(s) == sorted(d) else 'NO'
print d