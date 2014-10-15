cur_addr, n, k = raw_input().split()
n, k = int(n), int(k)
d = {}
for i in xrange(int(n)):
    addr, data, nxt = raw_input().split()
    d[addr] = {'addr': addr, 'data': data, 'next': nxt}
l = []
while cur_addr != '-1':
    l.append(d[cur_addr])
    cur_addr = d[cur_addr]['next']
for idx in xrange(0, len(l) - len(l) % k, k):
    l[idx:idx + k] = l[idx:idx + k][::-1]
for idx in xrange(0, len(l)):
    if idx + 1 < len(l):
        l[idx]['next'] = l[idx + 1]['addr']
    else:
        l[idx]['next'] = '-1'
for i in l:
    print '{} {} {}'.format(i['addr'], i['data'], i['next'])