from Queue import PriorityQueue

first_line_params = raw_input().split()
num_of_cities = int(first_line_params[0])
num_of_routes = int(first_line_params[1])
name_of_starting_city = first_line_params[2]

cities = [{'name': name_of_starting_city,
           'happiness': 0,
           'neighbors': []}]
pre = [[]] * num_of_cities

map_city_name_to_index = {name_of_starting_city: 0}

for i in xrange(num_of_cities - 1):
    city_params = raw_input().split()
    city_name = city_params[0]
    city_happiness = int(city_params[1])
    cities.append({
        'name': city_name,
        'happiness': city_happiness,
        'neighbors': []
    })
    map_city_name_to_index[city_name] = len(cities) - 1

for i in xrange(num_of_routes):
    route_params = raw_input().split()
    source_city_name = route_params[0]
    target_city_name = route_params[1]
    source_city_index = map_city_name_to_index[source_city_name]
    target_city_index = map_city_name_to_index[target_city_name]
    cost = int(route_params[2])
    cities[source_city_index]['neighbors'].append((target_city_index, cost))
    cities[target_city_index]['neighbors'].append((source_city_index, cost))

q = PriorityQueue()
dis = [2 ** 32] * num_of_cities
dis[0] = 0
q.put((0, 0))
while not q.empty():
    cur = q.get()
    x = cur[1]
    if cur[0] > dis[x]:
        continue
    for i in xrange(0, len(cities[x]['neighbors'])):
        y = cities[x]['neighbors'][i][0]
        d = cities[x]['neighbors'][i][1]
        if dis[x] + d < dis[y]:
            dis[y] = dis[x] + d
            q.put((dis[y], y))
            pre[y] = [x]
        elif dis[x] + d == dis[y]:
            pre[y].append(x)


def build_paths_from_pres(pre, source_index, target_index):
    if source_index == target_index:
        return [[source_index]]
    result = []
    for last in pre[target_index]:
        last_paths = build_paths_from_pres(pre, source_index, last)
        for last_path in last_paths:
            result.append(last_path + [target_index])
    return result


def calc_sum_happiness_from_path(path):
    return sum([cities[i]['happiness'] for i in path])


def calc_avg_happiness_from_path(path):
    return sum([cities[i]['happiness'] for i in path]) / (len(path) - 1)


target_city_index = map_city_name_to_index['ROM']
paths = build_paths_from_pres(pre, 0, target_city_index)

paths = [{'path': x,
          'sum_h': calc_sum_happiness_from_path(x),
          'avg_h': calc_avg_happiness_from_path(x)}
         for x in paths]

paths = sorted(paths, key=lambda x: (-x['sum_h'], -x['avg_h']))

the_num_of_diff_paths = len(paths)
the_cost = dis[target_city_index]
the_happiness = paths[0]['sum_h']
the_avg_happiness = paths[0]['avg_h']
print the_num_of_diff_paths, the_cost, the_happiness, the_avg_happiness
print '->'.join(cities[i]['name'] for i in paths[0]['path'])