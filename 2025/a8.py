from collections import defaultdict
import numpy as np

def dist(v1, v2):
    return ((v1[0]-v2[0])**2+(v1[1]-v2[1])**2+(v1[2]-v2[2])**2)**0.5

def p12(A):
    iter_count = 10 if len(A) == 20 else 1000
    dset = {}
    unique = set()
    p2_res = 0
    B = []
    for a in A:
        B.append(tuple([int(x) for x in a.split(',')]))

    pairs = []
    for i, v1 in enumerate(B):
        dset[v1] = i
        unique.add(i)
        for v2 in B[i+1:]:
            pairs.append((dist(v1,v2), v1, v2))
    pairs.sort()

    c = 0
    for i in range(len(pairs)):
        c += 1

        _, v1, v2 = pairs[i]
        i1 = dset.get(v1)
        i2 = dset.get(v2)
        unique.add(i1)
        for key, ix in dset.items():
            if ix == i2:
                dset[key] = i1
                if i2 in unique:
                    unique.remove(i2)

        # p1
        if c == iter_count:
            cnt_dict = defaultdict(int)
            for key, value in dset.items():
                cnt_dict[value] += 1

            res = np.prod(sorted(list(cnt_dict.values()), reverse=True)[:3])
            print(res)

        # p2
        if len(unique) == 0:
            print(p2_res)
            break
        p2_res = v1[0]*v2[0]
    

def main():
    A = []
    with open('data/a8.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    p12(A)
    

if __name__ == '__main__':
    main()
