# coding=utf-8
class DisjointSet:
    def __init__(self, size):
        self.set = [-1 for i in xrange(size)]

    def union_root(self, root1, root2):  # 根据大小合并
        if root1 == root2:
            return
        union_size = self.set[root1] + self.set[root2]
        if self.set[root1] <= self.set[root2]:
            self.set[root2] = root1
            self.set[root1] = union_size
        else:
            self.set[root1] = root2
            self.set[root2] = union_size

    def union(self, key1, key2):
        self.union_root(self.find(key1), self.find(key2))

    def find(self, key):
        if self.set[key] <= -1:
            return key
        else:
            root = self.find(self.set[key])
            self.set[key] = root
            return root

    def count(self):
        return len([i for i in self.set if i < 0])


n = input()
v = DisjointSet(n)
e = []
total_cost = 0

for i in xrange(n * (n - 1) / 2):
    params = raw_input().split()
    x, y, cost, built = int(params[0]) - 1, int(params[1]) - 1, int(params[2]), True if params[3] == '1' else False
    if built:
        v.union(x, y)
    else:
        e.append((x, y, cost))
e.sort(key=lambda x: x[2])
for i in e:
    if v.count() == 1:
        break
    x, y, cost = i
    if v.find(x) != v.find(y):
        v.union(x, y)
        total_cost += cost
print total_cost