import re


def is_good_str(the_str):
    m = re.match(r'(A*)P(A*)T(A*)$', the_str)
    if m:
        a = m.group(1)
        b = m.group(2)
        c = m.group(3)
        return is_good_abc(len(a), len(b), len(c))
    else:
        return False


def is_good_abc(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return False
    elif a == c and b == 1:
        return True
    else:
        return is_good_abc(a, b - 1, c - a)


for i in xrange(int(raw_input())):
    if is_good_str(raw_input()):
        print 'YES'
    else:
        print 'NO'