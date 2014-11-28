toll_of_hour = [int(i) / 100.0 for i in raw_input().split()]


def calc_bill(start_time, end_time):
    d1, h1, mm1 = [int(i) for i in start_time.split(':')]
    d2, h2, mm2 = [int(i) for i in end_time.split(':')]
    amount, last = 0, 0
    while not (d1 == d2 and h1 == h2 and mm1 == mm2):
        amount += toll_of_hour[h1]
        mm1 += 1
        last += 1
        if mm1 == 60:
            h1 += 1
            mm1 = 0
        if h1 == 24:
            d1 += 1
            h1 = 0
    return amount, last


customers = {}
for i in xrange(input()):
    name, time, event = raw_input().split()
    if name in customers:
        customers[name].append((time, event))
    else:
        customers[name] = [(time, event)]
for name, records in sorted(customers.items(), key=lambda x: x[0]):
    records.sort(key=lambda x: x[0])
    valid_indices = filter(
        lambda i: i + 1 < len(records) and records[i + 1][1].startswith('off') if records[i][1].startswith('on')
        else i - 1 >= 0 and records[i - 1][1].startswith('on'), xrange(len(records)))
    records = [records[i] for i in valid_indices]
    if records:
        print name, records[0][0][:2]
        total_amount = 0
        for i in xrange(0, len(records), 2):
            start_time = records[i][0][3:]
            end_time = records[i + 1][0][3:]
            amount, last = calc_bill(start_time, end_time)
            print start_time, end_time, last, '${:.2f}'.format(amount)
            total_amount += amount
        print 'Total amount: ${:.2f}'.format(total_amount)