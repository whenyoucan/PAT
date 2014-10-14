def GCD(a, b):
    a, b = max(abs(a), abs(b)), min(abs(a), abs(b))
    if 0 in (a, b):
        return 1
    while a % b:
        a, b = b, a % b
    return b


def simplify(n):
    gcd = GCD(n[0], n[1])
    n = (n[0] / gcd, n[1] / gcd)
    return n


def sum_of_rational_nums(a, b):
    result = (a[0] * b[1] + a[1] * b[0], a[1] * b[1])
    result = simplify(result)
    return result


raw_input()
nums = raw_input().split(' ')
the_sum = (0, 1)
for n in nums:
    the_num = tuple([int(i) for i in n.split('/')])
    the_sum = sum_of_rational_nums(the_sum, the_num)
if the_sum[0] == 0:
    print '0'
if the_sum[0] / the_sum[1] != 0:
    print the_sum[0] / the_sum[1],
if the_sum[0] % the_sum[1] != 0:
    print str(the_sum[0] % the_sum[1]) + '/' + str(the_sum[1])