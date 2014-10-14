d, p = map(int, raw_input().split())
if p == 3:
    print d - 1
else:
    print d - (p / 2 + 1)