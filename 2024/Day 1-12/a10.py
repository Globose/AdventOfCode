dir = ((0,-1), (-1,0), (1,0), (0,1))

def path(pos, grid, score_list, score_set):
    cell_value = grid.get(pos)

    if cell_value == 9:
        score_list.append(pos)
        score_set.add(pos)
        return
    
    for d in dir:
        pos2 = (pos[0]+d[0], pos[1]+d[1])
        if grid.get(pos2) == cell_value + 1:
            path(pos2, grid, score_list, score_set)

    return len(score_set), len(score_list)


def main():
    A = []
    with open('2024/data/a10.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    grid = {}
    heads = []

    for y, row in enumerate(A):
        for x, cell in enumerate(row):
            value = int(cell)
            grid[(x,y)] = value
            if value == 0:
                heads.append((x,y))
    
    tscore = [0,0]
    for h in heads:
        score = path(h, grid, [], set())
        tscore[0] += score[0]
        tscore[1] += score[1]

    print(f"{tscore[0]}\n{tscore[1]}")
    

if __name__ == '__main__':
    main()
