import re


def is_good_str(the_str):
    if re.match(r'A*PA*TA*$', the_str) is None:
        return False
    a, b, c = re.split('[PT]', the_str)
    return is_good_abc(len(a), len(b), len(c))


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