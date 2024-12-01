from collections import Counter
values = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
winning_patterns = ('0001', '0010', '1100', '0100', '2000', '1000', '0000')
joker_values = [(0,), (0,1), (0,), (0,2,3), (0,2), (0,2,4,5), (0,1,3,5,6,6)]

def rank_cards(hand, joker):
    order = 0
    jokers = 0

    if joker:
        values['J'] = 1
    for i in range(len(hand)):
        order += (14**(4-i))*int(values.get(hand[i], hand[i]))
    values['J'] = 11

    C1 = Counter(hand)
    count_grid = [0,0,0,0,0,0]
    for key in C1:
        if joker and key == 'J':
            jokers = C1.get(key)
        else:
            count_grid[C1.get(key)] += 1
    count_grid = ''.join(str(x) for x in count_grid)[2:]

    value = 10000000 + order
    for i, w in enumerate(winning_patterns):
        if w == count_grid:
            value += 1000000*joker_values[i][jokers]
            break
        value -= 1000000
    return value

def main():
    A = []
    with open('2023/data/a7.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip().split(' ') for line in file]
    C = []
    total = 0
    for hand in A:
        rank = rank_cards(hand[0], False)
        bid = int(hand[1])
        C.append((rank, bid))
    C.sort()
    for i, c in enumerate(C):
        total += c[1]*(i+1)
    print(total)

    ### Part 2
    C = []
    total = 0
    for hand in A:
        rank = rank_cards(hand[0], True)
        bid = int(hand[1])
        C.append((rank, bid))
    C.sort()
    for i, c in enumerate(C):
        total += c[1]*(i+1)
    print(total)


if __name__ == '__main__':
    main()