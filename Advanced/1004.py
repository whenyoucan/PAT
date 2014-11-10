N, M = [int(i) for i in raw_input().split()]
tree = [[]] * (N + 1)
for i in xrange(M):
    params = [int(i) for i in raw_input().split()]
    parent_id = params[0]
    children_ids = params[2:]
    tree[parent_id] = children_ids
cur_level_nodes = [1]
while cur_level_nodes:
    cur_level_leaf_nodes = filter(lambda x: not tree[x], cur_level_nodes)
    print len(cur_level_leaf_nodes),
    cur_level_nodes = reduce(lambda x, y: set(x) | set(y), [tree[i] for i in cur_level_nodes])