def primes(n):
    p = [True] * (n + 1)
    for i in xrange(2, int(n ** 0.5) + 1):
        if p[i]:
            p[i + i::i] = [False] * (n / i - 1)
    return [i for i in xrange(2, n + 1) if p[i]]

# def primes(n):
#     p = [1] * (n / 2)
#     for i in xrange(3, int(n ** 0.5) + 1, 2):
#         if p[i / 2]:
#             p[i * i / 2::i] = [0] * ((n - i * i - 1) / (2 * i) + 1)
#     return [2] + [2 * i + 1 for i in xrange(1, n / 2) if p[i]]

prime_list = primes(150000)
nums = [int(i) for i in raw_input().split()]
m, n, count = nums[0], nums[1], 0
for i in xrange(m, n + 1):
    count += 1
    if count == 10:
        count = 0
        print prime_list[i - 1]
    else:
        print prime_list[i - 1],