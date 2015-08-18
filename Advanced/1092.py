from string import digits, letters

whole_set = {c: 0 for c in digits + letters}
need_set = {c: 0 for c in digits + letters}
whole_string = raw_input()
need_string = raw_input()
for c in whole_string:
    whole_set[c] += 1
for c in need_string:
    need_set[c] += 1
num_of_extra = 0
num_of_missing = 0
to_buy = True
for c in digits + letters:
    whole_num = whole_set[c]
    need_num = need_set[c]
    if need_num <= whole_num:
        num_of_extra += whole_num - need_num
    else:
        to_buy = False
        num_of_missing += need_num - whole_num
if to_buy:
    print 'Yes', num_of_extra
else:
    print 'No', num_of_missing
