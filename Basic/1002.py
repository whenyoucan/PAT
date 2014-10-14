sum_str = str(sum([int(i) for i in raw_input()]))
map_digit_to_pinyin = {'0': 'ling',
                       '1': 'yi',
                       '2': 'er',
                       '3': 'san',
                       '4': 'si',
                       '5': 'wu',
                       '6': 'liu',
                       '7': 'qi',
                       '8': 'ba',
                       '9': 'jiu'}
print ' '.join([map_digit_to_pinyin[digit] for digit in sum_str])