import sys

n = int(raw_input())
record = [0, 0, 0]
a_wins = {'B': 0, 'C': 0, 'J': 0}
b_wins = {'B': 0, 'C': 0, 'J': 0}


def draw():
    record[1] += 1


def c_j():
    record[0] += 1
    a_wins['C'] += 1


def j_b():
    record[0] += 1
    a_wins['J'] += 1


def b_c():
    record[0] += 1
    a_wins['B'] += 1


def j_c():
    record[2] += 1
    b_wins['C'] += 1


def b_j():
    record[2] += 1
    b_wins['J'] += 1


def c_b():
    record[2] += 1
    b_wins['B'] += 1


functions = {
    'B B': draw,
    'C C': draw,
    'J J': draw,
    'C J': c_j,
    'J B': j_b,
    'B C': b_c,
    'J C': j_c,
    'C B': c_b,
    'B J': b_j
}

records = sys.stdin.read(n * 4).split('\n')[:-1]
for r in records:
    functions[r]()
print record[0], record[1], record[2]
print record[2], record[1], record[0]
print sorted(a_wins.items(), key=lambda x: (-x[1], x[0]))[0][0],
print sorted(b_wins.items(), key=lambda x: (-x[1], x[0]))[0][0],