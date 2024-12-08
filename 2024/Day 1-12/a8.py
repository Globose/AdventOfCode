def add_anti(p, grid, antinodes):
    in_grid = False
    if p in grid:
        in_grid = True
        antinodes.add(p)
    return in_grid

def get_freq(A, grid, antinodes, kstart, klim):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            xd, yd = A[i][0] - A[j][0], A[i][1] - A[j][1]
            ig = True
            k = kstart

            while ig and k < klim:
                ig = False
                ig = add_anti((A[i][0]+xd*k, A[i][1]+yd*k), grid, antinodes)
                ig = add_anti((A[j][0]-xd*k, A[j][1]-yd*k), grid, antinodes) or ig
                k += 1

    return antinodes

def main():
    A = []
    with open('2024/data/a8.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    antennas = {}
    grid = {}
    antinodes = set()

    for y, row in enumerate(A):
        for x, r in enumerate(row):
            grid[(x,y)] = r
            if r != '.':
                antennas.setdefault(r, []).append((x,y))
    
    ### Part 1
    for B in antennas:
        get_freq(antennas.get(B), grid, antinodes, 1, 2)
    print(len(antinodes))
    
    ### Part 2
    for B in antennas:
        get_freq(antennas.get(B), grid, antinodes, 0, 10**5)
    print(len(antinodes))


if __name__ == '__main__':
    main()
