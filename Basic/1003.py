import re


def is_good_str(the_str):
    if not all([c in 'PAT' for c in the_str]):
        return False
    if the_str.count('P') != 1 or the_str.count('T') != 1 or the_str.index('T') < the_str.index('P'):
        return False
    parts = re.split('[PT]', the_str)
    a = len(parts[0])
    b = len(parts[1])
    c = len(parts[2])
    return is_good_abc(a, b, c)


def is_good_abc(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return False
    elif a == c and b == 1:
        return True
    else:
        return is_good_abc(a, b - 1, c - a)


n = int(raw_input())
for i in range(n):
    s = raw_input()
    if is_good_str(s):
        print 'YES'
    else:
        print 'NO'