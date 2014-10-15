num_str = raw_input()
flag = num_str[0]
coe_str, exp_str = num_str[1:].split('E')
l_1 = len(coe_str.split('.')[1])
l_2 = int(exp_str)
coe_str = coe_str.replace('.', '')
if l_2 < 0:  # e.g:-1.234E-2
    result = '0.' + '0' * (-l_2 - 1) + coe_str
elif l_2 < l_1:  # e.g: -1.234E+2
    result = coe_str[:l_2 - l_1] + '.' + coe_str[l_2 - l_1:]
else:  # e.g: -1.2E+10
    result = coe_str + '0' * (l_2 - l_1)
print '{f}{num}'.format(f=flag if flag == '-' else '', num=result)