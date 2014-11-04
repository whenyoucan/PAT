num_str = raw_input()
flag = num_str[0]
coe_str, exp_str = num_str[1:].split('E')
offset = int(exp_str)
fraction_len = len(coe_str.split('.')[1])
coe_str = coe_str.replace('.', '')
if offset < 0:  # e.g. -1.234E-2
    result = '0.' + '0' * (-offset - 1) + coe_str
elif offset < fraction_len:  # e.g. -1.234E+2
    result = coe_str[:offset - fraction_len] + '.' + coe_str[offset - fraction_len:]
else:  # e.g. -1.2E+10
    result = coe_str + '0' * (offset - fraction_len)
print '{f}{num}'.format(f=flag if flag == '-' else '', num=result)