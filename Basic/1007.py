prime_list = []


def is_prime(n):
    for i in prime_list:
        if n % i == 0:
            return False
        if i * i > n:
            break
    return True


for i in range(2, 100000):
    if is_prime(i):
        prime_list.append(i)
n = int(raw_input())
count = 0
for i in range(len(prime_list) - 1):
    if prime_list[i + 1] > n:
        break
    elif prime_list[i + 1] - prime_list[i] == 2:
        count += 1
print count