floors = [int(i) for i in raw_input().split()[1:]]
time, cur_floor = 0, 0
for f in floors:
    if f > cur_floor:
        time += (f - cur_floor) * 6 + 5
    else:
        time += (cur_floor - f) * 4 + 5
    cur_floor = f
print time