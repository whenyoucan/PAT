nums = [int(i) for i in '{:0>3}'.format(raw_input())]
print ''.join(['B' * nums[0], 'S' * nums[1], '123456789'[:nums[2]]])