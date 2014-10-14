n = int(raw_input())
root = 2
flag = False
result = '%d=' % n
if n == 1:
    result += '1'
while n != 1:
    count = 0
    while n % root == 0:
        count += 1
        n /= root
    if count:
        if flag:
            result += '*'
        if count > 1:
            result += '%d^%d' % (root, count)
        else:
            result += '%d' % root
        flag = True
    root += 1
print result