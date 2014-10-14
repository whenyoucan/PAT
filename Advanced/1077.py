def common_tail(x, y):
    result = ''
    for i in xrange(1, min(len(x), len(y)) + 1):
        if x[-i] != y[-i]:
            break
        result += x[-i]
    return result[::-1]


n = int(raw_input())
lines = [raw_input() for i in xrange(n)]
lines.sort(key=lambda x: len(x))
kuchiguse = reduce(common_tail, lines)
if len(kuchiguse):
    print kuchiguse
else:
    print 'nai'