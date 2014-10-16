# coding=utf-8
# 此题会有case超时
cur_addr, n, k = [int(i) for i in raw_input().split()]
d = {}
for i in xrange(int(n)):
    addr, data, nxt = [int(i) for i in raw_input().split()]
    d[addr] = [data, nxt]
order = []
while cur_addr != -1:
    order.append(cur_addr)
    cur_addr = d[cur_addr][1]
for i in xrange(0, len(order) - len(order) % k, k):
    order[i:i + k] = order[i:i + k][::-1]
for i in xrange(0, len(order)):
    if i + 1 < len(order):
        print '{:0>5} {} {:0>5}'.format(order[i], d[order[i]][0], order[i + 1])
    else:
        print '{:0>5} {} -1'.format(order[i], d[order[i]][0])