n, c = raw_input().split()
level = int(((int(n) + 1) / 2) ** 0.5)
for l in range(level, 0, -1) + range(2, level + 1):
    print '{spaces}{chars}'.format(spaces=' ' * (level - l), chars=c * (2 * l - 1))
print int(n) - (level * level * 2 - 1)