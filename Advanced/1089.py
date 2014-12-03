N = input()
initial_seq = [int(i) for i in raw_input().split()]
partial_seq = [int(i) for i in raw_input().split()]

current_seq = initial_seq[:]
merge_sizes = [2 ** i for i in xrange(1, 8) if 2 ** (i - 1) < N]
# print merge_sizes
matched_merge_sort = False
for merge_size in merge_sizes:
    # print merge_size
    for i in xrange(0, len(initial_seq), merge_size):
        current_seq[i: i + merge_size] = sorted(current_seq[i: i + merge_size])
    # print current_seq
    if matched_merge_sort:
        print ' '.join([str(i) for i in current_seq])
        exit(0)
    if current_seq == partial_seq:
        print 'Merge Sort'
        matched_merge_sort = True
print 'Insertion Sort'
next_index = 0
for i in xrange(N):
    if i + 1 < N and partial_seq[i] > partial_seq[i + 1]:
        next_index = i + 1
        break
partial_seq[0:next_index + 1] = sorted(partial_seq[0:next_index + 1])
print ' '.join([str(i) for i in partial_seq])