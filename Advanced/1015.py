def is_prime(n):
    return all(n % i for i in xrange(2, int(n ** 0.5) + 1)) if n >= 2 else False


def int_to_str(num, radix):
    result = ''
    while num:
        result += str(num % radix)
        num /= radix
    return result[::-1]


while True:
    string = raw_input()
    if string.startswith('-'):
        break
    num, radix = [int(i) for i in string.split()]
    num_reverse = int(int_to_str(num, radix)[::-1], radix)
    print 'Yes' if is_prime(num) and is_prime(num_reverse) else 'No'