ops = {'+': lambda x, y: x + y,
       '-': lambda x, y: x - y,
       '*': lambda x, y: x * y,
       '/': lambda x, y: x / y}


def calc(nums, sum):
    if len(nums) > 1:
        for i in xrange(len(nums)):
            for j in xrange(len(nums)):
                if i == j:
                    continue
                for op in ops:
                    if op == '/' and nums[j]['value'] == 0.0:
                        continue
                    nums_copy = nums[:]
                    del nums_copy[max(i, j)], nums_copy[min(i, j)]
                    nums_copy.append({'value': ops[op](nums[i]['value'], nums[j]['value']),
                                      'expression': '(' + nums[i]['expression'] + op + nums[j]['expression'] + ')'})
                    for attempt in calc(nums_copy, sum):
                        yield attempt
    else:
        if nums[0]['value'] == sum:
            yield nums[0]['expression'][1:-1]


nums = [{'value': float(i),
         'expression': i}
        for i in raw_input().split()]
for result in calc(nums, 24):
    print result