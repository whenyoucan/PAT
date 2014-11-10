# coding=utf-8
raw_input()
nums = [int(i) for i in raw_input().split()]

max_seq = []
max_sum = -1  # 如果初始化为0，(-1, 0, -1)这种case会出错

cur_seq = []
cur_sum = 0

for index, num in enumerate(nums):
    cur_seq.append(num)
    cur_sum += num
    if cur_sum > max_sum:
        max_sum = cur_sum
        max_seq = cur_seq[:]
    elif cur_sum < 0:
        cur_sum = 0
        cur_seq = []
if all([n < 0 for n in nums]):
    print 0, nums[0], nums[-1]
else:
    print max_sum, max_seq[0], max_seq[-1]