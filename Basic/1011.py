for i in xrange(int(raw_input())):
    nums = [int(i) for i in raw_input().split()]
    if nums[0] + nums[1] > nums[2]:
        print "Case #%d: true" % (i + 1)
    else:
        print "Case #%d: false" % (i + 1)