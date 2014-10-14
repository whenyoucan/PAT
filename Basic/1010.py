n = [int(i) for i in raw_input().split()]
flag = False
for i in range(0, len(n), 2):
    if n[i + 1] != 0:
        flag = True
        print n[i] * n[i + 1], n[i + 1] - 1,
if not flag:
    print 0, 0,