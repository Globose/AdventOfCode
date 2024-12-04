dir = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
xm = "XMAS"

def xmas(A, x, y, d, i):
    """Looks for XMAS"""
    if i == 4:
        return 1
    if A.get((x,y)) == xm[i]:
        return xmas(A, x+d[0], y+d[1], d, i+1)
    return 0

def mas(A, x, y):
    """Looks for X-MAS"""
    if A.get((x,y)) != 'A':
        return 0
    diags = [(A.get((x-1,y-1),0), A.get((x+1,y+1),0)), (A.get((x+1,y-1),0), A.get((x-1,y+1),0))]
    return 'S' in diags[0] and 'S' in diags[1] and 'M' in diags[0] and 'M' in diags[1]

def main():
    A = []
    with open('2024/data/a4.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    B = {}
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[(j,i)] = A[j][i]
    
    ### Part 1
    c = 0
    for pos in B:
        for d in dir:
            c += xmas(B, pos[0], pos[1], d, 0)
    print(c)

    c = 0
    ### Part 2
    for pos in B:
        c += mas(B, pos[0], pos[1])
    print(c)


if __name__ == '__main__':
    main()