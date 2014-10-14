nums = [int(i) for i in raw_input().split()][1:]
flags = [False] * 5
a = [0] * 5
a1_flag = True
a3_count = 0
for n in nums:
    if n % 10 == 0:
        flags[0] = True
        a[0] += n
    if n % 5 == 1:
        flags[1] = True
        if a1_flag:
            a[1] += n
        else:
            a[1] -= n
        a1_flag = not a1_flag
    if n % 5 == 2:
        flags[2] = True
        a[2] += 1
    if n % 5 == 3:
        flags[3] = True
        a[3] += n
        a3_count += 1
    if n % 5 == 4 and n > a[4]:
        flags[4] = True
        a[4] = n
if flags[3]:
    a[3] = a[3] * 1.0 / a3_count
for i in range(5):
    if not flags[i]:
        print 'N',
    else:
        if i == 3:
            print "%.1f" % a[3],
        else:
            print a[i],