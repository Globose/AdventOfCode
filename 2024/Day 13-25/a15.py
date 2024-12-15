dir = {'^':(0,-1), '<':(-1,0), '>':(1,0), 'v':(0,1)}

def move_1(grid, move, pos):
    x,y = pos[0], pos[1]
    next = (x+move[0],y+move[1])
    
    while grid[(x,y)] != '.' and grid[(x,y)] != '#':
        x += move[0]
        y += move[1]
    
    last = (x,y)
    if grid[last] == '#':
        return pos
    
    while last != pos:
        nlast = (last[0]-move[0], last[1]-move[1])
        grid[last] = grid[nlast]
        last = nlast

    grid[pos] = '.'
    return next

def move_wide(grid, move, pos):
    x,y = pos[0], pos[1]+move[1]
    next = (x+move[0],y)
    to_be_moved = []
    block = False
    last_row = set()
    last_row.add(pos)
    to_be_moved.extend(last_row)

    while True:
        row = set()
        for x0, y0 in last_row:
            g = grid[(x0,y)]
            if g == '[':
                row.add((x0,y))
                row.add((x0+1,y))
            elif g == ']':
                row.add((x0,y))
                row.add((x0-1,y))
            elif g == '#':
                block = True
                break

        if len(row) == 0 or block:
            break
        to_be_moved.extend(row)
        last_row = row
        y += move[1]

    if block:
        return pos

    for i in range(len(to_be_moved)-1, -1, -1):
        c = to_be_moved[i]
        cnext = (c[0]+move[0], c[1]+move[1])
        grid[cnext] = grid[c]
        grid[c] = '.'
    
    grid[pos] = '.'
    return next

def move_a(grid, moves, pos, wide):
    for move in moves:
        if move[1] == 0 or not wide:
            pos = move_1(grid, move, pos)
        else:
            pos = move_wide(grid, move, pos)

    total = 0
    for item in grid.items():
        if item[1] == 'O' or item[1]=='[':
            total += item[0][0] + item[0][1]*100
    print(total)

def main():
    A = []
    with open('2024/data/a15.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    grid = {}
    sep = A.index('')
    pos = None

    ### Setup
    for y, row in enumerate(A[:sep]):
        for x, cell in enumerate(row):
            grid[(x,y)] = cell
            if cell == '@':
                pos = (x,y)
    
    moves = []
    for row in A[sep+1:]:
        moves.extend(dir[x] for x in list(row))
    
    ### Part 1
    move_a(grid, moves, pos, False)

    ### Part 2
    tile = {'#':('#','#'), 'O':('[',']'), '.':('.','.'), '@':('@','.')}
    wgrid = {}
    for y, row in enumerate(A[:sep]):
        for x, cell in enumerate(row):
            wgrid[(2*x,y)] = tile[cell][0]
            wgrid[(2*x+1,y)] = tile[cell][1]
            if cell == '@':
                pos = (2*x,y)
    
    move_a(wgrid, moves, pos, True)

if __name__ == '__main__':
    main()
