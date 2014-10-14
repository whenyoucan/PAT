args = [int(i) for i in raw_input().split()]
n, d = args[0] + args[1], args[2]
result = ''
if n == 0:
    print '0'
    exit()
else:
    while n != 0:
        result = str(n % d) + result
        n /= d
print result