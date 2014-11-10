import itertools

poly_a = raw_input().split()[1:]
poly_b = raw_input().split()[1:]
poly_a = {int(poly_a[i]): float(poly_a[i + 1]) for i in xrange(0, len(poly_a), 2)}
poly_b = {int(poly_b[i]): float(poly_b[i + 1]) for i in xrange(0, len(poly_b), 2)}
poly_c = {}
for exp_a, exp_b in itertools.product(poly_a, poly_b):
    if exp_a + exp_b not in poly_c:
        poly_c[exp_a + exp_b] = poly_a[exp_a] * poly_b[exp_b]
    else:
        poly_c[exp_a + exp_b] += poly_a[exp_a] * poly_b[exp_b]
poly_c = {exp: coe for (exp, coe) in poly_c.items() if coe != 0}
if len(poly_c) == 0:
    poly_c = {0: 0}
print len(poly_c),
for exp, coe in sorted(poly_c.items(), reverse=True):
    print '{} {:.1f}'.format(exp, coe),