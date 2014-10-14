vips = {}
n, k = map(int, raw_input().split())
for i in xrange(n):
    id_num, distance = raw_input().split()
    distance = int(distance)
    if id_num not in vips:
        if distance < k:
            vips[id_num] = k
        else:
            vips[id_num] = distance
    else:
        if distance < k:
            vips[id_num] += k
        else:
            vips[id_num] += distance
m = int(raw_input())
for i in xrange(m):
    query_id = raw_input()
    if query_id in vips:
        print vips[query_id]
    else:
        print "No Info"