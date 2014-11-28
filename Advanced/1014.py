def print_time(time):
    if time:
        hh, mm = time / 60 + 8, time % 60
        print '{:02}:{:02}'.format(hh, mm)
    else:
        print 'Sorry'


num_of_windows, max_length_of_window, num_of_customers, num_of_queries = [int(i) for i in raw_input().split()]
customers = list(enumerate([int(i) for i in raw_input().split()]))
windows = [[] for i in xrange(num_of_windows)]
served_times = [None for i in xrange(num_of_customers)]
close_time = (17 - 8) * 60
for time_offset in xrange(close_time):
    for window in filter(None, windows):
        customer_id, remain_time = window[0]
        if remain_time > 1:
            window[0] = (customer_id, remain_time - 1)
        else:
            window.pop(0)
            served_times[customer_id] = time_offset
    while customers and any(len(window) < max_length_of_window for window in windows):
        free_window_index = sorted(enumerate(windows), key=lambda x: (len(x[1]), x[0]))[0][0]
        customer = customers.pop(0)
        windows[free_window_index].append(customer)
for window in filter(None, windows):
    customer_id, remain_time = window.pop(0)
    served_times[customer_id] = close_time + remain_time - 1
for query in [int(i) for i in raw_input().split()]:
    print_time(served_times[query - 1])