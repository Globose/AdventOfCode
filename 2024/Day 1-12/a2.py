from collections import Counter

def safe(rep):
    diffs = [rep[i]-rep[i-1] for i in range (1,len(rep))]
    pos = sum(1 for x in diffs if x > 0)
    neg = sum(1 for x in diffs if x < 0)
    for i, d in enumerate(diffs):
        if abs(d) > 3 or (d > 0 and neg >= pos) or (d < 0 and pos >= neg) or d == 0:
            return i
    return -1


def main():
    A = []
    with open('2024/data/a2.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    reps = []
    for row in A:
        reps.append([int(x) for x in row.split()])
    
    ### Part 1
    sc = 0
    for r in reps:
        if safe(r) == -1:
            sc += 1
    print(sc)

    ### Part 2
    sc = 0
    for r in reps:
        unsafe = safe(r)
        if unsafe == -1:
            sc += 1
        else:
            r1 = r.copy()
            r2 = r.copy()
            r1.pop(unsafe)
            r2.pop(unsafe+1)
            if safe(r1) == -1 or safe(r2) == -1:
                sc += 1
    print(sc)


if __name__ == '__main__':
    main()