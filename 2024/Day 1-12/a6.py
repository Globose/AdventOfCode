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
            return visited
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
    start = None

    for y in range(len(A)):
        for x in range(len(A[0])):
            grid[(x,y)] = A[y][x]
            if A[y][x] == '^':
                start = (x,y)
    
    visited = walk(grid, start, 0)
    print(len(visited))

    ### Part 2
    counter = 0
    for v in visited:
        grid[v] = '#'
        if walk(grid, start, 0) == 0:
            counter += 1
        grid[v] = '.'
    print(counter)

if __name__ == '__main__':
    main()