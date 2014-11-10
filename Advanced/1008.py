floors = [int(i) for i in raw_input().split()[1:]]
cur_floor = 0
total_time = 0
for floor in floors:
    if floor > cur_floor:
        total_time += (floor - cur_floor) * 6 + 5
    else:
        total_time += (cur_floor - floor) * 4 + 5
    cur_floor = floor
print total_time