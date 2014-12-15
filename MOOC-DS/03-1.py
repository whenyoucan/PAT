def value(coefficients, x):
    return sum([coefficients[i] * (x ** i) for i in xrange(len(coefficients))])


def find_root(coefficients, a, b):
    middle = (a + b) / 2
    if b - a < 0.001:
        return middle
    for attempt in [a, b, middle]:
        if value(coefficients, attempt) == 0:
            return attempt
    if (value(coefficients, middle) > 0) == (value(coefficients, a) > 0):
        return find_root(coefficients, middle, b)
    else:
        return find_root(coefficients, a, middle)


coefficients = [float(i) for i in raw_input().split()][::-1]
a, b = [float(i) for i in raw_input().split()]
print '{:.2f}'.format(find_root(coefficients, a, b))