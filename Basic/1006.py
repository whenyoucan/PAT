num_list = [int(i) for i in '00' + raw_input()]
print 'B' * num_list[-3] + 'S' * num_list[-2] + ''.join(map(str, range(1, num_list[-1] + 1, 1)))