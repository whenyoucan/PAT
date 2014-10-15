import sys

n = int(raw_input())
a_record = {'win': 0, 'draw': 0, 'lose': 0}
a_wins = {'B': 0, 'C': 0, 'J': 0}
b_wins = {'B': 0, 'C': 0, 'J': 0}


def draw():
    a_record['draw'] += 1


def c_j():
    a_record['win'] += 1
    a_wins['C'] += 1


def j_b():
    a_record['win'] += 1
    a_wins['J'] += 1


def b_c():
    a_record['win'] += 1
    a_wins['B'] += 1


def j_c():
    a_record['lose'] += 1
    b_wins['C'] += 1


def b_j():
    a_record['lose'] += 1
    b_wins['J'] += 1


def c_b():
    a_record['lose'] += 1
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
print a_record['win'], a_record['draw'], a_record['lose']
print a_record['lose'], a_record['draw'], a_record['win']
print sorted(a_wins.items(), key=lambda x: (-x[1], x[0]))[0][0],
print sorted(b_wins.items(), key=lambda x: (-x[1], x[0]))[0][0],