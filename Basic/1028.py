valid_birthday_num = 0
valid_birthday_min = '1814/09/06'
valid_birthday_max = '2014/09/06'
oldest_name = ''
oldest_birthday = valid_birthday_max
youngest_name = ''
youngest_birthday = valid_birthday_min
for i in xrange(input()):
    name, birthday = raw_input().split()
    if valid_birthday_min <= birthday <= valid_birthday_max:
        valid_birthday_num += 1
        if birthday >= youngest_birthday:
            youngest_birthday = birthday
            youngest_name = name
        if birthday <= oldest_birthday:
            oldest_birthday = birthday
            oldest_name = name

print ' '.join([str(valid_birthday_num), oldest_name, youngest_name]).strip()