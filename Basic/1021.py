n = raw_input()
for i in xrange(10):
    if n.count(str(i)):
        print "%d:%d" % (i, n.count(str(i)))