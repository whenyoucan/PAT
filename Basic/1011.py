for i in xrange(input()):
    nums = [int(n) for n in raw_input().split()]
    if nums[0] + nums[1] > nums[2]:
        print "Case #{}: true".format(i + 1)
    else:
        print "Case #{}: false".format(i + 1)