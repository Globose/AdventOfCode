from collections import deque

dir = ((0,-1), (-1,0), (1,0), (0,1))

def BFS(grid, end):
    deq = deque()
    deq.append((0,0))
    root = {(0,0):None}

    while len(deq) > 0:
        cell = deq.popleft()
        if grid.get(cell) != '.':
            continue

        for d in dir:
            ncell = (cell[0]+d[0], cell[1]+d[1])
            if ncell in root:
                continue
            deq.append(ncell)
            root[ncell] = cell
    
    B = [end]
    while True:
        next = root.get(B[len(B)-1])
        if next:
            B.append(next)
        else:
            break

    return len(B)-1
    

def main():
    A = []
    with open('2024/data/a18.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    A = [a.split(',') for a in A]
    A = [(int(x[0]), int(x[1])) for x in A]

    width = max(A, key=lambda x:x[0])[0]+1
    height = max(A, key=lambda x:x[1])[1]+1

    ### Part 1
    time = 12
    B = set(A[:time])
    grid = {}
    for y in range(height):
        for x in range(width):
            grid[(x,y)] = '.'
            if (x,y) in B:
                grid[(x,y)] = '#'
    
    l = BFS(grid, (width-1, height-1))
    print(l)

    ### part 2
    low, mid, high = time+1, 0, len(A)-1
    while low < high - 2:
        mid = (low+high)//2

        for k in range(time+1, mid):
            grid[A[k]] = '#'
        for k in range(mid, len(A)):
            grid[A[k]] = '.'
        
        l = BFS(grid, (width-1, height-1))
        if l == 0:
            high = mid+1
        else:
            low = mid

    print(str(A[mid]).strip('()'))


if __name__ == '__main__':
    main()
