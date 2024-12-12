from collections import defaultdict
dir = ((0,-1), (-1,0), (1,0), (0,1))


def fill(pos, visited, B):
    reg = []
    v_list = {pos}
    val = B.get(pos)

    while len(v_list) > 0:
        cell = v_list.pop()
        visited.add(cell)
        reg.append(cell)
        for d in dir:
            npos = (cell[0]+d[0], cell[1]+d[1])
            if npos not in visited and B.get(npos) == val:
                v_list.add(npos)
    return reg


def remove_dupes(fdata, region, B):
    dupes = 0
    for cell in region:
        for d in dir:
            npos = (cell[0]+d[0], cell[1]+d[1])
            if B.get(cell) == B.get(npos):
                for fd in fdata[npos]:
                    for f2 in fdata[cell]:
                        if fd == f2:
                            dupes += 1
    return dupes//2


def fence(region, B, lim):
    fcount = 0
    fdata = defaultdict(list)
    for cell in region:
        for i, d in enumerate(dir):
            npos = (cell[0]+d[0], cell[1]+d[1])
            if B.get(cell) != B.get(npos):
                fdata[cell].append(i)
                fcount += 1
    if lim:
        fcount -= remove_dupes(fdata, region, B)

    return fcount


def main():
    A = []
    with open('2024/data/a12.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    B = {}
    for y, row in enumerate(A):
        for x, cell in enumerate(row):
            B[(x,y)] = cell
    
    regions = []
    visited = set()

    for y, row in enumerate(A):
        for x, cell in enumerate(row):
            if (x,y) not in visited:
                regions.append(fill((x,y),visited, B))
    
    s1 = 0
    s2 = 0
    for region in regions:
        s1 += len(region)*fence(region, B, False)
        s2 += len(region)*fence(region, B, True)
    
    print(s1)
    print(s2)


if __name__ == '__main__':
    main()
