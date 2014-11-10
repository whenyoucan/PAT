n = str(sum(map(int, list(raw_input()))))
for c in n:
    print ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][int(c)],