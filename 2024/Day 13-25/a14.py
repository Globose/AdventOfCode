import re
from math import prod

def print_grid(B, w, h):
    for i in range(h):
        for j in range(w):
            if (j,i) in B:
                print(str(B.count((j,i))), end='')
            else:
                print('.', end='') 
        print()


def get_f(A, f, w, h):
    B = []

    for a in A:
        x = (a[0]+f*a[2])%w
        y = (a[1]+f*a[3])%h
        B.append((x,y))
    return B


def main():
    A = []
    with open('2024/data/a14.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]

    for i, a in enumerate(A):
        A[i] = tuple([int(x) for x in re.findall(r"-?\d+", a)])
    
    w = 101
    h = 103

    ### Part 1
    Q = [0,0,0,0]
    B = get_f(A, 100, w, h)
    for x, y in B:
        rx = ry = 1
        if x == w//2 or y == h//2:
            continue
        if x < w//2:
            rx = 0
        if y < h//2:
            ry = 0
        Q[rx+2*ry]+=1
    print(prod(Q))

    ### Part 2
    tree = 0
    for f in range(10000):
        B = get_f(A, f, w, h)
        allin = True
        for i in range(w//2-1, w//2+2):
            for j in range(h//2-1, h//2+2):
                if (i,j) not in B:
                    allin = False
        if allin:
            tree = f
            break
    
    print(tree)
    B = get_f(A, tree, w, h)
    print_grid(B, w, h)


if __name__ == '__main__':
    main()
