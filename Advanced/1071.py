import re

words = {}
s = raw_input().lower()
for w in re.findall(r'([0-9a-z]+)', s):
    if w in words:
        words[w] += 1
    else:
        words[w] = 1
max_word, max_count = sorted(words.items(), key=lambda x: -x[1])[0]
print max_word, max_count