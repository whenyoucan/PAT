def is_binary_search_tree(nodes, root, min_bound, max_bound):
    if nodes[root][0] <= min_bound:
        return False
    if nodes[root][0] >= max_bound:
        return False
    left_child = nodes[root][2]
    right_child = nodes[root][3]
    if left_child == -1 and right_child == -1:
        return True
    elif right_child == -1:
        return is_binary_search_tree(nodes, left_child, min_bound, nodes[root][0])
    elif left_child == -1:
        return is_binary_search_tree(nodes, right_child, nodes[root][0], max_bound)
    else:
        return is_binary_search_tree(nodes, left_child, min_bound, nodes[root][0]) \
            and is_binary_search_tree(nodes, right_child, nodes[root][0], max_bound)


def is_min_heap(nodes, n):
    for i in xrange(n):
        if nodes[i][2] != -1 and nodes[nodes[i][2]][1] <= nodes[i][1]:
            return False
        if nodes[i][3] != -1 and nodes[nodes[i][3]][1] <= nodes[i][1]:
            return False
    return True


n = int(raw_input().strip())
nodes = [[0, 0, 0, 0]] * n
root = 0
for i in xrange(n):
    nodes[i] = map(int, raw_input().split(' '))
    if nodes[i][2] == root or nodes[i][3] == root:
        root = i
if is_binary_search_tree(nodes, root, -100000000, 100000000) and is_min_heap(nodes, n):
    print "YES"
else:
    print "NO"