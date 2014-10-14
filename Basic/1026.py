def calc_hhmmss(second):
    hh = second / 3600
    second %= 3600
    mm = second / 60
    second %= 60
    ss = second
    return hh, mm, ss


c1, c2 = raw_input().split()
c = int(c2) - int(c1)
c = int(c / 100.0 + 0.5)
print ':'.join(str(i).rjust(2, '0') for i in calc_hhmmss(c))