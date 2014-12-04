all_chars = raw_input().upper()
remaining_chars = raw_input().upper()
broken_chars = set(all_chars).difference(set(remaining_chars))
print ''.join(sorted(list(broken_chars), key=lambda c: all_chars.find(c)))