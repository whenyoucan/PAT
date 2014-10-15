nums = [int(i) for i in raw_input().split()]
old_pairs = zip(*[iter(nums)] * 2)  # [3, 4, -5, 2, 6, 1, -2, 0] -> [(3, 4), (-5, 2), (6, 1), (-2, 0)]
new_pairs = [(i[0] * i[1], i[1] - 1) for i in old_pairs if i[0] * i[1] != 0]
if new_pairs:
    print ' '.join(['{} {}'.format(pair[0], pair[1]) for pair in new_pairs])
else:
    print '0 0'