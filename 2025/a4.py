
def remove_paper(pmap:dict):
    cnt = 0
    removed = []
    for pos, symbol in pmap.items():
        if symbol != '@':
            continue
        x,y = pos
        papercnt = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i == x and j == y:
                    continue
                if pmap.get((i,j)) == '@':
                    papercnt += 1
        if papercnt < 4:
            cnt += 1
            removed.append((x,y))

    for pos in removed:
        pmap[pos] = '.'
    return cnt

def p1(pmap):
    print(remove_paper(pmap))

def p2(pmap):
    pcnt = 0
    while True:
        rmv = remove_paper(pmap)
        pcnt += rmv
        if rmv == 0:
            break
    print(pcnt)

def main():
    A = []
    with open('data/a4.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    papermap = {}
    for y, row in enumerate(A):
        for x, c in enumerate(row):
            papermap[(x,y)] = c

    p1(papermap.copy())
    p2(papermap)
    

if __name__ == '__main__':
    main()