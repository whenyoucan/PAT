import string


def first_diff_char(str_a, str_b):
    for i in xrange(0, min(len(str_a), len(str_b))):
        if str_a[i] != str_b[i]:
            return str_a[i]
    return ''


original_string = raw_input()
typed_out_string = raw_input()
worn_out_letters = []

while original_string != typed_out_string:
    diff_char = first_diff_char(original_string, typed_out_string)
    if diff_char in string.ascii_letters:
        worn_out_letters.append(diff_char.upper())
        original_string = original_string.replace(diff_char.upper(), '')
        original_string = original_string.replace(diff_char.lower(), '')
    else:
        worn_out_letters.append(diff_char)
        original_string = original_string.replace(diff_char, '')
print ''.join(worn_out_letters)