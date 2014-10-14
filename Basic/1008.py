l, n = [int(i) for i in raw_input().split()]
num_list = [int(i) for i in raw_input().split()] * 2
for i in range(l - n, 2 * l - n):
    print num_list[i],