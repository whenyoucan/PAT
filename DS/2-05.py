n = raw_input()
nums = map(float, raw_input().split())
avg = sum(nums) / len(nums)
print "%.5f" % (sum(map(lambda x: (x - avg) ** 2, nums)) / len(nums)) ** 0.5