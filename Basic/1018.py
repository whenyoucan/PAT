import sys

n = int(raw_input())
record = [0, 0, 0]
a_wins = [0, 0, 0]
b_wins = [0, 0, 0]


def draw():
    record[1] += 1


def c_j():
    record[0] += 1
    a_wins[1] += 1


def j_b():
    record[0] += 1
    a_wins[2] += 1


def b_c():
    record[0] += 1
    a_wins[0] += 1


def j_c():
    record[2] += 1
    b_wins[1] += 1


def b_j():
    record[2] += 1
    b_wins[2] += 1


def c_b():
    record[2] += 1
    b_wins[0] += 1


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
record = record[::-1]
print record[0], record[1], record[2]
if a_wins[0] == max(a_wins):
    print 'B',
elif a_wins[1] == max(a_wins):
    print 'C',
else:
    print 'J',
if b_wins[0] == max(b_wins):
    print 'B',
elif b_wins[1] == max(b_wins):
    print 'C',
else:
    print 'J',