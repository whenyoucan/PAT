n, m = [int(i) for i in raw_input().split()]
nums = [int(i) for i in raw_input().split()]
for i in xrange(- m, n - m):
    print nums[i % n],