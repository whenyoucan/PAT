nums = [int(i) for i in raw_input().split()]
s = []
for i in xrange(10):
    s += [str(i)] * nums[i]
first_non_zero = filter(lambda x: x != '0', s)[0]
s.remove(first_non_zero)
s = first_non_zero + ''.join(s)
print s