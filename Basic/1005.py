n = raw_input()
num_list = [int(n) for n in raw_input().split()]
for n in num_list[:]:
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n + 1) / 2
        while n in num_list:
            num_list.remove(n)
num_list.sort(reverse=True)
for n in num_list:
    print n,