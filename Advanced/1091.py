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

    def count(self, threshold):
        return sum([-i for i in self.set if i <= -threshold])


m, n, l, t = [int(i) for i in raw_input().split()]
slices = [[[] for i in xrange(m)] for i in xrange(l)]
for i in xrange(l):
    for j in xrange(m):
        slices[i][j] = raw_input().split()
s = DisjointSet(m * n * l)
num_of_0 = 0
for li in xrange(l):
    for mi in xrange(m):
        for ni in xrange(n):
            if slices[li][mi][ni] == '0':
                num_of_0 += 1
                continue
            if ni - 1 >= 0 and slices[li][mi][ni - 1] == '1':
                s.union(li * m * n + mi * n + ni, li * m * n + mi * n + (ni - 1))
            if mi - 1 >= 0 and slices[li][mi - 1][ni] == '1':
                s.union(li * m * n + mi * n + ni, li * m * n + (mi - 1) * n + ni)
            if li - 1 >= 0 and slices[li - 1][mi][ni] == '1':
                s.union(li * m * n + mi * n + ni, (li - 1) * m * n + mi * n + ni)
if t > 1:
    print s.count(t)
else:
    print s.count(t) - num_of_0