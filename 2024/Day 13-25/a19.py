from functools import lru_cache

tlen = 0
towels = set()

@lru_cache
def match(pattern):
    if pattern == '':
        return 1
    mc = 0
    for i in range(1,tlen+1):
        if i > len(pattern):
            break
        pt = pattern[:i]
        if pt in towels:
            mc += match(pattern[i:])
    return mc

def main():
    A = []
    with open('2024/data/a19.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    global towels, tlen
    towels = [t.strip() for t in A[0].split(',')]
    tlen = max([len(t) for t in towels])
    patterns = A[2:]
    
    t1 = 0
    t2 = 0
    for p in patterns:
        m = match(p)
        t1 += m > 0
        t2 += m
    print(t1)
    print(t2)

if __name__ == '__main__':
    main()
