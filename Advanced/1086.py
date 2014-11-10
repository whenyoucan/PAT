def build_tree(in_order, pre_order):
    if len(pre_order) <= 0:
        return {}
    node = pre_order.pop(0)
    pivot = in_order.index(node)
    left_inorder = in_order[:pivot]
    right_inorder = in_order[pivot + 1:]
    left_preorder = []
    right_preorder = []
    for i in pre_order:
        if i in left_inorder:
            left_preorder.append(i)
        else:
            right_preorder.append(i)
    return {
        'value': node,
        'left': build_tree(left_inorder, left_preorder),
        'right': build_tree(right_inorder, right_preorder),
    }


def print_post_order(tree):
    if tree != {}:
        print_post_order(tree['left'])
        print_post_order(tree['right'])
        print tree['value'],


N = input()
pre_order = []
in_order = []
post_order = []
stack = []
for i in xrange(2 * N):
    operation = raw_input()
    if operation.startswith('Push'):
        num = int(operation.split()[-1])
        stack.append(num)
        pre_order.append(num)
    else:
        in_order.append(stack.pop())
tree = build_tree(in_order, pre_order)
print_post_order(tree)