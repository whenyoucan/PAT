people_who_follow = [0 for i in xrange(1000)]
args = raw_input().split(' ')
n = int(args[0])
l = int(args[1])
for i in xrange(n):
    follows = [int(k) - 1 for k in raw_input().split(' ')]
    for j in follows[1:]:
        people_who_follow[j] |= 1 << i

queries = [int(i) - 1 for i in raw_input().split(' ')][1:]
for q in queries:
    follows = 0
    is_old = [False] * 1000
    follows |= 1 << q
    for i in xrange(l):
        for j in [tmp for tmp in xrange(1000) if (follows >> tmp) & 1 and not is_old[tmp]]:
            follows |= people_who_follow[j]
            is_old[j] = True
    print bin(follows).count('1') - 1