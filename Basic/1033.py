broken_keys = set(raw_input())
all_chars = raw_input()
if '+' in broken_keys:
    output_chars = [c for c in all_chars if not c.isupper() and c.upper() not in broken_keys]
else:
    output_chars = [c for c in all_chars if c.upper() not in broken_keys]
print ''.join(output_chars)