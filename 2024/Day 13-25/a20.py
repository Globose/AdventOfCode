from collections import deque

dir = ((0,-1), (-1,0), (1,0), (0,1))

def BFS(grid, start, end):
    deq = deque()
    deq.append(start)
    root = {start:None}

    while len(deq) > 0:
        cell = deq.popleft()
        if grid.get(cell) == '#':
            continue
        
        for d in dir:
            ncell = (cell[0]+d[0], cell[1]+d[1])
            if ncell in root:
                continue
            deq.append(ncell)
            root[ncell] = cell
    
    times = {}
    B = [end]
    t = 0
    while True:
        next = root.get(B[len(B)-1])
        if next:
            times[B[len(B)-1]] = t
            B.append(next)
        else:
            times[start] = t
            break
        t+=1

    return times


def dist(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


def cnt_close(pos, time, times, cheats, lim):
    for dy in range(-lim, lim+1):
        for dx in range(-lim+abs(dy), lim+1-abs(dy)):
            npos = (pos[0]+dx, pos[1]+dy)
            if npos not in times:
                continue
            cart = tuple(sorted([npos, pos]))
            s = abs(time-times[npos])-dist(npos,pos)
            if npos != pos and npos in times:
                cheats[cart] = s

def skip(times, limit):
    cheats = {}
    for pos, time in times.items():
        cnt_close(pos, time, times, cheats, limit)
    
    cnt = 0
    for key, c in cheats.items():
        cnt += c >= 100
    return cnt


def main():
    A = []
    with open('2024/data/a20.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    start = end = None
    grid = {}
    for y, row in enumerate(A):
        for x, cell in enumerate(row):
            grid[(x,y)] = cell
            if cell == 'S':
                start = (x,y)
            elif cell == 'E':
                end = (x,y)

    ### Part 1
    times = BFS(grid, start, end)
    print(skip(times, 2))
    print(skip(times, 20))


if __name__ == '__main__':
    main()
