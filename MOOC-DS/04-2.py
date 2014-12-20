# coding=utf-8
from time import sleep


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
s = DisjointSet(n)
while True:
    the_input = raw_input()
    if the_input.startswith('S'):
        break
    args = the_input.split()

    # 这题巨坑，input里有一行是类似 C 3 2I 3 2，也就是少了个换行符，我试了60多次才试出来
    if len(args) == 5 and args[0] == 'C':
        the_inputs = the_input.split('I')
        the_inputs[1] = 'I' + the_inputs[1]
        for the_input in the_inputs:
            op, c1, c2 = the_input.split()
            c1, c2 = int(c1) - 1, int(c2) - 1
            if op == 'I':
                s.union(c1, c2)
            elif op == 'C':
                print 'yes' if s.find(c1) == s.find(c2) else 'no'

    else:
        op, c1, c2 = the_input.split()
        c1, c2 = int(c1) - 1, int(c2) - 1
        if op == 'I':
            s.union(c1, c2)
        elif op == 'C':
            print 'yes' if s.find(c1) == s.find(c2) else 'no'
num_of_components = s.count()
if num_of_components == 1:
    print 'The network is connected.'
else:
    print 'There are {} components.'.format(num_of_components)