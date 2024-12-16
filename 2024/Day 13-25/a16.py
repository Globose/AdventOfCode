import heapq
from collections import defaultdict

dir = ((0,-1), (-1,0), (1,0), (0,1))


def get_adj(pos, maze, visited, cdir):
    adj = []
    for d in dir:
        if cdir != d and (cdir[0] == d[0] or cdir[1] == d[1]):
            continue 
        npos = (pos[0]+d[0], pos[1]+d[1])
        if maze[npos] == '#' or npos in visited:
            continue
        adj.append((npos, d))
    return adj


def get_tiles(roots, end, score, enddir):
    best = {end}
    queue = [(end, d, score) for d in enddir]

    while len(queue) > 0:
        tile = queue.pop()
        rs = roots[tile]
        for r in rs:
            best.add(r[0])
            queue.append(r)
    return len(best)


def solve_maze(maze, start, end):
    visited = set()
    queue = [(0, start, dir[2])]
    maze[start] = 0
    
    low_score = None
    enddir = set()
    roots = defaultdict(set)

    counter = 0
    while len(queue) > 0:
        counter += 1
        score, pos, cdir = heapq.heappop(queue)
        if pos == end:
            if low_score is None or low_score == score:
                enddir.add(cdir)
                low_score = score
                continue
            elif score > low_score:
                break
        if (pos,cdir) in visited:
            continue
        visited.add((pos, cdir))
        adj = get_adj(pos, maze, visited, cdir)

        for adj_cell in adj:
            adj_pos = adj_cell[0]
            adj_dir = adj_cell[1]
            nscore = score+1 + 1000*int(adj_dir != cdir)
            heapq.heappush(queue, (nscore, adj_pos, adj_dir))
            roots[(adj_pos, adj_dir, nscore)].add((pos, cdir, score))
    
    return low_score, roots, list(enddir)
    

def main():
    A = []
    with open('2024/data/a16.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]

    ### Load maze
    maze = {}
    start = end = 0
    for y, row in enumerate(A):
        for x, cell in enumerate(row):
            maze[(x,y)] = cell
            if cell == 'S':
                start = (x,y)
            elif cell == 'E':
                end = (x,y)

    score, roots, enddir = solve_maze(maze, start, end)
    best = get_tiles(roots, end, score, enddir)
    
    print(score)
    print(best)


if __name__ == '__main__':
    main()
