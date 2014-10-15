n = '{:0>4}'.format(raw_input())
while True:
    a = int(''.join(sorted(n, reverse=True)))
    b = int(''.join(sorted(n)))
    result = a - b
    print "{:0>4} - {:0>4} = {:0>4}".format(a, b, result)
    if result == 0 or result == 6174:
        break
    n = '{:0>4}'.format(result)