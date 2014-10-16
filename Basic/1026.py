c1, c2 = raw_input().split()
c = int(c2) - int(c1)
c = int(c / 100.0 + 0.5)
print '{:0>2}:{:0>2}:{:0>2}'.format(c / 3600, c % 3600 / 60, c % 60)