def is_prime(n):
    if n == 1:
        return False
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


m = int(raw_input().split()[0])
nums = [int(i) for i in raw_input().split()]
while not is_prime(m):
    m += 1
table = [-1] * m
for n in nums:
    inserted = False
    for i in xrange(m):
        index = (n + i ** 2) % m
        if table[index] == -1:
            table[index] = n
            print index,
            inserted = True
            break
    if not inserted:
        print '-',