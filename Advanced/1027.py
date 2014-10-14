import string


def convert(old_base, old_str, new_base):
    n = 0
    chars = string.digits + string.uppercase
    for c in old_str:
        n = n * old_base + chars.index(c)
    new_str = ''
    while n:
        new_str = chars[n % new_base] + new_str
        n /= new_base
    return new_str


r, g, b = raw_input().split()
print ''.join(['#',
               convert(10, r, 13).rjust(2, '0'),
               convert(10, g, 13).rjust(2, '0'),
               convert(10, b, 13).rjust(2, '0')])