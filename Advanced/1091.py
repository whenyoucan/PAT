m, n, l, t = [int(i) for i in raw_input().split()]
slices = [[[] for i in xrange(m)] for i in xrange(l)]
for i in xrange(l):
    for j in xrange(m):
        slices[i][j] = raw_input().split()
total_volume = 0
for i in xrange(l):
    for j in xrange(m):
        for k in xrange(n):
            if slices[i][j][k] != '1':
                continue
            volume = 0
            q = [(i, j, k)]
            while q:
                i, j, k = q[-1]
                q.pop()
                if slices[i][j][k] != '1':
                    continue
                slices[i][j][k] = -1
                volume += 1
                if i - 1 >= 0 and slices[i - 1][j][k] == '1':
                    q.append((i - 1, j, k))
                if i + 1 < l and slices[i + 1][j][k] == '1':
                    q.append((i + 1, j, k))
                if j - 1 >= 0 and slices[i][j - 1][k] == '1':
                    q.append((i, j - 1, k))
                if j + 1 < m and slices[i][j + 1][k] == '1':
                    q.append((i, j + 1, k))
                if k - 1 >= 0 and slices[i][j][k - 1] == '1':
                    q.append((i, j, k - 1))
                if k + 1 < n and slices[i][j][k + 1] == '1':
                    q.append((i, j, k + 1))
            if volume >= t:
                total_volume += volume
print total_volume