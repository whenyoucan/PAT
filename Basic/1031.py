import string

weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
z_to_m = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
all_passed = True
for num in xrange(input()):
    id_str = raw_input()
    if any([c not in string.digits for c in id_str[:17]]):
        all_passed = False
        print id_str
        continue
    m = z_to_m[sum([int(id_str[i]) * weights[i] for i in xrange(17)]) % 11]
    if m != id_str[-1]:
        all_passed = False
        print id_str
if all_passed:
    print 'All passed'