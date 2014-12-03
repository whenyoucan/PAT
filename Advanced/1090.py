args = raw_input().split()
n = int(args[0])
p = float(args[1])
r = float(args[2])
indices = [int(i) for i in raw_input().split()]
tree = [[indices[i], []] for i in xrange(n)]
root = 0
for i in xrange(n):
    if indices[i] == -1:
        root = i
        continue
    tree[indices[i]][1].append(i)
cur_level = [root]
cur_price = p
num_of_retailers = 1
while True:
    temp = cur_level
    cur_level = []
    for i in temp:
        cur_level += tree[i][1]
    if not cur_level:
        break
    cur_price = (1 + r / 100.0) * cur_price if cur_price else p
    num_of_retailers = len(cur_level)
print '{:.2f}'.format(cur_price), num_of_retailers