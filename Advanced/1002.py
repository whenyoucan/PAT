poly_a = raw_input().split()[1:]
poly_b = raw_input().split()[1:]
poly_a = {int(poly_a[i]): float(poly_a[i + 1]) for i in xrange(0, len(poly_a), 2)}
poly_b = {int(poly_b[i]): float(poly_b[i + 1]) for i in xrange(0, len(poly_b), 2)}
poly_c = poly_a.copy()
for exp, coe in poly_b.items():
    if exp not in poly_c:
        poly_c[exp] = coe
    else:
        poly_c[exp] += coe
poly_c = {exp: coe for (exp, coe) in poly_c.items() if coe != 0}
print len(poly_c),
for exp, coe in sorted(poly_c.items(), reverse=True):
    print '{} {:.1f}'.format(exp, coe),