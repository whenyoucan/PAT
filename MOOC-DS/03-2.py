n = input()
nodes = [[] for i in xrange(n)]
for i in xrange(n):
    left, right = [int(c) if c != '-' else None for c in raw_input().split()]
    nodes[i] = [left, right]
q = [i for i in xrange(n) if i not in set(sum(nodes, []))]
while q:
    cur_node = q.pop(0)
    left, right = nodes[cur_node]
    if left is not None:
        q.append(left)
    if right is not None:
        q.append(right)
    if left is None and right is None:
        print cur_node,