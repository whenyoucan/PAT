import re


def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a == 0 or b == 0:
        return 1
    a, b = max(a, b), min(a, b)
    while a % b != 0:
        a, b = a % b, b
        a, b = max(a, b), min(a, b)
    return b


def expr(numerator, denominator):
    if denominator == 0:
        return 'Inf'
    flag = False if numerator < 0 < denominator or numerator > 0 > denominator else True
    numerator, denominator = abs(numerator), abs(denominator)
    the_gcd = gcd(numerator, denominator)
    numerator /= the_gcd
    denominator /= the_gcd
    k, a, b = numerator / denominator, numerator % denominator, denominator
    if k != 0:
        if a != 0:
            result = '{} {}/{}'.format(k, a, b)
        else:
            result = '{}'.format(k)
    else:
        if a != 0:
            result = '{}/{}'.format(a, b)
        else:
            result = '0'
    if flag == False:
        result = '(-{})'.format(result)
    return result


a1, b1, a2, b2 = [int(i) for i in re.split(r'[ /]', raw_input())]
print '{} + {} = {}'.format(expr(a1, b1), expr(a2, b2), expr(a1 * b2 + a2 * b1, b1 * b2))
print '{} - {} = {}'.format(expr(a1, b1), expr(a2, b2), expr(a1 * b2 - a2 * b1, b1 * b2))
print '{} * {} = {}'.format(expr(a1, b1), expr(a2, b2), expr(a1 * a2, b1 * b2))
print '{} / {} = {}'.format(expr(a1, b1), expr(a2, b2), expr(a1 * b2, b1 * a2))