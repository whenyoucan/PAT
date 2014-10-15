nums = [int(i) for i in raw_input().split()]
s = ''.join([str(i) * nums[i] for i in xrange(10)])
first_non_zero = filter(lambda x: x != '0', s)[0]
s = first_non_zero + s.replace(first_non_zero, '', 1)
print s