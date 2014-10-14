def list_primes(the_range):
    p = [True] * (the_range + 1)
    for i in xrange(2, int(the_range ** 0.5) + 1):
        if p[i]:
            p[i + i::i] = [False] * (the_range / i - 1)
    return [i for i in xrange(2, the_range + 1) if p[i]]


n = int(raw_input())
primes = set(list_primes(n))
prime_pairs = [(i, i + 2) for i in primes if i + 2 in primes]
print len(prime_pairs)