# coding=utf-8
class DisjointSet:
    def __init__(self, size):
        self.set = [-1 for i in xrange(size)]

    def union_root(self, root1, root2):  # by tree size
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


N, M, K = [int(i) for i in raw_input().split()]
roads = set()
for i in xrange(M):
    source, target = [int(i) - 1 for i in raw_input().split()]
    if source > target:
        source, target = target, source
    roads.add((source, target))
for lost_city in [int(i) - 1 for i in raw_input().split()]:
    s = DisjointSet(N)
    for r in roads:
        if lost_city in r:
            continue
        s.union(r[0], r[1])
    remain = s.count() - 1
    print remain - 1 if remain > 0 else 0