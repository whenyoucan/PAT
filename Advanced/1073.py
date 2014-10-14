original = raw_input().split('E')
real = original[0]
expo = int(original[1])
positive = real[0] == '+'
real = [i for i in real[1:]]
real.remove('.')
if expo > 0:
    if len(real) <= expo + 1:
        real += ['0'] * (expo + 1 - len(real))
    else:
        real.insert(1 + expo, '.')
else:
    real = ['0'] * (-expo) + real
    real.insert(1, '.')
real = ''.join(real)
if not positive:
    real = '-' + real
print real