dir = ((0,-1), (1,0), (0,1), (-1,0))

def walk(grid, pos, di):
    visited = set()
    visited_d = set()
    while True:
        if (pos,di) in visited_d:
            return 0
        
        visited_d.add((pos, di))
        next = (pos[0]+dir[di][0], pos[1]+dir[di][1])

        if grid.get(next) is None:
            return len(visited)
        if grid.get(next) == '#':
            di = (di+1)%4
        else:
            pos = next
            visited.add((pos))
    

def main():
    A = []
    with open('2024/data/a6.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    grid = {}
    pos = None
    start = None
    di = 0
    visited = set()

    for y in range(len(A)):
        for x in range(len(A[0])):
            grid[(x,y)] = A[y][x]
            if A[y][x] == '^':
                pos = (x,y)
    
    start = pos
    print(walk(grid, pos, di))

    ### Part 2
    counter = 0
    for y in range(len(A)):
        print('-',end='')
        for x in range(len(A[0])):
            if grid.get((x,y)) == '#':
                continue
            grid[(x,y)] = '#'
            
            if walk(grid, start, 0) == 0:
                counter += 1
            grid[(x,y)] = '.'
    print(counter)

if __name__ == '__main__':
    main()