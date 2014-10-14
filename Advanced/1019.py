def convert(num, radix):
    result = []
    while num:
        result.append(num % radix)
        num /= radix
    return result[::-1]


n, b = [int(i) for i in raw_input().split()]
r = convert(n, b)
if r == r[::-1]:
    print 'YES'
else:
    print 'NO'
print ' '.join([str(i) for i in r])