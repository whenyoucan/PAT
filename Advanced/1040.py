def is_symmetric(s, begin, end):
    while begin < end:
        if s[begin] != s[end]:
            return False
        begin, end = begin + 1, end - 1
    return True


s = raw_input()
for l in xrange(len(s), 0, -1):
    for i in xrange(0, len(s) - l + 1):
        if is_symmetric(s, i, i + l - 1):
            print l
            exit()