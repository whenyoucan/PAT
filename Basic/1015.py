n, l, h = [int(i) for i in raw_input().split()]
sr, jz, yr, xr = [], [], [], []
for i in xrange(n):
    info = raw_input().split()
    d, c = int(info[1]), int(info[2])
    info[1] = d
    info[2] = c
    if d >= l and c >= l:
        if d >= h and c >= h:
            sr.append(info)
        elif d >= h and c < h:
            jz.append(info)
        elif d >= c:
            yr.append(info)
        else:
            xr.append(info)
print len(sr) + len(jz) + len(yr) + len(xr)
sr.sort(key=lambda x: (-x[1] - x[2], -x[1], x[0]))
jz.sort(key=lambda x: (-x[1] - x[2], -x[1], x[0]))
yr.sort(key=lambda x: (-x[1] - x[2], -x[1], x[0]))
xr.sort(key=lambda x: (-x[1] - x[2], -x[1], x[0]))
for info in sr + jz + yr + xr:
    print info[0], info[1], info[2]