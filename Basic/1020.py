n, d = [int(i) for i in raw_input().split()]
cakes = [{} for i in xrange(n)]
stocks = [float(f) for f in raw_input().split()]
total_prices = [float(f) for f in raw_input().split()]
for i in xrange(n):
    cakes[i]['stock'] = stocks[i]
    cakes[i]['unit_price'] = total_prices[i] / stocks[i]
cakes.sort(key=lambda x: -x['unit_price'])
cur_d, cur_price = 0, 0
for i in xrange(n):
    cake = cakes[i]
    if cur_d + cake['stock'] < d:
        cur_d += cake['stock']
        cur_price += cake['stock'] * cake['unit_price']
    else:
        cur_price += (d - cur_d) * cake['unit_price']
        break
print '{:.2f}'.format(cur_price)