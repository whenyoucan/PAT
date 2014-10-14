a, da, b, db = raw_input().split()
a = '0' + filter(lambda x: x == da, a)
b = '0' + filter(lambda x: x == db, b)
print int(a) + int(b)