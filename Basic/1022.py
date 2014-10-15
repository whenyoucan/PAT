args = [int(i) for i in raw_input().split()]
n, d = args[0] + args[1], args[2]
result = ''
if n:
    while n != 0:
        result = str(n % d) + result
        n /= d
else:
    result = '0'
print result