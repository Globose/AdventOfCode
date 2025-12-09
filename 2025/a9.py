import matplotlib.pyplot as plt

def is_inside(x1, x2, y1, y2, xx, yy):
    return xx > x1 and xx < x2 and yy > y1 and yy < y2

def is_inside_inclusive(x1, y1, x2, y2, xx, yy):
    mx1 = min(x1, x2)
    mx2 = max(x1, x2)
    my1 = min(y1, y2)
    my2 = max(y1, y2)
    return mx1 <= xx <= mx2 and my1 <= yy <= my2

def check_inside(t1, t2, tile, index, tiles):
    rec_x1 = min(t1[0], t2[0])
    rec_x2 = max(t1[0], t2[0])
    rec_y1 = min(t1[1], t2[1])
    rec_y2 = max(t1[1], t2[1])
    cur_x = tile[0]
    cur_y = tile[1]

    if is_inside(rec_x1, rec_x2, rec_y1, rec_y2, cur_x, cur_y):
        return True

    next_tile = tiles[(index+1)%len(tiles)]
    nx, ny = next_tile

    if nx > cur_x:
        delta = (1,0)
    elif nx < cur_x:
        delta = (-1,0)
    elif ny > cur_y:
        delta = (0,1)
    elif ny < cur_y:
        delta = (0,-1)

    if is_inside(rec_x1, rec_x2, rec_y1, rec_y2, cur_x+delta[0], cur_y+delta[1]):
        return True

    if (cur_x < rec_x1 and nx > rec_x2) and (rec_y1 <= cur_y <= rec_y2):
        return True
    if (cur_x > rec_x2 and nx < rec_x1) and (rec_y1 <= cur_y <= rec_y2):
        return True
    if (cur_y < rec_y1 and ny > rec_y2) and (rec_x1 <= cur_x <= rec_x2):
        return True
    if (cur_y > rec_y2 and ny < rec_y1) and (rec_x1 <= cur_x <= rec_x2):
        return True

    return False


def p12(tiles):
    tile_sizes = []
    tmax = 0
    tile_dict = set()
    
    for i, t1 in enumerate(tiles):
        prev_x, prev_y = tiles[(i-1)%len(tiles)]
        next_x, next_y = tiles[(i+1)%len(tiles)]
        plt.plot((t1[0], next_x), (t1[1],next_y))
        cur_x, cur_y = t1

        inside_area = []
        if prev_x > cur_x: # left
            inside_area.append((100000,0))
            if next_y > cur_y:
                inside_area.append((0,0))
                inside_area.append((0,100000))

        if prev_x < cur_x: # right
            inside_area.append((0,100000))
            if next_y < cur_y:
                inside_area.append((100000,0))
                inside_area.append((100000,100000))

        if prev_y > cur_y: # up
            inside_area.append((100000,100000))
            if next_x < cur_x:
                inside_area.append((100000,0))
                inside_area.append((0,0))

        if prev_y < cur_y: # down
            inside_area.append((0,0))
            if next_x > cur_x:
                inside_area.append((0,100000))
                inside_area.append((100000,100000))

        for t2 in tiles:
            size = (abs(t1[0]-t2[0])+1)*(abs(t1[1]-t2[1])+1)
            tmax = max(tmax, size)

            allowed = False
            for x, y in inside_area:
                if is_inside_inclusive(cur_x, cur_y, x, y, t2[0], t2[1]):
                    allowed = True
                    break
            
            if allowed:
                if (t1,t2) in tile_dict or (t2,t1) in tile_dict:
                    tile_sizes.append((size, t1, t2))
                else:
                    tile_dict.add((t1,t2))
                    tile_dict.add((t2,t1))
    tile_sizes.sort(reverse=True)

    # p1
    print(tmax)

    # p2
    for size, t1, t2 in tile_sizes:
        found = True
        for i, t3 in enumerate(tiles):
            if check_inside(t1, t2, t3, i, tiles):
                found = False
                break

        if found:
            print(size)
            plt.scatter((t1[0],t2[0]), (t1[1], t2[1]), color='red')
            plt.show()
            break

def main():
    A = []
    with open('data/a9.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    tiles = []
    for cpair in A:
        c1, c2 = [int(x) for x in cpair.split(',')]
        tiles.append((c1,c2))

    p12(tiles)


if __name__ == '__main__':
    main()
