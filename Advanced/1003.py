from Queue import PriorityQueue

N, M, C1, C2 = [int(i) for i in raw_input().split()]

cities = [{'rescue_team_num': int(i),
           'neighbors': []}
          for i in raw_input().split()]

for i in xrange(M):
    c1, c2, l = [int(i) for i in raw_input().split()]
    cities[c1]['neighbors'].append((c2, l))
    cities[c2]['neighbors'].append((c1, l))

q = PriorityQueue()
dis = [2 ** 32] * N
dis[C1] = 0
cnt = [1] * N
num = [i['rescue_team_num'] for i in cities]
q.put((0, C1))
while not q.empty():
    cur = q.get()
    x = cur[1]
    if cur[0] > dis[x]:
        continue
    for i in xrange(0, len(cities[x]['neighbors'])):
        y = cities[x]['neighbors'][i][0]
        d = cities[x]['neighbors'][i][1]
        if dis[x] + d < dis[y]:
            dis[y] = dis[x] + d
            q.put((dis[y], y))
            num[y] = num[x] + cities[y]['rescue_team_num']
            cnt[y] = cnt[x]
        elif dis[x] + d == dis[y]:
            num[y] = max(num[y], num[x] + cities[y]['rescue_team_num'])
            cnt[y] += cnt[x]

print cnt[C2], num[C2]