args = raw_input().split(' ')
h = int(args[0])
n = int(args[1])
k = int(args[2])

nodes = [[0, -1] for i in xrange(100000)]
for i in xrange(n):
    info = raw_input().split(' ')
    addr = int(info[0])
    nodes[addr][0] = int(info[1])
    nodes[addr][1] = int(info[2])

orders = []
while h != -1:
    orders.append(h)
    if len(orders) % k == 0:
        temp = orders[-k:]
        orders[-k:] = temp[::-1]
    h = nodes[h][1]

for index, i in enumerate(orders):
    if i != orders[-1]:
        nxt = orders[index + 1]
    else:
        nxt = -1
    if nxt != -1:
        print "%05d %d %05d" % (i, nodes[i][0], nxt)
    else:
        print "%05d %d -1" % (i, nodes[i][0])