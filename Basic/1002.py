num_str = raw_input()
num_lst = [int(c) for c in num_str]
sum_num = sum(num_lst)
sum_str = str(sum_num)
map_digit_char_to_pinyin = {'0': 'ling',
                            '1': 'yi',
                            '2': 'er',
                            '3': 'san',
                            '4': 'si',
                            '5': 'wu',
                            '6': 'liu',
                            '7': 'qi',
                            '8': 'ba',
                            '9': 'jiu'}
for digit_char in sum_str:
    print map_digit_char_to_pinyin[digit_char],