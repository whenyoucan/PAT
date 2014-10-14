repeat = int(raw_input())
cards = [c + str(n) for c in ['S', 'H', 'C', 'D'] for n in xrange(1, 14)] + ['J1', 'J2']
orders = [int(i) for i in raw_input().split()]
for r in xrange(repeat):
    cards_copy = cards[:]
    for i in xrange(len(cards)):
        cards_copy[orders[i] - 1] = cards[i]
    cards = cards_copy
for card in cards:
    print card,