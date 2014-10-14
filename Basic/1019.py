n = raw_input().rjust(4, '0')
while True:
    a = int(''.join(sorted(n, reverse=True)))
    b = int(''.join(sorted(n)))
    result = a - b
    print "%04d - %04d = %04d" % (a, b, result)
    if result == 0 or result == 6174:
        break
    n = "%04d" % result