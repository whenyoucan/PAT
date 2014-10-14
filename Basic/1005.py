raw_input()
nums = {int(i) for i in raw_input().split()}
for n in nums.copy():
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n + 1) / 2
        if n in nums:
            nums.remove(n)
print ' '.join([str(i) for i in sorted(list(nums), reverse=True)])