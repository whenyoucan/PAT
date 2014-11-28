result = ''.join(sorted(raw_input().split()[1:], cmp=lambda x, y: cmp(x + y, y + x))).lstrip('0')
print result if result else '0'