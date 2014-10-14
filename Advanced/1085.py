N, p = [int(i) for i in raw_input().split()]
nums = [int(i) for i in raw_input().split()]
d = {}
for n in nums:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
d = sorted(d.items(), key=lambda x: x[0])
max_num = 0
cur_num = 0
cur_head = -1
cur_tail = 0
while cur_tail < len(d):
    cur_head += 1
    if cur_head != 0:
        cur_num -= d[cur_head - 1][1]
    while cur_tail < len(d) and d[cur_head][0] * p >= d[cur_tail][0]:
        cur_num += d[cur_tail][1]
        cur_tail += 1
    if cur_num > max_num:
        max_num = cur_num
print max_num