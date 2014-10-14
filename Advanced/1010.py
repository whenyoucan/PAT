import string


def convert(num_str, index):
    if index == 1:
        return len(num_str)
    result = 0
    for c in num_str:
        result *= index
        result += (string.digits + string.lowercase).index(c)
    return result


def base_index(num_str):
    max_char = max(num_str)
    return (string.digits + string.lowercase).index(max_char)


def try_radix(num_str, known_value, min_radix, max_radix):
    if min_radix == max_radix:
        try_value = convert(num_str, min_radix)
        if try_value == known_value:
            return min_radix
        else:
            return False
    else:
        mid_radix = (min_radix + max_radix) / 2
        try_value = convert(num_str, mid_radix)
        if try_value >= known_value:
            return try_radix(num_str, known_value, min_radix, mid_radix)
        else:
            return try_radix(num_str, known_value, mid_radix + 1, max_radix)


args = raw_input().split()
n1, n2, tag, known_index = args[0], args[1], int(args[2]), int(args[3])
if tag == 2:
    n1, n2 = n2, n1
known_value = convert(n1, known_index)
radix = try_radix(n2, known_value, base_index(n2) + 1, 2147483647)
print radix if radix else 'Impossible'