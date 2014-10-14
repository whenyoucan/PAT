def list_primes(the_range):
    p = [True] * (the_range + 1)
    for i in xrange(2, int(the_range ** 0.5) + 1):
        if p[i]:
            p[i + i::i] = [False] * (the_range / i - 1)
    return [i for i in xrange(2, the_range + 1) if p[i]]


m, n = [int(i) for i in raw_input().split()]
primes = list_primes(150000)[m - 1:n]

for idx in xrange(0, len(primes), 10):
    print ' '.join([str(i) for i in primes[idx:idx + 10]])