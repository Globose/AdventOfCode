from collections import defaultdict
from functools import cache

df = defaultdict(set)

@cache
def add_node(tup):
    first_adj = df[tup[0]]
    new_tups = []
    for adj in first_adj:
        if adj in tup:
            continue
        stop = False
        for comp in tup:
            if adj not in df[comp]:
                stop = True
                break
        if stop:
            continue
        lst_n = list(tup)
        lst_n.append(adj)
        new_tups.append(tuple(sorted(lst_n)))
    
    rmax = (len(tup), tup)
    for t2 in new_tups:
        next = add_node(t2)
        if len(next) > rmax[0]:
            rmax = (len(next), next)
    return rmax[1]

def main():
    A = []
    with open('2024/data/a23.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    for a in A:
        C = a.split('-')
        df[C[0]].add(C[1])
        df[C[1]].add(C[0])

    ### Part 1
    triplets = set()
    for c0 in df:
        for c1 in df[c0]:
            for c2 in df[c1]:
                if c0 in df[c2] and 't' in [x[0] for x in (c0,c1,c2)]:
                    triplets.add(tuple(sorted([c0, c1, c2])))
    print(len(triplets))

    ### Part 2
    mmax = (0, None)
    for c0 in df:
        q1 = add_node((c0,))
        if len(q1) > mmax[0]:
            mmax = (len(q1), q1) 
    print(",".join(mmax[1]))

if __name__ == '__main__':
    main()
